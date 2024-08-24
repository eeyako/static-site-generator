from __future__ import annotations


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other: TextNode) -> bool:
        return all([
            self.text == other.text,
            self.text_type == other.text,
            self.url == other.url
        ])

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return f'{class_name}({self.text}, {self.text_type}, {self.url})'
