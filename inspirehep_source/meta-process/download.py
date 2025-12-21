import argparse
import json
import os
import sys
import time
import uuid
import shutil
import zipfile
import hashlib
import random
import requests
import re
from urllib.parse import unquote
import configparser
import concurrent.futures
import threading
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Optional, Any, Tuple
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

DEFAULT_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}

# ==========================================
# 1. Configuration & Utils
# ==========================================

PROJ_ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = PROJ_ROOT / 'config.ini'
PROGRESS_FILE = PROJ_ROOT / 'inspirehep_source/meta-process/processed.json'
PROGRESS_LOCK = threading.Lock()
GLOBAL_PROCESSED_CACHE = None

METADATA_LOCK = threading.Lock()

def update_teacher_metadata(teacher_dir: Path, new_item: Dict[str, Any]):
    metadata_file = teacher_dir / 'metadata_items.json'
    with METADATA_LOCK:
        existing_items = []
        if metadata_file.exists():
            try:
                with open(metadata_file, 'r', encoding='utf-8') as f:
                    existing_data = json.load(f)
                    existing_items = existing_data.get("items", [])
            except Exception as e:
                print(f"  Warning: Failed to load existing metadata from {metadata_file}: {e}")

        # Deduplicate by DOI (or record_id, or title)
        merged_map = {}
        
        def get_key(itm):
            return itm.get("doi") or itm.get("record_id") or itm.get("title")

        # Add existing items first
        for item in existing_items:
            k = get_key(item)
            if k:
                merged_map[k] = item
        
        # Add/Update with new item
        k = get_key(new_item)
        if k:
            merged_map[k] = new_item

        final_items = list(merged_map.values())

        try:
            with open(metadata_file, 'w', encoding='utf-8') as f:
                json.dump({"items": final_items}, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"  Error saving metadata to {metadata_file}: {e}")

# Import generic downloader
# Use importlib to avoid name collision with current script (also named download.py)
import importlib.util
try:
    doi_source_path = PROJ_ROOT / 'DOI_source' / 'download.py'
    if doi_source_path.exists():
        spec = importlib.util.spec_from_file_location("doi_downloader_module", doi_source_path)
        doi_downloader = importlib.util.module_from_spec(spec)
        sys.modules["doi_downloader_module"] = doi_downloader
        spec.loader.exec_module(doi_downloader)
    else:
        doi_downloader = None
        print(f"Warning: DOI source file not found at {doi_source_path}")
except Exception as e:
    doi_downloader = None
    print(f"Warning: Could not import doi_downloader from DOI_source: {e}")

def load_config():
    config = configparser.ConfigParser()
    if CONFIG_PATH.exists():
        config.read(CONFIG_PATH, encoding='utf-8')
    return config

def sync_processed_from_metadata():
    """
    Sync processed status from metadata_items.json files.
    If have_md is true, add DOI and record_id to processed cache.
    """
    global GLOBAL_PROCESSED_CACHE
    if GLOBAL_PROCESSED_CACHE is None:
        return

    data_dir = PROJ_ROOT / 'data'
    if not data_dir.exists():
        return

    print("Syncing processed status from metadata...")
    count = 0
    
    for teacher_dir in data_dir.iterdir():
        if not teacher_dir.is_dir():
            continue
            
        teacher_name = teacher_dir.name
        metadata_file = teacher_dir / 'metadata_items.json'
        
        if not metadata_file.exists():
            continue
            
        try:
            with open(metadata_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            items = data.get("items", [])
            if teacher_name not in GLOBAL_PROCESSED_CACHE:
                GLOBAL_PROCESSED_CACHE[teacher_name] = set()
                
            teacher_cache = GLOBAL_PROCESSED_CACHE[teacher_name]
            
            for item in items:
                if item.get("have_md") is True:
                    doi = item.get("doi")
                    rid = item.get("record_id")
                    
                    added = False
                    if doi and doi not in teacher_cache:
                        teacher_cache.add(doi)
                        added = True
                    if rid and str(rid) not in teacher_cache:
                        teacher_cache.add(str(rid))
                        added = True
                        
                    if added:
                        count += 1
                        
        except Exception as e:
            print(f"  Error reading metadata for {teacher_name}: {e}")
            
    if count > 0:
        print(f"  Added {count} items to processed cache from metadata.")
        # Save updated cache
        try:
            with open(PROGRESS_FILE, 'w', encoding='utf-8') as f:
                json_data = {k: list(v) for k, v in GLOBAL_PROCESSED_CACHE.items()}
                json.dump(json_data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Failed to save synced progress: {e}")

def load_progress() -> Dict[str, set[str]]:
    global GLOBAL_PROCESSED_CACHE
    if GLOBAL_PROCESSED_CACHE is not None:
        return GLOBAL_PROCESSED_CACHE

    data = defaultdict(set)
    txt_file = PROJ_ROOT / 'inspirehep_source/meta-process/processed.txt'
    
    loaded_list = []
    is_legacy_list = False

    if txt_file.exists() and not PROGRESS_FILE.exists():
        print("Migrating processed.txt to processed.json...")
        try:
            with open(txt_file, 'r', encoding='utf-8') as f:
                loaded_list = [line.strip() for line in f if line.strip()]
            txt_file.rename(txt_file.with_suffix('.txt.bak'))
            is_legacy_list = True
        except Exception as e:
            print(f"Migration failed: {e}")
    elif PROGRESS_FILE.exists():
        try:
            with open(PROGRESS_FILE, 'r', encoding='utf-8') as f:
                content = json.load(f)
                if isinstance(content, list):
                    loaded_list = content
                    is_legacy_list = True
                elif isinstance(content, dict):
                    for k, v in content.items():
                        data[k] = set(v)
        except Exception:
            pass
            
    if is_legacy_list:
        for item in loaded_list:
            if '|' in item:
                t, d = item.split('|', 1)
                data[t].add(d)
        # Save immediately in new format
        try:
            with open(PROGRESS_FILE, 'w', encoding='utf-8') as f:
                json_data = {k: list(v) for k, v in data.items()}
                json.dump(json_data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Failed to save migrated progress: {e}")
            
    GLOBAL_PROCESSED_CACHE = data
    sync_processed_from_metadata()
    return GLOBAL_PROCESSED_CACHE

def save_progress(teacher: str, doi: str):
    global GLOBAL_PROCESSED_CACHE
    with PROGRESS_LOCK:
        if GLOBAL_PROCESSED_CACHE is None:
            load_progress()
            
        if teacher not in GLOBAL_PROCESSED_CACHE:
            GLOBAL_PROCESSED_CACHE[teacher] = set()
            
        if doi not in GLOBAL_PROCESSED_CACHE[teacher]:
            GLOBAL_PROCESSED_CACHE[teacher].add(doi)
            try:
                with open(PROGRESS_FILE, 'w', encoding='utf-8') as f:
                    json_data = {k: list(v) for k, v in GLOBAL_PROCESSED_CACHE.items()}
                    json.dump(json_data, f, ensure_ascii=False, indent=2)
            except Exception as e:
                print(f"Failed to save progress: {e}")

def get_sampling_cfg(config) -> Tuple[Optional[int], Optional[int]]:
    try:
        if config.has_section('download'):
            n_raw = config.get('download', 'sample_threshold', fallback='').strip()
            m_raw = config.get('download', 'sample_size', fallback='').strip()
            n_val = int(n_raw) if n_raw.isdigit() else None
            m_val = int(m_raw) if m_raw.isdigit() else None
            if (n_val is not None and n_val <= 0) or (m_val is not None and m_val <= 0):
                return None, None
            return n_val, m_val
    except Exception:
        pass
    return None, None

def get_worker_cfg(config) -> Tuple[int, int]:
    wm, wr = 4, 6
    try:
        if config.has_section('download'):
            wmr = config.get('download', 'workers_main', fallback='').strip()
            wrr = config.get('download', 'workers_related', fallback='').strip()
            if wmr.isdigit(): wm = max(1, int(wmr))
            if wrr.isdigit(): wr = max(1, int(wrr))
    except Exception:
        pass
    return wm, wr

def get_limit_cfg(config) -> Tuple[int, int]:
    lr, lc = 10, 100
    try:
        # Prioritize [limits] section if it exists
        if config.has_section('limits'):
            r_raw = config.get('limits', 'limit_ref', fallback='').strip()
            c_raw = config.get('limits', 'limit_cited', fallback='').strip()
            if r_raw.isdigit(): lr = int(r_raw)
            if c_raw.isdigit(): lc = int(c_raw)
        # Fallback to [download] section
        elif config.has_section('download'):
            r_raw = config.get('download', 'top_n_ref', fallback='').strip()
            c_raw = config.get('download', 'top_n_cited', fallback='').strip()
            if r_raw.isdigit(): lr = int(r_raw)
            if c_raw.isdigit(): lc = int(c_raw)
    except Exception:
        pass
    return lr, lc

def get_young_author_years(config) -> int:
    val_env = os.getenv("YOUNG_AUTHOR_YEARS")
    if val_env and val_env.isdigit():
        return int(val_env)
    try:
        if config.has_section("metadata") and config.has_option("metadata", "young_author_years"):
            years = config.get("metadata", "young_author_years").strip()
            if years.isdigit():
                return int(years)
    except Exception:
        pass
    return 5

def ensure_dir(path: Path):
    path.mkdir(parents=True, exist_ok=True)

def validate_pdf(path: Path, min_size_kb: int = 10) -> bool:
    """
    Check if a PDF file is valid:
    1. Exists and is a file.
    2. Size is greater than min_size_kb.
    3. Starts with %PDF header.
    """
    if not path.exists() or not path.is_file():
        return False
    
    # Check size
    size_kb = path.stat().st_size / 1024
    if size_kb < min_size_kb:
        print(f"  [Warning] PDF too small ({size_kb:.1f} KB): {path.name}")
        return False
        
    # Check header
    try:
        with open(path, 'rb') as f:
            header = f.read(4)
            if header != b'%PDF':
                print(f"  [Warning] Invalid PDF header: {path.name}")
                return False
    except Exception as e:
        print(f"  [Error] Failed to read PDF header: {e}")
        return False
        
    return True

def _sanitize_dir_name(name: str) -> str:
    return (
        name.replace('/', '_').replace('\\', '_').replace(':', '_')
        .replace('?', '_').replace('*', '_').replace('"', "'")
        .replace('<', '_').replace('>', '_').replace('|', '_')
    )

def parse_year_month(pub_date: Any) -> Dict[str, int]:
    year_month: Dict[str, int] = {}
    if pub_date is None:
        return year_month
    try:
        if isinstance(pub_date, int):
            if 1000 <= pub_date <= 9999:
                year_month["year"] = pub_date
                return year_month
        if isinstance(pub_date, str) and pub_date.strip():
            txt = pub_date.strip()
            for fmt in ("%Y-%m-%d", "%Y-%m", "%Y"):
                try:
                    dt = datetime.strptime(txt, fmt)
                    year_month["year"] = dt.year
                    if fmt in ("%Y-%m-%d", "%Y-%m"):
                        year_month["month"] = dt.month
                    return year_month
                except ValueError:
                    continue
    except Exception:
        pass
    return year_month

# ==========================================
# 2. OpenAlex Utils
# ==========================================

OPENALEX_BASE = "https://api.openalex.org"

def normalize_doi(doi: str) -> str:
    if not doi: return ""
    doi = unquote(doi).strip()
    doi = re.sub(r"^(https?://(dx\.)?doi\.org/|doi:)", "", doi, flags=re.I)
    return doi.strip().strip(' .;')

def get_openalex_id_for_doi(doi: str) -> Optional[str]:
    doi = normalize_doi(doi)
    if not doi: return None
    try:
        url = f"{OPENALEX_BASE}/works/doi:{requests.utils.quote(doi, safe='')}"
        r = requests.get(url, headers=DEFAULT_HEADERS, timeout=30)
        if r.status_code == 404: return None
        r.raise_for_status()
        data = r.json()
        oid = data.get("id")
        return oid.rsplit("/", 1)[-1] if oid else None
    except Exception:
        return None

def get_citing_dois_openalex(doi: str, limit: int = 100) -> List[str]:
    oid = get_openalex_id_for_doi(doi)
    if not oid: return []
    
    url = f"{OPENALEX_BASE}/works"
    params = {
        "filter": f"cites:{oid}",
        "select": "doi",
        "per_page": min(limit, 200),
        "sort": "publication_year:desc",
    }
    
    dois = set()
    try:
        while len(dois) < limit:
            r = requests.get(url, params=params, headers=DEFAULT_HEADERS, timeout=60)
            r.raise_for_status()
            data = r.json()
            results = data.get("results", [])
            if not results: break
            
            for item in results:
                d = item.get("doi")
                if d:
                    nd = normalize_doi(d)
                    if nd: dois.add(nd)
            
            if len(dois) >= limit: break
            
            cursor = (data.get("meta") or {}).get("next_cursor")
            if not cursor: break
            params["cursor"] = cursor
            
    except Exception as e:
        print(f"OpenAlex error: {e}")
        
    return list(dois)[:limit]

# ==========================================
# 3. InspireHEP Client
# ==========================================

class InspireHEPClient:
    BASE_URL = "https://inspirehep.net/api"
    
    def __init__(self, timeout: int = 30):
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update(DEFAULT_HEADERS)
        self.session.headers.update({
            "Accept": "application/json",
        })
        retries = Retry(
            total=5, 
            backoff_factor=1.0, 
            status_forcelist=(429, 500, 502, 503, 504),
            allowed_methods=("GET", "HEAD")
        )
        adapter = HTTPAdapter(pool_connections=64, pool_maxsize=64, max_retries=retries)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)
    
    def _request(self, url: str, params: Optional[Dict] = None, stream: bool = False, **kwargs) -> requests.Response:
        # Random sleep to distribute requests and avoid hitting rate limits
        if "arxiv.org" in url:
            time.sleep(random.uniform(3.0, 5.0))
        else:
            time.sleep(random.uniform(0.5, 1.5))
            
        response = self.session.get(url, params=params, timeout=self.timeout, stream=stream, **kwargs)
        response.raise_for_status()
        return response

    def search_literature(self, query: str, size: int = 10, page: int = 1, fields: Optional[str] = None) -> Dict:
        url = f"{self.BASE_URL}/literature"
        params = {"q": query, "size": size, "page": page}
        if fields: params["fields"] = fields
        return self._request(url, params=params).json()

    def find_record_by_doi(self, doi: str) -> Optional[Dict]:
        query = f"doi:{doi}"
        # Reverted to full fetch to ensure 'documents' and 'arxiv_eprints' are present
        results = self.search_literature(query, size=1)
        hits = results.get("hits", {}).get("hits", [])
        return hits[0] if hits else None
    
    def get_record(self, record_id: str, fields: Optional[str] = None) -> Dict:
        url = f"{self.BASE_URL}/literature/{record_id}"
        params = {}
        if fields: params["fields"] = fields
        return self._request(url, params=params).json()

    def get_citations(self, record_id: str, size: int = 50, page: int = 1, fields: Optional[str] = None) -> Dict:
        query = f"refersto:recid:{record_id}"
        return self.search_literature(query, size=size, page=page, fields=fields)
    
    def get_metadata(self, record_id: str) -> Dict:
        fields = "metadata.titles,metadata.authors,metadata.abstracts,metadata.preprint_date,metadata.publication_info,metadata.arxiv_eprints,metadata.dois,metadata.citation_count,metadata.keywords,metadata.document_type,metadata.number_of_pages"
        record = self.get_record(record_id, fields=fields)
        metadata = record.get("metadata", {})
        return {
            "record_id": record_id,
            "title": metadata.get("titles", [{}])[0].get("title", "N/A"),
            "authors": [author.get("full_name", "N/A") for author in metadata.get("authors", [])],
            "abstract": metadata.get("abstracts", [{}])[0].get("value", "N/A"),
            "publication_date": metadata.get("preprint_date") or metadata.get("publication_info", [{}])[0].get("year", "N/A"),
            "arxiv_id": metadata.get("arxiv_eprints", [{}])[0].get("value", "N/A"),
            "doi": metadata.get("dois", [{}])[0].get("value", "N/A"),
            "citations": metadata.get("citation_count", 0),
            "keywords": [kw.get("value", "") for kw in metadata.get("keywords", [])],
            "inspire_url": f"https://inspirehep.net/literature/{record_id}",
            "document_type": metadata.get("document_type", []),
            "number_of_pages": metadata.get("number_of_pages"),
        }
    
    def download_file(self, url: str, output_path: str) -> None:
        kwargs = {}
        if "arxiv.org" in url:
            url = url.replace("https://arxiv.org/", "https://export.arxiv.org/")
            kwargs["headers"] = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            }
            
        response = self._request(url, stream=True, **kwargs)
        with open(output_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk: f.write(chunk)
        
        # Validate downloaded file
        if not validate_pdf(Path(output_path)):
            if os.path.exists(output_path):
                os.remove(output_path)
            raise ValueError(f"Downloaded file is not a valid PDF or too small: {url}")

# ==========================================
# 3. Downloader Logic (Migrated)
# ==========================================

AUTHOR_FIRST_YEAR_CACHE: Dict[str, Optional[int]] = {}
CACHE_LOCK = threading.Lock()

def extract_year_from_inspire_metadata(md: Dict[str, Any]) -> Optional[int]:
    preprint = md.get("preprint_date")
    ym = parse_year_month(preprint)
    if "year" in ym: return ym["year"]
    pub_infos = md.get("publication_info", []) or []
    if pub_infos and isinstance(pub_infos, list):
        year = pub_infos[0].get("year")
        if isinstance(year, (int, str)): return int(year)
    earliest = md.get("earliest_date") or md.get("earliestdate")
    ym2 = parse_year_month(earliest)
    if "year" in ym2: return ym2["year"]
    return None

def get_author_first_year(client: InspireHEPClient, author_name: str) -> Optional[int]:
    with CACHE_LOCK:
        if author_name in AUTHOR_FIRST_YEAR_CACHE:
            return AUTHOR_FIRST_YEAR_CACHE[author_name]
    
    min_year: Optional[int] = None
    try:
        results = client.search_literature(f"author:\"{author_name}\"", size=25)
        hits = results.get("hits", {}).get("hits", [])
        for h in hits:
            y = extract_year_from_inspire_metadata(h.get("metadata", {}))
            if y is not None:
                if min_year is None or y < min_year: min_year = y
        if min_year is None:
            results2 = client.search_literature(f"find a {author_name}", size=25)
            hits2 = results2.get("hits", {}).get("hits", [])
            for h in hits2:
                y = extract_year_from_inspire_metadata(h.get("metadata", {}))
                if y is not None:
                    if min_year is None or y < min_year: min_year = y
    except Exception:
        min_year = None
    
    with CACHE_LOCK:
        AUTHOR_FIRST_YEAR_CACHE[author_name] = min_year
    return min_year

def compute_young_author_fields(client: InspireHEPClient, authors: List[str], pub_year: Optional[int], years_window: int) -> Dict[str, Any]:
    # Disabled young scholar calculation for performance
    return {"young_scholar_index": -1, "young_authors": [], "author_first_years": {}, "young_author_years_window": years_window}

    result = {"young_scholar_index": -1, "young_authors": [], "author_first_years": {}, "young_author_years_window": years_window}
    if not authors or pub_year is None: return result
    
    # Optimization: Skip for large collaborations (likely > 30 authors)
    if len(authors) > 30:
        # print(f"    [Info] Skipping young author check for {len(authors)} authors (limit 30)")
        return result

    young_any = False
    for name in authors:
        fy = get_author_first_year(client, name)
        if fy is not None:
            result["author_first_years"][name] = fy
            if 0 <= (pub_year - fy) <= years_window:
                young_any = True
                result["young_authors"].append(name)
    result["young_scholar_index"] = 1 if young_any else -1
    return result

def is_prl_or_prd(info_or_list: Any) -> bool:
    if not info_or_list: return False
    if isinstance(info_or_list, dict):
        infos = [info_or_list]
    elif isinstance(info_or_list, list):
        infos = info_or_list
    else:
        return False
        
    for info in infos:
        if not isinstance(info, dict): continue
        title = info.get('journal_title', '').lower().replace('.', '')
        if 'phys rev lett' in title or 'physical review letters' in title:
            return True
        if 'phys rev d' in title or 'physical review d' in title:
            return True
    return False

def fetch_related_ids(client: InspireHEPClient, record_id: str, kind: str, limit: int, doi: Optional[str] = None) -> List[str]:
    ids: List[str] = []
    try:
        if kind == "citations" and doi:
            return get_citing_dois_openalex(doi, limit)

        if kind == "references":
            record = client.get_record(record_id, fields="metadata.references")
            refs = (record.get('metadata', {}) or {}).get('references', []) or []
            # print(f"    [Debug] Found {len(refs)} references for {record_id}")
            for ref in refs:
                # Filter by Journal (PRL/PRD) - DISABLED
                #if not is_prl_or_prd(ref.get('publication_info')):
                #    continue

                rec = ref.get('record') if isinstance(ref, dict) else None
                if isinstance(rec, dict):
                    ref_url = rec.get('$ref') or rec.get('$REF') or rec.get('url')
                    if isinstance(ref_url, str) and '/literature/' in ref_url:
                        try:
                            rid = ref_url.rstrip('/').split('/')[-1]
                            if rid: ids.append(str(rid))
                        except Exception: pass
                    cn = rec.get('control_number') or rec.get('controlNumber')
                    if cn: ids.append(str(cn))
                if len(ids) >= limit: break
        else:
            # Fetch citations
            data = client.get_citations(record_id, size=limit, fields="metadata.control_number,metadata.dois")
            hits = (data.get('hits', {}) or {}).get('hits', []) or []
            for h in hits:
                rid = h.get('id') or (h.get('metadata', {}) or {}).get('control_number')
                if rid: ids.append(str(rid))
                if len(ids) >= limit: break
    except Exception as e:
        print(f"⚠️ 获取{kind}失败: {e}")
    return ids[:limit]

def _pdf_url_from_inspire_metadata_raw(md_raw: Dict[str, Any]) -> Optional[str]:
    docs = md_raw.get("documents", []) or []
    
    # Priority 1: Explicit fulltext
    for doc in docs:
        if doc.get("fulltext") is True:
            url = doc.get("url") or doc.get("source")
            if url: return url

    # Priority 2: Any PDF file
    for doc in docs:
        key = (doc.get("key") or "").lower()
        url = doc.get("url") or doc.get("source")
        if key.endswith(".pdf") and url: return url
        if url and str(url).lower().endswith('.pdf'): return url
        
    eprints = md_raw.get("arxiv_eprints", []) or []
    if eprints:
        arxiv_id = eprints[0].get("value")
        if arxiv_id: return f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    return None

def get_pdf_url_from_all_sources(client: InspireHEPClient, doi: Optional[str], md_raw: Optional[Dict[str, Any]] = None) -> Optional[str]:
    """Try to get PDF URL from all available sources: InspireHEP, Publisher, OpenAlex, Semantic Scholar, Unpaywall, Sci-Hub."""
    pdf_url = None
    
    # 1. Try InspireHEP metadata if provided
    if md_raw:
        pdf_url = _pdf_url_from_inspire_metadata_raw(md_raw)
        if pdf_url: return pdf_url
        
    # 2. Try InspireHEP lookup by DOI if not provided
    if not pdf_url and doi:
        try:
            hit = client.find_record_by_doi(doi)
            if hit:
                md_raw_hit = hit.get('metadata', {}) or {}
                pdf_url = _pdf_url_from_inspire_metadata_raw(md_raw_hit)
                if pdf_url: return pdf_url
        except Exception: pass
        
    # 3. Try other sources via doi_downloader
    if not pdf_url and doi and doi_downloader:
        pdf_url = doi_downloader.get_pdf_from_publisher(doi)
        if not pdf_url: pdf_url = doi_downloader.get_pdf_from_openalex(doi)
        if not pdf_url: pdf_url = doi_downloader.get_pdf_from_semanticscholar(doi)
        if not pdf_url: pdf_url = doi_downloader.get_pdf_from_unpaywall(doi, None)
        if not pdf_url:
            try: pdf_url = doi_downloader.GetDownloadUrl(doi)
            except Exception: pass
            
    return pdf_url

def dir_name_from_metadata(meta_norm: Dict[str, Any]) -> str:
    doi = meta_norm.get('doi')
    if doi: return _sanitize_dir_name(doi)
    aid = meta_norm.get('arxiv_id')
    if aid: return _sanitize_dir_name(aid)
    rid = meta_norm.get('record_id') or 'unknown'
    return _sanitize_dir_name(str(rid))

def to_items_metadata(record_meta: Dict[str, Any], role: Optional[str] = None) -> Dict[str, Any]:
    item: Dict[str, Any] = {
        "title": record_meta.get("title", ""),
        "doi": record_meta.get("doi", ""),
        "authors": record_meta.get("authors", []),
    }
    published = parse_year_month(record_meta.get("publication_date"))
    if published: item["published"] = published
    item["record_id"] = record_meta.get("record_id")
    item["inspire_url"] = record_meta.get("inspire_url")
    item["citations_count"] = record_meta.get("citations", 0)
    if role: item["role"] = role
    return item

def should_skip_document(doc_types: List[str]) -> bool:
    if not doc_types: return False
    skip_types = {'book', 'conference paper', 'proceedings'}
    types = {t.lower() for t in doc_types}
    for t in types:
        if t in skip_types:
            return True
    return False

def process_one_by_doi(client: InspireHEPClient, doi: str, out_dir: Path, download: bool = True, years_window: int = 5, max_pages: Optional[int] = None) -> Dict[str, Any]:
    ensure_dir(out_dir)
    
    base_name = _sanitize_dir_name(doi)
    pdf_path = out_dir / f"{base_name}.pdf"
    meta_path = out_dir / f"{base_name}_metadata.json"

    # Early check: if metadata exists and (PDF exists or not downloading), skip API
    if meta_path.exists():
        try:
            with open(meta_path, 'r', encoding='utf-8') as f:
                meta_norm = json.load(f)
            
            # Check if PDF exists and is valid
            pdf_valid = pdf_path.exists() and validate_pdf(pdf_path)
            
            if not download or pdf_valid:
                print(f"  [Skipped] {doi} (Files exist and valid)")
                item = to_items_metadata(meta_norm)
                pub_year = item.get("published", {}).get("year")
                ya = compute_young_author_fields(client, item.get("authors", []), pub_year, years_window)
                item.update(ya)
                return item
            elif pdf_path.exists() and not pdf_valid:
                print(f"  [Info] Existing PDF for {doi} is invalid, will re-download.")
                os.remove(pdf_path)
        except Exception:
            pass

    hit = client.find_record_by_doi(doi)
    if not hit: raise ValueError(f"未找到 DOI={doi} 的记录")
    rid = str(hit.get('id'))
    md_raw = hit.get('metadata', {}) or {}
    meta_norm = client.get_metadata(rid)
    
    if should_skip_document(meta_norm.get('document_type', [])):
        print(f"  [Skipped Download] {doi} is {meta_norm.get('document_type')}")
        download = False

    if max_pages and meta_norm.get('number_of_pages'):
        try:
            pages = int(meta_norm.get('number_of_pages'))
            if pages > max_pages:
                print(f"  [Skipped Download] {doi} has {pages} pages (> {max_pages})")
                download = False
        except ValueError:
            pass

    item = to_items_metadata(meta_norm)
    
    pdf_filename = f"{_sanitize_dir_name(doi)}.pdf"
    pdf_path = out_dir / pdf_filename
    
    if download:
        if pdf_path.exists():
            print(f"  [Skipped Download] {pdf_filename} exists")
        else:
            pdf_url = get_pdf_url_from_all_sources(client, doi, md_raw)
            if pdf_url:
                try:
                    client.download_file(pdf_url, str(pdf_path))
                except Exception as e:
                    print(f"警告: 无法下载 PDF ({pdf_url}): {e}")
            else:
                print(f"  [Warning] No PDF URL found for {doi} in any source")
    
    meta_path = out_dir / f"{_sanitize_dir_name(doi)}_metadata.json"
    if pdf_path.exists():
        with open(meta_path, 'w', encoding='utf-8') as f:
            json.dump(meta_norm, f, ensure_ascii=False, indent=2)
    
    pub_year = item.get("published", {}).get("year")
    ya = compute_young_author_fields(client, item.get("authors", []), pub_year, years_window)
    item.update(ya)
    return item

def process_one_by_record_id_using_url(client: InspireHEPClient, record_id: str, out_dir: Path, download: bool = True, years_window: int = 5, max_pages: Optional[int] = None) -> Dict[str, Any]:
    ensure_dir(out_dir)
    
    # Early check: if metadata exists, we can determine base_name and check PDF
    # But we need meta_norm first to get base_name. 
    # For simplicity, we'll fetch metadata first, then check.
    
    rec = client.get_record(record_id)
    md_raw = rec.get('metadata', {}) or {}
    meta_norm = client.get_metadata(record_id)
    
    base_name = dir_name_from_metadata(meta_norm)
    pdf_path = out_dir / f"{base_name}.pdf"
    meta_path = out_dir / f"{base_name}_metadata.json"
    
    if meta_path.exists():
        pdf_valid = pdf_path.exists() and validate_pdf(pdf_path)
        if not download or pdf_valid:
            print(f"  [Skipped] {record_id} (Files exist and valid)")
            item = to_items_metadata(meta_norm)
            pub_year = item.get("published", {}).get("year")
            ya = compute_young_author_fields(client, item.get("authors", []), pub_year, years_window)
            item.update(ya)
            return item
        elif pdf_path.exists() and not pdf_valid:
            print(f"  [Info] Existing PDF for {record_id} is invalid, will re-download.")
            os.remove(pdf_path)

    if should_skip_document(meta_norm.get('document_type', [])):
        print(f"  [Skipped Download] {record_id} is {meta_norm.get('document_type')}")
        download = False

    if max_pages and meta_norm.get('number_of_pages'):
        try:
            pages = int(meta_norm.get('number_of_pages'))
            if pages > max_pages:
                print(f"  [Skipped Download] {record_id} has {pages} pages (> {max_pages})")
                download = False
        except ValueError:
            pass

    item = to_items_metadata(meta_norm)
    
    if download:
        if pdf_path.exists():
            print(f"  [Skipped Download] {base_name}.pdf exists")
        else:
            doi = meta_norm.get('doi')
            pdf_url = get_pdf_url_from_all_sources(client, doi, md_raw)
            if pdf_url:
                try:
                    client.download_file(pdf_url, str(pdf_path))
                except Exception as e:
                    print(f"警告: 关联文献 PDF 下载失败 ({pdf_url}): {e}")
            else:
                print(f"  [Warning] No PDF URL found for {record_id} in any source")
    
    if pdf_path.exists() and not meta_path.exists():
        with open(meta_path, 'w', encoding='utf-8') as f:
            json.dump(meta_norm, f, ensure_ascii=False, indent=2)
            
    pub_year = item.get("published", {}).get("year")
    ya = compute_young_author_fields(client, item.get("authors", []), pub_year, years_window)
    item.update(ya)
    return item

# ==========================================
# 4. PDF2MD Logic (Migrated)
# ==========================================

def _build_header(token: str) -> dict:
    h = DEFAULT_HEADERS.copy()
    h.update({"Content-Type": "application/json", "Authorization": f"Bearer {token}"})
    return h

def _file_signature(path: Path, sample_bytes: int = 4 * 1024 * 1024) -> str:
    try:
        size = path.stat().st_size
        h = hashlib.sha1()
        with open(path, 'rb') as f:
            chunk = f.read(sample_bytes)
            h.update(chunk)
        return f"{size}-" + h.hexdigest()
    except Exception:
        return f"0-err-{path.name}"

def _is_converted_rel(output_dir: Path, rel_pdf: Path) -> bool:
    return (output_dir / rel_pdf.with_suffix('.md')).exists() or (output_dir / rel_pdf.with_suffix('.zip')).exists()

def _gather_candidates_and_duplicates(file_dir: Path, output_dir: Path) -> tuple[dict[str, list[str]], dict[str, str]]:
    rel_pdfs = [p.relative_to(file_dir) for p in file_dir.rglob('*.pdf')]
    groups: dict[str, list[Path]] = defaultdict(list)
    for rel in rel_pdfs:
        groups[_file_signature(file_dir / rel)].append(rel)
    
    uniques: dict[str, list[str]] = {}
    duplicates_map: dict[str, str] = {}
    for sig, rel_list in groups.items():
        primary_rel = next((r for r in rel_list if _is_converted_rel(output_dir, r)), None)
        if not primary_rel:
            primary_rel = next((r for r in rel_list if not _is_converted_rel(output_dir, r)), rel_list[0])
        
        for rel in rel_list:
            if rel != primary_rel:
                duplicates_map[str(rel)] = str(primary_rel)
        
        if not _is_converted_rel(output_dir, primary_rel):
            uniques.setdefault(primary_rel.stem, []).append(str(primary_rel))
            
    return uniques, duplicates_map

def process_zip_file(zip_path: Path):
    parent = zip_path.parent
    stem = zip_path.stem
    img_out = parent / "images"
    
    # Determine target filename stem from metadata if available
    target_stem = stem
    meta_path = parent / f"{stem}_metadata.json"
    if meta_path.exists():
        try:
            with open(meta_path, 'r', encoding='utf-8') as f:
                meta = json.load(f)
                title = meta.get('title')
                if title:
                    sanitized_title = _sanitize_dir_name(title)
                    # Truncate to avoid filesystem limits
                    if len(sanitized_title) > 150:
                        sanitized_title = sanitized_title[:150]
                    target_stem = sanitized_title
        except Exception:
            pass

    try:
        with zipfile.ZipFile(zip_path, 'r') as zf:
            for info in zf.infolist():
                if info.is_dir(): continue
                fn = info.filename.strip('/')
                if fn == 'full.md':
                    with zf.open(info) as src, open(parent / f"{target_stem}.md", 'wb') as dst:
                        shutil.copyfileobj(src, dst)
                elif fn == 'full.json':
                    with zf.open(info) as src, open(parent / f"{target_stem}.json", 'wb') as dst:
                        shutil.copyfileobj(src, dst)
                elif fn.startswith('images/'):
                    target = img_out / fn.replace('images/', '', 1)
                    target.parent.mkdir(parents=True, exist_ok=True)
                    with zf.open(info) as src, open(target, 'wb') as dst:
                        shutil.copyfileobj(src, dst)
    except Exception as e:
        print(f"Failed to process zip {zip_path}: {e}")

def batch_upload(file_names: list[str], unique_dict: dict[str, list[str]], file_dir: Path, header: dict) -> str | None:
    url = "https://mineru.org.cn/api/v4/file-urls/batch"
    data = {
        "is_ocr": False, "enable_formula": True, "enable_table": True,
        "model_version": "vlm", "language": None, "is_chem": False,
        "files": [{"name": f"{fn}.pdf", "data_id": str(uuid.uuid4())} for fn in file_names]
    }
    try:
        res = requests.post(url, headers=header, json=data)
        if res.status_code == 200 and res.json().get("code") == 0:
            batch_id = res.json()["data"]["batch_id"]
            urls = res.json()["data"]["file_urls"]
            
            def upload_one(idx_url):
                idx, u = idx_url
                try:
                    with open(file_dir / unique_dict[file_names[idx]][0], 'rb') as f:
                        if requests.put(u, data=f).status_code == 200:
                            print(f"Uploaded: {file_names[idx]}")
                except Exception as e:
                    print(f"Upload failed for {file_names[idx]}: {e}")

            with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
                list(executor.map(upload_one, enumerate(urls)))
                
            return batch_id
    except Exception as e:
        print(e)
    return None

def batch_retrieve(batch_id: str, unique_dict: dict[str, list[str]], file_dir: Path, output_dir: Path, header: dict):
    url = f"https://mineru.org.cn/api/v4/extract-results/batch/{batch_id}"
    done_files = set()
    start_time = time.time()
    MAX_WAIT_SECONDS = 600  # 10 minutes timeout for batch processing
    
    def download_one(item):
        fname = item.get("file_name", "")
        zip_url = item.get("full_zip_url")
        if zip_url:
            stem = Path(fname).stem
            path = unique_dict.get(stem, [stem])[0]
            out_path = output_dir / Path(path).with_suffix(".zip")
            out_path.parent.mkdir(parents=True, exist_ok=True)
            try:
                with requests.get(zip_url, stream=True, timeout=60, headers=DEFAULT_HEADERS) as r, open(out_path, 'wb') as f:
                    shutil.copyfileobj(r.raw, f)
                print(f"Downloaded: {out_path}")
                process_zip_file(out_path)
            except Exception as e:
                print(f"Download/Process failed for {fname}: {e}")

    while True:
        if time.time() - start_time > MAX_WAIT_SECONDS:
            print(f"Timeout waiting for batch {batch_id}")
            break

        try:
            res = requests.get(url, headers=header, timeout=30)
        except requests.RequestException as e:
            print(f"Polling error: {e}")
            time.sleep(5)
            continue

        if res.status_code != 200:
            print(f"Batch status check failed: {res.status_code}")
            break
            
        result = res.json().get("data", {}).get("extract_result", [])
        
        all_finished = True
        new_done = []
        
        for item in result:
            state = item.get("state")
            fname = item.get("file_name", "")
            
            if state == "done":
                if fname not in done_files:
                    done_files.add(fname)
                    new_done.append(item)
            elif state in ["failed", "error", "cancelled"]:
                if fname not in done_files:
                    print(f"File failed processing: {fname}, state: {state}")
                    done_files.add(fname)
            else:
                all_finished = False
        
        if new_done:
            with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
                list(executor.map(download_one, new_done))

        if result and all_finished:
            print("All files processed (done or failed)")
            break
        
        print(f"Waiting for batch processing... ({len(done_files)}/{len(result)})", end='\r')
        time.sleep(5)
    print("")

def replicate_files(file_dir: Path, output_dir: Path):
    for p in file_dir.rglob("*.pdf"):
        rel = p.relative_to(file_dir)
        md = output_dir / rel.with_suffix(".md")
        js = output_dir / rel.with_suffix(".json")
        if md.exists():
            # Logic to replicate if needed, simplified here as we process in place mostly
            pass

def _replicate_duplicates(duplicates_map: dict[str, str], output_dir: Path):
    for dup, pri in duplicates_map.items():
        pri_md = output_dir / Path(pri).with_suffix('.md')
        dup_md = output_dir / Path(dup).with_suffix('.md')
        if pri_md.exists():
            dup_md.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(pri_md, dup_md)

def convert_pdfs_to_md(teacher: str, pdf_root: Path, md_root: Path, token: str):
    file_dir = pdf_root / teacher
    output_dir = md_root / teacher
    uniques, duplicates_map = _gather_candidates_and_duplicates(file_dir, output_dir)
    
    if not uniques:
        print("No new PDFs to convert.")
        return

    header = _build_header(token)
    batch_id = batch_upload(list(uniques.keys()), uniques, file_dir, header)
    if batch_id:
        print(f"Batch ID: {batch_id}")
        batch_retrieve(batch_id, uniques, file_dir, output_dir, header)
        _replicate_duplicates(duplicates_map, output_dir)
        
        # Cleanup PDFs that have been successfully converted
        print("  Cleaning up converted PDFs...")
        for pdf_name in uniques.keys():
            pdf_path = file_dir / pdf_name
            # Check if MD exists (simple check based on name)
            # Note: batch_retrieve saves as .md, but might be in subfolders if we passed relative paths?
            # _gather_candidates_and_duplicates uses rglob, so keys in uniques are relative paths or names.
            # Let's assume if batch_retrieve succeeded, we can delete.
            # Or better, check if corresponding MD exists.
            
            # uniques keys are relative paths from file_dir (as strings) or filenames?
            # In _gather_candidates_and_duplicates: uniques[rel_path] = file_id (initially None)
            
            # Construct expected MD path
            # If pdf is "main/paper.pdf", md should be "main/paper.md"
            rel_path = Path(pdf_name)
            md_path = output_dir / rel_path.with_suffix('.md')
            
            if md_path.exists():
                try:
                    if pdf_path.exists():
                        pdf_path.unlink()
                    
                    # Delete corresponding metadata json
                    meta_json = pdf_path.with_name(f"{pdf_path.stem}_metadata.json")
                    if meta_json.exists():
                        meta_json.unlink()

                except Exception as e:
                    print(f"    Failed to delete source files for {pdf_path.name}: {e}")
            
        # Also cleanup duplicates if their primary MD exists
        for dup_name, pri_name in duplicates_map.items():
             pri_md_path = output_dir / Path(pri_name).with_suffix('.md')
             if pri_md_path.exists():
                 dup_pdf_path = file_dir / dup_name
                 if dup_pdf_path.exists():
                     try:
                         dup_pdf_path.unlink()
                         
                         # Delete corresponding metadata json for duplicate
                         dup_meta = dup_pdf_path.with_name(f"{dup_pdf_path.stem}_metadata.json")
                         if dup_meta.exists():
                             dup_meta.unlink()
                     except Exception: pass

# ==========================================
# 5. Main Logic
# ==========================================

def safe_cleanup_converted_files(teacher_dir: Path):
    """
    Safely delete PDF, ZIP, and JSON files only if the corresponding MD file exists.
    """
    print(f"  Safe cleanup for {teacher_dir.name}...")
    for subdir_name in ['main', 'ref1', 'cited']:
        subdir = teacher_dir / subdir_name
        if not subdir.exists(): continue
        
        # Gather all candidate files by stem
        candidates = defaultdict(list)
        for p in subdir.iterdir():
            if not p.is_file(): continue
            if p.suffix.lower() in ['.pdf', '.zip', '.json']:
                # Identify stem
                if p.name.endswith('_metadata.json'):
                    stem = p.name[:-14]
                else:
                    stem = p.stem
                candidates[stem].append(p)
        
        for stem, files in candidates.items():
            # Check if MD exists with this stem
            md_path = subdir / f"{stem}.md"
            should_delete = False
            
            if md_path.exists():
                should_delete = True
            else:
                # Check for title-based MD using metadata
                meta_json = next((f for f in files if f.name.endswith('_metadata.json')), None)
                
                if meta_json:
                    try:
                        with open(meta_json, 'r', encoding='utf-8') as f:
                            meta = json.load(f)
                            title = meta.get('title')
                            if title:
                                sanitized_title = _sanitize_dir_name(title)
                                if len(sanitized_title) > 150:
                                    sanitized_title = sanitized_title[:150]
                                
                                title_md_path = subdir / f"{sanitized_title}.md"
                                if title_md_path.exists():
                                    should_delete = True
                    except Exception:
                        pass
            
            if should_delete:
                for p in files:
                    try:
                        if p.exists():
                            p.unlink()
                    except Exception as e:
                        print(f"    Failed to delete {p.name}: {e}")

        # Unconditionally delete 'images' folder
        images_dir = subdir / 'images'
        if images_dir.exists() and images_dir.is_dir():
            try:
                shutil.rmtree(images_dir)
            except Exception as e:
                print(f"    Failed to delete images folder in {subdir_name}: {e}")

def cleanup_intermediate_files(teacher_dir: Path):
    """
    Delete intermediate files (.pdf, .zip, .json) and 'images' folder in subdirectories,
    keeping only .md files.
    The metadata_items.json in teacher_dir is preserved.
    """
    print(f"  Cleaning up intermediate files for {teacher_dir.name}...")
    for subdir_name in ['main', 'ref1', 'cited']:
        subdir = teacher_dir / subdir_name
        if not subdir.exists():
            continue
            
        for p in subdir.iterdir():
            if p.is_file():
                # Delete .pdf, .zip
                if p.suffix.lower() in ['.pdf', '.zip']:
                    try:
                        p.unlink()
                    except Exception as e:
                        print(f"    Failed to delete {p.name}: {e}")
                # Delete .json (individual metadata or full.json from extraction)
                elif p.suffix.lower() == '.json':
                    try:
                        p.unlink()
                    except Exception as e:
                        print(f"    Failed to delete {p.name}: {e}")
            elif p.is_dir() and p.name == 'images':
                try:
                    shutil.rmtree(p)
                except Exception as e:
                    print(f"    Failed to delete images folder in {subdir_name}: {e}")

def parse_papers_data(file_path: Path) -> Dict[str, List[str]]:
    data = {}
    current_teacher = None
    current_dois = []
    if not file_path.exists():
        print(f"File not found: {file_path}")
        return {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('=') or line.startswith('#'):
                continue
            
            # Handle Teacher|DOI format (manuallist.txt)
            if '|' in line and not line.startswith('👤'):
                parts = line.split('|')
                if len(parts) >= 2:
                    t_name = parts[0].strip()
                    t_doi = parts[1].strip()
                    if t_name and t_doi:
                        if t_name not in data:
                            data[t_name] = []
                        data[t_name].append(t_doi)
                continue

            if line.startswith('👤'):
                if current_teacher: data[current_teacher] = current_dois
                current_teacher = line.replace('👤', '').strip()
                current_dois = []
            elif line.startswith('DOI:'):
                doi = line.split(':', 1)[1].strip()
                if doi: current_dois.append(doi)
            elif line.startswith('10.'): # Handle raw DOIs from results.txt
                current_dois.append(line)
                
        if current_teacher: data[current_teacher] = current_dois
    return data

def process_one_by_doi_generic(client, doi, output_dir, role='main', download=True):
    if not doi_downloader:
        raise ImportError("doi_downloader not available")
        
    print(f"    [Generic] Processing {doi}...")
    official_title = doi_downloader.get_official_title_from_doi(doi)
    if not official_title:
        raise ValueError(f"Could not get title for {doi}")
        
    base_name = _sanitize_dir_name(doi)
    pdf_path = output_dir / f"{base_name}.pdf"
    meta_path = output_dir / f"{base_name}_metadata.json"
    
    if meta_path.exists():
        pdf_valid = pdf_path.exists() and validate_pdf(pdf_path)
        if not download or pdf_valid:
            print(f"    [Generic] [Skipped] {doi} (Files exist and valid)")
            try:
                with open(meta_path, 'r', encoding='utf-8') as f:
                    meta_simple = json.load(f)
                item = {
                    "title": meta_simple.get("title"),
                    "doi": meta_simple.get("doi"),
                    "authors": meta_simple.get("authors"),
                    "published": parse_year_month(meta_simple.get("publication_date")),
                    "role": meta_simple.get("role"),
                    "record_id": None,
                    "inspire_url": None,
                    "citations_count": 0
                }
                return item
            except Exception: pass
        elif pdf_path.exists() and not pdf_valid:
            print(f"    [Generic] [Info] Existing PDF for {doi} is invalid, will re-download.")
            os.remove(pdf_path)

    if download:
        pdf_url = get_pdf_url_from_all_sources(client, doi)
        if not pdf_url:
            raise ValueError(f"Could not get PDF URL for {doi} in any source")
            
        client.download_file(pdf_url, str(pdf_path))

    # Create minimal metadata
    meta_path = output_dir / f"{base_name}_metadata.json"
    meta_simple = {
        "doi": doi,
        "title": official_title,
        "authors": [],
        "role": role
    }
    # Try to enrich with CrossRef
    try:
        cr_meta = doi_downloader.get_crossref_metadata(doi)
        if cr_meta:
            meta_simple["title"] = cr_meta.get('title', [official_title])[0]
            meta_simple["authors"] = doi_downloader._extract_authors_from_meta(cr_meta)
            y, m = doi_downloader._extract_pub_year_month(cr_meta)
            if y: meta_simple["publication_date"] = f"{y}-{m}" if m else str(y)
    except Exception: pass
    
    with open(meta_path, 'w', encoding='utf-8') as f:
        json.dump(meta_simple, f, ensure_ascii=False, indent=2)
            
    # Convert to item format
    item = {
        "title": meta_simple.get("title"),
        "doi": meta_simple.get("doi"),
        "authors": meta_simple.get("authors"),
        "published": parse_year_month(meta_simple.get("publication_date")),
        "role": meta_simple.get("role"),
        "record_id": None,
        "inspire_url": None,
        "citations_count": 0
    }
    return item

def process_doi_task(args_tuple):
    client, doi, main_dir, ref_dir, cited_dir, sample_size, years_window, workers_related, limit_ref, limit_cited, teacher, only_main, metadata_only, method = args_tuple
    print(f"  Downloading Main DOI: {doi} (Method: {method})")
    try:
        if method == 'doi_source':
             item = process_one_by_doi_generic(client, doi, main_dir, role='main', download=not metadata_only)
        else:
             item = process_one_by_doi(client, doi, main_dir, download=not metadata_only, years_window=years_window)
        
        item['role'] = 'main'
        
        # Save metadata immediately
        teacher_dir = main_dir.parent
        update_teacher_metadata(teacher_dir, item)
        
        rid = item.get('record_id')
        if not rid and method != 'doi_source': 
            save_progress(teacher, doi)
            return item
        
        # If method is doi_source, we might not have record_id, but we still want to fetch related papers if possible.
        # But fetch_related_ids needs record_id (for inspire) or DOI (for openalex).
        # If we have DOI, we can use OpenAlex for citations.
        # For references, it needs record_id for Inspire, or it can use OpenAlex if implemented.
        # fetch_related_ids supports DOI for citations (OpenAlex).
        # For references, it currently only supports Inspire record_id.
        
        if method == 'doi_source' and not rid:
            # Try to get record_id from Inspire using DOI, just for fetching references
             try:
                 rec = client.get_record_by_doi(doi)
                 if rec:
                     rid = rec.get('id') or rec.get('metadata', {}).get('control_number')
             except Exception: pass

        if only_main:
            print(f"  [Skipped] Related papers for {doi} (Only Main requested)")
            save_progress(teacher, doi)
            return item

        # Parallel fetch of IDs
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as fetch_executor:
            # If we have rid, we can fetch references from Inspire
            if rid:
                future_ref_ids = fetch_executor.submit(fetch_related_ids, client, str(rid), 'references', limit_ref)
            else:
                # TODO: Implement OpenAlex references fetching if needed
                future_ref_ids = None
                
            # For citations, we can use DOI (OpenAlex) or rid (Inspire)
            # fetch_related_ids uses OpenAlex if kind='citations' and doi is provided
            future_cited_ids = fetch_executor.submit(fetch_related_ids, client, str(rid) if rid else "", 'citations', limit_cited, doi)
            
            ref_ids = future_ref_ids.result() if future_ref_ids else []
            cited_ids = future_cited_ids.result()

        # Sampling
        if sample_size and len(ref_ids) > 0:
            ref_ids = random.sample(ref_ids, min(len(ref_ids), sample_size))
        if sample_size and len(cited_ids) > 0:
            cited_ids = random.sample(cited_ids, min(len(cited_ids), sample_size))

        # Prepare download tasks
        download_tasks = []
        for r_id in ref_ids:
            download_tasks.append({'id': r_id, 'dir': ref_dir, 'role': 'reference'})
        for c_id in cited_ids:
            download_tasks.append({'id': c_id, 'dir': cited_dir, 'role': 'citation'})

        def download_related(task):
            tid = task['id']
            tdir = task['dir']
            trole = task['role']
            
            # Check if already processed
            if GLOBAL_PROCESSED_CACHE and teacher in GLOBAL_PROCESSED_CACHE:
                if tid in GLOBAL_PROCESSED_CACHE[teacher]:
                    return

            print(f"    Downloading {trole.capitalize()}: {tid}")
            try:
                if method == 'doi_source':
                    # Resolve to DOI if needed
                    target_doi = tid
                    if '/' not in tid: # Likely a record ID
                         try:
                             rec = client.get_record(tid, fields="metadata.dois")
                             dois = (rec.get('metadata', {}) or {}).get('dois', [])
                             if dois:
                                 target_doi = dois[0].get('value')
                         except Exception: pass
                    
                    if target_doi and '/' in target_doi:
                        # Use generic
                        t_item = process_one_by_doi_generic(client, target_doi, tdir, role=trole, download=not metadata_only)
                        # Save metadata immediately
                        teacher_dir = tdir.parent
                        update_teacher_metadata(teacher_dir, t_item)
                    else:
                        # Fallback to inspire if no DOI found
                        t_item = process_one_by_record_id_using_url(client, tid, tdir, download=not metadata_only, years_window=years_window, max_pages=50)
                        t_item['role'] = trole
                        teacher_dir = tdir.parent
                        update_teacher_metadata(teacher_dir, t_item)
                else:
                    if '/' in tid:
                        # Try InspireHEP first
                        try:
                            t_item = process_one_by_doi(client, tid, tdir, download=not metadata_only, years_window=years_window, max_pages=50)
                            t_item['role'] = trole
                            # Save metadata immediately
                            teacher_dir = tdir.parent
                            update_teacher_metadata(teacher_dir, t_item)
                        except Exception as e_inspire:
                            # Fallback to generic downloader if available
                            if doi_downloader and not metadata_only:
                                print(f"    InspireHEP failed for {tid}, trying generic downloader...")
                                # Use doi_downloader to download PDF
                                # Note: doi_downloader saves to its own structure, we might need to adapt or move file
                                # For simplicity, we call download_and_process_doi but we need to handle the output path
                                # Or better, use DownloadFileByUrl directly if we can get a URL
                                
                                # Let's try to use doi_downloader's logic to get PDF URL and download to our tdir
                                official_title = doi_downloader.get_official_title_from_doi(tid)
                                if official_title:
                                    # Try to get PDF URL
                                    pdf_url = get_pdf_url_from_all_sources(client, tid)
                                    
                                    if pdf_url:
                                        base_name = _sanitize_dir_name(tid)
                                        pdf_path = tdir / f"{base_name}.pdf"
                                        client.download_file(pdf_url, str(pdf_path))
                                        
                                        # Create minimal metadata
                                        meta_path = tdir / f"{base_name}_metadata.json"
                                        meta_simple = {
                                            "doi": tid,
                                            "title": official_title,
                                            "authors": [], # We could fetch from CrossRef if needed
                                            "role": trole
                                        }
                                        # Try to enrich with CrossRef
                                        try:
                                            cr_meta = doi_downloader.get_crossref_metadata(tid)
                                            if cr_meta:
                                                meta_simple["title"] = cr_meta.get('title', [official_title])[0]
                                                meta_simple["authors"] = doi_downloader._extract_authors_from_meta(cr_meta)
                                                y, m = doi_downloader._extract_pub_year_month(cr_meta)
                                                if y: meta_simple["publication_date"] = f"{y}-{m}" if m else str(y)
                                        except Exception: pass
                                        
                                        with open(meta_path, 'w', encoding='utf-8') as f:
                                            json.dump(meta_simple, f, ensure_ascii=False, indent=2)
                                        
                                        # Save metadata immediately
                                        teacher_dir = tdir.parent
                                        # Convert meta_simple to item format
                                        simple_item = {
                                            "title": meta_simple.get("title"),
                                            "doi": meta_simple.get("doi"),
                                            "authors": meta_simple.get("authors"),
                                            "published": parse_year_month(meta_simple.get("publication_date")),
                                            "role": meta_simple.get("role"),
                                            "record_id": None,
                                            "inspire_url": None,
                                            "citations_count": 0
                                        }
                                        update_teacher_metadata(teacher_dir, simple_item)
                                    else:
                                        print(f"    Generic download failed (no URL) for {tid}")
                                else:
                                    print(f"    Generic download failed (no title) for {tid}")
                            elif metadata_only:
                                 print(f"    InspireHEP failed for {tid}, skipping generic downloader (metadata only mode)")
                            else:
                                raise e_inspire

                    else:
                        t_item = process_one_by_record_id_using_url(client, tid, tdir, download=not metadata_only, years_window=years_window, max_pages=50)
                        t_item['role'] = trole
                        # Save metadata immediately
                        teacher_dir = tdir.parent
                        update_teacher_metadata(teacher_dir, t_item)
                
                # Save progress for related item
                save_progress(teacher, tid)
            except Exception as e:
                print(f"    Failed {trole.capitalize()} {tid}: {e}")

        # Execute downloads in parallel
        with concurrent.futures.ThreadPoolExecutor(max_workers=workers_related) as executor:
            list(executor.map(download_related, download_tasks))
            
        save_progress(teacher, doi)
        return item

    except Exception as e:
        print(f"  Failed Main DOI {doi}: {e}")
        return None

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--papers-data', default=str(PROJ_ROOT / 'inspirehep_source/pre-process/results.txt'))
    parser.add_argument('--manual-list', help='Path to manual list file (Teacher|DOI format)')
    parser.add_argument('--token', default=os.getenv('MINERU_TOKEN'))
    parser.add_argument('--teacher', help='Specify a single teacher to process')
    parser.add_argument('--only-main', action='store_true', help='Only download main papers, skip references and citations')
    parser.add_argument('--metadata-only', action='store_true', help='Only process metadata, skip PDF download and ignore processed status')
    parser.add_argument('--force', action='store_true', help='Force re-process even if already processed. Will reset progress for the target teacher(s).')
    parser.add_argument('--method', choices=['inspire', 'doi_source'], default='inspire', help='Download method to use')
    parser.add_argument('--retry', action='store_true', help='Retry downloading items present in metadata but missing MD files')
    parser.add_argument('--convert-only', action='store_true', help='Only convert existing PDFs to MD, skip download')
    args = parser.parse_args()

    if args.method == 'doi_source':
        if doi_downloader:
            # Monkeypatch OUTPUT_ROOT_PDF to point to data directory
            # doi_downloader uses os.path.join(OUTPUT_ROOT_PDF, folder_teacher, subdirectory)
            # We want data/Teacher/subdirectory
            # So OUTPUT_ROOT_PDF should be PROJ_ROOT / 'data'
            doi_downloader.OUTPUT_ROOT_PDF = str(PROJ_ROOT / 'data')
            # Enable production mode to simplify output
            doi_downloader.production_mode = True
            print(f"Using DOI Source method. Output root set to: {doi_downloader.OUTPUT_ROOT_PDF}")
        else:
            print("Error: doi_downloader module not available. Cannot use doi_source method.")
            return

    if not args.token:
        print("Warning: MINERU_TOKEN is missing. PDF to MD conversion will be skipped.")
    
    config = load_config()
    sample_threshold, sample_size = get_sampling_cfg(config)
    years_window = get_young_author_years(config)
    workers_main, workers_related = get_worker_cfg(config)
    limit_ref, limit_cited = get_limit_cfg(config)
    
    data_root = PROJ_ROOT / 'data'

    if args.convert_only:
        if not args.token:
            print("Error: MINERU_TOKEN is required for conversion.")
            return
            
        teachers_to_process = []
        if args.teacher:
            teachers_to_process = [args.teacher]
        else:
            # Scan data directory
            if data_root.exists():
                teachers_to_process = [d.name for d in data_root.iterdir() if d.is_dir()]
            else:
                print(f"Data directory not found: {data_root}")
                return
            
        for teacher in teachers_to_process:
            print(f"\n[Convert Only] Processing Teacher: {teacher}")
            teacher_dir = data_root / teacher
            if not teacher_dir.exists():
                print(f"  Directory not found: {teacher_dir}")
                continue
                
            convert_pdfs_to_md(teacher, data_root, data_root, args.token)
            safe_cleanup_converted_files(teacher_dir)
        return

    papers_data = parse_papers_data(Path(args.papers_data))
    
    if args.teacher:
        if args.teacher in papers_data:
            papers_data = {args.teacher: papers_data[args.teacher]}
        else:
            print(f"Error: Teacher '{args.teacher}' not found in papers data.")
            return

    processed_records = load_progress()
    
    # data_root is already defined above
    
    for teacher, dois in papers_data.items():
        print(f"\nProcessing Teacher: {teacher}")
        
        if args.retry:
            retry_missing_items(teacher, data_root, InspireHEPClient(), sample_size, years_window, workers_related, limit_ref, limit_cited, args.method)
            if args.token:
                print(f"  Converting PDFs to MD for {teacher}...")
                convert_pdfs_to_md(teacher, data_root, data_root, args.token)
            continue

        if args.force:
            print(f"  [Force Mode] Resetting progress for {teacher}...")
            with PROGRESS_LOCK:
                if teacher in processed_records:
                    processed_records[teacher] = set()
                    try:
                        with open(PROGRESS_FILE, 'w', encoding='utf-8') as f:
                            json_data = {k: list(v) for k, v in processed_records.items()}
                            json.dump(json_data, f, ensure_ascii=False, indent=2)
                    except Exception as e:
                        print(f"Failed to clear progress file: {e}")
        
        teacher_dir = data_root / teacher
        main_dir = teacher_dir / 'main'
        ref_dir = teacher_dir / 'ref1'
        cited_dir = teacher_dir / 'cited'
        
        # Use a new client per thread if needed, but requests.Session is thread-safe.
        # However, to avoid sharing connection pool limits too aggressively, we can pass the same client.
        client = InspireHEPClient()

        # Prepare tasks
        tasks = []
        for doi in dois:
            if not args.metadata_only and doi in processed_records.get(teacher, set()):
                print(f"  [Skipped] {doi} (Already processed)")
                continue
            tasks.append((client, doi, main_dir, ref_dir, cited_dir, sample_size, years_window, workers_related, limit_ref, limit_cited, teacher, args.only_main, args.metadata_only, args.method))
        
        if tasks:
            with concurrent.futures.ThreadPoolExecutor(max_workers=workers_main) as executor:
                results = list(executor.map(process_doi_task, tasks))
        else:
            print(f"  All DOIs for {teacher} are already processed.")

        # 3. Convert to MD (Batch process for the teacher)
        if args.token:
            print(f"  Converting PDFs to MD for {teacher}...")
            convert_pdfs_to_md(teacher, data_root, data_root, args.token)
        else:
            print(f"  Skipping PDF to MD conversion for {teacher} (no token).")
        
        # 4. Generate Metadata JSON
        new_items = []
        for subdir in [main_dir, ref_dir, cited_dir]:
            if not subdir.exists(): continue
            for meta_file in subdir.glob('*_metadata.json'):
                try:
                    with open(meta_file, 'r', encoding='utf-8') as f:
                        meta = json.load(f)
                        if subdir.name == 'main': meta['role'] = 'main'
                        elif subdir.name == 'ref1': meta['role'] = 'reference'
                        elif subdir.name == 'cited': meta['role'] = 'citation'
                        
                        item = {
                            "title": meta.get("title"),
                            "doi": meta.get("doi"),
                            "authors": meta.get("authors"),
                            "published": parse_year_month(meta.get("publication_date")),
                            "role": meta.get("role"),
                            "record_id": meta.get("record_id"),
                            "inspire_url": meta.get("inspire_url"),
                            "citations_count": meta.get("citations", 0)
                        }
                        pub_year = item.get("published", {}).get("year")
                        ya = compute_young_author_fields(client, item.get("authors", []), pub_year, years_window)
                        item.update(ya)
                        new_items.append(item)
                except Exception as e:
                    print(f"  Error processing metadata file {meta_file}: {e}")
        
        # Merge with existing metadata
        metadata_file = teacher_dir / 'metadata_items.json'
        existing_items = []
        if metadata_file.exists():
            try:
                with open(metadata_file, 'r', encoding='utf-8') as f:
                    existing_data = json.load(f)
                    existing_items = existing_data.get("items", [])
            except Exception as e:
                print(f"  Warning: Failed to load existing metadata from {metadata_file}: {e}")

        # Deduplicate by DOI (or record_id, or title)
        merged_map = {}
        
        def get_key(itm):
            return itm.get("doi") or itm.get("record_id") or itm.get("title")

        # Add existing items first
        for item in existing_items:
            k = get_key(item)
            if k:
                merged_map[k] = item
        
        # Add/Update with new items
        for item in new_items:
            k = get_key(item)
            if k:
                merged_map[k] = item

        final_items = list(merged_map.values())

        with open(metadata_file, 'w', encoding='utf-8') as f:
            json.dump({"items": final_items}, f, ensure_ascii=False, indent=2)
        print(f"  Metadata saved to {metadata_file} (Merged {len(existing_items)} old + {len(new_items)} new -> {len(final_items)} total)")

        # 5. Cleanup Intermediate Files
        cleanup_intermediate_files(teacher_dir)

def retry_missing_items(teacher, data_root, client, sample_size, years_window, workers_related, limit_ref, limit_cited, method):
    teacher_dir = data_root / teacher
    metadata_file = teacher_dir / 'metadata_items.json'
    if not metadata_file.exists():
        print(f"  No metadata file found for {teacher}, skipping retry.")
        return

    try:
        with open(metadata_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            items = data.get("items", [])
    except Exception as e:
        print(f"  Error loading metadata for {teacher}: {e}")
        return

    tasks = []
    main_dir = teacher_dir / 'main'
    ref_dir = teacher_dir / 'ref1'
    cited_dir = teacher_dir / 'cited'

    print(f"  Checking {len(items)} items for missing MD files...")
    
    for item in items:
        doi = item.get("doi")
        record_id = item.get("record_id")
        title = item.get("title")
        role = item.get("role", "main")
        
        # Determine target directory
        if role == 'main': target_dir = main_dir
        elif role == 'reference': target_dir = ref_dir
        elif role == 'citation': target_dir = cited_dir
        else: target_dir = main_dir # Default
        
        # Determine filename base
        if doi:
            base_name = _sanitize_dir_name(doi)
        elif record_id:
            base_name = _sanitize_dir_name(str(record_id))
        elif title:
             base_name = _sanitize_dir_name(title)
        else:
            continue

        md_path = target_dir / f"{base_name}.md"
        
        if not md_path.exists():
            tasks.append({
                "doi": doi,
                "record_id": record_id,
                "target_dir": target_dir,
                "role": role
            })

    if not tasks:
        print("  No missing MD files found.")
        return

    print(f"  Found {len(tasks)} items with missing MD files. Retrying download...")
    
    def process_retry(task):
        doi = task['doi']
        rid = task['record_id']
        tdir = task['target_dir']
        role = task['role']
        
        try:
            if doi:
                if method == 'doi_source':
                     process_one_by_doi_generic(client, doi, tdir, role=role, download=True)
                else:
                     process_one_by_doi(client, doi, tdir, download=True, years_window=years_window)
            elif rid:
                process_one_by_record_id_using_url(client, str(rid), tdir, download=True, years_window=years_window)
            else:
                pass
        except Exception as e:
            print(f"    Failed to retry {doi or rid}: {e}")

    with concurrent.futures.ThreadPoolExecutor(max_workers=workers_related) as executor:
        list(executor.map(process_retry, tasks))

if __name__ == '__main__':
    main()
