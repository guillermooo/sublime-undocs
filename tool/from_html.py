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

    def funcs_from_table(self, t):
        trs = t.find_all('tr')
        fs = []

        for tr in trs:
            data = list(tr.children)
            if data[0] is None:
                print (tr)
            func_name = data[0].text
            if func_name == 'Methods':
                continue
            ret_value = data[1].text

            try:
                desc = data[2].text
            except:
                desc = "n/a"

            m = Member (None)
            m.name = func_name
            m.return_value = ret_value
            m.description = desc
            fs.append(m)

        return fs

    def classes_from_html(self, classes):
        final_clasess = []
        for cs in classes:
            new_class = Class (None)
            new_class.name = cs.attrs ['name']
            t = cs.find_next('table')
            assert t.attrs ['class'] == ['functions']
            new_class.members = self.funcs_from_table (t)
            final_clasess.append (new_class)
        return final_clasess

    def module_from_section(self, a_tag):
        m = Module(None)
        m.name = a_tag.attrs['name']
        t = a_tag.find_next('table')
        assert t.attrs['class'] == ['functions']
        m.functions = self.funcs_from_table(t)
        cc = [a for a in self.html.find_all('a') if a.attrs.get('name', '.').split('.')[0] == m.name]
        # skip the module
        m.classes = self.classes_from_html(cc[1:])
        return m

    def sections_from_tables(self, tables):
        api = SublimeApi(None)
        # for each t, find a#name
        for t in tables:
            a = t.find_previous('a')
            try:
                assert 'name' in a.attrs, 'boo!'
            except:
                print ("IGNORED:", a)
            if '.' in a.attrs['name']:
                pass
            else:
                api.modules.append(self.module_from_section(a))
        return api

    def to_api(self):
        tables = [t for t in self.html.find_all('table') if t.attrs['class'] == ['functions']]
        return self.sections_from_tables(tables)

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
        print(read_api('api.html'))
    except IOError:
        here = os.path.abspath(os.path.dirname(__file__))
        print('no api.html file found in {}'.format(here))
