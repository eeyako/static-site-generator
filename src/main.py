from textnode import TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode


def main():
    text_node = TextNode(
        text='a cat on a black background',
        text_type='image',
        url='https://i.natgeofe.com/n/548467d8-c5f1-4551-9f58-6817a8d2c45e/NationalGeographic_2572187_square.jpg'
    )
    leaf_node = text_node_to_html_node(text_node=text_node)

    print(leaf_node.to_html())


def text_node_to_html_node(text_node):
    # type: (TextNode) -> LeafNode
    """
    Converts a TextNode to the appropriate LeafNode
    """
    # define functions
    def text_type_text(text_node):
        # type: (TextNode) -> LeafNode
        return LeafNode(value=text_node.text)

    def text_type_bold(text_node):
        # type: (TextNode) -> LeafNode
        return LeafNode(tag='b', value=text_node.text)

    def text_type_italic(text_node):
        # type: (TextNode) -> LeafNode
        return LeafNode(tag='i', value=text_node.text)

    def text_type_code(text_node):
        # type: (TextNode) -> LeafNode
        return LeafNode(tag='code', value=text_node.text)

    def text_type_link(text_node):
        # type: (TextNode) -> LeafNode
        return LeafNode(
            tag='a',
            value=text_node.text,
            props={'href': text_node.url}
        )

    def text_type_image(text_node):
        # type: (TextNode) -> LeafNode
        return LeafNode(
            tag='img',
            value='',
            props={'src': text_node.url, 'alt': text_node.text}
        )

    # define types
    text_type_dict = {
        'text': text_type_text,
        'bold': text_type_bold,
        'italic': text_type_italic,
        'code': text_type_code,
        'link': text_type_link,
        'image': text_type_image
    }

    type_func = text_type_dict.get(text_node.text_type)
    if not type_func:
        raise Exception(f'Invalid type provided: "{text_node.text_type}"')

    return type_func(text_node=text_node)


if __name__ == '__main__':
    main()
