import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )


class testLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode(
            "p",
            "What a strange world",
            None
        )

        node2 = LeafNode(
            "a",
            "Boot.dev, link to success ! (LUL)",
            {"href" : "https://www.google.com"}
        )

        self.assertEqual(
            node.to_html(),
            "<p>What a strange world</p>"
        )

        self.assertEqual(
            node2.to_html(),
            "<a href=\"https://www.google.com\">Boot.dev, link to success ! (LUL)</a>"
        )

    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")


class TestParentNode(unittest.TestCase):
    def test_to_html_classic(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
            )       
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )

    def test_to_html_no_tag(self):
        node = ParentNode(
            None,
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
            )       
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_no_child(self):
        node = ParentNode(
            "p",
            None,
            )       
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_nested_parents(self):
        node = ParentNode(
            "p",
            [
                ParentNode("b", 
                           [
                    LeafNode("h1", "title text"), 
                    LeafNode(None, "Normal text")
                    ],
                    ),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
            )       
        self.assertEqual(
            node.to_html(),
            "<p><b><h1>title text</h1>Normal text</b>Normal text<i>italic text</i>Normal text</p>"
        )
    


if __name__ == "__main__":
    unittest.main()