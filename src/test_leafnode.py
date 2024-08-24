import unittest

from leafnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_raw_eq(self):
        node = LeafNode(
            tag='p',
            value='This is a paragraph of text.'
        )
        self.assertEqual(
            '<p>This is a paragraph of text.</p>',
            node.to_html()
        )

    def test_props_eq(self):
        node = LeafNode(
            tag='a',
            value='Click me!',
            props={'href': 'https://www.google.com'}
        )
        self.assertEqual(
            '<a href="https://www.google.com">Click me!</a>',
            node.to_html()
        )

    def test_requires_value(self):
        node = LeafNode(
            tag='a',
            props={'href': 'https://www.google.com'}
        )
        self.assertRaises(
            ValueError,
            node.to_html
        )

    def test_ignores_children(self):
        self.assertRaises(
            TypeError,
            LeafNode,
            tag='a',
            value='Click me!',
            children=LeafNode(
                tag='p',
                value='This is a paragraph of text.'
            ),
            props={'href': 'https://www.google.com'}
        )


if __name__ == '__main__':
    unittest.main()
