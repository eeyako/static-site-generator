from htmlnode import HTMLNode


class ParentNode(HTMLNode):

    def __init__(self, tag=None, children=None, props=None) -> None:
        # type: (str, list[HTMLNode], dict[str, str]) -> None
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        # type: () -> str
        if not self.tag:
            raise ValueError("ParentNodes must have a tag.")
        if not self.children:
            raise ValueError("ParentNodes must have children nodes.")

        result = ''

        # open tag
        result += f'<{self.tag}'
        if self.props:
            result += self.props_to_html()
        result += '>'

        # children
        for child in self.children:
            result += child.to_html()

        # close tag
        result += f'</{self.tag}>'

        return result
