import unittest

from textnode import *
from split_nodes import *

class Test_split_nodes_delimiter(unittest.TestCase):
    def test_delimiter_code(self):
        node = TextNode("This is text with a `code block` word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        result = [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.NORMAL),
        ]
        self.assertEqual(new_nodes, result)

    def test_delimiter_bold(self):
        node = TextNode("This is text with a **bold block** word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        result = [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("bold block", TextType.BOLD),
            TextNode(" word", TextType.NORMAL),
        ]
        self.assertEqual(new_nodes, result)

    def test_delimiter_italic(self):
        node = TextNode("This is text with a *italic block* word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        result = [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("italic block", TextType.ITALIC),
            TextNode(" word", TextType.NORMAL),
        ]
        self.assertEqual(new_nodes, result)