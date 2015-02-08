#!/usr/bin/env python3

import os

import yaml

import from_html
from orderddict_yaml import OrderedDictSafeDumper


class APIDumper(OrderedDictSafeDumper):
    """Some adjustments for value representations."""
    def represent_scalar(self, tag, value, style=None):
        if tag == u'tag:yaml.org,2002:str':
            # Block style for multiline strings
            if any(c in value for c in u"\u000a\u000d\u001c\u001d\u001e\u0085\u2028\u2029"):
                style = '|'

            # Use " to denote strings if the string contains ' but not ";
            # but try to do this only when necessary as non-quoted strings are always better
            elif ("'" in value and '"' not in value
                  and (value[0] in "[]{#'}@"
                       or any(s in value for s in (" '", ' #', ', ', ': ')))):
                style = '"'

        return super().represent_scalar(tag, value, style)


class ToYamlWriter(object):
    """Translates Sublime Text API from `SublimeApi` to a YAML string."""

    def __init__(self, api):
        self.api = api

    def to_yaml(self):
        """Build a YAML string from a `SublimeApi` instance.
        """
        return yaml.dump(data, default_flow_style=False, dumper=APIDumper)


def read(api):
    return ToYamlWriter(api)


if __name__ == '__main__':
    if os.path.exists('api.html'):
        api = from_html.read('api.html').to_api()
        yaml_api = read(api).to_yaml()

        print(yaml_api)
        # with open('api.yaml', 'w') as f:
        #     f.write(yaml_api)
    else:
        here = os.path.abspath(os.path.dirname(__file__))
        print('no api.html file found in {}'.format(here))
