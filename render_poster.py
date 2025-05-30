import frontmatter
import markdown
from jinja2 import Environment, FileSystemLoader, select_autoescape
import os
from datetime import datetime

# --- 配置 ---
MARKDOWN_FILE_PATH = 'content/Compliance-to-Code/_index.md'
TEMPLATE_NAME = 'poster_template.html' # 假设模板和脚本在同一目录，或者提供完整路径
OUTPUT_HTML_PATH = 'static/compliance_to_code_poster.html'
# ------------

def render_md_to_html():
    """ 
    读取 Markdown 文件，使用模板渲染为独立的 HTML 页面。
    """
    try:
        # 1. 读取 Markdown 文件并解析 front matter
        with open(MARKDOWN_FILE_PATH, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
        
        title = post.get('title', 'Untitled Poster')
        author = post.get('author', 'Me') # 从 front matter 获取作者，如果没有则默认为 'Me'
        markdown_content = post.content

        # 2. 将 Markdown 内容转换为 HTML
        #    使用 'fenced_code' (代码块), 'tables' (表格), 'sane_lists' (更合理的列表) 等扩展
        html_content = markdown.markdown(markdown_content, extensions=['fenced_code', 'tables', 'sane_lists', 'toc', 'extra'])

        # 3. 设置 Jinja2 环境并加载模板
        #    假设模板文件和脚本在同一目录下。如果不在，修改 FileSystemLoader 的路径。
        env = Environment(
            loader=FileSystemLoader(os.path.dirname(os.path.abspath(__file__)) or '.'), 
            autoescape=select_autoescape(['html', 'xml'])
        )

        template = env.get_template(TEMPLATE_NAME)

        # 4. 渲染模板
        current_year = datetime.utcnow().strftime('%Y') # 获取当前年份字符串
        rendered_html = template.render(
            title=title,
            content=html_content,
            author=author,
            current_year=current_year # 将年份传递给模板
        )

        # 5. 保存渲染的 HTML 到输出文件
        #    确保输出目录存在 (如果 OUTPUT_HTML_PATH 包含子目录)
        output_dir = os.path.dirname(OUTPUT_HTML_PATH)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
            print(f"Created directory: {output_dir}")

        with open(OUTPUT_HTML_PATH, 'w', encoding='utf-8') as f_out:
            f_out.write(rendered_html)
        
        print(f"Successfully rendered '{MARKDOWN_FILE_PATH}' to '{OUTPUT_HTML_PATH}'")
        print(f"You can now access it (after Hugo build/server) at /{OUTPUT_HTML_PATH.replace('static/', '')}")

    except FileNotFoundError:
        print(f"Error: File not found. Please check paths.")
        print(f"  Markdown file: {os.path.abspath(MARKDOWN_FILE_PATH)}")
        print(f"  Template file: {os.path.abspath(TEMPLATE_NAME)}")
    except Exception as e:
        print(f"An error occurred: {e}")
        import traceback
        print("--- TRACEBACK ---")
        traceback.print_exc()
        print("-----------------")

if __name__ == '__main__':
    render_md_to_html()
