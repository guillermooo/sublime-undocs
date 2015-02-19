#!/usr/bin/env python3

import os

import yaml
from yaml.nodes import MappingNode, ScalarNode

import from_html
from ordereddict_yaml import OrderedDictSafeDumper


class APIDumper(OrderedDictSafeDumper):
    """Some adjustments for value representations."""
    literal_style_keys = ("description", "original",)

    def represent_mapping(self, tag, mapping, flow_style=None):
        """Changed in that it looks up keys to adjust scalar style"""
        value = []
        node = MappingNode(tag, value, flow_style=flow_style)
        if self.alias_key is not None:
            self.represented_objects[self.alias_key] = node
        best_style = True
        if hasattr(mapping, 'items'):
            mapping = list(mapping.items())
            try:
                mapping = sorted(mapping)
            except TypeError:
                pass
        for item_key, item_value in mapping:
            node_key = self.represent_data(item_key)
            # CHANGES BEGIN
            default_style = self.default_style
            if item_key in self.literal_style_keys:
                self.default_style = '|'
            node_value = self.represent_data(item_value)
            if item_key in self.literal_style_keys:
                self.default_style = default_style
            # CHANGES END
            if not (isinstance(node_key, ScalarNode) and not node_key.style):
                best_style = False
            if not (isinstance(node_value, ScalarNode) and not node_value.style):
                best_style = False
            value.append((node_key, node_value))
        if flow_style is None:
            if self.default_flow_style is not None:
                node.flow_style = self.default_flow_style
            else:
                node.flow_style = best_style
        return node


def to_yaml(api):
    """Build a YAML string from a `SublimeApi` instance.
    """
    return yaml.dump(api.to_data(), default_flow_style=False, Dumper=APIDumper)


def main():
    if not os.path.exists('api.html'):
        here = os.path.abspath(os.path.dirname(__file__))
        print('no api.html file found in {}'.format(here))
        return

    api = from_html.read('api.html').to_api()
    yaml_api = to_yaml(api)

    print(yaml_api)
    with open('api.yaml', 'w') as f:
        f.write(yaml_api)


if __name__ == '__main__':
    main()
