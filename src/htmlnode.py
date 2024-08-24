from __future__ import annotations


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        # type: (str, str, list[HTMLNode], dict[str, str]) -> None
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        # type: () -> str
        result = ''
        for prop, val in self.props.items():
            result += f' {prop}="{val}"'
        return result

    def __repr__(self):
        # type: () -> str
        from pprint import pformat

        return pformat(self.__get_data_dict(), sort_dicts=False)

    def __get_data_dict(self):
        data_dict = {}
        data_dict['name'] = self.__class__.__name__
        data_dict['tag'] = self.tag
        data_dict['value'] = self.value
        if self.children:
            data_dict['children'] = []
            for child in self.children:
                child_data = child.__get_data_dict()
                data_dict['children'].append(child_data)
        else:
            data_dict['children'] = None
        if self.props:
            data_dict['props'] = {}
            for prop, val in self.props.items():
                data_dict['props'][prop] = val
        else:
            data_dict['props'] = None

        return data_dict
