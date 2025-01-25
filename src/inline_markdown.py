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

        split_node = []
        images = extract_markdown_images(old_node.text)

        regex = r"\!\[(.*?)\)"
        split_text = re.split(regex, old_node.text)

        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        
        image_number = 0
        for element in split_text:
            if element == "":
                continue
            if "](" in element:
                split_node.append(TextNode(images[image_number][0], TextType.IMAGE, images[image_number][1]))
                image_number += 1
            else:
                split_node.append(TextNode(element, TextType.NORMAL))

        new_nodes.extend(split_node)        
    return new_nodes 



def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.NORMAL:
            new_nodes.append(old_node)
            continue

        split_node = []
        links = extract_markdown_links(old_node.text)

        regex = r"[^\!]\[(.*?)\)"
        split_text = re.split(regex, old_node.text)

        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        
        link_number = 0
        for element in split_text:
            if element == "":
                continue
            if "](" in element:
                split_node.append(TextNode(links[link_number][0], TextType.LINK, links[link_number][1]))
                link_number += 1
            else:
                if element == split_text[-1]:
                    split_node.append(TextNode(element, TextType.NORMAL))
                else:
                    split_node.append(TextNode(element + " ", TextType.NORMAL))
        new_nodes.extend(split_node)        
    return new_nodes 
