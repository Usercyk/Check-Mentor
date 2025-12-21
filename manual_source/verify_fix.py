
import sys
import os
import re
import requests

# Add inspirehep_downloader to path
sys.path.append(os.path.join(os.getcwd(), 'inspirehep_source', 'inspirehep_downloader'))

def clean_article_string(text):
    # Remove (本研学生) or similar Chinese text in parens
    text = re.sub(r'\([^)]*[\u4e00-\u9fa5]+[^)]*\)', '', text)
    # Remove * from author names
    text = text.replace('*', '')
    # Remove quotes
    text = text.replace('"', '').replace("'", "")
    # Remove leading/trailing whitespace
    return text.strip()

def search_crossref(query):
    url = "https://api.crossref.org/works"
    params = {
        "query.bibliographic": query,
        "rows": 1,
        "select": "DOI,title,score"
    }
    try:
        headers = {'User-Agent': 'CheckMentor/1.0 (mailto:example@example.com)'}
        response = requests.get(url, params=params, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            items = data.get("message", {}).get("items", [])
            if items:
                return items[0].get("DOI")
    except Exception as e:
        print(f"  Crossref error: {e}")
    return None

articles = [
    "Wang C(本研学生), Liu* F, Huang* H. Effective Model for Fractional Topological Corner Modes in Quasicrystals. Phys. Rev. Lett. 2022;129:056403",
    "Wang C (本研学生), Cheng T, Liu Z, Liu* F, Huang* H. Structural amorphization-induced topological order. Phys. Rev. Lett. 2022;128:056401.",
    "Ni X, Huang H, Brédas J-L. Organic Higher-Order Topological Insulators: Heterotriangulene-based Covalent Organic Frameworks. J. Am. Chem. Soc. 2022;144(49):22778 - 22786."
]

for article in articles:
    print(f"Original: {article}")
    cleaned = clean_article_string(article)
    print(f"Cleaned: {cleaned}")
    
    doi = search_crossref(cleaned)
    if doi:
        print(f"Found DOI: {doi}")
    else:
        print("Not found with full string.")
        # Try title extraction
        parts = cleaned.split('. ')
        if len(parts) >= 2:
            title = parts[1]
            print(f"Trying title: {title}")
            doi = search_crossref(title)
            print(f"Found DOI (title): {doi}")
    print("-" * 20)
