from textnode import *
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue
        
        split_node = []
        node_text_split = node.text.split(delimiter)
        if len(node_text_split) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        
        for i in range(len(node_text_split)):
            if node_text_split[i] == "":
                continue
            if i % 2 == 0:
                split_node.append(TextNode(node_text_split[i], TextType.NORMAL))
            else:
                split_node.append(TextNode(node_text_split[i], text_type))
        new_nodes.extend(split_node)
    return new_nodes

def extract_markdown_images(text):
    markdown_images = []
    regex = r"\!\[(.*?)\]\((.*?)\)"
    return re.findall(regex, text)
    


def extract_markdown_links(text):
    markdown_links = []
    regex = r"[^\!]\[(.*?)\]\((.*?)\)"
    links = re.findall(regex, text)
    return links


