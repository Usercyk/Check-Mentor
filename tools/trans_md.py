import os
import shutil

def filter_and_copy_files(source_dir, target_dir):
    """
    遍历 source_dir，筛选出 markdown 文件、metadata_items.json 和 finish_mentor.txt，
    并将它们保留到 target_dir 中，保持原始文件结构。

    :param source_dir: 源目录
    :param target_dir: 目标目录
    """
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            # 筛选需要的文件
            if file.endswith('.md') or file == 'metadata_items.json' or file == 'finish_mentor.txt':
                # 构造源文件路径
                source_file = os.path.join(root, file)
                # 构造目标文件路径
                relative_path = os.path.relpath(root, source_dir)
                target_file_dir = os.path.join(target_dir, relative_path)
                target_file = os.path.join(target_file_dir, file)

                # 确保目标目录存在
                os.makedirs(target_file_dir, exist_ok=True)

                # 跳过已存在的文件
                if os.path.exists(target_file):
                    print(f"Skipped (already exists): {target_file}")
                    continue

                # 复制文件
                shutil.copy2(source_file, target_file)
                print(f"Copied: {source_file} -> {target_file}")

if __name__ == "__main__":
    # 示例：用户可以修改 source_dir 和 target_dir
    source_dir = os.path.abspath("E:\\program\\Check-Mentor-1\\data")  # 源目录
    target_dir = os.path.abspath("E:\\data")  # 目标目录

    print(f"Filtering files from {source_dir} to {target_dir}...")
    filter_and_copy_files(source_dir, target_dir)
    print("File filtering and copying completed.")