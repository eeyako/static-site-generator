import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_single_props_to_html(self):
        node = HTMLNode(
            tag='a',
            props={
                'href': 'https://www.boot.dev'
            }
        )
        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.boot.dev"'
        )

    def test_multiple_props_to_html(self):
        node = HTMLNode(
            tag='a',
            props={
                'href': 'https://www.boot.dev',
                'target': '_blank'
            }
        )
        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.boot.dev" target="_blank"'
        )

    def test_repr(self):
        sub_node = HTMLNode(
            tag='a',
            value='sub test link',
            props={
                'href': 'https://www.sub-boot.dev'
            }
        )
        node = HTMLNode(
            tag='a',
            value='test link',
            children=[sub_node],
            props={
                'href': 'https://www.boot.dev',
                'target': '_blank'
            }
        )
        self.assertEqual(
            node.__repr__(),
"""{'name': 'HTMLNode',
 'tag': 'a',
 'value': 'test link',
 'children': [{'name': 'HTMLNode',
               'tag': 'a',
               'value': 'sub test link',
               'children': None,
               'props': {'href': 'https://www.sub-boot.dev'}}],
 'props': {'href': 'https://www.boot.dev', 'target': '_blank'}}"""
        )

    def test_none_initialization(self):
        node = HTMLNode()
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)


if __name__ == '__main__':
    unittest.main()
