import json
import re
from pathlib import Path
import os

def sanitize_filename(name: str, max_length: int = 200) -> str:
    """
    Sanitize the filename to match the logic used for creating markdown files.
    Replaces invalid characters with underscores.
    """
    # Replace invalid characters with underscore
    # Windows invalid: < > : " / \ | ? *
    name = re.sub(r'[<>:"/\\|?*\n\t]', '_', name)
    name = name.strip()
    if len(name) > max_length:
        name = name[:max_length].strip()
    return name

def update_metadata(data_dir: Path):
    """
    Iterate through teacher directories, check for markdown files, and update metadata_items.json.
    """
    if not data_dir.exists():
        print(f"Data directory not found: {data_dir}")
        return

    for teacher_dir in data_dir.iterdir():
        if not teacher_dir.is_dir():
            continue
            
        metadata_path = teacher_dir / "metadata_items.json"
        if not metadata_path.exists():
            continue
            
        print(f"Processing {teacher_dir.name}...")
        
        # Collect all md files in teacher's directory
        # We store just the filename (with extension) in a set for fast lookup
        md_files = set()
        try:
            for md_file in teacher_dir.rglob("*.md"):
                md_files.add(md_file.name)
        except Exception as e:
            print(f"  Error scanning directory {teacher_dir}: {e}")
            continue
            
        try:
            with open(metadata_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            items = data.get("items", [])
            if not isinstance(items, list):
                print(f"  Warning: 'items' is not a list in {metadata_path}")
                continue

            updated_count = 0
            
            for item in items:
                if not isinstance(item, dict):
                    continue

                title = item.get("title", "")
                if not title:
                    # If no title, we can't match a file. Set have_md to False if not present.
                    if item.get("have_md") is not False:
                        item["have_md"] = False
                        updated_count += 1
                    continue
                    
                sanitized_title = sanitize_filename(title)
                md_filename = f"{sanitized_title}.md"
                
                has_md = md_filename in md_files
                
                # Check if update is needed
                if item.get("have_md") != has_md:
                    item["have_md"] = has_md
                    updated_count += 1
            
            if updated_count > 0:
                with open(metadata_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                print(f"  Updated {updated_count} items.")
                
        except json.JSONDecodeError:
            print(f"  Error: Invalid JSON in {metadata_path}")
        except Exception as e:
            print(f"  Error processing {metadata_path}: {e}")

if __name__ == "__main__":
    # Assuming the script is run from the project root or tools folder
    # Adjust the path to point to the 'data' directory
    
    # Try to find the data directory relative to this script
    script_path = Path(__file__).resolve()
    project_root = script_path.parents[1] # Assuming tools/update_have_md.py
    data_dir = project_root / "data"
    
    if not data_dir.exists():
        # Fallback to absolute path if relative path fails (e.g. if structure is different)
        data_dir = Path(r"E:\program\Check-Mentor-1\data")
        
    print(f"Using data directory: {data_dir}")
    update_metadata(data_dir)
