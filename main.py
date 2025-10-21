
import os
import json
import google.generativeai as genai
import pathlib
import textwrap

# Get the absolute path of the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

def load_config(config_path='config.json'):
    """加载配置文件"""
    try:
        print(f"诊断信息：正在尝试从以下路径加载配置文件: {config_path}")
        with open(config_path, 'r', encoding='utf-8') as f:
            content = f.read()
            print(f"诊断信息：读取到的文件内容: {content}")
            return json.loads(content)
    except FileNotFoundError:
        print(f"错误：配置文件 '{config_path}' 未找到。")
        return None
    except json.JSONDecodeError:
        print(f"错误：配置文件 '{config_path}' 格式不正确。")
        return None
def clean_summary(text):
    """强制清理模型返回的多余格式和引言"""
    # 按行分割文本
    lines = text.splitlines()
    
    # 过滤掉不需要的行
    unwanted_starts = ("好的", "这是", "以下是")
    cleaned_lines = [
        line for line in lines 
        if not line.strip().startswith(unwanted_starts) and 
           "---" not in line and 
           "***" not in line
    ]
    
    # 重新组合为字符串
    cleaned_text = "\n".join(cleaned_lines)
    
    # 移除所有剩余的Markdown符号和标题
    cleaned_text = cleaned_text.replace("###", "").replace("**", "").replace("论文摘要", "")
    
    # 返回清理并去除首尾空格后的纯文本
    return cleaned_text.strip()

def summarize_paper(api_key, paper_content, summary_length):
    """使用Gemini API总结论文"""
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-2.5-pro') # 使用最新的Gemini模型
        
        prompt = f"""
        你是一个文本摘要引擎。严格按照以下规则执行任务：
        1. 直接开始写摘要，绝对不要有任何开场白或引言。
        2. 只输出纯文本，绝对不要使用任何Markdown格式（如'###', '**', '---'）。
        3. 将以下内容总结为一段约{summary_length}词的英文文本。

        内容：
        {paper_content}
        """
        
        response = model.generate_content(prompt)
        
        # 对模型输出进行强制清理
        cleaned_summary = clean_summary(response.text)
        return cleaned_summary
    except Exception as e:
        return f"调用API时出错: {e}"

def process_papers(input_dir, output_dir, config):
    """处理所有论文文件"""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    summary_length = config.get('summary_length', 200)
    api_key = config.get('api_key')

    if not api_key or api_key == "YOUR_API_KEY_HERE":
        print("错误：请在 config.json 文件中设置您的 Gemini API 密钥。")
        return

    for filename in os.listdir(input_dir):
        if filename.endswith(".md"):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)

            print(f"正在处理: {filename}...")

            try:
                with open(input_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                summary = summarize_paper(api_key, content, summary_length)

                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(summary)
                
                print(f"已生成摘要并保存至: {output_path}")

            except Exception as e:
                print(f"处理文件 {filename} 时出错: {e}")

def main():
    """主函数"""
    config_path = os.path.join(script_dir, 'config.json')
    config = load_config(config_path)
    print(f"加载的配置内容: {config}") # <-- 我添加了这一行用于诊断
    if config:
        input_directory = os.path.join(script_dir, 'input_papers')
        output_directory = os.path.join(script_dir, 'output_summaries')
        process_papers(input_directory, output_directory, config)

if __name__ == '__main__':
    main()
"""
This script reads markdown files from an 'input_papers' directory,
summarizes them using the Google Gemini API, and saves the summaries
to an 'output_summaries' directory. Configuration for the API key and
summary length is loaded from a 'config.json' file.
"""
