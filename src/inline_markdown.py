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


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.NORMAL:
            new_nodes.append(old_node)
            continue

        original_text = old_node.text
        images = extract_markdown_images(old_node.text)

        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.NORMAL))
            new_nodes.append(
                TextNode(
                    image[0],
                    TextType.IMAGE,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.NORMAL))
    return new_nodes 



def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.NORMAL:
            new_nodes.append(old_node)
            continue

        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.NORMAL))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.NORMAL))   
    return new_nodes 


def text_to_textnodes(text):
    old_node = TextNode(text, TextType.NORMAL)

    code_node = split_nodes_delimiter([old_node], "`", TextType.CODE)
    bold_node = split_nodes_delimiter(code_node, "**", TextType.BOLD)
    italic_node = split_nodes_delimiter(bold_node, "*", TextType.ITALIC)
    image_node = split_nodes_image(italic_node)
    link_node = split_nodes_link(image_node)
    return link_node

def markdown_to_blocks(markdown):
    blocks = []
    split_markdown = markdown.split("\n\n")
    for block in split_markdown:
        if block == "":
            continue
        blocks.append(block.strip())
    return blocks

