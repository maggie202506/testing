# generate_docs.py
import os
import yaml

def combine_markdown_files(selected_modules, output_file):
    combined_content = ""
    for module in selected_modules:
        file_path = os.path.join("docs", f"{module}.md")
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                combined_content += file.read() + "\n\n"
    
    # 将组合后的内容写入新的 Markdown 文件
    output_path = os.path.join("docs", output_file)
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(combined_content)

def update_mkdocs_config(selected_model, output_file):
    config_path = "mkdocs.yml"
    with open(config_path, 'r', encoding='utf-8') as file:
        config = yaml.safe_load(file)
    
    # 检查机型分类是否存在，如果不存在则创建
   _section model = next((item for item in config['nav'] if selected_model in item), None)
    if not model_section:
        config['nav'].append({ selected_model: [] })
        model_section = config['nav'][-1][selected_model]
    
    # 添加新的组合文档到机型分类中
    model_section.append({ 'Combined Document': output_file })
    
    with open(config_path, 'w', encoding='utf-8') as file:
        yaml.dump(config, file, default_flow_style=False, sort_keys=False)

def build_mkdocs_site():
    os.system('mkdocs build')

# 示例：用户选择的机型和模块
selected_model = input("Enter model (e.g., modelA): ")
selected_modules = input("Enter modules (comma-separated, e.g., module1,module3): ").split(',')

output_file = f"{selected_model}_combined.md"

# 动态生成文档
combine_markdown_files(selected_modules, output_file)

# 更新 MkDocs 配置
update_mkdocs_config(selected_model, output_file)

# 重新生成文档网站
build_mkdocs_site()