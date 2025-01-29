from htmlnode import (HTMLNode, LeafNode, ParentNode)

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"

def markdown_to_blocks(markdown):
    blocks = []
    split_markdown = markdown.split("\n\n")
    for block in split_markdown:
        if block == "":
            continue
        blocks.append(block.strip())
    return blocks

def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return block_type_heading
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return block_type_code
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return block_type_paragraph
        return block_type_ulist
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return block_type_paragraph
        return block_type_ulist
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return block_type_paragraph
            i += 1
        return block_type_olist
    return block_type_paragraph
            

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    HTMLNode_from_block = []

    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == block_type_paragraph:
            HTMLNode_from_block.append(LeafNode("p", block))
        elif block_type == block_type_heading:
            HTMLNode_from_block.append(block_heading(block))
        elif block_type == block_type_code:
            child_code = LeafNode("code", block)
            HTMLNode_from_block.append(ParentNode("pre", child_code))
        elif block_type == block_type_quote:
            HTMLNode_from_block.append(LeafNode("blockquote", block))
        elif block_type == block_type_olist:
            HTMLNode_from_block.append(block_list(block, "ol"))
        elif block_type == block_type_ulist:
            HTMLNode_from_block.append(block_list(block, "ul"))
    
    return ParentNode("div", HTMLNode_from_block)

def block_heading(block):
    block_split = block.split(" ", 1)
    len_heading = len(block_split[0])
    text = block_split[1]
    return LeafNode(f"h{len_heading}", text)

    
def block_list(block, tag):
    lines = block.split("\n")
    list_of_li = []

    for line in lines:
        line_split = line.split(" ", 1)
        list_of_li.append(LeafNode("li", line_split[1]))

    return ParentNode(tag, list_of_li)

