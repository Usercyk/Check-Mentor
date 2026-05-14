"""
工作流编排器 (Workflow Orchestrator)

该模块是新架构的核心，负责：
1. 接收分离后的数据源（main_papers, ref1_papers, cited_papers）。
2. 初始化并调用三个独立的工作流，分别处理三个核心问题。
3. 收集每个工作流的分析结果。
4. 将整合后的结果返回给主流程，用于最终报告的生成。
"""
import os
import uuid
import json
from pathlib import Path
from typing import List, Dict, Any, Optional

from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatTongyi
from langchain_google_genai import ChatGoogleGenerativeAI

from . import config
from .final_analysis import FinalAnalyzer
from .metadata_manager import MetadataManager
from .workflows.workflow_contribution import ContributionWorkflow
from .workflows.workflow_field_problems import FieldProblemsWorkflow
from .workflows.workflow_undergrad_projects import UndergradProjectsWorkflow

def prepare_workflow_inputs(test_mode: bool, limit: int,
                            main_papers: List[Dict[str, Any]],
                            ref1_papers: List[Dict[str, Any]],
                            cited_papers: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    """根据新规则与 test_mode，准备三条工作流的输入。

    假设 main/ref1/cited 已按元数据时序排序（新→旧）。
    """
    if test_mode:
        return {
            # Workflow 1: main（不截断）
            "wf1_main": main_papers,
            # Workflow 2: main 前N + cited 前N（无 ref1）
            "wf2_main": main_papers[:limit],
            "wf2_ref1": [],
            "wf2_cited": cited_papers[:limit],
            # Workflow 3: 仅 cited 前N
            "wf3_main": [],
            "wf3_cited": cited_papers[:limit],
        }
    else:
        return {
            "wf1_main": main_papers,
            "wf2_main": main_papers,
            "wf2_ref1": ref1_papers,
            "wf2_cited": cited_papers,
            "wf3_main": main_papers,
            "wf3_cited": cited_papers,
        }

class WorkflowOrchestrator:
    """
    负责调度和执行所有分析工作流的中心控制器。
    """
    def __init__(self, professor_name: str, test_mode: bool, data_root: Optional[str | Path] = None):
        """
        初始化所有LLM实例、工作流以及配置。
        """
        self._print_section_header("学术开盒demo - 整体流程", level=1)
        print("⚙️  Initializing Workflow Orchestrator...")
        
        self.professor_name = professor_name
        self.test_mode = test_mode
        # 允许外部指定数据根目录（应直接指向包含 main/ref1/ref2 的目录），
        # 默认仍为 data/{professor_name}
        self.data_root = Path(data_root) if data_root else Path(f"data/{self.professor_name}")
        
        # 1. 统一初始化LLM实例
        main_llm = ChatOpenAI(
            model=config.LLM_MODEL,
            openai_api_key=config.OPENAI_API_KEY,
            base_url=config.OPENAI_API_BASE,
            temperature=config.LLM_TEMPERATURE
        )
        
        fallback_llm = None
        if config.DASHSCOPE_API_KEY:
            try:
                fallback_llm = ChatTongyi(
                    model=config.LLM_FALLBACK_MODEL,
                    dashscope_api_key=config.DASHSCOPE_API_KEY,
                    temperature=config.LLM_TEMPERATURE
                )
                print("  -> Fallback LLM (DashScope) initialized successfully.")
            except Exception as e:
                print(f"  ⚠️ Could not initialize Fallback LLM. Reason: {e}")
                fallback_llm = None
        else:
            print("  -> INFO: Fallback LLM not configured. The program will run with the main LLM only.")

        # Initialize Gemini LLM for synthesis
        gemini_llm = None
        if config.GEMINI_API_KEY:
            try:
                # Check if a custom API Base is provided
                if config.GEMINI_API_BASE:
                    print(f"  -> Initializing Gemini via Custom Gateway")
                    # Note: The error "Unknown name 'messages'" indicates the gateway expects Google-native JSON format,
                    # even if it's an 'OpenAI-compatible' gateway URL. It likely proxies directly to Google.
                    # Therefore, we use ChatGoogleGenerativeAI (which sends Google format) but point it to the custom endpoint.
                    gemini_llm = ChatGoogleGenerativeAI(
                        model=config.GEMINI_MODEL,
                        google_api_key=config.GEMINI_API_KEY,
                        temperature=config.LLM_TEMPERATURE,
                        transport="rest",
                        client_options={"api_endpoint": config.GEMINI_API_BASE},
                        timeout=30
                    )
                else:
                    # Use native Google API
                    gemini_llm = ChatGoogleGenerativeAI(
                        model=config.GEMINI_MODEL,
                        google_api_key=config.GEMINI_API_KEY,
                        temperature=config.LLM_TEMPERATURE,
                        transport="rest",
                        timeout=30
                    )
                print("  -> Gemini LLM initialized successfully.")
            except Exception as e:
                print(f"  ⚠️ Could not initialize Gemini LLM. Reason: {e}")
                gemini_llm = None
        else:
            print("  -> INFO: Gemini LLM not configured.")

        # 2. 将LLM实例注入到各个工作流中
        self.contribution_workflow = ContributionWorkflow(main_llm, fallback_llm, gemini_llm)
        self.field_problems_workflow = FieldProblemsWorkflow(main_llm, fallback_llm, gemini_llm)
        # 传递测试模式标志，以便在测试模式下进行更稳健的回退处理
        self.undergrad_projects_workflow = UndergradProjectsWorkflow(main_llm, fallback_llm, gemini_llm, test_mode=self.test_mode)
        
        # 3. 初始化最终分析器，并注入LLM用于翻译
        self.final_analyzer = FinalAnalyzer(self.professor_name, main_llm, gemini_llm)
        
        # 4. 初始化元数据管理器
        self.metadata_manager = MetadataManager()
        
        config.validate_config()
        print("✅ Orchestrator initialized successfully.")

    def _print_section_header(self, title: str, level: int = 1):
        """打印带样式的章节标题"""
        if level == 1:
            print(f"\n{'='*70}\n🎓 {title}\n{'='*70}")
        elif level == 2:
            print(f"\n--- {title} ---")

    def _load_papers_from_dir(self, dir_path: str, author: str, limit: int = 0, source_type: str = "primary") -> List[Dict[str, Any]]:
        """从指定目录加载所有论文的元数据。"""
        papers = []
        full_path = Path(dir_path)
        if not full_path.is_dir():
            # print(f"    ⚠️ Directory does not exist, skipping: {full_path}")
            return papers

        md_files = sorted(list(full_path.glob("*.md")))
        if limit > 0:
            md_files = md_files[:limit]

        for md_file in md_files:
            paper_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, md_file.stem))
            papers.append({
                "id": paper_id,
                "title": md_file.stem,
                "authors": [author],
                "md_filename": str(md_file),
                "source_type": source_type,  # Add source type tag
            })
        return papers

    def run(self):
        """
        执行完整的分析流程，从数据加载到报告生成。
        """
        # 步骤 1: 准备和分离数据源
        self._print_section_header("任务一：准备和分离论文数据源", level=2)
        
        limit = config.TEST_MODE_PAPER_LIMIT if self.test_mode else 0
        
        # 定义主数据路径和副数据路径
        primary_data_path = self.data_root
        secondary_data_path = Path(str(self.data_root) + "+")
        
        # 1. 加载元数据
        print("\n🔍 检查并加载元数据文件...")
        
        # 加载主文件夹元数据
        metadata_file_primary = primary_data_path / "metadata_items.json"
        if metadata_file_primary.exists():
            print(f"  [Metadata Primary] {metadata_file_primary}")
            self.metadata_manager.load_metadata_file(metadata_file_primary)
        else:
            print(f"  ⚠️  未找到主元数据文件: {metadata_file_primary}")
            
        # 加载副文件夹元数据（如果存在）
        if secondary_data_path.exists():
            metadata_file_secondary = secondary_data_path / "metadata_items.json"
            if metadata_file_secondary.exists():
                print(f"  [Metadata Secondary] {metadata_file_secondary}")
                self.metadata_manager.load_metadata_file(metadata_file_secondary)
        
        # 打印元数据统计
        if len(self.metadata_manager.metadata_cache) > 0:
            self.metadata_manager.print_statistics()
        else:
            print("    ℹ️  未加载任何元数据，将使用默认配置")
            
        # 2. 加载论文数据
        def load_papers_from_root(root_path: Path, source_type: str):
            """Helper to load papers from a specific root path."""
            if not root_path.exists():
                return [], [], []
                
            p_main_path = root_path / "main"
            p_ref1_path = root_path / "ref1"
            p_cited_path = root_path / "cited"
            
            # 兼容性检查
            legacy_ref2_path = root_path / "ref2"
            if not p_cited_path.exists() and legacy_ref2_path.exists():
                if source_type == "primary": # 只在主文件夹报兼容性警告，避免重复
                    print("  ⚠️  兼容模式：未找到 'cited' 目录，检测到旧目录 'ref2'，将临时使用 'ref2'。")
                p_cited_path = legacy_ref2_path
            
            p_main = self._load_papers_from_dir(str(p_main_path), self.professor_name, source_type=source_type)
            p_ref1 = self._load_papers_from_dir(str(p_ref1_path), "Various Authors", source_type=source_type)
            p_cited = self._load_papers_from_dir(str(p_cited_path), "Various Authors", source_type=source_type)
            
            return p_main, p_ref1, p_cited

        # 加载主文件夹论文
        main_p, ref1_p, cited_p = load_papers_from_root(primary_data_path, "primary")
        
        # 加载副文件夹论文
        main_s, ref1_s, cited_s = load_papers_from_root(secondary_data_path, "secondary")
        if secondary_data_path.exists():
            print(f"  -> Detected secondary data folder: {secondary_data_path}")
            print(f"     Loaded {len(main_s)} main, {len(ref1_s)} ref1, {len(cited_s)} cited papers from secondary source.")
        
        # 合并论文列表
        main_papers = main_p + main_s
        ref1_papers = ref1_p + ref1_s
        cited_papers = cited_p + cited_s
        
        # 为论文添加元数据信息
        print("\n📝 为论文添加元数据...")
        main_papers = self.metadata_manager.get_papers_with_metadata(main_papers)
        ref1_papers = self.metadata_manager.get_papers_with_metadata(ref1_papers)
        cited_papers = self.metadata_manager.get_papers_with_metadata(cited_papers)
        
        # 按发布时间对论文进行排序（更新的论文在前），为后续“先时序、再取前N”做准备
        if len(self.metadata_manager.metadata_cache) > 0:
            print("  ✓ 按发布时间对论文进行排序（新→旧）...")
            main_papers = self.metadata_manager.sort_papers_by_recency(main_papers, descending=True)
            ref1_papers = self.metadata_manager.sort_papers_by_recency(ref1_papers, descending=True)
            cited_papers = self.metadata_manager.sort_papers_by_recency(cited_papers, descending=True)

        print("  -> 数据源分离完成:")
        print(f"    - 教授代表作 (main): {len(main_papers)} 篇")
        print(f"    - 引用文献 (ref1): {len(ref1_papers)} 篇")
        print(f"    - 潜在项目文献 (cited): {len(cited_papers)} 篇")

        # 基于新规则，准备各工作流的输入（在已排序的列表上再做截断）
        limit = config.TEST_MODE_PAPER_LIMIT
        prepared = prepare_workflow_inputs(self.test_mode, limit, main_papers, ref1_papers, cited_papers)
        if self.test_mode:
            print(f"  -> 测试模式启用：第二工作流使用 main/cited 各前{limit}篇；第三工作流使用 cited 前{limit}篇。")
        wf1_main = prepared["wf1_main"]
        wf2_main = prepared["wf2_main"]
        wf2_ref1 = prepared["wf2_ref1"]
        wf2_cited = prepared["wf2_cited"]
        wf3_main = prepared["wf3_main"]
        wf3_cited = prepared["wf3_cited"]

        def is_core(p: Dict[str, Any]) -> bool:
            md = p.get("metadata") if isinstance(p, dict) else None
            return bool(md.get("is_core_journal", False)) if isinstance(md, dict) else False

        # Workflow-level analysis tasks (papers passed to AI in three workflows)
        workflow_tasks = wf1_main + wf2_main + wf2_ref1 + wf2_cited + wf3_main + wf3_cited
        total_analysis_tasks = len(workflow_tasks)
        core_analysis_tasks = sum(1 for p in workflow_tasks if is_core(p))

        # Unique paper-level statistics (deduplicated by paper_id)
        unique_papers = {}
        for p in workflow_tasks:
            if isinstance(p, dict) and p.get("id"):
                unique_papers[p["id"]] = p
        total_unique_papers = len(unique_papers)
        core_unique_papers = sum(1 for p in unique_papers.values() if is_core(p))

        print(
            "[ANALYSIS_STATS] "
            f"workflow_tasks_total={total_analysis_tasks}, "
            f"workflow_tasks_core={core_analysis_tasks}, "
            f"unique_papers_total={total_unique_papers}, "
            f"unique_papers_core={core_unique_papers}"
        )

        # 创建日志目录
        log_dir = "log"
        os.makedirs(log_dir, exist_ok=True)

        def log_workflow_output(workflow_name: str, data: Any):
            """将工作流的输出结果以JSON格式记录到日志文件。"""
            log_path = os.path.join(log_dir, f"{self.professor_name}_{workflow_name}_output.json")
            try:
                with open(log_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                # print(f"    -> Logged {workflow_name} output to {log_path}")
            except Exception as e:
                print(f"    ⚠️ Failed to log {workflow_name} output. Reason: {e}")

        # 步骤 2: 执行各个工作流
        self._print_section_header("任务二：执行分析工作流", level=2)
        all_results = {}

        # --- 工作流1: 分析教授的核心贡献 ---
        print("\n➡️ [Workflow 1/3] 分析教授的核心贡献...")
        contribution_results = self.contribution_workflow.run(self.professor_name, wf1_main)
        log_workflow_output("contribution", contribution_results)
        all_results['contribution_analysis'] = contribution_results

        # --- 工作流2: 分析领域的热点问题 ---
        print("\n➡️ [Workflow 2/3] 分析领域的热点问题...")
        field_problems_results = self.field_problems_workflow.run(
            professor_name=self.professor_name,
            main_papers=wf2_main,
            ref1_papers=wf2_ref1,
            cited_papers=wf2_cited,
        )
        log_workflow_output("field_problems", field_problems_results)
        all_results['field_problems_analysis'] = field_problems_results

        # --- 工作流3: 分析本科生可参与的项目 ---
        print("\n➡️ [Workflow 3/3] 分析本科生可参与的项目...")
        # 将工作流1的总结作为输入，传递给工作流3
        contribution_summary = contribution_results.get("contribution_summary", "")
        undergrad_projects_results = self.undergrad_projects_workflow.run(
            self.professor_name,
            wf3_main,
            wf3_cited,
            contribution_summary,
        )
        log_workflow_output("undergrad_projects", undergrad_projects_results)
        all_results['undergrad_projects_analysis'] = undergrad_projects_results

        print("\n--- 所有工作流执行完毕 ---\n")

        # 步骤 3: 整合结果并生成最终报告
        self._print_section_header("任务三：整合结果并生成最终报告", level=2)
        
        # 分别生成报告主体（前三章）和附录（第四章）
        report_body = self.final_analyzer.generate_report_body(all_results)
        report_appendix = self.final_analyzer.generate_report_appendix(all_results)

        # 步骤 4: 将报告翻译为中文
        self._print_section_header("任务四：翻译报告为中文", level=2)
        
        # 仅翻译报告主体
        chinese_body = self.final_analyzer.translate_report(report_body, "Chinese")
        
        # 将未翻译的附录拼接到翻译后的主体后面
        chinese_report = chinese_body + "\n\n" + report_appendix

        # 步骤 5: 保存最终报告
        report_filename = config.OUTPUT_DIR / f"{self.professor_name}_final_report.md"
        with open(report_filename, 'w', encoding='utf-8') as f:
            f.write(chinese_report)
        print(f"\n✅ 最终报告已保存至: {report_filename}")

        self._print_section_header("学术开盒完成", level=1)
