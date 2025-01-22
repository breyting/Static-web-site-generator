import unittest

from textnode import *
from htmlnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.BOLD, "https:/boot.dev")
        node4 = TextNode("This is a text node", TextType.NORMAL, "https:/boot.dev")
        self.assertEqual(node, node2)
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node3, node4)

    def test_text_node_to_html_node(self):
        text_node_normal = TextNode("blabla", TextType.NORMAL)
        html_node = text_node_to_html_node(text_node_normal)
        result_text_node_normal_to_html_node = LeafNode(None, "blabla")
        self.assertEqual(
            text_node_to_html_node(text_node_normal), 
            result_text_node_normal_to_html_node
        )

        text_node_link = TextNode("blabla", TextType.LINK, "haha.com")
        result_text_node_link_to_html_node = LeafNode("a", "blabla", {"href" : "haha.com"})
        self.assertEqual(
            text_node_to_html_node(text_node_link), 
            result_text_node_link_to_html_node
        )

        text_node_wrong = TextNode("blibli", "hihi", "huhu.com")
        with self.assertRaises(ValueError):
            text_node_to_html_node(text_node_wrong)
    
    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )



if __name__ == "__main__":
    unittest.main()