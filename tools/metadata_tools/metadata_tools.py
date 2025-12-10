"""
元数据工具脚本

提供命令行工具用于：
1. 验证元数据文件的格式
2. 生成元数据模板
3. 查看元数据统计
4. 测试元数据功能
"""
import json
import argparse
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, Any

# Ensure core modules can be imported when running as a script
sys.path.append(str(Path(__file__).resolve().parents[1]))

from core.metadata_manager import MetadataManager, PaperMetadata


def validate_metadata_file(file_path: Path) -> tuple[bool, list[str]]:
    """
    验证元数据文件的格式
    
    支持两种格式：
    1. 新格式（items数组）：{"items": [{title, doi, authors, published: {year, month}}]}
    2. 旧格式（文件名映射）：{"filename.md": {doi, authors, published: {year, month}}}
    
    Returns:
        (是否有效, 错误列表)
    """
    errors = []
    
    if not file_path.exists():
        errors.append(f"文件不存在: {file_path}")
        return False, errors
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        errors.append(f"JSON格式错误: {e}")
        return False, errors
    except Exception as e:
        errors.append(f"读取文件失败: {e}")
        return False, errors
    
    if not isinstance(data, dict):
        errors.append("根节点必须是字典")
        return False, errors
    
    # 检测格式类型
    if "items" in data:
        # 新格式：items 数组
        items = data.get("items", [])
        if not isinstance(items, list):
            errors.append("items 必须是数组")
            return False, errors
        
        for i, item in enumerate(items):
            prefix = f"[item {i}]"
            
            if not isinstance(item, dict):
                errors.append(f"{prefix} 必须是字典")
                continue
            
            # 检查必需字段
            required_fields = ["title", "doi", "authors"]
            for field in required_fields:
                if field not in item:
                    errors.append(f"{prefix} 缺少必需字段: {field}")
            
            # 验证字段类型
            if "title" in item and not isinstance(item["title"], str):
                errors.append(f"{prefix} title 必须是字符串")
            
            if "doi" in item and not isinstance(item["doi"], str):
                errors.append(f"{prefix} doi 必须是字符串")
            
            if "authors" in item:
                if not isinstance(item["authors"], list):
                    errors.append(f"{prefix} authors 必须是列表")
                elif not all(isinstance(a, str) for a in item["authors"]):
                    errors.append(f"{prefix} authors 列表中的所有元素必须是字符串")
            
            # 验证 published 字段（可选）
            if "published" in item:
                if not isinstance(item["published"], dict):
                    errors.append(f"{prefix} published 必须是字典")
                else:
                    if "year" in item["published"]:
                        if not isinstance(item["published"]["year"], int):
                            errors.append(f"{prefix} published.year 必须是整数")
                    if "month" in item["published"]:
                        month = item["published"]["month"]
                        if not isinstance(month, int) or not (1 <= month <= 12):
                            errors.append(f"{prefix} published.month 必须是1-12之间的整数")
    
    else:
        # 旧格式：文件名映射（向后兼容）
        for filename, metadata in data.items():
            prefix = f"[{filename}]"
            
            # 检查必需字段
            required_fields = ["doi", "authors"]
            for field in required_fields:
                if field not in metadata:
                    errors.append(f"{prefix} 缺少必需字段: {field}")
            
            # 验证字段类型
            if "doi" in metadata and not isinstance(metadata["doi"], str):
                errors.append(f"{prefix} doi 必须是字符串")
            
            if "authors" in metadata:
                if not isinstance(metadata["authors"], list):
                    errors.append(f"{prefix} authors 必须是列表")
                elif not all(isinstance(a, str) for a in metadata["authors"]):
                    errors.append(f"{prefix} authors 列表中的所有元素必须是字符串")
            
            # 验证 published 字段（可选）
            if "published" in metadata:
                if not isinstance(metadata["published"], dict):
                    errors.append(f"{prefix} published 必须是字典")
                else:
                    if "year" in metadata["published"]:
                        if not isinstance(metadata["published"]["year"], int):
                            errors.append(f"{prefix} published.year 必须是整数")
                    if "month" in metadata["published"]:
                        month = metadata["published"]["month"]
                        if not isinstance(month, int) or not (1 <= month <= 12):
                            errors.append(f"{prefix} published.month 必须是1-12之间的整数")
    
    return len(errors) == 0, errors


def generate_template(output_path: Path, paper_directory: Path = None):
    """
    生成元数据模板
    
    Args:
        output_path: 输出文件路径
        paper_directory: 论文目录（如果提供，将为所有 .md 文件生成条目）
    """
    if paper_directory and paper_directory.exists():
        # 为目录中的所有 .md 文件生成模板（新格式）
        md_files = sorted(paper_directory.glob("*.md"))
        items = []
        for md_file in md_files:
            # 去掉 .md 扩展名作为 title
            title = md_file.stem
            items.append({
                "title": title,
                "doi": "",
                "authors": [],
                "published": {
                    "year": 2024,
                    "month": 1
                }
            })
        template = {"items": items}
        print(f"✓ 为 {len(md_files)} 篇论文生成了模板条目")
    else:
        # 生成示例模板（新格式）
        template = {
            "items": [
                {
                    "title": "示例论文标题",
                    "doi": "10.xxxx/xxxxx",
                    "authors": ["作者1", "作者2", "作者3"],
                    "published": {
                        "year": 2024,
                        "month": 1
                    }
                }
            ]
        }
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(template, f, ensure_ascii=False, indent=2)
    
    print(f"✓ 模板已生成: {output_path}")


def merge_metadata_files(input_files: list[Path], output_file: Path):
    """
    合并多个元数据文件
    
    Args:
        input_files: 输入文件路径列表
        output_file: 输出文件路径
    """
    merged_items = []
    seen_dois = set()
    
    print(f"正在合并 {len(input_files)} 个文件...")
    
    for file_path in input_files:
        if not file_path.exists():
            print(f"⚠️ 跳过不存在的文件: {file_path}")
            continue
            
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            items = []
            if isinstance(data, list):
                items = data
            elif isinstance(data, dict):
                if "items" in data and isinstance(data["items"], list):
                    items = data["items"]
                else:
                    # 判断是"旧格式(文件名->元数据)"还是"单条元数据"
                    # 如果所有值都是字典，则认为是旧格式映射；否则认为是单条记录
                    is_map_of_items = True
                    if not data:
                        is_map_of_items = False
                    else:
                        for v in data.values():
                            if not isinstance(v, dict):
                                is_map_of_items = False
                                break
                    
                    if is_map_of_items:
                        # 旧格式转换
                        for filename, meta in data.items():
                            item = meta.copy()
                            # 如果没有 title，尝试从文件名获取
                            if "title" not in item:
                                item["title"] = Path(filename).stem
                            items.append(item)
                    else:
                        # 单条记录格式
                        item = data.copy()
                        if "title" not in item:
                            item["title"] = file_path.stem
                        items.append(item)
            
            count = 0
            for item in items:
                # 简单的去重策略：基于 DOI
                doi = item.get("doi")
                if doi:
                    # 规范化 DOI (简单去除空白)
                    doi = doi.strip()
                    if doi in seen_dois:
                        continue
                    seen_dois.add(doi)
                
                merged_items.append(item)
                count += 1
            
            print(f"  + 从 {file_path.name} 添加了 {count} 条记录")
            
        except Exception as e:
            print(f"❌ 处理文件 {file_path} 时出错: {e}")
    
    result = {"items": merged_items}
    
    try:
        # 确保输出目录存在
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        print(f"✅ 合并完成! 结果已保存至: {output_file}")
        print(f"   总记录数: {len(merged_items)}")
    except Exception as e:
        print(f"❌ 保存输出文件时出错: {e}")


def show_statistics(file_path: Path):
    """显示元数据统计信息"""
    manager = MetadataManager()
    
    if manager.load_metadata_file(file_path):
        print("\n" + "="*60)
        manager.print_statistics()
        print("="*60)
        
        # 显示详细信息
        print("\n📝 详细信息:")
        for filename, metadata in sorted(manager.metadata_cache.items()):
            print(f"\n  📄 {filename}")
            print(f"     DOI: {metadata.doi}")
            print(f"     作者: {', '.join(metadata.authors) if metadata.authors else '无'}")
            print(f"     发布日期: {metadata.get_publish_date_str()}")
            print(f"     时效性得分: {metadata.get_recency_score():.3f}")


def test_metadata_features():
    """测试元数据功能"""
    print("🧪 测试元数据功能...\n")
    
    # 测试1: 创建元数据对象
    print("测试 1: 创建元数据对象")
    metadata = PaperMetadata(
        doi="10.1038/test",
        authors=["Alice", "Bob", "Charlie"],
        publish_year=2024,
        publish_month=1
    )
    print(f"  ✓ 创建成功")
    print(f"    - 发布年份: {metadata.get_publish_year()}")
    print(f"    - 发布日期字符串: {metadata.get_publish_date_str()}")
    print(f"    - 时效性得分: {metadata.get_recency_score():.3f}")
    
    # 测试2: 时效性计算
    print("\n测试 2: 不同年份的时效性得分")
    test_years = [2024, 2020, 2015, 2010, 2000]
    current_year = datetime.now().year
    for year in test_years:
        m = PaperMetadata(publish_year=year)
        score = m.get_recency_score()
        age = current_year - year
        print(f"  {year} ({age}年前): {score:.3f}")
    
    # 测试3: 字典转换（新格式）
    print("\n测试 3: 字典序列化和反序列化（新格式）")
    original = PaperMetadata(
        doi="10.1234/test",
        authors=["Author1", "Author2"],
        publish_year=2023,
        publish_month=6
    )
    dict_data = original.to_dict()
    restored = PaperMetadata.from_dict(dict_data)
    print(f"  ✓ 序列化成功: {json.dumps(dict_data, ensure_ascii=False)}")
    print(f"  ✓ 反序列化成功: DOI={restored.doi}, 作者数={len(restored.authors)}")
    
    # 测试4: 元数据管理器
    print("\n测试 4: 元数据管理器")
    manager = MetadataManager()
    manager.add_metadata("test1.md", metadata)
    retrieved = manager.get_metadata("test1.md")
    print(f"  ✓ 添加和检索成功")
    print(f"  ✓ 检索到的 DOI: {retrieved.doi}")
    
    # 测试5: 从items数组加载
    print("\n测试 5: 从items数组格式加载")
    test_data = {
        "items": [
            {
                "title": "Test Paper 1",
                "doi": "10.1234/test1",
                "authors": ["Author A", "Author B"],
                "published": {"year": 2023, "month": 5}
            },
            {
                "title": "Test Paper 2",
                "doi": "10.1234/test2",
                "authors": ["Author C"],
                "published": {"year": 2024}
            }
        ]
    }
    # 创建临时文件
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False, encoding='utf-8') as f:
        json.dump(test_data, f, ensure_ascii=False, indent=2)
        temp_file = f.name
    
    manager2 = MetadataManager()
    success = manager2.load_metadata_file(Path(temp_file))
    print(f"  ✓ 加载成功: {success}")
    print(f"  ✓ 加载了 {len(manager2.metadata_cache)} 条记录")
    
    # 清理临时文件
    import os
    os.unlink(temp_file)
    
    print("\n✅ 所有测试通过!")


def main():
    parser = argparse.ArgumentParser(
        description="元数据工具 - 验证、生成和测试论文元数据"
    )
    
    subparsers = parser.add_subparsers(dest='command', help='子命令')
    
    # validate 命令
    validate_parser = subparsers.add_parser('validate', help='验证元数据文件')
    validate_parser.add_argument('file', type=str, help='元数据文件路径')
    
    # generate 命令
    generate_parser = subparsers.add_parser('generate', help='生成元数据模板')
    generate_parser.add_argument('output', type=str, help='输出文件路径')
    generate_parser.add_argument(
        '--paper-dir',
        type=str,
        help='论文目录（可选，为目录中的所有 .md 文件生成条目）'
    )
    
    # stats 命令
    stats_parser = subparsers.add_parser('stats', help='显示元数据统计')
    stats_parser.add_argument('file', type=str, help='元数据文件路径')
    
    # merge 命令
    merge_parser = subparsers.add_parser('merge', help='合并多个元数据文件')
    merge_parser.add_argument('inputs', nargs='+', help='输入文件路径列表')
    merge_parser.add_argument('-o', '--output', required=True, help='输出文件路径')

    # test 命令
    test_parser = subparsers.add_parser('test', help='测试元数据功能')
    
    args = parser.parse_args()
    
    if args.command == 'validate':
        file_path = Path(args.file)
        print(f"🔍 验证元数据文件: {file_path}\n")
        is_valid, errors = validate_metadata_file(file_path)
        
        if is_valid:
            print("✅ 元数据文件有效!")
        else:
            print("❌ 元数据文件无效:\n")
            for error in errors:
                print(f"  • {error}")
            return 1
    
    elif args.command == 'generate':
        output_path = Path(args.output)
        paper_dir = Path(args.paper_dir) if args.paper_dir else None
        
        print(f"📝 生成元数据模板: {output_path}\n")
        generate_template(output_path, paper_dir)
    
    elif args.command == 'stats':
        file_path = Path(args.file)
        print(f"📊 分析元数据文件: {file_path}\n")
        show_statistics(file_path)

    elif args.command == 'merge':
        input_files = [Path(p) for p in args.inputs]
        output_file = Path(args.output)
        merge_metadata_files(input_files, output_file)
    
    elif args.command == 'test':
        test_metadata_features()
    
    else:
        parser.print_help()
    
    return 0


if __name__ == "__main__":
    exit(main())
