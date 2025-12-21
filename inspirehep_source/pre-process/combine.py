import os
import shutil
from collections import defaultdict

def parse_results(filepath):
    data = defaultdict(set)
    current_author = None
    
    if not os.path.exists(filepath):
        return data

    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        if line.startswith('👤'):
            current_author = line.replace('👤', '').strip()
        elif line.startswith('='):
            continue
        elif line.startswith('#'):
            continue
        elif current_author:
            # Assume it's a DOI if we have an author context and it's not a separator/header
            # Basic validation to ensure it looks like a DOI or at least not garbage
            if line: 
                data[current_author].add(line)
    return data

def parse_manuallist(filepath, data):
    if not os.path.exists(filepath):
        print(f"{filepath} not found.")
        return data

    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if '|' in line:
                parts = line.split('|')
                if len(parts) >= 2:
                    name = parts[0].strip()
                    doi = parts[1].strip()
                    data[name].add(doi)
    return data

def parse_old_results(filepath, data):
    if not os.path.exists(filepath):
        print(f"{filepath} not found.")
        return data

    current_author = None
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        if line.startswith('='):
            continue
        
        # Heuristic: DOIs usually start with 10.
        if line.startswith('10.'):
            if current_author:
                data[current_author].add(line)
        else:
            # Assume it's an author name if it's not a separator and not a DOI
            # Also skip if it looks like a header or comment
            if not line.startswith('#'):
                current_author = line
            
    return data

def write_results(filepath, data):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write("## 论文 DOI 及作者列表 (严格匹配模式)\n\n")
        
        sorted_authors = sorted(data.keys())
        
        for author in sorted_authors:
            f.write("=" * 50 + "\n")
            f.write(f"👤 {author}\n")
            f.write("=" * 50 + "\n\n")
            
            sorted_dois = sorted(list(data[author]))
            for doi in sorted_dois:
                f.write(f"{doi}\n")
            f.write("\n")

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    results_path = os.path.join(base_dir, 'results.txt')
    manuallist_path = os.path.join(base_dir, 'manuallist.txt')
    old_results_path = os.path.join(base_dir, 'old_result.txt')
    
    # Backup results.txt
    if os.path.exists(results_path):
        shutil.copy(results_path, results_path + '.bak')
        print(f"Backed up {results_path} to {results_path}.bak")

    data = parse_results(results_path)
    data = parse_manuallist(manuallist_path, data)
    data = parse_old_results(old_results_path, data)
    
    write_results(results_path, data)
    print(f"Merged {manuallist_path} and {old_results_path} into {results_path}")

if __name__ == "__main__":
    main()
