from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        # type: (str, str, dict[str, str]) -> None
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        # type: () -> str
        if self.value is None:
            raise ValueError("LeafNodes must have a value")

        if not self.tag:
            return self.value

        result = ''

        # open tag
        result += f'<{self.tag}'
        if self.props:
            result += self.props_to_html()
        result += '>'

        # innerHTML
        result += f'{self.value}'

        # close tag
        result += f'</{self.tag}>'

        return result
