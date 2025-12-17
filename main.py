import argparse
import sys
import subprocess
from pathlib import Path



def _run_py(script: Path, argv: list[str]) -> int:
    cmd = [sys.executable, str(script), *argv]
    print(f"Running: {cmd}")
    return subprocess.call(cmd)


def cmd_analyze(ns: argparse.Namespace) -> int:
    # 延迟导入，避免未安装依赖时 -h 失败
    from core.workflow_orchestrator import WorkflowOrchestrator
    from core.department_analysis import DepartmentAnalyzer
    
    target = ns.target
    data_root = ns.data_root
    list_file = ns.list_file

    if list_file:
        # --- 批量/系所模式 ---
        print(f"\n🚀 Starting Department Analysis for: {target}")
        print(f"📋 Reading professor list from: {list_file}")
        
        analyzer = DepartmentAnalyzer()
        try:
            professors = analyzer.load_professors(list_file)
        except Exception as e:
            print(f"❌ Error loading list file: {e}")
            return 1
            
        print(f"👥 Found {len(professors)} professors.")
        
        # 1. 批量运行个人分析
        for i, prof_name in enumerate(professors, 1):
            print(f"\n[{i}/{len(professors)}] Analyzing professor: {prof_name} ...")
            try:
                # 批量模式下默认使用 data/<name> 结构，暂不通过 data_root 覆盖
                orchestrator = WorkflowOrchestrator(
                    professor_name=prof_name,
                    test_mode=ns.test_mode,
                    data_root=None 
                )
                orchestrator.run()
            except Exception as e:
                print(f"❌ Error analyzing {prof_name}: {e}")
                # 继续处理下一个
        
        # 2. 运行系所画像生成
        print(f"\n[Department Analysis] Generating portrait for {target}...")
        output_filename = f"{target}_portrait.md"
        analyzer.run(list_file, output_file=output_filename, test_mode=ns.test_mode, department_name=target)
        print(f"✨ All done! Department portrait: output/{output_filename}")
        
    else:
        # --- 单人模式 ---
        # 若未指定 data_root，优先使用 Downloads_md/<target>，否则回退到 data/<target>
        if not data_root:
            repo = Path(__file__).resolve().parent
            dl_md = repo / 'Downloads_md' / target
            data_root = str(dl_md) if dl_md.exists() else None

        orchestrator = WorkflowOrchestrator(
            professor_name=target,
            test_mode=ns.test_mode,
            data_root=data_root,
        )
        orchestrator.run()
    return 0


def cmd_download(ns: argparse.Namespace) -> int:
    repo = Path(__file__).resolve().parent
    script = repo / 'DOIdownloader' / 'download.py'
    # 透传参数（保持与 download.py 对齐的常见选项子集）
    argv = []
    if ns.prod:
        argv.append('--prod')
    if ns.doi:
        argv += ['--doi', ns.doi]
    if ns.teacher:
        argv += ['--teacher', ns.teacher]
    if ns.depth is not None:
        argv += ['--depth', str(ns.depth)]
    if ns.workers is not None:
        argv += ['--workers', str(ns.workers)]
    if ns.from_results:
        # 如果未提供路径，则传 AUTO 由脚本自行决定
        if ns.from_results == 'AUTO':
            argv += ['--from-results']
        else:
            argv += ['--from-results', ns.from_results]
    if ns.pdf_root:
        argv += ['--pdf-root', ns.pdf_root]
    if ns.max_pages is not None:
        argv += ['--max-pages', str(ns.max_pages)]
    if ns.no_cited:
        argv.append('--no-cited')
    return _run_py(script, argv)


def cmd_pdf2md(ns: argparse.Namespace) -> int:
    repo = Path(__file__).resolve().parent
    script = repo / 'pdf2md' / 'pdf2md.py'
    argv = ['--teacher', ns.teacher]
    if ns.pdf_root:
        argv += ['--pdf-root', ns.pdf_root]
    if ns.md_root:
        argv += ['--md-root', ns.md_root]
    if ns.token:
        argv += ['--token', ns.token]
    if ns.subdirs:
        argv += ['--subdirs', ns.subdirs]
    if ns.limit is not None:
        argv += ['--limit', str(ns.limit)]
    return _run_py(script, argv)


def cmd_merge_history(ns: argparse.Namespace) -> int:
    repo = Path(__file__).resolve().parent
    script = repo / 'DOIdownloader' / 'merge_history_to_md.py'
    argv = ['--teacher', ns.teacher]
    if ns.subdir:
        argv += ['--subdir', ns.subdir]
    return _run_py(script, argv)


def cmd_run_all(ns: argparse.Namespace) -> int:
    # 仅整合：pdf2md -> merge_history(main/ref1/ref2) -> analyze
    repo = Path(__file__).resolve().parent
    teacher = ns.target
    pdf_root = ns.pdf_root or str(repo / 'Downloads_pdf')
    md_root = ns.md_root or str(repo / 'Downloads_md')

    # 1) 转换 PDF -> MD（限定 main/ref1/ref2）
    print("[1/3] Converting PDFs to Markdown...")
    ret = cmd_pdf2md(argparse.Namespace(
        teacher=teacher,
        pdf_root=pdf_root,
        md_root=md_root,
        token=ns.token,
        subdirs='main,ref1,ref2',
        limit=ns.limit,
    ))
    if ret != 0:
        return ret

    # 2) 合并 history.json（供前端/后续查看）
    print("[2/3] Merging histories into Downloads_md...")
    for sd in ['main', 'ref1', 'ref2']:
        r = cmd_merge_history(argparse.Namespace(teacher=teacher, subdir=sd))
        if r != 0:
            return r

    # 3) 分析（直接使用 Downloads_md/<teacher> 作为数据根）
    print("[3/3] Running analysis...")
    return cmd_analyze(argparse.Namespace(target=teacher, test_mode=ns.test_mode, data_root=str(Path(md_root) / teacher)))


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description='Check-Mentor 统一入口')
    sub = p.add_subparsers(dest='cmd', required=True)

    # analyze
    pa = sub.add_parser('analyze', help='运行分析工作流，生成最终报告')
    pa.add_argument('--target', required=True, help='要分析的目标教授姓名（或系所名称，若指定了 --list-file）')
    pa.add_argument('--list-file', default=None, help='教授名单文件路径（如 data/finish_mentor.txt）。若指定此项，将批量分析名单中的教授并生成系所画像。')
    pa.add_argument('--test-mode', action='store_true', help='测试模式，仅处理少量数据')
    pa.add_argument('--data-root', default=None, help='数据根目录（包含 main/ref1/ref2 的目录）；默认优先使用 Downloads_md/<target>')
    pa.set_defaults(func=cmd_analyze)

    # download
    pd = sub.add_parser('download', help='从DOI下载PDF（封装 DOIdownloader/download.py）')
    pd.add_argument('--prod', action='store_true', help='生产模式输出')
    pd.add_argument('--doi', default=None, help='DOI 列表，逗号或空白分隔')
    pd.add_argument('--teacher', default=None, help='教师名称（输出目录名）')
    pd.add_argument('--depth', type=int, default=1, help='递归深度')
    pd.add_argument('--workers', type=int, default=4, help='并发线程数')
    pd.add_argument('--from-results', default='AUTO', help='从 results.txt 读取DOI（可指定路径，默认 AUTO）')
    pd.add_argument('--pdf-root', default=None, help='PDF 输出根目录（默认 ./Downloads_pdf）')
    pd.add_argument('--max-pages', type=int, default=None, help='最大页数阈值，超过则跳过下载')
    pd.add_argument('--no-cited', action='store_true', help='禁用被引文章下载')
    pd.set_defaults(func=cmd_download)

    # pdf2md
    pp = sub.add_parser('pdf2md', help='批量将 PDF 转换为 MD（封装 pdf2md/pdf2md.py）')
    pp.add_argument('--teacher', required=True, help='教师名称（输入/输出目录名）')
    pp.add_argument('--pdf-root', default=None, help='PDF 根目录（默认 ./Downloads_pdf）')
    pp.add_argument('--md-root', default=None, help='MD 根目录（默认 ./Downloads_md）')
    pp.add_argument('--token', default=None, help='MinerU API Token（默认读环境变量 MINERU_TOKEN）')
    pp.add_argument('--subdirs', default=None, help='限定处理子目录，逗号分隔，如 main,ref1,ref2')
    pp.add_argument('--limit', type=int, default=None, help='最多处理的文件数')
    pp.set_defaults(func=cmd_pdf2md)

    # merge-history
    pm = sub.add_parser('merge-history', help='合并 Downloads_pdf 与 Downloads_md 下的 history.json')
    pm.add_argument('--teacher', required=True, help='教师名称（文件夹）')
    pm.add_argument('--subdir', default='main', help='子目录（main|cited|ref1|ref2|...）')
    pm.set_defaults(func=cmd_merge_history)

    # run-all
    pr = sub.add_parser('run-all', help='一条龙：pdf2md -> merge-history -> analyze')
    pr.add_argument('--target', required=True, help='教师名称（目标教授）')
    pr.add_argument('--test-mode', action='store_true', help='测试模式，仅处理少量数据')
    pr.add_argument('--pdf-root', default=None, help='PDF 根目录（默认 ./Downloads_pdf）')
    pr.add_argument('--md-root', default=None, help='MD 根目录（默认 ./Downloads_md）')
    pr.add_argument('--token', default=None, help='MinerU API Token（默认读环境变量 MINERU_TOKEN）')
    pr.add_argument('--limit', type=int, default=None, help='最多处理的文件数')
    pr.set_defaults(func=cmd_run_all)

    return p


def main():
    parser = build_parser()
    ns = parser.parse_args()
    return ns.func(ns)

if __name__ == "__main__":
    main()

