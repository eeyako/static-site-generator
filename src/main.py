from textnode import TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode


def main():
    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            ParentNode(
                "p",
                [
                    LeafNode("b", "Bold sub text"),
                ],
            ),
            LeafNode("i", "italic text")
        ],
    )

    print(node.to_html())


if __name__ == '__main__':
    main()
