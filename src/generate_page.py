import os
import shutil
from blocktohtml import markdown_to_html_node  

def extract_title(markdown):
    if "# " in markdown.strip().splitlines()[0]:
        return markdown.strip().splitlines()[0][2:]
    raise Exception("The heading must have a single #")

"""
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using template {template_path}")
    md_content = open(from_path).read()
    template_content = open(template_path).read()

    node = markdown_to_html_node(md_content)
    html = node.to_html()
    title = extract_title(md_content)
    
    full_html = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html)
    with open(f"{dest_path}/index.html", "w") as file:
        file.write(full_html)
"""

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):

    template_content = open(template_path).read()

    for content in os.listdir(dir_path_content):
        file_path = os.path.join(dir_path_content, content)
        if os.path.isfile(file_path):
            md_content = open(file_path).read()

            node = markdown_to_html_node(md_content)
            html = node.to_html()
            title = extract_title(md_content)
            full_html = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html)
            real_html = full_html.replace('href="/', 'href="{BASEPATH}"').replace('src="/', 'src="{BASEPATH}"')
            with open(f"{dest_dir_path}/{content.replace(".md", ".html")}", "w") as file:
                file.write(full_html)
            continue

        new_dest_path = os.path.join(dest_dir_path, content)
        os.makedirs(new_dest_path, exist_ok = True)
        generate_pages_recursive(file_path, template_path, new_dest_path)


def copy_files_and_directories(current_path, target_path):
    for content in os.listdir(current_path):
        #print(content)
        path_to_copy = os.path.join(current_path, content)
        if os.path.isfile(path_to_copy):
            shutil.copy(path_to_copy, target_path)
            continue
        new_path = os.path.join(target_path, content)
        os.mkdir(new_path)
        copy_files_and_directories(path_to_copy, new_path)
    return


