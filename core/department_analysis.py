import os
import json
from typing import List, Dict, Any
from pathlib import Path
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

from . import config

class DepartmentAnalyzer:
    def __init__(self):
        self.llm = self._init_llm()
        self.log_dir = Path("log")
        self.output_dir = Path("output")
        self.output_dir.mkdir(exist_ok=True)

    def _init_llm(self):
        """Initialize LLM based on config."""
        if config.LLM_PROVIDER == "openai":
            return ChatOpenAI(
                model=config.LLM_MODEL,
                temperature=config.LLM_TEMPERATURE,
                openai_api_key=config.OPENAI_API_KEY,
                openai_api_base=config.OPENAI_API_BASE
            )
        # Add other providers if needed, defaulting to OpenAI for now as per existing code patterns
        return ChatOpenAI(
            model=config.LLM_MODEL,
            temperature=config.LLM_TEMPERATURE,
            openai_api_key=config.OPENAI_API_KEY,
            openai_api_base=config.OPENAI_API_BASE
        )

    def load_professors(self, list_file: str) -> List[str]:
        """Load professor names from a file."""
        path = Path(list_file)
        if not path.exists():
            raise FileNotFoundError(f"Professor list file not found: {list_file}")
        
        with open(path, "r", encoding="utf-8") as f:
            names = [line.strip() for line in f if line.strip()]
        return names

    def collect_data(self, professors: List[str]) -> Dict[str, Any]:
        """
        Collect contribution data for each professor.
        Returns a dictionary mapping professor names to their research summary.
        """
        data = {}
        missing = []
        
        print(f"Collecting data for {len(professors)} professors...")
        
        for name in professors:
            # Try to find contribution output
            # Filename format: {name}_contribution_output.json
            file_path = self.log_dir / f"{name}_contribution_output.json"
            
            if file_path.exists():
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = json.load(f)
                        # Extract relevant info. 
                        # We prefer 'research_directions' or 'contribution_summary'
                        summary = content.get("contribution_summary", "")
                        directions = content.get("research_directions", [])
                        
                        # Combine them for a rich context
                        full_text = f"Summary: {summary}\n\nKey Directions:\n" + "\n".join(directions)
                        data[name] = full_text
                except Exception as e:
                    print(f"Error reading log for {name}: {e}")
                    missing.append(name)
            else:
                missing.append(name)
        
        if missing:
            print(f"⚠️ Warning: Missing analysis logs for {len(missing)} professors: {', '.join(missing)}")
            print("These professors will be skipped in the department analysis.")
            
        return data

    def step1_extract_problems(self, professor_data: Dict[str, str]) -> Dict[str, List[str]]:
        """
        Agent 1: Extract specific research problems for each professor.
        """
        print("\n--- Step 1: Extracting Research Problems ---")
        
        prompt = ChatPromptTemplate.from_template("""
        You are an expert academic analyst.
        
        Analyze the following research summary for professor {name}.
        Extract 3-5 specific "Research Problems" or "Scientific Questions" they are working on.
        
        Rules:
        1. Focus on the *problem* (e.g., "Origin of Neutrino Mass"), not just the field ("Particle Physics").
        2. Be specific but concise (5-10 words per problem).
        3. Return ONLY a JSON list of strings.
        
        Research Summary:
        {summary}
        """)
        
        results = {}
        parser = JsonOutputParser()
        chain = prompt | self.llm | parser
        
        for name, summary in professor_data.items():
            print(f"Processing {name}...")
            try:
                problems = chain.invoke({"name": name, "summary": summary})
                results[name] = problems
            except Exception as e:
                print(f"Error extracting problems for {name}: {e}")
                results[name] = []
                
        return results

    def step2_cluster_themes(self, all_problems: Dict[str, List[str]]) -> Dict[str, Any]:
        """
        Agent 2: Cluster all problems into department-wide themes.
        """
        print("\n--- Step 2: Clustering Research Themes ---")
        
        # Flatten the list for the prompt, but keep track of who does what
        problem_list_text = ""
        for name, problems in all_problems.items():
            problem_list_text += f"{name}: {', '.join(problems)}\n"
            
        prompt = ChatPromptTemplate.from_template("""
        You are a Senior Research Strategist.
        
        Here is a list of research problems worked on by professors in a department:
        
        {problem_list}
        
        Your task:
        1. Analyze these problems to identify 3-6 major "Research Themes" or "Clusters" that define this department.
        2. For each theme, provide:
           - A **Bilingual Title** (e.g., "高能唯象学 (High Energy Phenomenology)")
           - A **Bilingual Description**: Write the description in **Chinese**, but MUST keep key scientific terms in English or use the format "中文术语 (English Term)" to ensure accuracy.
           - A list of "Associated Professors" (based on the input list).
        3. Also provide a **Bilingual Department Summary** (one sentence in Chinese, followed by one sentence in English).
        
        Return the result as a JSON object with the following structure:
        {{
            "department_summary": "中文总结。English summary.",
            "themes": [
                {{
                    "title": "中文标题 (English Title)",
                    "description": "中文描述，包含 English Terms。",
                    "professors": ["Name1", "Name2"]
                }}
            ]
        }}
        """)
        
        parser = JsonOutputParser()
        chain = prompt | self.llm | parser
        
        try:
            return chain.invoke({"problem_list": problem_list_text})
        except Exception as e:
            print(f"Error clustering themes: {e}")
            return {}

    def step3_generate_portrait(self, clusters: Dict[str, Any], output_file: str, department_name: str = "Department"):
        """
        Agent 3: Generate the final Markdown portrait.
        """
        print("\n--- Step 3: Generating Department Portrait ---")
        
        if not clusters:
            print("No clusters to report.")
            return

        md_content = f"# {department_name} - 研究画像 (Research Portrait)\n\n"
        md_content += f"**生成日期**: {os.popen('date /t').read().strip()}\n\n"
        
        md_content += f"## 1. 系所全景\n\n"
        md_content += f"{clusters.get('department_summary', 'N/A')}\n\n"
        
        md_content += f"## 2. 核心研究方向与专家矩阵\n\n"
        
        for theme in clusters.get("themes", []):
            title = theme.get("title", "Untitled")
            desc = theme.get("description", "")
            profs = theme.get("professors", [])
            
            md_content += f"### 🔬 {title}\n\n"
            md_content += f"**核心问题**: {desc}\n\n"
            md_content += f"**相关教授**: {', '.join(profs)}\n\n"
            md_content += "---\n\n"
            
        # Save to file
        out_path = self.output_dir / output_file
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(md_content)
            
        print(f"✅ Department portrait saved to: {out_path}")

    def run(self, list_file: str, output_file: str = "department_portrait.md", test_mode: bool = False, department_name: str = "Department"):
        # 1. Load List
        professors = self.load_professors(list_file)
        
        if test_mode:
            limit = 5
            print(f"⚠️ TEST MODE: Limiting analysis to first {limit} professors.")
            professors = professors[:limit]

        # 2. Collect Data
        data = self.collect_data(professors)
        if not data:
            print("No data collected. Please run individual analysis first.")
            return
            
        # 3. Agent Workflow
        # Step 1: Extract
        problems_map = self.step1_extract_problems(data)
        
        # Step 2: Cluster
        clusters = self.step2_cluster_themes(problems_map)
        
        # Step 3: Report
        self.step3_generate_portrait(clusters, output_file, department_name)

if __name__ == "__main__":
    # Example usage
    analyzer = DepartmentAnalyzer()
    analyzer.run("data/finish_mentor.txt")
