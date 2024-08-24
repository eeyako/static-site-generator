from textnode import TextNode
from htmlnode import HTMLNode


def main():
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
    print(node)


if __name__ == '__main__':
    main()
