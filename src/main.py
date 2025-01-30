from textnode import *
import os, shutil

def copy_static_to_public(src, dst):
    list_public_dir = os.listdir(dst)
    print(list_public_dir)
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
    

def main():
    text_node_test = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(text_node_test)
    copy_static_to_public("./static", "./public")

main()