from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        node_text_split = node.text.split(delimiter)
        new_nodes.append(TextNode(node_text_split[0], TextType.NORMAL))
        new_nodes.append(TextNode(node_text_split[1], text_type))
        new_nodes.append(TextNode(node_text_split[2], TextType.NORMAL))

    return new_nodes