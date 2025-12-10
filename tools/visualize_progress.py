import json
import sys
from pathlib import Path
import platform
import argparse

# 尝试导入可视化库，如果不存在则优雅降级
try:
    import matplotlib.pyplot as plt
    import pandas as pd
    HAS_VIZ_LIBS = True
except ImportError:
    HAS_VIZ_LIBS = False

def get_chinese_font():
    """尝试获取系统中的中文字体，以便在图表中正确显示中文"""
    system = platform.system()
    if system == 'Windows':
        return ['Microsoft YaHei', 'SimHei', 'SimSun', 'KaiTi']
    elif system == 'Darwin': # macOS
        return ['Arial Unicode MS', 'PingFang SC', 'Heiti TC']
    else: # Linux
        return ['WenQuanYi Micro Hei', 'Droid Sans Fallback']

def analyze_progress(data_dir: Path):
    """分析数据目录下的进度"""
    stats = []
    
    if not data_dir.exists():
        print(f"错误: 数据目录不存在 {data_dir}")
        return []

    print(f"正在扫描数据目录: {data_dir} ...")
    
    for teacher_dir in data_dir.iterdir():
        if not teacher_dir.is_dir():
            continue
            
        meta_path = teacher_dir / "metadata_items.json"
        if not meta_path.exists():
            continue
            
        try:
            with open(meta_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            items = data.get("items", [])
            total = len(items)
            if total == 0:
                continue
                
            have_md = sum(1 for i in items if i.get("have_md") is True)
            
            # 按角色统计
            main_total = sum(1 for i in items if i.get("role") == "main")
            main_md = sum(1 for i in items if i.get("role") == "main" and i.get("have_md") is True)
            
            ref_total = sum(1 for i in items if i.get("role") == "reference")
            ref_md = sum(1 for i in items if i.get("role") == "reference" and i.get("have_md") is True)
            
            cited_total = sum(1 for i in items if i.get("role") == "citation")
            cited_md = sum(1 for i in items if i.get("role") == "citation" and i.get("have_md") is True)
            
            stats.append({
                "Teacher": teacher_dir.name,
                "Total Items": total,
                "Total MD": have_md,
                "Completion %": (have_md / total * 100) if total > 0 else 0.0,
                "Main Total": main_total,
                "Main MD": main_md,
                "Ref Total": ref_total,
                "Ref MD": ref_md,
                "Cited Total": cited_total,
                "Cited MD": cited_md
            })
            
        except Exception as e:
            print(f"处理 {teacher_dir.name} 时出错: {e}")
            
    return stats

def print_text_report(stats):
    """打印文本报告"""
    if not stats:
        print("没有找到数据。")
        return

    # 按总数降序排序
    stats.sort(key=lambda x: x["Total Items"], reverse=True)
    
    print("\n" + "="*110)
    print(f"{'老师':<10} | {'总数':<6} | {'原文':<6} | {'已完成':<6} | {'进度':<6} | {'主文章 (完/总)':<15} | {'参考文献 (完/总)':<15} | {'引用 (完/总)':<15}")
    print("-" * 110)
    
    total_items_all = 0
    total_main_all = 0
    total_md_all = 0
    
    for row in stats:
        total_items_all += row['Total Items']
        total_main_all += row['Main Total']
        total_md_all += row['Total MD']
        
        print(f"{row['Teacher']:<10} | {row['Total Items']:<6} | {row['Main Total']:<6} | {row['Total MD']:<6} | {row['Completion %']:<5.1f}% | "
              f"{row['Main MD']}/{row['Main Total']:<13} | {row['Ref MD']}/{row['Ref Total']:<13} | {row['Cited MD']}/{row['Cited Total']:<13}")
    
    print("="*110)
    overall_pct = (total_md_all / total_items_all * 100) if total_items_all > 0 else 0
    print(f"{'总计':<10} | {total_items_all:<6} | {total_main_all:<6} | {total_md_all:<6} | {overall_pct:<5.1f}% |")
    print("="*110)

def generate_chart(stats, output_file):
    """生成图表"""
    if not HAS_VIZ_LIBS:
        print("\n[提示] 未安装 matplotlib 或 pandas，跳过图表生成。")
        print("您可以运行: pip install matplotlib pandas 来启用图表功能。")
        return

    if not stats:
        return

    df = pd.DataFrame(stats)
    df = df.sort_values("Total Items", ascending=False)
    
    # 设置中文字体
    plt.rcParams['font.sans-serif'] = get_chinese_font() + plt.rcParams['font.sans-serif']
    plt.rcParams['axes.unicode_minus'] = False
    
    # 设置图表大小
    plt.figure(figsize=(20, 10))
    
    x = range(len(df))
    width = 0.35
    
    # 绘制柱状图
    plt.bar(x, df["Total Items"], width, label='总条目数 (Total Items)', color='#e0e0e0', edgecolor='grey')
    plt.bar(x, df["Total MD"], width, label='已转换 MD (Converted)', color='#4caf50', edgecolor='darkgreen')
    
    # 绘制原文数量折线
    plt.plot(x, df["Main Total"], color='#2196F3', marker='o', linewidth=2, label='原文数量 (Main Items)', linestyle='-')
    
    # 添加标题和标签
    plt.ylabel('文章数量 (Count)', fontsize=12)
    plt.title('各老师文献处理进度 (Project Progress by Teacher)', fontsize=16)
    plt.xticks(x, df["Teacher"], rotation=45, ha='right', fontsize=10)
    plt.legend(fontsize=12)
    
    # 在柱子上添加数值标签
    for i, v in enumerate(df["Total Items"]):
        plt.text(i, v + 1, str(v), ha='center', va='bottom', fontsize=8, color='grey')
        
    for i, v in enumerate(df["Total MD"]):
        if v > 0:
            plt.text(i, v/2, str(v), ha='center', va='center', fontsize=8, color='white', fontweight='bold')

    # 添加原文数量标签
    for i, v in enumerate(df["Main Total"]):
        plt.text(i, v + 3, str(v), ha='center', va='bottom', fontsize=9, color='#2196F3', fontweight='bold')

    plt.tight_layout()
    
    try:
        plt.savefig(output_file, dpi=300)
        print(f"\n图表已保存至: {output_file}")
    except Exception as e:
        print(f"\n保存图表失败: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="可视化项目进度")
    parser.add_argument("--output", default="progress_chart.png", help="输出图表文件名")
    args = parser.parse_args()
    
    # 自动定位 data 目录
    script_path = Path(__file__).resolve()
    # 假设脚本在 tools/visualize_progress.py，data 在 ../data
    project_root = script_path.parents[1]
    data_dir = project_root / "data"
    
    if not data_dir.exists():
        # 尝试硬编码路径作为回退
        data_dir = Path(r"d:\programs\checkmentor\Check-Mentor-1\data")

    stats = analyze_progress(data_dir)
    print_text_report(stats)
    generate_chart(stats, args.output)
