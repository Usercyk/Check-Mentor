import requests
import os
import re
from bs4 import BeautifulSoup
import Levenshtein
import argparse
import configparser
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from functools import lru_cache
from urllib.parse import unquote
import json
import shutil
import time
import threading
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

# Global flag for production mode
production_mode = False

# Verification level: 'strict' (default, fetch DOI page), 'light' (use Crossref fast path), 'off' (skip)
VERIFY_LEVEL = 'strict'

# Behavior flag: when true, do not download PDFs for main layer; only filter main, then download ref1 and cited
ONLY_REF1_AND_CITED = False

# Max pages threshold for downloading (configurable via CLI)
MAX_PAGES = 30

# Global HTTP session with retries
session = requests.Session()
retry_strategy = Retry(
    total=3,
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["GET", "HEAD"],
    backoff_factor=0.5,
)
adapter = HTTPAdapter(max_retries=retry_strategy)
session.mount("http://", adapter)
session.mount("https://", adapter)
DEFAULT_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Default networking knobs (overridable via CLI)
REQUEST_TIMEOUT = 15

# Optional integrations and runtime knobs
UNPAYWALL_EMAIL: str | None = None
SCIHUB_DOMAINS: list[str] | None = None
OPENALEX_MAILTO: str | None = None
OPENALEX_BASE = "https://api.openalex.org"
# Impact factor / selection config
TOP_N: int | None = None  # legacy: used as fallback for ref/cited if specific values absent
TOP_N_MAIN: int | None = None
TOP_N_REF: int | None = None
TOP_N_CITED: int | None = None
IMPACT_FACTORS: dict = {}
RECENT_YEARS: int | None = None


# Simple global rate limiter (shared among threads)
class RateLimiter:
    def __init__(self, rps: float):
        self.interval = 0.0 if rps <= 0 else 1.0 / float(rps)
        self.lock = threading.Lock()
        self.last = 0.0

    def wait(self):
        if self.interval <= 0:
            return
        with self.lock:
            now = time.monotonic()
            elapsed = now - self.last
            if elapsed < self.interval:
                time.sleep(self.interval - elapsed)
                now = time.monotonic()
            self.last = now

RATE_LIMITER: RateLimiter | None = None

def http_get(url: str, *, timeout: float | None = None, headers=None, **kwargs):
    if RATE_LIMITER is not None:
        RATE_LIMITER.wait()
    return session.get(url, timeout=timeout or REQUEST_TIMEOUT, headers=headers or DEFAULT_HEADERS, **kwargs)

# Output roots (configurable via CLI)
OUTPUT_ROOT_PDF = os.path.join(os.getcwd(), "Downloads_pdf")
SAVE_ONLY_DEPTH: int | None = None  # if set, only save PDFs for this depth (0=main,1=ref1,2=ref2,...)
CHECKPOINT_DIR: str | None = None   # where to persist task checkpoints
ENABLE_CHECKPOINT: bool = True      # whether to persist/restore task checkpoints
RESUME_FROM_CHECKPOINT: bool = False

# Persistent download history (centralized under OUTPUT_ROOT_PDF)
_history_lock = threading.Lock()
_history_cache = None

def _history_path() -> str:
    # Store a single global history to deduplicate downloads across teachers
    return os.path.join(OUTPUT_ROOT_PDF, ".history.json")

def _ensure_history_loaded():
    global _history_cache
    if _history_cache is None:
        os.makedirs(OUTPUT_ROOT_PDF, exist_ok=True)
        hp = _history_path()
        if os.path.exists(hp):
            try:
                with open(hp, 'r', encoding='utf-8') as f:
                    _history_cache = json.load(f)
            except Exception:
                _history_cache = {}
        else:
            _history_cache = {}

def history_get(doi: str):
    _ensure_history_loaded()
    return _history_cache.get(doi)

def history_set(doi: str, record: dict):
    _ensure_history_loaded()
    with _history_lock:
        _history_cache[doi] = record
        try:
            with open(_history_path(), 'w', encoding='utf-8') as f:
                json.dump(_history_cache, f, ensure_ascii=False, indent=2)
        except Exception:
            pass

def configure_http(retries: int | None = None, backoff: float | None = None, timeout: float | None = None, rps: float | None = None):
    global REQUEST_TIMEOUT, RATE_LIMITER
    if timeout is not None and timeout > 0:
        REQUEST_TIMEOUT = timeout
    if rps is not None:
        RATE_LIMITER = RateLimiter(rps)
    if retries is not None or backoff is not None:
        r = retries if retries is not None else retry_strategy.total
        b = backoff if backoff is not None else retry_strategy.backoff_factor
        new_strategy = Retry(
            total=r,
            status_forcelist=retry_strategy.status_forcelist,
            allowed_methods=retry_strategy.allowed_methods,
            backoff_factor=b,
        )
        new_adapter = HTTPAdapter(max_retries=new_strategy)
        session.mount("http://", new_adapter)
        session.mount("https://", new_adapter)

def configure_http_pool(pool_connections: int | None = None, pool_maxsize: int | None = None):
    """Configure HTTP connection pool sizes (useful when increasing --workers)."""
    # Re-mount adapters with custom pool sizes if provided
    kwargs = {}
    if pool_connections is not None:
        kwargs['pool_connections'] = int(pool_connections)
    if pool_maxsize is not None:
        kwargs['pool_maxsize'] = int(pool_maxsize)
    if not kwargs:
        return
    new_adapter = HTTPAdapter(max_retries=retry_strategy, **kwargs)
    session.mount("http://", new_adapter)
    session.mount("https://", new_adapter)

def configure_outputs(pdf_root: str | None = None):
    """Configure output roots (e.g., Downloads_pdf) and reset history cache if root changes."""
    global OUTPUT_ROOT_PDF, _history_cache
    if pdf_root:
        new_root = os.path.abspath(pdf_root)
        if OUTPUT_ROOT_PDF != new_root:
            OUTPUT_ROOT_PDF = new_root
            _history_cache = None  # force reload from new location
    # default checkpoint dir under OUTPUT_ROOT_PDF
    global CHECKPOINT_DIR
    CHECKPOINT_DIR = os.path.join(OUTPUT_ROOT_PDF, ".checkpoints")
    try:
        os.makedirs(CHECKPOINT_DIR, exist_ok=True)
    except Exception:
        pass

def configure_checkpoint(dir_path: str | None = None, *, enable: bool | None = None, resume: bool | None = None):
    """Configure checkpointing directory and switches."""
    global CHECKPOINT_DIR, ENABLE_CHECKPOINT, RESUME_FROM_CHECKPOINT
    if dir_path:
        CHECKPOINT_DIR = os.path.abspath(dir_path)
        try:
            os.makedirs(CHECKPOINT_DIR, exist_ok=True)
        except Exception:
            pass
    if enable is not None:
        ENABLE_CHECKPOINT = bool(enable)
    if resume is not None:
        RESUME_FROM_CHECKPOINT = bool(resume)

def get_official_title_from_doi(doi):
    """
    Fetches the official title of an article from the CrossRef API.
    This is considered the ground truth for title comparison.
    """
    try:
        crossref_url = f"https://api.crossref.org/works/{doi}"
        response = http_get(crossref_url, headers=DEFAULT_HEADERS, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        data = response.json()
        title = data.get('message', {}).get('title', [None])[0]
        if title:
            if not production_mode:
                print(f"Fetched official title from CrossRef: '{title}'")
            return title.strip()
    except Exception as e:
        if not production_mode:
            print(f"Error fetching official title from CrossRef API: {e}")
    return None

def verify_title_similarity(official_title, downloaded_title):
    """
    Compares the official title with the downloaded title using Levenshtein distance.
    Returns True if they are similar enough, False otherwise.
    """
    if not official_title or not downloaded_title:
        if not production_mode:
            print("Warning: Cannot verify title similarity because one of the titles is missing.")
        return False # Cannot verify

    similarity = Levenshtein.ratio(official_title.lower(), downloaded_title.lower())
    if not production_mode:
        print(f"Title similarity ratio: {similarity:.2f}")
    if similarity < 0.8:
        if not production_mode:
            print(f"Warning: Potential title mismatch!")
            print(f"  - Official Title:   '{official_title}'")
            print(f"  - Downloaded Title: '{downloaded_title}'")
        return False
    
    if not production_mode:
        print("Titles match. Download is likely correct.")
    return True

def ExtractReferences(response_text):
    """
    Extract references from the response text and convert them to DOI format.
    """
    references = set()
    try:
        soup = BeautifulSoup(response_text, 'html.parser')
        # 1. 链接中的DOI
        for link in soup.find_all('a', href=True):
            href = link['href']
            if 'doi.org/' in href:
                doi = href.split('doi.org/')[-1].split('?')[0].split('#')[0]
                references.add(doi)
        # 2. meta标签中的DOI
        for meta in soup.find_all('meta'):
            if meta.get('name', '').lower() == 'citation_doi' and meta.get('content'):
                references.add(meta['content'])
        # 3. 参考文献区块中的DOI（常见于期刊页面）
        ref_blocks = soup.find_all(['div', 'li', 'span', 'p'], string=re.compile(r'10\.\d{4,9}/[-._;()/:A-Z0-9]+', re.I))
        for block in ref_blocks:
            found = re.findall(r'10\.\d{4,9}/[-._;()/:A-Z0-9]+', block.get_text(), re.I)
            for doi in found:
                references.add(doi)
        # 4. 全文正则匹配DOI（兜底方案）
        found = re.findall(r'10\.\d{4,9}/[-._;()/:A-Z0-9]+', response_text, re.I)
        for doi in found:
            references.add(doi)
        # 规范化与去重
        references = list({normalize_doi(d) for d in references if d})
        if not production_mode:
            print("Extracted References (enhanced):", references)
    except Exception as e:
        if not production_mode:
            print(f"Error extracting references: {e}")
    return references

def normalize_doi(doi: str) -> str:
    """Normalize DOI text for consistency and deduplication."""
    if not doi:
        return doi
    doi = unquote(doi).strip()
    # 去掉前缀如 doi: 或 https://doi.org/
    doi = re.sub(r"^(https?://(dx\.)?doi\.org/|doi:)", "", doi, flags=re.I)
    # 空白与末尾标点
    doi = doi.strip().strip(' .;')
    return doi

def sanitize_folder_name(name: str) -> str:
    """Sanitize folder names for Windows/Unix compatibility."""
    name = name.strip().replace('..', '.').strip()
    return re.sub(r'[\\/:*?"<>|#&]', '_', name) or "unknown"

def sanitize_file_title(title: str) -> str:
    sane_title = re.sub(r'[\\/:*?"<>|#&]', '_', title)
    sane_title = (sane_title[:150] + '..') if len(sane_title) > 150 else sane_title
    return sane_title

def subdir_to_depth(subdirectory: str) -> int:
    if subdirectory == "main":
        return 0
    if subdirectory == "cited":
        # Treat cited as depth 1 for the purpose of SAVE_ONLY_DEPTH so that --save-only-depth 1 saves ref1 and cited
        return 1
    m = re.match(r"ref(\d+)$", subdirectory)
    if m:
        try:
            return int(m.group(1))
        except Exception:
            return 0
    return 0

# CrossRef metadata cache
@lru_cache(maxsize=1024)
def get_crossref_metadata(doi: str) -> dict | None:
    try:
        url = f"https://api.crossref.org/works/{doi}"
        resp = http_get(url)
        resp.raise_for_status()
        return resp.json().get('message', {})
    except Exception:
        return None

def estimate_page_count_from_metadata(meta: dict | None) -> int | None:
    """Estimate page count from Crossref metadata.
    Prefer 'number-of-pages' if present, otherwise parse 'page' range like 'S12-34' or '1–15'.
    Returns None if not determinable.
    """
    if not meta or not isinstance(meta, dict):
        return None
    # Direct field if provided by Crossref
    n = meta.get('number-of-pages') or meta.get('number_of_pages')
    try:
        if isinstance(n, int):
            return n if n > 0 else None
        if isinstance(n, str) and n.strip().isdigit():
            v = int(n.strip())
            return v if v > 0 else None
    except Exception:
        pass
    # Parse 'page' string like '123-145', 'S5–S20', '1 — 32'
    page_str = meta.get('page')
    if isinstance(page_str, str) and page_str.strip():
        # Extract numeric tokens and compute last - first + 1 when feasible
        nums = [int(x) for x in re.findall(r"(\d+)", page_str)]
        if len(nums) >= 2:
            try:
                start = nums[0]
                end = nums[-1]
                if end >= start:
                    pages = end - start + 1
                    # Defensive bounds: ignore absurdly large results from bad parsing
                    if 1 <= pages <= 5000:
                        return pages
            except Exception:
                return None
    return None

DEFAULT_YOUNG_KEYWORDS = [
    'student', 'phd', 'doctoral', 'candidate', 'undergraduate', 'master',
    '硕士', '博士', '博后', '研究生', '学生', '博士生', '博士候选人', '本科生'
]

def paper_has_young_author(doi: str, keywords: list[str] | None = None) -> bool:
    """Heuristic: an article is considered to have a 'young author' if any author's affiliation
    contains youth-related keywords (student/PhD/研究生/博士等)."""
    kw = [k.lower() for k in (keywords or DEFAULT_YOUNG_KEYWORDS)]
    meta = get_crossref_metadata(doi)
    if not meta:
        return False
    authors = meta.get('author') or []
    for a in authors:
        affs = a.get('affiliation') or []
        # affiliation is list of {name: str}
        for aff in affs:
            name = (aff.get('name') or '').lower()
            if any(k in name for k in kw):
                return True
    return False

@lru_cache(maxsize=512)
def GetTitleFromDOI(DOI):
    doi_url = f"https://doi.org/{DOI}"
    headers = DEFAULT_HEADERS

    # Strategy order depends on VERIFY_LEVEL for speed/robustness
    # light/off: Crossref first (fast and structured), strict: DOI landing first (for stricter verification)
    try_crossref_first = (VERIFY_LEVEL in ('light', 'off'))

    # Helper: fetch via Crossref
    def _try_crossref():
        try:
            crossref_url = f"https://api.crossref.org/works/{DOI}"
            response = http_get(crossref_url, headers=headers, timeout=REQUEST_TIMEOUT)
            if not production_mode:
                print("CrossRef API Status Code:", response.status_code)
            if response.status_code == 200:
                data = response.json()
                title = data.get('message', {}).get('title', [None])[0]
                references = [item.get('DOI') for item in data.get('message', {}).get('reference', []) if item.get('DOI')]
                if title:
                    if not production_mode:
                        print("Extracted Title from CrossRef:", title)
                        print("Extracted References from CrossRef:", references)
                    return title, references
        except Exception as e:
            if not production_mode:
                print(f"Error fetching title from CrossRef API: {e}")
        return None

    # Helper: fetch via DOI landing page
    def _try_doi_page():
        try:
            response = http_get(doi_url, headers=headers, timeout=REQUEST_TIMEOUT)
            if not production_mode:
                print("DOI URL Status Code:", response.status_code)
            if response.status_code == 200:
                if not production_mode:
                    print("DOI URL Response Text:", response.text[:500])
                references = ExtractReferences(response.text)
                soup = BeautifulSoup(response.text, 'html.parser')
                title_tag = soup.find('title')
                if not production_mode:
                    print("Extracted Title Tag:", title_tag)
                if title_tag and title_tag.text:
                    return title_tag.text.strip(), references
        except Exception as e:
            if not production_mode:
                print(f"Error fetching title from DOI: {e}")
        return None

    # Helper: fetch via Sci-Hub
    def _try_scihub():
        try:
            sci_hub_url = f"https://sci-hub.se/{DOI}"
            response = http_get(sci_hub_url, headers=headers, timeout=REQUEST_TIMEOUT)
            if not production_mode:
                print("Sci-Hub URL Status Code:", response.status_code)
            if response.status_code == 200:
                references = ExtractReferences(response.text)
                soup = BeautifulSoup(response.text, 'html.parser')
                title_tag = soup.find('title')
                if not production_mode:
                    print("Extracted Title Tag from Sci-Hub:", title_tag)
                if title_tag and title_tag.text:
                    return title_tag.text.strip(), references
        except Exception as e:
            if not production_mode:
                print(f"Error fetching title from Sci-Hub: {e}")
        return None

    # Execution order
    if try_crossref_first:
        out = _try_crossref() or _try_doi_page() or _try_scihub()
    else:
        out = _try_doi_page() or _try_crossref() or _try_scihub()
    if out:
        return out

    return "unknown_title", []

def get_recent_dois_from_crossref(query="physics", num_articles=5):
    """
    Get recent article DOIs from CrossRef API based on a query.
    """
    try:
        # Query CrossRef API for recent works related to the query, sorted by publication date
        url = f"https://api.crossref.org/works?query.bibliographic={query}&sort=published&order=desc&rows={num_articles}"
        response = http_get(url, headers=DEFAULT_HEADERS, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        
        dois = [item['DOI'] for item in data['message']['items']]
        if not production_mode:
            print(f"Found {len(dois)} recent DOIs from CrossRef for query '{query}': {dois}")
        return dois
    except Exception as e:
        if not production_mode:
            print(f"Error fetching recent DOIs from CrossRef: {e}")
        return []

def get_recent_dois_from_arxiv(category="physics", num_articles=5):
    """
    Get recent article DOIs from arXiv.
    Note: arXiv papers might not have a DOI immediately. This function gets arXiv IDs.
    The rest of the script can try to find a DOI or download directly if possible.
    """
    try:
        # Scrape the 'new' page for the given category
        url = f"https://arxiv.org/list/{category}/new"
        headers = DEFAULT_HEADERS
        response = http_get(url, headers=headers, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find links to the abstracts
        arxiv_ids = []
        for dt in soup.find_all('dt'):
            span = dt.find('span', class_='list-identifier')
            if span:
                arxiv_id_tag = span.find('a', title='Abstract')
                if arxiv_id_tag:
                    arxiv_ids.append(arxiv_id_tag.text.replace('arXiv:', ''))
            if len(arxiv_ids) >= num_articles:
                break
        
        if not production_mode:
            print(f"Found {len(arxiv_ids)} recent arXiv IDs from category '{category}': {arxiv_ids}")
        return arxiv_ids
    except Exception as e:
        if not production_mode:
            print(f"Error fetching recent DOIs from arXiv: {e}")
        return []

def get_recent_dois_from_pubmed(query="cancer", num_articles=5):
    """
    Get recent article DOIs from PubMed.
    """
    try:
        # Step 1: Search for PubMed IDs (PMIDs)
        search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
        search_params = {
            'db': 'pubmed',
            'term': query,
            'sort': 'pub_date',
            'retmax': num_articles,
            'retmode': 'json'
        }
        headers = DEFAULT_HEADERS
        response = http_get(search_url, params=search_params, headers=headers, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        search_data = response.json()
        pmids = search_data.get('esearchresult', {}).get('idlist', [])
        
        if not pmids:
            if not production_mode:
                print(f"No articles found on PubMed for query '{query}'.")
            return []

        # Step 2: Fetch details for the PMIDs to get the DOIs
        summary_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
        summary_params = {
            'db': 'pubmed',
            'id': ','.join(pmids),
            'retmode': 'json'
        }
        response = http_get(summary_url, params=summary_params, headers=headers, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        summary_data = response.json()
        
        dois = []
        results = summary_data.get('result', {})
        for pmid in pmids:
            article_info = results.get(pmid, {})
            article_ids = article_info.get('articleids', [])
            for article_id in article_ids:
                if article_id.get('idtype') == 'doi':
                    dois.append(article_id.get('value'))
                    break # Found DOI, move to next PMID
        
        if not production_mode:
            print(f"Found {len(dois)} recent DOIs from PubMed for query '{query}': {dois}")
        return dois
    except Exception as e:
        if not production_mode:
            print(f"Error fetching recent DOIs from PubMed: {e}")
        return []

def get_recent_dois_from_semantic_scholar(query="quantum computing", num_articles=5):
    """
    Get recent article DOIs from Semantic Scholar.
    Note: The API's default sort is by relevance, which often includes recent papers.
    """
    try:
        url = "https://api.semanticscholar.org/graph/v1/paper/search"
        params = {
            'query': query,
            'limit': num_articles,
            'fields': 'externalIds'
        }
        headers = DEFAULT_HEADERS
        response = http_get(url, params=params, headers=headers, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        data = response.json()
        
        dois = []
        papers = data.get('data', [])
        for paper in papers:
            external_ids = paper.get('externalIds', {})
            if 'DOI' in external_ids:
                dois.append(external_ids['DOI'])
        
        if not production_mode:
            print(f"Found {len(dois)} DOIs from Semantic Scholar for query '{query}': {dois}")
        return dois
    except Exception as e:
        if not production_mode:
            print(f"Error fetching DOIs from Semantic Scholar: {e}")
        return []

def get_pdf_from_publisher(doi):
    """
    Tries to find the direct PDF download link from the publisher's website.
    This method is most effective when run from an academic network (e.g., via University VPN).
    """
    try:
        landing_url = f"https://doi.org/{doi}"
        if not production_mode:
            print(f"Attempting to find PDF via publisher page: {landing_url}")
        
        headers = DEFAULT_HEADERS
        response = http_get(landing_url, headers=headers, allow_redirects=True, timeout=20)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # --- Heuristics to find the PDF link ---
        # This may need to be expanded for different publishers
        for link in soup.find_all('a', href=True):
            href = link['href']
            # Rule 1: Direct link to a .pdf file
            if href.lower().endswith('.pdf'):
                if not production_mode:
                    print(f"Found potential PDF link (ends with .pdf): {href}")
                # Handle relative URLs
                return requests.compat.urljoin(response.url, href)
            
            # Rule 2: Link contains '/pdf/' which is common (e.g., Wiley, Springer)
            if '/pdf/' in href or '/content/pdf/' in href:
                if not production_mode:
                    print(f"Found potential PDF link (contains /pdf/): {href}")
                return requests.compat.urljoin(response.url, href)

            # Rule 3: Link text suggests it's a PDF download
            if 'pdf' in link.text.lower() or 'full text' in link.text.lower():
                if not production_mode:
                    print(f"Found potential PDF link (text match): {href}")
                return requests.compat.urljoin(response.url, href)

        if not production_mode:
            print("Could not find a direct PDF link on the publisher page.")
        return None

    except Exception as e:
        if not production_mode:
            print(f"Error fetching from publisher page: {e}")
        return None

# function: Download English-paper by DOI
def GetDownloadUrl(doi, scihub_domains: list[str] | None = None):
    base_urls = scihub_domains or SCIHUB_DOMAINS or [
        "https://sci-hub.se",
        "https://sci-hub.st",
        "https://sci-hub.ru",
        "https://sci-hub.wf",
        "https://sci-hub.ee",
    ]
    for base_url in base_urls:
        url = f"{base_url}/{doi}"
        try:
            if not production_mode:
                print(f"Trying URL: {url}")
            r = http_get(url, timeout=10, headers=DEFAULT_HEADERS)
            if r.status_code == 200 and r.text:
                # Try to parse direct PDF URL from Sci-Hub page
                pdf = parse_scihub_pdf_url(r.text, r.url)
                if pdf:
                    return pdf
                return url
            else:
                if not production_mode:
                    print(f"Failed with status code: {r.status_code}")
        except requests.exceptions.RequestException as e:
            if not production_mode:
                print(f"Error accessing {url}: {e}")
    raise ConnectionError("All Sci-Hub domains failed.")

def parse_scihub_pdf_url(html: str, base_url: str) -> str | None:
    """Parse a likely PDF url from Sci-Hub HTML.
    Heuristics:
      - <iframe src="...pdf"> or <embed src="...pdf">
      - citation pdf links in <a> tags
    """
    try:
        soup = BeautifulSoup(html, 'html.parser')
        # iframe/pdf
        for tag in soup.find_all(['iframe', 'embed'], src=True):
            src = tag.get('src')
            if not src:
                continue
            if src.lower().endswith('.pdf') or 'pdf' in src.lower():
                return requests.compat.urljoin(base_url, src)
        # a href pdf
        for a in soup.find_all('a', href=True):
            href = a['href']
            if href.lower().endswith('.pdf') or 'pdf' in href.lower():
                return requests.compat.urljoin(base_url, href)
    except Exception:
        return None
    return None

def get_pdf_from_unpaywall(doi: str, email: str | None) -> str | None:
    """Try obtain OA PDF via Unpaywall API using a contact email.
    Returns direct PDF URL if available, else None.
    """
    if not email:
        return None
    try:
        api = f"https://api.unpaywall.org/v2/{requests.utils.quote(doi)}"
        params = {"email": email}
        r = http_get(api, params=params, headers={"Accept": "application/json", **DEFAULT_HEADERS}, timeout=REQUEST_TIMEOUT)
        r.raise_for_status()
        data = r.json()
        # Prefer best_oa_location.url_for_pdf, fallback to any oa_locations
        def pick(loc):
            if not isinstance(loc, dict):
                return None
            return loc.get("url_for_pdf") or loc.get("url")
        pdf = pick(data.get("best_oa_location"))
        if pdf:
            if not production_mode:
                print(f"Unpaywall best OA PDF: {pdf}")
            return pdf
        for loc in data.get("oa_locations", []) or []:
            pdf = pick(loc)
            if pdf:
                if not production_mode:
                    print(f"Unpaywall OA PDF: {pdf}")
                return pdf
    except Exception as e:
        if not production_mode:
            print(f"Unpaywall lookup failed: {e}")
    return None

# --- OpenAlex cited-by utilities ---
def get_openalex_id_for_doi(doi: str, email: str | None = None) -> str | None:
    doi = normalize_doi(doi)
    if not doi:
        return None
    try:
        url = f"{OPENALEX_BASE}/works/doi:{requests.utils.quote(doi, safe='')}"
        params = {}
        if email:
            params["mailto"] = email
        r = http_get(url, params=params, headers={**DEFAULT_HEADERS, "Accept": "application/json"}, timeout=30)
        if r.status_code == 404:
            return None
        r.raise_for_status()
        data = r.json() or {}
        oid = data.get("id")
        if not oid:
            return None
        return oid.rsplit("/", 1)[-1]
    except Exception:
        return None

def iter_openalex_citing_works(openalex_id: str, email: str | None = None):
    url = f"{OPENALEX_BASE}/works"
    params = {
        "filter": f"cites:{openalex_id}",
        "select": "id,doi,display_name,publication_year",
        "per_page": 200,
        "cursor": "*",
        "sort": "publication_year:desc",
    }
    if email:
        params["mailto"] = email
    while True:
        r = http_get(url, params=params, headers={**DEFAULT_HEADERS, "Accept": "application/json"}, timeout=60)
        r.raise_for_status()
        data = r.json() or {}
        for item in data.get("results", []) or []:
            yield item
        next_cursor = (data.get("meta") or {}).get("next_cursor")
        if not next_cursor:
            break
        params["cursor"] = next_cursor

def get_citing_dois_for_one(doi: str, email: str | None = None, min_year: int | None = None) -> list[str]:
    oid = get_openalex_id_for_doi(doi, email=email)
    if not oid:
        return []
    out: set[str] = set()
    for w in iter_openalex_citing_works(oid, email=email):
        if min_year is not None:
            try:
                wy = int(w.get("publication_year") or 0)
                if wy and wy < min_year:
                    continue
            except Exception:
                pass
        raw = (w.get("doi") or "").strip()
        nd = normalize_doi(raw)
        if nd:
            out.add(nd)
    return sorted(out)


def _load_impact_factors(path: str) -> dict:
    try:
        if path and os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                # Expect mapping of issn/title(lower)->float
                return {k.lower(): float(v) for k, v in data.items()}
    except Exception:
        pass
    return {}


def _get_impact_for_meta(meta: dict | None) -> float | None:
    """Try to find an impact factor from IMPACT_FACTORS using ISSN(s) or container-title.
    Return numeric impact or None if not found."""
    if not meta:
        return None
    # ISSN from Crossref may be in 'ISSN' or 'issn'
    issns = meta.get('ISSN') or meta.get('issn') or []
    for issn in issns:
        v = IMPACT_FACTORS.get(issn.lower())
        if v is not None:
            return v
    # try container-title
    ct = ''
    try:
        ct = ((meta.get('container-title') or []) + (meta.get('container_title') or []) )
    except Exception:
        ct = meta.get('container-title') or []
    if isinstance(ct, list) and ct:
        name = ct[0].lower()
        v = IMPACT_FACTORS.get(name)
        if v is not None:
            return v
    # fallback: try title of journal if available
    journal = (meta.get('short-container-title') or [])
    if isinstance(journal, list) and journal:
        v = IMPACT_FACTORS.get(journal[0].lower())
        if v is not None:
            return v
    return None


def _score_for_doi(doi: str) -> float:
    """Return a numeric score for ranking based on article citation count (Crossref is-referenced-by-count)."""
    meta = get_crossref_metadata(doi)
    if not meta:
        return 0.0
    cnt = meta.get('is-referenced-by-count') or 0
    try:
        return float(cnt)
    except Exception:
        return 0.0


def _select_top_n(dois: list[str], n: int) -> list[str]:
    if not dois or n is None or n <= 0:
        return dois
    scored = []
    for d in dois:
        try:
            s = _score_for_doi(d)
        except Exception:
            s = 0.0
        scored.append((s, d))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [d for _, d in scored[:n]]


def _min_year_cutoff() -> int | None:
    if RECENT_YEARS is None or RECENT_YEARS <= 0:
        return None
    try:
        return datetime.now().year - RECENT_YEARS + 1
    except Exception:
        return None


def _is_recent_doi(doi: str, min_year: int | None) -> bool:
    if min_year is None:
        return True
    meta = get_crossref_metadata(doi)
    if not meta:
        return False
    y, _m = _extract_pub_year_month(meta)
    try:
        return (y or 0) >= min_year
    except Exception:
        return False

def DownloadFileByUrl(DownloadUrl, FileTitle, subdirectory="main", teacher: str | None = None):
    """
    Downloads a file from a URL and saves it.
    Returns the full path to the saved file, or None if download fails.
    """
    if not DownloadUrl or 'http' not in DownloadUrl:
        if not production_mode:
            print("Invalid download URL provided.")
        return None

    # Sanitize the file name to remove illegal characters
    sane_title = sanitize_file_title(FileTitle)
    file_name = f"{sane_title}.pdf"

    # If saving is restricted to a specific depth, skip others
    if SAVE_ONLY_DEPTH is not None and subdir_to_depth(subdirectory) != SAVE_ONLY_DEPTH:
        # We still consider the download logically successful for recursion, but do not persist or verify file
        if not production_mode:
            print(f"Skip saving (only depth={SAVE_ONLY_DEPTH}): {subdirectory}")
        return None

    # Ensure the save path exists
    folder_teacher = sanitize_folder_name(teacher or "sample")
    save_path = os.path.join(OUTPUT_ROOT_PDF, folder_teacher, subdirectory)
    os.makedirs(save_path, exist_ok=True)
    full_path = os.path.join(save_path, file_name)
    part_path = full_path + ".part"

    try:
        if not production_mode:
            print(f"Downloading from: {DownloadUrl}")
        # Prepare for resume if partial exists
        existing = 0
        if os.path.exists(part_path):
            try:
                existing = os.path.getsize(part_path)
            except Exception:
                existing = 0
        dl_headers = {**DEFAULT_HEADERS, "Accept": "application/pdf,application/octet-stream;q=0.9,*/*;q=0.8"}
        if existing > 0:
            dl_headers["Range"] = f"bytes={existing}-"
        # Stream the response to reduce memory footprint and start writing early
        with session.get(DownloadUrl, timeout=60, headers=dl_headers, stream=True) as r:
            # If server doesn't support range it may return 200; if we tried to resume, restart from 0
            if existing > 0 and r.status_code == 200:
                if not production_mode:
                    print("Server does not support resume (Range). Restarting from beginning.")
                existing = 0
            r.raise_for_status()

            content_type = (r.headers.get('Content-Type') or '').lower()
            wrote_any = False

            # When starting from 0, validate first chunk to ensure it's a PDF
            need_header_check = (existing == 0)

            # Open file handle appropriately
            mode = "ab" if existing > 0 else "wb"
            with open(part_path, mode) as code:
                if existing == 0:
                    first_chunk = None
                for chunk in r.iter_content(chunk_size=1024 * 256):  # 256KB chunks
                    if not chunk:
                        continue
                    if need_header_check:
                        if first_chunk is None:
                            first_chunk = chunk
                            # Validate PDF content early
                            is_pdf = ('pdf' in content_type) or (first_chunk[:4] == b'%PDF')
                            if not is_pdf:
                                if not production_mode:
                                    print(f"Error: The content at the URL is not a PDF. Content-Type: {r.headers.get('Content-Type')}")
                                    print("Skipping download.")
                                return None
                            code.write(first_chunk)
                            wrote_any = True
                            continue
                    code.write(chunk)
                    wrote_any = True

        # Move .part to final path atomically only if we actually wrote data this round,
        # or we resumed from a non-empty partial and size increased.
        moved = False
        try:
            grew = False
            if os.path.exists(part_path):
                try:
                    size_now = os.path.getsize(part_path)
                    grew = (existing > 0 and size_now > existing)
                except Exception:
                    grew = False
            if wrote_any or grew:
                try:
                    os.replace(part_path, full_path)
                    moved = True
                except Exception:
                    # Fallback copy
                    try:
                        shutil.copy2(part_path, full_path)
                        os.remove(part_path)
                        moved = True
                    except Exception:
                        pass
        except Exception:
            pass

        if production_mode:
            print(f"Downloaded: {file_name}")
        else:
            if wrote_any:
                print(f"File '{file_name}' has been downloaded successfully to '{save_path}'.")
            else:
                print(f"Download produced no data for '{file_name}'.")
        return full_path if (moved or wrote_any) else None
    except requests.exceptions.RequestException as e:
        if not production_mode:
            print(f"Failed to download file: {e}")
        return None

_folder_history_locks: dict[str, threading.Lock] = {}

def _get_folder_history_lock(folder: str) -> threading.Lock:
    # one lock per folder path
    lock = _folder_history_locks.get(folder)
    if lock is None:
        lock = threading.Lock()
        _folder_history_locks[folder] = lock
    return lock

def _extract_authors_from_meta(meta: dict | None) -> list[str]:
    authors: list[str] = []
    if not meta:
        return authors
    for a in meta.get('author') or []:
        name = a.get('name')
        if not name:
            given = (a.get('given') or '').strip()
            family = (a.get('family') or '').strip()
            name = (given + ' ' + family).strip()
        if name:
            authors.append(name)
    return authors

def _extract_pub_year_month(meta: dict | None) -> tuple[int | None, int | None]:
    def pick_date(m: dict, key: str):
        obj = m.get(key) if m else None
        parts = (obj or {}).get('date-parts') or []
        if parts and isinstance(parts[0], list):
            arr = parts[0]
            year = arr[0] if len(arr) > 0 else None
            month = arr[1] if len(arr) > 1 else None
            return year, month
        return None, None
    if not meta:
        return None, None
    for k in ('published-print', 'published_online', 'published-online', 'issued'):
        y, m = pick_date(meta, k)
        if y:
            return y, m
    return None, None

def _get_young_authors_from_meta(meta: dict | None, keywords: list[str] | None) -> list[str]:
    if not meta:
        return []
    kw = [k.lower() for k in (keywords or DEFAULT_YOUNG_KEYWORDS)]
    young: list[str] = []
    for a in meta.get('author') or []:
        affs = a.get('affiliation') or []
        hit = False
        for aff in affs:
            name = (aff.get('name') or '').lower()
            if any(k in name for k in kw):
                hit = True
                break
        if hit:
            name = a.get('name') or (f"{a.get('given','').strip()} {a.get('family','').strip()}".strip())
            if name:
                young.append(name)
    return young

def _update_folder_history(teacher: str | None, subdirectory: str, entry: dict):
    folder_teacher = sanitize_folder_name(teacher or "sample")
    folder = os.path.join(OUTPUT_ROOT_PDF, folder_teacher, subdirectory)
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, 'history.json')
    lock = _get_folder_history_lock(folder)
    with lock:
        data = {"items": []}
        try:
            if os.path.exists(path):
                with open(path, 'r', encoding='utf-8') as f:
                    data = json.load(f) or {"items": []}
        except Exception:
            data = {"items": []}
        items = data.get('items') if isinstance(data, dict) else None
        if items is None:
            data = {"items": []}
            items = data['items']
        # upsert by doi
        doi = entry.get('doi')
        updated = False
        for i, it in enumerate(items):
            if isinstance(it, dict) and it.get('doi') == doi:
                items[i] = entry
                updated = True
                break
        if not updated:
            items.append(entry)
        tmp = path + ".tmp"
        try:
            with open(tmp, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            os.replace(tmp, path)
        except Exception:
            # best-effort; ignore write error to not break download pipeline
            pass

def download_and_process_doi(doi, subdirectory="main", teacher: str | None = None, young_keywords: list[str] | None = None, *, download_pdf: bool = True):
    """Helper function to get title, download, verify, and process one DOI."""
    if not production_mode:
        print(f"\n--- Processing DOI: {doi} ---")
    
    # 1. Get the official title from CrossRef as the ground truth
    official_title = get_official_title_from_doi(doi)
    if not official_title:
        if not production_mode:
            print("Could not retrieve official title. Aborting processing for this DOI.")
        return [] # Return empty list of references

    # 2. Get the title from the source page (this will be used for verification)
    page_title, references = GetTitleFromDOI(doi)
    
    # 2.5 Page limit check using Crossref metadata
    try:
        meta = get_crossref_metadata(doi)
        page_count = estimate_page_count_from_metadata(meta)
        if page_count is not None and page_count > MAX_PAGES:
            if not production_mode:
                print(f"Skip download: page count {page_count} exceeds limit {MAX_PAGES}. DOI: {doi}")
            # 不下载，且不再迭代引用
            return []
    except Exception as e:
        if not production_mode:
            print(f"Page count check failed (ignored): {e}")
    
    # Use the official title for the filename for consistency
    if not production_mode:
        print(f"Using official title for filename: '{official_title}'")
    
    # Fast path: history check
    hist = history_get(doi)
    if hist and os.path.exists(hist.get('path', '')):
        # 文件已存在，直接返回引用（若历史中有）
        if production_mode:
            print(f"Cache hit: {hist.get('path')}")
        # 若需要按老师分类且历史文件不在该老师目录，复制到目标老师目录
        try:
            if teacher:
                # 在复制之前进行页数检查，避免复制超过阈值的已缓存论文
                try:
                    meta = get_crossref_metadata(doi)
                    page_count = estimate_page_count_from_metadata(meta)
                    if page_count is not None and page_count > MAX_PAGES:
                        if not production_mode:
                            print(f"Skip copying cached PDF: page count {page_count} exceeds limit {MAX_PAGES}. DOI: {doi}")
                        # 不复制，且不再迭代引用
                        return []
                except Exception as e:
                    if not production_mode:
                        print(f"Page count check (cache copy) failed (ignored): {e}")
                folder_teacher = sanitize_folder_name(teacher)
                # 目标目录
                target_dir = os.path.join(OUTPUT_ROOT_PDF, folder_teacher, subdirectory)
                os.makedirs(target_dir, exist_ok=True)
                desired_name = f"{sanitize_file_title(official_title)}.pdf"
                dst_path = os.path.join(target_dir, desired_name)
                if not os.path.exists(dst_path):
                    shutil.copy2(hist['path'], dst_path)
        except Exception as e:
            if not production_mode:
                print(f"Copy from cache to teacher folder failed: {e}")
        # 写入该子目录的 history.json（使用 Crossref 元数据，避免遗漏）
        try:
            meta2 = get_crossref_metadata(doi)
            authors = _extract_authors_from_meta(meta2)
            y, m = _extract_pub_year_month(meta2)
            young_list = _get_young_authors_from_meta(meta2, young_keywords)
            entry = {
                "title": official_title,
                "doi": normalize_doi(doi),
                "authors": authors,
                "published": {"year": y, "month": m},
                "young_authors": young_list,
            }
            _update_folder_history(teacher, subdirectory, entry)
        except Exception:
            pass
        # 返回当前解析的引用列表用于递归
        return references or []

    # If configured to skip downloading for main layer (only filter main), return references directly
    if not download_pdf and subdirectory == "main":
        if not production_mode:
            print("Skip main PDF download per setting; returning references only.")
        # 仍然返回引用以便后续生成 ref1 与 cited
        return references or []

    # 3. Attempt to get a download URL
    paperDownloadUrl = None
    
    # Strategy A: Prioritize direct download from publisher
    if not production_mode:
        print("\nStep 1: Trying to download directly from publisher (requires VPN for off-campus).")
    paperDownloadUrl = get_pdf_from_publisher(doi)
    
    # Strategy B: Try Unpaywall (OA) if configured
    if not paperDownloadUrl:
        if not production_mode:
            print("Step 2: Trying Unpaywall for Open Access PDF...")
        paperDownloadUrl = get_pdf_from_unpaywall(doi, UNPAYWALL_EMAIL)

    # Strategy C: Fallback to Sci-Hub if above fails
    if not paperDownloadUrl:
        if not production_mode:
            print("Step 3: Falling back to Sci-Hub (may require accessible mirror)...")
        try:
            paperDownloadUrl = GetDownloadUrl(doi, scihub_domains=SCIHUB_DOMAINS)
        except ConnectionError as e:
            if not production_mode:
                print(f"Could not get a download URL from any source for {doi}: {e}")
                print("Proceeding with references only (no file).")
            # 即便下载失败，也返回已解析的引用，允许继续递归
            return references or []

    # 4. Download the file
    downloaded_file_path = DownloadFileByUrl(paperDownloadUrl, official_title, subdirectory, teacher)
    
    # 5. Verify and Cleanup
    if downloaded_file_path:
        if VERIFY_LEVEL == 'off':
            if not production_mode:
                print("Verification disabled; keeping downloaded file.")
            is_verified = True
        else:
            # Compare the official title with the title scraped from the download page
            is_verified = verify_title_similarity(official_title, page_title)

        if not is_verified:
            if not production_mode:
                print(f"Verification failed. Deleting downloaded file: {downloaded_file_path}")
            try:
                os.remove(downloaded_file_path)
                if not production_mode:
                    print("File deleted successfully.")
            except OSError as e:
                if not production_mode:
                    print(f"Error deleting file: {e}")
            # 标题校验失败也继续返回引用，允许递归到下一层
            return references or []
        else:
            if not production_mode:
                print("Verification successful. File has been kept.")
            # 记录历史
            history_set(doi, {
                'title': official_title,
                'path': downloaded_file_path,
                'subdir': subdirectory,
                'teacher': teacher or 'sample',
                'ts': datetime.utcnow().isoformat() + 'Z'
            })
            # 写入子目录 history.json
            try:
                meta2 = get_crossref_metadata(doi)
                authors = _extract_authors_from_meta(meta2)
                y, m = _extract_pub_year_month(meta2)
                young_list = _get_young_authors_from_meta(meta2, young_keywords)
                entry = {
                    "title": official_title,
                    "doi": normalize_doi(doi),
                    "authors": authors,
                    "published": {"year": y, "month": m},
                    "young_authors": young_list,
                }
                _update_folder_history(teacher, subdirectory, entry)
            except Exception:
                pass
            return references
    
    # 下载失败也返回引用，让递归继续
    return references or []

def download_with_references(initial_doi, depth=1, teacher: str | None = None):
    """
    Downloads a paper and recursively downloads its references up to a specified depth.
    """
    from collections import deque
    dois_to_process = deque([(initial_doi, 0, "main")])
    processed_dois = set()
    total_downloads = 0

    while dois_to_process:
        doi, current_depth, subdirectory = dois_to_process.popleft()

        if doi in processed_dois:
            if not production_mode:
                print(f"Skipping already processed DOI: {doi}")
            continue

        if current_depth > depth:
            if not production_mode:
                print(f"Reached max depth ({depth}). Skipping DOI: {doi}")
            continue

        processed_dois.add(doi)

        if production_mode:
            total_downloads += 1
            print(f"[{total_downloads}/{len(processed_dois) + len(dois_to_process)}] Processing DOI: {doi} at depth {current_depth}")

        references = download_and_process_doi(doi, subdirectory, teacher, None)
        if not references or not isinstance(references, list):
            continue
        # 去重，只添加未处理过的DOI
        new_refs = set(references) - processed_dois
        if new_refs and current_depth < depth:
            if not production_mode:
                print(f"Queueing {len(new_refs)} references for download...")
            for ref_doi in new_refs:
                dois_to_process.append((ref_doi, current_depth + 1, f"ref{current_depth + 1}"))

    print(f"\n--- Iterative download complete. Total unique articles processed: {len(processed_dois)} ---")


def download_with_references_concurrent(initial_doi: str, depth: int = 1, max_workers: int = 4,
                                        young_filter: bool = False, young_depth: int = 2,
                                        young_keywords: list[str] | None = None,
                                        copy_ref1_young_to_ref2: bool = True,
                                        teacher: str | None = None,
                                        cited: bool = True):
    """
    Concurrent BFS download: per depth level, download all DOIs concurrently, then expand to next level.
    """
    initial_doi = normalize_doi(initial_doi)
    processed_dois = set()
    current_level = {initial_doi}

    # --- checkpoint helpers ---
    def _ckpt_name() -> str:
        t = sanitize_folder_name(teacher or "sample")
        # keep DOI chars safe
        d = sanitize_file_title(initial_doi)
        return f"task__{t}__{d}.json"

    def _ckpt_path() -> str:
        base = CHECKPOINT_DIR or os.path.join(OUTPUT_ROOT_PDF, ".checkpoints")
        try:
            os.makedirs(base, exist_ok=True)
        except Exception:
            pass
        return os.path.join(base, _ckpt_name())

    def _save_ckpt(state: dict):
        if not ENABLE_CHECKPOINT:
            return
        try:
            path = _ckpt_path()
            tmp = path + ".tmp"
            with open(tmp, 'w', encoding='utf-8') as f:
                json.dump(state, f, ensure_ascii=False, indent=2)
            os.replace(tmp, path)
        except Exception:
            pass

    def _load_ckpt() -> dict | None:
        if not ENABLE_CHECKPOINT:
            return None
        try:
            path = _ckpt_path()
            if os.path.exists(path):
                with open(path, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except Exception:
            return None
        return None

    def _clear_ckpt():
        try:
            path = _ckpt_path()
            if os.path.exists(path):
                os.remove(path)
        except Exception:
            pass

    # Try resume
    start_depth = 0
    cited_done = False
    if RESUME_FROM_CHECKPOINT:
        ck = _load_ckpt()
        if ck and ck.get("root_doi") == initial_doi and (ck.get("teacher") == (teacher or "sample")):
            try:
                start_depth = int(ck.get("current_depth") or 0)
                processed_dois = set(ck.get("processed", []) or [])
                current_level = set(ck.get("current_level", []) or current_level)
                cited_done = bool(ck.get("cited_done", False))
                if not production_mode:
                    print(f"Resumed from checkpoint: depth={start_depth}, processed={len(processed_dois)}, current_level={len(current_level)}")
            except Exception:
                pass

    for d in range(start_depth, max(0, depth) + 1):
        if not current_level:
            break
        subdir = "main" if d == 0 else f"ref{d}"
        # 剔除已处理
        batch = [doi for doi in current_level if doi not in processed_dois]
        if not batch:
            current_level = set()
            continue

        if production_mode:
            print(f"Depth {d}: scheduling {len(batch)} downloads -> folder '{subdir}' with {max_workers} workers")

        next_level = set()
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            # 当仅下载 ref1 与 cited 时，在 main 层不下载 PDF，仅提取引用
            if ONLY_REF1_AND_CITED and d == 0:
                future_map = {executor.submit(download_and_process_doi, doi, subdir, teacher, young_keywords, download_pdf=False): doi for doi in batch}
            else:
                future_map = {executor.submit(download_and_process_doi, doi, subdir, teacher, young_keywords): doi for doi in batch}
            for fut in as_completed(future_map):
                doi = future_map[fut]
                try:
                    refs = fut.result() or []
                    processed_dois.add(doi)
                    # 新增：默认将 ref1 层中判定为“年轻作者”的文章复制一份到 ref2 目录，便于集中查看。
                    # 仅当允许保存 ref2 时才执行复制（与 SAVE_ONLY_DEPTH 兼容）
                    if copy_ref1_young_to_ref2 and d == 1 and (SAVE_ONLY_DEPTH is None or SAVE_ONLY_DEPTH == 2):
                        try:
                            if paper_has_young_author(doi, young_keywords):
                                # 从历史中找到已下载文件路径
                                hist = history_get(doi) or {}
                                src_path = hist.get('path')
                                if src_path and os.path.exists(src_path):
                                    # 目标目录为 ref2
                                    folder_teacher = sanitize_folder_name(teacher or "sample")
                                    target_dir = os.path.join(OUTPUT_ROOT_PDF, folder_teacher, f"ref{d+1}")
                                    os.makedirs(target_dir, exist_ok=True)
                                    dst_path = os.path.join(target_dir, os.path.basename(src_path))
                                    if not os.path.exists(dst_path):
                                        shutil.copy2(src_path, dst_path)
                                        if not production_mode:
                                            print(f"Copied young-author paper from ref1 to ref2: {os.path.basename(dst_path)}")
                                else:
                                    if not production_mode:
                                        print(f"Skip copying (file not found for DOI): {doi}")
                        except Exception as e:
                            if not production_mode:
                                print(f"Copy-to-ref2 failed for {doi}: {e}")
                    # 规范化引用DOI并去重；先收集父条目的所有候选项，以便按 TOP_N（若配置）与近 m 年筛选
                    candidates: list[str] = []
                    for r in refs:
                        r_norm = normalize_doi(r)
                        if not r_norm or r_norm in processed_dois:
                            continue
                        # 若开启年轻作者筛选，且下一层正好是目标层，则过滤
                        if young_filter and (d + 1) == young_depth:
                            try:
                                if not paper_has_young_author(r_norm, young_keywords):
                                    if not production_mode:
                                        print(f"Filtered (no young author): {r_norm}")
                                    continue
                            except Exception as e:
                                if not production_mode:
                                    print(f"Young-author check error for {r_norm}: {e}")
                                continue
                        # 若配置了近 m 年，并且目标是生成 ref1（d+1==1），按年份过滤
                        if (d + 1) == 1:
                            cut = _min_year_cutoff()
                            if cut is not None and not _is_recent_doi(r_norm, cut):
                                if not production_mode:
                                    print(f"Filtered (older than {cut}): {r_norm}")
                                continue
                        candidates.append(r_norm)

                    # 如果在生成 ref{d+1}（例如 ref1）阶段启用了 TOP_N，则对该父条目的候选按影响因子/引用数排序并取前 N
                    if TOP_N_REF and (d + 1) == 1:
                        try:
                            chosen = _select_top_n(candidates, TOP_N_REF)
                        except Exception:
                            chosen = candidates
                    else:
                        chosen = candidates

                    for r_norm in chosen:
                        next_level.add(r_norm)
                except Exception as e:
                    if not production_mode:
                        print(f"Error processing DOI {doi}: {e}")
                    processed_dois.add(doi)

        # Persist checkpoint at a safe point (end of a depth before cited-by)
        _save_ckpt({
            "version": 1,
            "root_doi": initial_doi,
            "teacher": teacher or "sample",
            "current_depth": d,
            "processed": sorted(processed_dois),
            "current_level": sorted(next_level),
            "cited_done": cited_done,
            "ts": datetime.utcnow().isoformat() + 'Z'
        })

        # After finishing depth 0 (main), optionally fetch and download 'cited-by' set (no further recursion)
        if d == 0 and cited and not cited_done:
            try:
                cited_set: set[str] = set()
                for root_doi in batch:
                    try:
                        cdois = get_citing_dois_for_one(root_doi, email=OPENALEX_MAILTO, min_year=_min_year_cutoff())
                    except Exception:
                        cdois = []
                    # apply per-root TOP_N filtering when configured
                    cdois_norm = [normalize_doi(x) for x in cdois if normalize_doi(x) and normalize_doi(x) not in processed_dois]
                    if TOP_N_CITED:
                        try:
                            pick = _select_top_n(cdois_norm, TOP_N_CITED)
                        except Exception:
                            pick = cdois_norm
                    else:
                        pick = cdois_norm
                    for nd in pick:
                        if nd and nd not in processed_dois:
                            cited_set.add(nd)
                if cited_set:
                    if production_mode:
                        print(f"Depth 0: scheduling {len(cited_set)} cited-by downloads -> folder 'cited'")
                    with ThreadPoolExecutor(max_workers=max_workers) as cexec:
                        cmap = {cexec.submit(download_and_process_doi, cd, "cited", teacher, young_keywords): cd for cd in cited_set}
                        for cfut in as_completed(cmap):
                            cdoi = cmap[cfut]
                            try:
                                _ = cfut.result()  # ignore returned refs for cited
                            except Exception as ce:
                                if not production_mode:
                                    print(f"Error processing cited-by DOI {cdoi}: {ce}")
                            finally:
                                processed_dois.add(cdoi)
            except Exception as e:
                if not production_mode:
                    print(f"Failed to fetch/process cited-by DOIs: {e}")
            finally:
                cited_done = True
                # Save after cited-by completion
                _save_ckpt({
                    "version": 1,
                    "root_doi": initial_doi,
                    "teacher": teacher or "sample",
                    "current_depth": d,
                    "processed": sorted(processed_dois),
                    "current_level": sorted(next_level),
                    "cited_done": True,
                    "ts": datetime.utcnow().isoformat() + 'Z'
                })

        current_level = next_level

    print(f"\n--- Concurrent iterative download complete. Total unique articles processed: {len(processed_dois)} ---")
    # Clear checkpoint on success
    _clear_ckpt()


def parse_results_file(path: str) -> dict:
    """Parse a results.txt file to extract mapping: teacher -> list of DOIs.
    Supports formats like:
      --- 姓名 (机构) ---
      OpenAlex Profile: <url>
      Combined DOIs (N found):
      1. 10.xxxx/xxxx
      2. ...
    Lines without DOIs are ignored. DOIs are detected anywhere in the line.
    """
    teacher_to_dois: dict[str, list[str]] = {}
    current_teacher: str | None = None
    # Header like: --- 姓名 (机构) ---  or  --- 姓名 ---
    teacher_header = re.compile(r"^---\s*(.+?)\s*(?:\([^)]*\))?\s*---\s*$")
    doi_regex = re.compile(r"10\.\d{4,9}/[-._;()/:A-Z0-9]+", re.I)
    try:
        with open(path, 'r', encoding='utf-8') as f:
            for raw in f:
                line = raw.strip()
                if not line:
                    continue
                m = teacher_header.match(line)
                if m:
                    current_teacher = m.group(1).strip()
                    teacher_to_dois.setdefault(current_teacher, [])
                    continue
                if not current_teacher:
                    continue
                # Skip obviously non-DOI lines
                if (
                    line.lower().startswith("openalex profile:") or
                    line.lower().startswith("combined dois") or
                    "未能获取到任何DOI" in line
                ):
                    # keep empty list
                    continue
                # Extract any DOIs found in this line
                for d in doi_regex.findall(line):
                    nd = normalize_doi(d)
                    if nd and nd not in teacher_to_dois[current_teacher]:
                        teacher_to_dois[current_teacher].append(nd)
    except FileNotFoundError:
        print(f"results file not found: {path}")
    except Exception as e:
        print(f"Error parsing results file '{path}': {e}")
    return teacher_to_dois


# --- Main Execution ---
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download scientific articles and their references.")
    parser.add_argument('--prod', action='store_true', help='Enable production mode for simplified output.')
    parser.add_argument('--doi', type=str, help='DOI(s) to download; comma or space separated.')
    parser.add_argument('--teacher', type=str, default=None, help='Teacher name for output folder when using --doi (defaults to sample).')
    parser.add_argument('--depth', type=int, default=1, help='Depth for recursive reference download (>=0).')
    parser.add_argument('--workers', type=int, default=4, help='Max concurrent downloads per level.')
    parser.add_argument('--young', action='store_true', help='Enable filtering for young authors at a target depth (default depth=2).')
    parser.add_argument('--young-depth', type=int, default=2, help='Depth at which to apply young-author filtering (default 2).')
    parser.add_argument('--young-keywords', type=str, default=None, help='Comma-separated keywords to detect young authors in affiliations.')
    # 默认启用将 ref1 的年轻作者文章复制到 ref2，可用该开关禁用
    parser.add_argument('--no-copy-ref1-young-to-ref2', dest='copy_ref1_young_to_ref2', action='store_false',
                        help='Disable copying young-author papers from ref1 to ref2 (enabled by default).')
    parser.add_argument('--rps', type=float, default=0.0, help='Global rate limit (requests per second). 0 = unlimited.')
    parser.add_argument('--retries', type=int, default=None, help='Total HTTP retries (override default).')
    parser.add_argument('--backoff', type=float, default=None, help='HTTP retry backoff factor (override default).')
    parser.add_argument('--timeout', type=float, default=None, help='HTTP request timeout in seconds (override default).')
    parser.add_argument('--pool-maxsize', type=int, default=None, help='HTTP connection pool max size; defaults to ~workers*4 when not set.')
    parser.add_argument('--unpaywall-email', type=str, default=None, help='Optional email for Unpaywall API to find OA PDFs.')
    parser.add_argument('--openalex-email', type=str, default=None, help='Optional email (mailto) for OpenAlex requests when fetching cited-by DOIs.')
    parser.add_argument('--verify', type=str, choices=['strict', 'light', 'off'], default='strict', help='Verification strategy: strict (default), light (Crossref-first), or off (skip).')
    parser.add_argument('--no-rank-main', action='store_true', help='Do not rank/sort main DOIs by Crossref citation count (faster).')
    parser.add_argument('--top-n', type=int, default=None, help='Legacy: keep top N for ref1/cited by citation count; overrides config.ini when specific values are not set')
    parser.add_argument('--top-n-main', type=int, default=None, help='Keep top N main DOIs by citation count; overrides config.ini')
    parser.add_argument('--top-n-ref', type=int, default=None, help='Keep top N ref1 DOIs by citation count; overrides config.ini')
    parser.add_argument('--top-n-cited', type=int, default=None, help='Keep top N cited DOIs by citation count; overrides config.ini')
    parser.add_argument('--impact-factors', type=str, default=None, help='Path to JSON file mapping ISSN or journal name to impact factor; overrides config.ini')
    parser.add_argument('--recent-years', type=int, default=None, help='Only keep articles within the last M years for ref1 and cited; overrides config.ini')
    parser.add_argument('--scihub-domains', type=str, default=None, help='Comma-separated Sci-Hub base URLs to try in order.')
    parser.add_argument('--from-results', type=str, nargs='?', const='AUTO', default='AUTO',
                        help='Read DOIs from results.txt and download into per-teacher folders. Optional custom path.')
    parser.add_argument('--pdf-root', type=str, default=None, help='Base output folder for PDFs (default ./Downloads_pdf).')
    parser.add_argument('--save-only-depth', type=int, default=None, help='Only save PDFs for this depth (0=main,1=ref1,2=ref2,...)')
    parser.add_argument('--max-pages', type=int, default=30, help='Maximum page count to download; skip if exceeded (default 30).')
    # Cited-by control: enabled by default; use --no-cited to disable
    parser.add_argument('--no-cited', dest='cited', action='store_false', help='Disable downloading cited-by (被引) articles for root DOIs. Enabled by default.')
    # New: only filter main, and download ref1 & cited results
    parser.add_argument('--only-ref1-cited', action='store_true', help='先筛选 main，不下载 main PDF；仅下载 ref1 与 cited 的筛选结果。')
    # Checkpoint & resume
    parser.add_argument('--resume', action='store_true', help='从上次断点继续（如果存在 checkpoint）。')
    parser.add_argument('--no-checkpoint', action='store_true', help='运行时不写入 checkpoint。')
    parser.add_argument('--checkpoint-dir', type=str, default=None, help='自定义 checkpoint 存放目录（默认在 Downloads_pdf/.checkpoints）。')
    parser.set_defaults(cited=True)
    args = parser.parse_args()

    if args.prod:
        production_mode = True
        print("--- Running in Production Mode ---")

    # Configure HTTP knobs from CLI
    configure_http(retries=args.retries, backoff=args.backoff, timeout=args.timeout, rps=args.rps)
    # Configure HTTP pool sizes based on workers (if not explicitly provided)
    try:
        pool_sz = args.pool_maxsize if args.pool_maxsize is not None else max(10, int(args.workers) * 4)
        configure_http_pool(pool_connections=pool_sz, pool_maxsize=pool_sz)
    except Exception:
        pass

    # Configure outputs
    configure_outputs(args.pdf_root)
    # Configure checkpointing
    try:
        configure_checkpoint(dir_path=args.checkpoint_dir, enable=(not getattr(args, 'no_checkpoint', False)), resume=getattr(args, 'resume', False))
    except Exception:
        pass
    # Restrict saving to a specific depth, if requested
    SAVE_ONLY_DEPTH = args.save_only_depth
    # Page count threshold
    try:
        if isinstance(args.max_pages, int) and args.max_pages > 0:
            MAX_PAGES = args.max_pages
    except Exception:
        pass

    # Optional integrations
    UNPAYWALL_EMAIL = args.unpaywall_email or None
    OPENALEX_MAILTO = args.openalex_email or None
    # Verification level
    try:
        VERIFY_LEVEL = args.verify
    except Exception:
        VERIFY_LEVEL = 'strict'
    # Behavior
    ONLY_REF1_AND_CITED = bool(getattr(args, 'only_ref1_cited', False))
    # Load config.ini defaults (if present) and possibly override with CLI
    cfg = configparser.ConfigParser()
    # Prefer UTF-8 to avoid Windows default cp936/gbk decoding issues
    cfg_path = os.path.join(os.getcwd(), 'config.ini')
    try:
        cfg.read(cfg_path, encoding='utf-8')
    except Exception:
        # Fallback to default encoding if UTF-8 read fails
        cfg.read(cfg_path)
    cfg_top_n = None
    cfg_top_n_main = None
    cfg_top_n_ref = None
    cfg_top_n_cited = None
    cfg_ifpath = None
    cfg_recent_years = None
    try:
        if cfg.has_section('download'):
            cfg_top_n = cfg.getint('download', 'top_n', fallback=None)  # legacy
            cfg_top_n_main = cfg.getint('download', 'top_n_main', fallback=None)
            cfg_top_n_ref = cfg.getint('download', 'top_n_ref', fallback=None)
            cfg_top_n_cited = cfg.getint('download', 'top_n_cited', fallback=None)
            cfg_ifpath = cfg.get('download', 'impact_factors', fallback='').strip() or None
            ry = cfg.get('download', 'recent_years', fallback='').strip()
            cfg_recent_years = int(ry) if ry.isdigit() else None
    except Exception:
        cfg_top_n = None
        cfg_ifpath = None
    # Final top_n and impact_factors path
    impact_factors_path = args.impact_factors or cfg_ifpath
    # Top-N resolution with precedence: specific CLI > specific config > legacy CLI (--top-n) > legacy config (top_n)
    final_top_n_main = args.top_n_main if args.top_n_main is not None else cfg_top_n_main
    final_top_n_ref = args.top_n_ref if args.top_n_ref is not None else cfg_top_n_ref
    final_top_n_cited = args.top_n_cited if args.top_n_cited is not None else cfg_top_n_cited
    legacy_n = args.top_n if args.top_n is not None else cfg_top_n
    TOP_N_MAIN = final_top_n_main if final_top_n_main is not None else None
    TOP_N_REF = final_top_n_ref if final_top_n_ref is not None else legacy_n
    TOP_N_CITED = final_top_n_cited if final_top_n_cited is not None else legacy_n
    # Keep legacy TOP_N for any remaining internal fallback uses
    TOP_N = legacy_n
    IMPACT_FACTORS = _load_impact_factors(impact_factors_path) if impact_factors_path else {}
    # Set recent years window
    try:
        RECENT_YEARS = args.recent_years if args.recent_years is not None else cfg_recent_years
    except Exception:
        RECENT_YEARS = None
    if args.scihub_domains:
        SCIHUB_DOMAINS = [u.strip() for u in args.scihub_domains.split(',') if u.strip()]
    else:
        SCIHUB_DOMAINS = None

    # If user provides --doi, run concurrent recursive downloader for those DOIs
    if args.doi:
        # 支持逗号或空白分隔的多DOI输入
        raw = [p.strip() for p in re.split(r'[\s,]+', args.doi) if p.strip()]
        two_all = [normalize_doi(d) for d in raw]
        # Apply recent-years and Top-N for main layer
        cut_main = _min_year_cutoff()
        dois_recent = [d for d in two_all if _is_recent_doi(d, cut_main)] if cut_main is not None else list(two_all)
        # Rank by citation count unless disabled
        if getattr(args, 'no_rank_main', False):
            base_list = dois_recent
        else:
            base_list = sorted(dois_recent, key=lambda x: _score_for_doi(x), reverse=True)
        if TOP_N_MAIN is not None and TOP_N_MAIN > 0:
            dois = base_list[:TOP_N_MAIN]
        else:
            dois = base_list
        print(f"\n=== Running for {len(dois)} DOI(s) with depth={args.depth}, workers={args.workers} ===")
        yk = [s.strip() for s in (args.young_keywords.split(',') if args.young_keywords else []) if s.strip()] or None
        for i, d in enumerate(dois, 1):
            print(f"\n--- Target {i}/{len(dois)}: {d} ---")
            download_with_references_concurrent(d, depth=args.depth, max_workers=args.workers,
                                                young_filter=args.young, young_depth=args.young_depth,
                                                young_keywords=yk,
                                                copy_ref1_young_to_ref2=getattr(args, 'copy_ref1_young_to_ref2', True),
                                                teacher=args.teacher,
                                                cited=args.cited)
        print("\n--- All requested DOI tasks completed. ---")
    else:
        # Default: read DOIs per teacher from results.txt
        # Determine results path
        results_path = None
        if args.from_results and args.from_results != 'AUTO':
            results_path = args.from_results
        else:
            # default to DOIdownloader/results.txt next to this script
            results_path = os.path.join(os.path.dirname(__file__), 'results.txt')

        print(f"\n=== Reading DOIs from: {results_path} ===")
        mapping = parse_results_file(results_path)
        if not mapping:
            print("No DOIs found in results file. Falling back to example DOI.")
            production_mode = True
            default_doi = '10.1038/nphys4074'
            download_with_references_concurrent(default_doi, depth=2, max_workers=args.workers,
                                                young_filter=True, young_depth=2,
                                                copy_ref1_young_to_ref2=True,
                                                teacher='sample',
                                                cited=args.cited)
            print("\n--- Task completed. ---")
        else:
            yk = [s.strip() for s in (args.young_keywords.split(',') if args.young_keywords else []) if s.strip()] or None
            for teacher_name, dois_all in mapping.items():
                if not dois_all:
                    if not production_mode:
                        print(f"Skipping teacher '{teacher_name}': no DOIs.")
                    continue
                # Apply recent-years and Top-N for main layer per teacher
                cut_main = _min_year_cutoff()
                dois_recent = [d for d in dois_all if _is_recent_doi(d, cut_main)] if cut_main is not None else list(dois_all)
                # Rank by citation count unless disabled
                if getattr(args, 'no_rank_main', False):
                    base_list = dois_recent
                else:
                    base_list = sorted(dois_recent, key=lambda x: _score_for_doi(x), reverse=True)
                if TOP_N_MAIN is not None and TOP_N_MAIN > 0:
                    selected = base_list[:TOP_N_MAIN]
                else:
                    selected = base_list
                if not selected:
                    if not production_mode:
                        print(f"Skipping teacher '{teacher_name}': no DOIs after recent-years/top-N filtering.")
                    continue
                print(f"\n=== Teacher: {teacher_name} | {len(selected)}/{len(dois_all)} selected main DOI(s) | depth={args.depth}, workers={args.workers} ===")
                for i, d in enumerate(selected, 1):
                    print(f"\n--- {teacher_name} [{i}/{len(selected)}]: {d} ---")
                    download_with_references_concurrent(d, depth=args.depth, max_workers=args.workers,
                                                        young_filter=args.young, young_depth=args.young_depth,
                                                        young_keywords=yk,
                                                        copy_ref1_young_to_ref2=getattr(args, 'copy_ref1_young_to_ref2', True),
                                                        teacher=teacher_name,
                                                        cited=args.cited)
            print("\n--- All teachers completed. ---")
