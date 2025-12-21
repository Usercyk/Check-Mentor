import json
import sys
from pathlib import Path
import platform
import argparse

# 尝试导入可视化库，如果不存在则优雅降级
try:
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np
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
        
        items = []
        if meta_path.exists():
            try:
                with open(meta_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                items = data.get("items", [])
            except Exception as e:
                print(f"处理 {teacher_dir.name} 时出错: {e}")
            
        total = len(items)
        # if total == 0: continue # Show all teachers even if 0 items
            
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
            
    return stats

def merge_and_sort_stats(stats):
    """
    合并同名老师（Teacher 和 Teacher+）并按总条目数排序
    如果有合并（存在 Teacher+），在名字后标记 (+)
    """
    groups = {}
    for item in stats:
        name = item['Teacher']
        base_name = name[:-1] if name.endswith('+') else name
        if base_name not in groups:
            groups[base_name] = {
                "Teacher": base_name,
                "Total Items": 0,
                "Total MD": 0,
                "Main Total": 0,
                "Main MD": 0,
                "Ref Total": 0,
                "Ref MD": 0,
                "Cited Total": 0,
                "Cited MD": 0,
                "has_plus": False,
                "Base Total Items": 0,
                "Base Total MD": 0,
                "Plus Total Items": 0,
                "Plus Total MD": 0,
                "Base Main Total": 0,
                "Plus Main Total": 0
            }
        
        g = groups[base_name]
        
        if name.endswith('+'):
            g["has_plus"] = True
            g["Plus Total Items"] += item["Total Items"]
            g["Plus Total MD"] += item["Total MD"]
            g["Plus Main Total"] += item["Main Total"]
        else:
            g["Base Total Items"] += item["Total Items"]
            g["Base Total MD"] += item["Total MD"]
            g["Base Main Total"] += item["Main Total"]

        g["Total Items"] += item["Total Items"]
        g["Total MD"] += item["Total MD"]
        g["Main Total"] += item["Main Total"]
        g["Main MD"] += item["Main MD"]
        g["Ref Total"] += item["Ref Total"]
        g["Ref MD"] += item["Ref MD"]
        g["Cited Total"] += item["Cited Total"]
        g["Cited MD"] += item["Cited MD"]

    # 计算百分比并转为列表
    merged_stats = []
    for base_name, g in groups.items():
        g.pop("has_plus")
            
        total = g["Total Items"]
        g["Completion %"] = (g["Total MD"] / total * 100) if total > 0 else 0.0
        merged_stats.append(g)
    
    # 按总条目数降序排序
    merged_stats.sort(key=lambda x: x["Total Items"], reverse=True)
    
    return merged_stats

def print_text_report(stats):
    """打印文本报告"""
    if not stats:
        print("没有找到数据。")
        return

    # 使用合并排序
    stats = merge_and_sort_stats(stats)
    
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

    # 使用合并排序
    stats = merge_and_sort_stats(stats)
    df = pd.DataFrame(stats)
    # df = df.sort_values("Total Items", ascending=False)
    
    # 设置中文字体
    plt.rcParams['font.sans-serif'] = get_chinese_font() + plt.rcParams['font.sans-serif']
    plt.rcParams['axes.unicode_minus'] = False
    
    # 设置图表大小
    # 动态计算高度：每位老师 0.5 英寸，最小 12 英寸
    height_per_teacher = 0.5
    fig_height = max(12, len(df) * height_per_teacher)
    plt.figure(figsize=(20, fig_height))
    
    # 使用分段线性缩放 (Piecewise Linear Scaling)
    # 0-200: 线性 (1:1) - 重点展示区域
    # >200:  压缩 (1:0.15) - 缩小大数据以便观看
    threshold = 200
    compression = 0.15
    
    def forward(x):
        return np.where(x < threshold, x, threshold + (x - threshold) * compression)

    def inverse(x):
        return np.where(x < threshold, x, threshold + (x - threshold) / compression)

    try:
        plt.xscale('function', functions=(forward, inverse))
        # 手动设置 X 轴刻度以显示压缩效果
        major_ticks = [0, 50, 100, 150, 200, 300, 400, 500, 750, 1000]
        plt.xticks(major_ticks)
    except Exception as e:
        print(f"设置自定义缩放失败，回退到对数刻度: {e}")
        plt.xscale('symlog')

    plt.grid(True, axis='x', which='major', linestyle='--', alpha=0.3)
    
    y = list(range(len(df)))
    
    # 调整柱状图高度 (Horizontal Bar Chart)
    height_total = 0.85
    height_sub = 0.35
    
    # 绘制水平柱状图 (barh)
    # Total Items (Base) - 背景宽柱
    plt.barh(y, df["Base Total Items"], height=height_total, label='基础条目 (Base Items)', color='#f5f5f5', edgecolor='#bdbdbd')
    # Total Items (Plus) - Stacked on Base
    plt.barh(y, df["Plus Total Items"], height=height_total, left=df["Base Total Items"], label='增补条目 (Plus Items)', color='#e0e0e0', edgecolor='#bdbdbd')
    
    # Main Total (Upper) - 上方中柱
    y_upper = [i + 0.2 for i in y]
    plt.barh(y_upper, df["Base Main Total"], height=height_sub, label='基础原文 (Base Main)', color='#90caf9', edgecolor='#1976D2', alpha=0.9)
    plt.barh(y_upper, df["Plus Main Total"], height=height_sub, left=df["Base Main Total"], label='增补原文 (Plus Main)', color='#f48fb1', edgecolor='#C2185B', alpha=0.9)

    # Total MD (Lower) - 下方中柱
    y_lower = [i - 0.2 for i in y]
    plt.barh(y_lower, df["Base Total MD"], height=height_sub, label='基础已转 (Base MD)', color='#a5d6a7', edgecolor='#2e7d32', alpha=0.9)
    plt.barh(y_lower, df["Plus Total MD"], height=height_sub, left=df["Base Total MD"], label='增补已转 (Plus MD)', color='#ffcc80', edgecolor='#ef6c00', alpha=0.9)
    
    # 添加标题和标签
    plt.xlabel('文章数量', fontsize=14)
    plt.title('各老师文献处理进度', fontsize=18)
    plt.yticks(y, df["Teacher"], fontsize=10) # 默认水平显示
    plt.legend(fontsize=12, loc='lower right')
    
    # 反转 Y 轴，使第一项在顶部
    plt.gca().invert_yaxis()
    
    # 在柱子上添加数值标签
    # 总数标签 (Total Items) - 放在宽柱右侧
    for i, (base, plus) in enumerate(zip(df["Base Total Items"], df["Plus Total Items"])):
        total = base + plus
        if total > 0:
            plt.text(total * 1.02, i, str(total), va='center', ha='left', fontsize=8, color='grey')
        
    # 原文标签 (Main Total) - 放在上方柱子
    for i, (base, plus) in enumerate(zip(df["Base Main Total"], df["Plus Main Total"])):
        total = base + plus
        if total > 0:
            plt.text(total, i + 0.2, str(total), va='center', ha='left', fontsize=8, color='#0d47a1', fontweight='bold')

    # 已完成标签 (Total MD) - 放在下方柱子
    for i, (base, plus) in enumerate(zip(df["Base Total MD"], df["Plus Total MD"])):
        total = base + plus
        if total > 0:
            plt.text(total, i - 0.2, str(total), va='center', ha='left', fontsize=8, color='#1b5e20', fontweight='bold')

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
        data_dir = Path(r"E:\program\Check-Mentor-1\data")

    stats = analyze_progress(data_dir)
    print_text_report(stats)
    generate_chart(stats, args.output)
