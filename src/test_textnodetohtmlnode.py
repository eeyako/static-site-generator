import unittest

from textnode import TextNode
from main import text_node_to_html_node


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_raw_text(self):
        text_node = TextNode(
            text='This is a raw text value',
            text_type='text'
        )
        leaf_node = text_node_to_html_node(text_node=text_node)

        self.assertEqual(
            'This is a raw text value',
            leaf_node.to_html()
        )

    def test_bold_text(self):
        text_node = TextNode(
            text='This is a bold text',
            text_type='bold'
        )
        leaf_node = text_node_to_html_node(text_node=text_node)

        self.assertEqual(
            '<b>This is a bold text</b>',
            leaf_node.to_html()
        )

    def test_italic_text(self):
        text_node = TextNode(
            text='This is an italic text',
            text_type='italic'
        )
        leaf_node = text_node_to_html_node(text_node=text_node)

        self.assertEqual(
            '<i>This is an italic text</i>',
            leaf_node.to_html()
        )

    def test_code_text(self):
        text_node = TextNode(
            text='This is a code text',
            text_type='code'
        )
        leaf_node = text_node_to_html_node(text_node=text_node)

        self.assertEqual(
            '<code>This is a code text</code>',
            leaf_node.to_html()
        )

    def test_link_text(self):
        text_node = TextNode(
            text='This is a link text',
            text_type='link',
            url='https://www.boot.dev'
        )
        leaf_node = text_node_to_html_node(text_node=text_node)

        self.assertEqual(
            '<a href="https://www.boot.dev">This is a link text</a>',
            leaf_node.to_html()
        )

    def test_image(self):
        text_node = TextNode(
            text='a cat on a black background',
            text_type='image',
            url='https://i.natgeofe.com/n/548467d8-c5f1-4551-9f58-6817a8d2c45e/NationalGeographic_2572187_square.jpg'
        )
        leaf_node = text_node_to_html_node(text_node=text_node)

        self.assertEqual(
            '<img src="https://i.natgeofe.com/n/548467d8-c5f1-4551-9f58-6817a8d2c45e/NationalGeographic_2572187_square.jpg" alt="a cat on a black background"></img>',
            leaf_node.to_html()

        )


if __name__ == '__main__':
    unittest.main()
