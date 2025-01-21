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



if __name__ == "__main__":
    unittest.main()