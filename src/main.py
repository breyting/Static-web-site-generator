from textnode import *
import os, shutil
from markdown_blocks import *

def copy_static_to_public(src, dst):
    list_public_dir = os.listdir(dst)

    for dir in list_public_dir:
        path = os.path.join(dst, dir)
        if os.path.isfile(path):
            os.remove(path)
        else:
            shutil.rmtree(path)
    list_static_dir = os.listdir(src)
    for element in list_static_dir:
        element_path = os.path.join(src, element)
        dst_path = os.path.join(dst, element)
        if os.path.isfile(element_path):
            shutil.copy(element_path, dst_path)
        else:
            os.mkdir(dst_path)
            copy_static_to_public(element_path, dst_path)

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block.startswith("# "):
            block_split = block.split(" ", 1)
            return block_split[1]

    raise Exception("No h1 header in the template")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as path:
        markdown = path.read()
    with open(template_path) as path:
        template = path.read()
    html_string = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    template_a = template.replace("{{ Title }}", title)
    template_b = template_a.replace("{{ Content }}", html_string)

    with open(dest_path, "a") as file:
        file.write(template_b)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
    list_content_dir = os.listdir(dir_path_content)

    for dir in list_content_dir:
        
        path_dir = os.path.join(dir_path_content, dir)
        new_dest = os.path.join(dest_dir_path, dir)
        if os.path.isfile(path_dir):
            new_dest_file = new_dest[:-3] + ".html"
            print(f"add file : {new_dest_file}")
            generate_page(path_dir, template_path, new_dest_file)
        else:
            print(f"add directory : {new_dest}")
            generate_pages_recursive(path_dir, template_path, new_dest)

def main():

    copy_static_to_public("./static", "./public")
    generate_pages_recursive("./content", "./template.html", "./public")


main()