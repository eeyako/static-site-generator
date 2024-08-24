import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_eq(self):
        node = ParentNode(
            tag='p',
            children=[
                LeafNode(
                    tag='b',
                    value='Bold text'
                ),
                LeafNode(
                    tag=None,
                    value='Normal text'
                ),
                LeafNode(
                    tag='i',
                    value='italic text'
                ),
                LeafNode(
                    tag=None,
                    value='Normal text'
                )
            ]
        )

        self.assertEqual(
            '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>',
            node.to_html()
        )

    def test_nested_eq(self):
        node = ParentNode(
            tag='p',
            children=[
                LeafNode(
                    tag='b',
                    value='Bold text'
                ),
                LeafNode(
                    tag=None,
                    value='Normal text'
                ),
                ParentNode(
                    tag='p',
                    children=[
                        LeafNode(
                            tag='b',
                            value='Bold sub text'),
                    ]
                ),
                LeafNode(
                    tag='i',
                    value='italic text'
                )
            ],
        )

        self.assertEqual(
            '<p><b>Bold text</b>Normal text<p><b>Bold sub text</b></p><i>italic text</i></p>',
            node.to_html()
        )

    def test_no_children(self):
        node = ParentNode(
            tag='p'
        )

        self.assertRaises(
            ValueError,
            node.to_html
        )


if __name__ == '__main__':
    unittest.main()
