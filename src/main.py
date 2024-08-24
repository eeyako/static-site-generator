from textnode import TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode


def main():
    node_a = LeafNode("p", "This is a paragraph of text.")
    print(node_a.to_html())

    node_b = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    print(node_b.to_html())


if __name__ == '__main__':
    main()
