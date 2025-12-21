import os
import sys
import re
import time
import requests

# Add inspirehep_downloader to path
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'inspirehep_source', 'inspirehep_downloader'))

try:
    from inspirehep_downloader import InspireHEPClient
except ImportError:
    print("Could not import inspirehep_downloader. Please ensure it is in the correct path.")
    sys.exit(1)

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
        # Add a polite User-Agent
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

def extract_doi_from_md(md_file_path, output_file_path):
    with open(md_file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    
    teacher_articles = {} # {teacher_name: [article_lines]}
    
    # Regex for headers
    header_pattern = re.compile(r'^#\s*(.+)$')
    
    # Regex to clean teacher name (remove (2), etc.)
    # Handles: (2) Name, ② Name, 2. Name, Name
    teacher_name_clean_pattern = re.compile(r'^(?:(?:\(\d+\))|[①-⑩]|[0-9]+\.)\s*(.+)$|^(?!(?:\(\d+\))|[①-⑩]|[0-9]+\.)(.+)$')

    ignore_headers = [
        "CONTENTS 目录", "手册使用说明", "本科生科研训练项目简介", "关于本科生科研训练的几点建议", 
        "常见问题", "来自学长的建议", "优秀本研学生感想", "本研教师信息",
        "普通物理教学中心", "基础物理实验教学中心", "理论物理研究所", "凝聚态物理与材料物理研究所",
        "现代光学研究所", "重离子物理研究所", "技术物理系", "天文学系", "大气与海洋科学系",
        "电子显微镜实验室", "量子材料科学中心", "科维理天文与天体物理研究所",
        "1.北京大学促进本科生研究型学习实施办法", "一、项目申请", "二、中期审核", "三、结题答辩",
        "1.过程管理", "2. 中期审核和资助发放", "1.结题要求", "2.答辩过程",
        "四、课程学分及成绩", "五、评优与奖励", "2. 基金项目介绍", "3. 本科生科研时间表：",
        "4. 本科生科研系统学生指南：", "4.1本科生系统学生操作流程", "北京大学", "本科生科研项目系统"
    ]
    
    subsection_headers = [
        "科研信息", "导师寄语", "研究方向", "精选文章", "key words", "☆ 研究方向",
        "个人本研课题对学生的先修课程要求", "个人本研课题对学生课程之外的要求",
        "曾指导学生完成的本研课题"
    ]

    potential_teacher = None
    in_selected_articles = False
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Check for header
        match = header_pattern.match(line)
        if match:
            raw_header = match.group(1).strip()
            
            # Check if it's a subsection
            is_subsection = False
            for sub in subsection_headers:
                if sub in raw_header:
                    is_subsection = True
                    break
            
            if is_subsection:
                # It's a subsection, keep potential_teacher
                # But if it is "精选文章", we mark it
                if "精选文章" in raw_header:
                    if potential_teacher:
                        if potential_teacher not in teacher_articles:
                            teacher_articles[potential_teacher] = []
                        in_selected_articles = True
                else:
                    in_selected_articles = False
                continue
            
            # Check if it's an ignored header
            is_ignored = False
            for ignored in ignore_headers:
                if ignored in raw_header:
                    is_ignored = True
                    break
            
            if is_ignored:
                potential_teacher = None
                in_selected_articles = False
                continue
            
            # Assume it's a teacher
            # Clean the name
            # The regex returns two groups, one for matched prefix, one for no prefix.
            # We need to find which group matched.
            name_match = teacher_name_clean_pattern.match(raw_header)
            if name_match:
                teacher_name = name_match.group(1) or name_match.group(2)
                teacher_name = teacher_name.strip()
                
                # Heuristic: Teacher names are usually short (2-4 chars for Chinese)
                # But some headers might be "1. ..." which we missed.
                if len(teacher_name) > 10 and not re.match(r'^[a-zA-Z\s]+$', teacher_name):
                     # Likely not a name if it's long and not English
                     potential_teacher = None
                     in_selected_articles = False
                     continue
                
                potential_teacher = teacher_name
                in_selected_articles = False
                # print(f"Found teacher candidate: {potential_teacher}")
            continue
            
        # Not a header
        if "精选文章" in line and not line.startswith("#"):
             # Sometimes "精选文章" is not a header but a standalone line
             if potential_teacher:
                if potential_teacher not in teacher_articles:
                    teacher_articles[potential_teacher] = []
                in_selected_articles = True
             continue

        if in_selected_articles:
            # Improved article detection
            is_article = False
            if line.startswith("-") or line.startswith("•"):
                is_article = True
            elif re.match(r'^\d+\.', line):
                is_article = True
            elif re.search(r'\b(19|20)\d{2}\b', line):
                # Contains a year, likely a citation
                is_article = True
            
            if is_article:
                article = line
                if article.startswith("-") or article.startswith("•"):
                    article = article[1:].strip()
                elif re.match(r'^\d+\.', article):
                    article = re.sub(r'^\d+\.\s*', '', article)
                
                if article.endswith(";"):
                    article = article[:-1]
                
                if potential_teacher:
                    teacher_articles[potential_teacher].append(article)

    print(f"Found {len(teacher_articles)} teachers with selected articles.")
    # print(teacher_articles.keys())
    
    client = InspireHEPClient()
    
    # Clear the file first
    with open(output_file_path, 'w', encoding='utf-8') as f:
        pass

    count = 0
    for teacher, articles in teacher_articles.items():
        print(f"Processing teacher: {teacher}")
        for article in articles:
            # Basic cleaning for DOI search in text
            article_clean_basic = re.sub(r'https?://\S+', '', article).strip()
            
            if not article_clean_basic:
                continue
                
            # Check for DOI in text
            doi_match = re.search(r'10\.\d{4,9}/[-._;()/:A-Z0-9]+', article_clean_basic, re.IGNORECASE)
            doi = None
            if doi_match:
                doi = doi_match.group(0).rstrip('.,;')
                print(f"  Found DOI in text: {doi}")
            else:
                # Advanced cleaning for search
                article_clean = clean_article_string(article_clean_basic)
                
                # 1. Search InspireHEP
                try:
                    search_res = client.search_literature(article_clean, size=1)
                    hits = search_res.get("hits", {}).get("hits", [])
                    
                    if hits:
                        metadata = hits[0].get("metadata", {})
                        dois = metadata.get("dois", [])
                        if dois:
                            doi = dois[0].get("value")
                            print(f"  Found DOI from InspireHEP: {doi}")
                except Exception as e:
                    print(f"  InspireHEP Error: {e}")
                
                # 2. If not found, search Crossref
                if not doi:
                    doi = search_crossref(article_clean)
                    if doi:
                        print(f"  Found DOI from Crossref: {doi}")
                
                # 3. If still not found, try to extract title and search Crossref
                if not doi:
                    # Heuristic: Split by ". " and take the longest part or the second part
                    parts = article_clean.split('. ')
                    if len(parts) >= 2:
                        # Often: Authors. Title. Journal.
                        # Try the second part as title
                        title_candidate = parts[1]
                        if len(title_candidate) > 10:
                             doi = search_crossref(title_candidate)
                             if doi:
                                 print(f"  Found DOI from Crossref (Title search): {doi}")

                time.sleep(0.2) 

            if doi:
                with open(output_file_path, 'a', encoding='utf-8') as f:
                    f.write(f"{teacher}|{doi}\n")
                count += 1

    print(f"Written {count} entries to {output_file_path}")

if __name__ == "__main__":
    md_file = r"d:\programs\checkmentor\Check-Mentor-1\manual_source\202405物理学院本研路上v3.md"
    output_file = r"d:\programs\checkmentor\Check-Mentor-1\inspirehep_source\meta-process\processed.txt"
    extract_doi_from_md(md_file, output_file)
