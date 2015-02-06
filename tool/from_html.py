import os

import bs4

from st_api import *


class FromHtmlReader(object):
    """
    Translates the Sublime Text API html representation to a `SublimeApi`
    instance.
    """
    def __init__(self, html):
        self.html = html

    def extract_functions(self, table):
        trs = table.find_all('tr')
        funcs = []
        for tr in trs:
            # skip newlines
            data = list(item for item in tr.children
                             if not isinstance(item, bs4.NavigableString))
            func_name = data[0].text
            # skip headings
            if func_name in ('Methods', 'Properties', 'Constructors'):
                continue
            ret_value = data[1].text
            try:
                desc = data[2].text
            except:
                desc = "n/a"

            member = Member(None)
            member.name = func_name
            member.return_value = ret_value
            member.description = desc
            funcs.append(member)

        return funcs

    def make_class(self, name, table):
        cls = Class(None)
        cls.name = name
        cls.members = self.extract_functions(table)
        return cls

    def make_module(self, a_tag, table):
        m = Module(None)
        m.name = a_tag.attrs['name']
        assert table.attrs['class'] == ['functions']
        m.functions = self.extract_functions(table)
        return m

    def to_api(self):
        tables = [t for t in self.html.find_all('table')
                          if t.attrs['class'] == ['functions']]

        api = SublimeApi(None)
        for table in tables:
            # each module/class is associated with an 'a' tag
            a = table.find_previous('a')
            assert 'name' in a.attrs, 'unexpected anchor'
            name = a.attrs['name']

            module_name = class_name = None
            if '.' in name:
                module_name, class_name = name.split('.')

            if not module_name:
                module = self.make_module(a, table)
                api.modules[module.name] = module
            else:
                cls = self.make_class(class_name, table)
                if cls.name in api.modules[module_name].classes:
                    api.modules[module_name
                        ].classes[cls.name].members.extend(cls.members)
                else:
                    api.modules[module_name].classes[cls.name] = cls
        return api

    @staticmethod
    def from_path(path):
        with open(path, 'rt') as f:
            return FromHtmlReader(bs4.BeautifulSoup(f.read()))


def read_api(path):
    """
    Returns a `SublimeApi` instance.

    @path
      Path to an .html representation of then Sublime Text API.
    """
    return FromHtmlReader.from_path(path).to_api()


if __name__ == '__main__':
    try:
        print('testing...')
        print(read_api('api.html'))
    except IOError:
        here = os.path.abspath(os.path.dirname(__file__))
        print('no api.html file found in {}'.format(here))
