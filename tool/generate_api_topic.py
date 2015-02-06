# WIP

"""
Generates an api.rst file containing information about the Sublime Text API.
"""

from itertools import zip_longest
import from_html
import visitor

items = [
    'name',
    'copy',
    'delete',
    'delete_and_destroy',
    'sublime_text',
    'something_here',
    'whatever',
    'and_here_too_some_stuff',
    'hi_there',
    'something',
    'whatever_ever',
    'since',
    'id',
    'rewind',
    'play',
    'fast_forward',
    '0mq',
    'django',
    'ruby',
    'python',
    'dart',
    'c',
]


# min widths for each col 0..n
col_min_widths = []


def generate_cols(source, col_count=5):
   """
   Groups @source elements by columns.

   @source
     A list of short strings.
   """
   total = len(source)
   # Round up the number of items to the next int divisible by col_count.
   total = total if (total == 0) else (col_count - (total % col_count)) + total
   for i in range(0, total, col_count):
      items = source[i:i + col_count]
      col = ['func:`{}`'.format(item) for item in items]
      col_min_widths.append(max(len(word) for word in col))
      yield col


def make_sep(sep='=', col_count=5, end=''):
    items = []
    for i in range(col_count):
        items.append((sep * col_min_widths[i]) + end)
    return ''.join(items)


def main():
    cols = list(generate_cols(sorted(items)))
    rows = zip_longest(*cols)
    print(make_sep(end='  '))
    for row in rows:
        for i, item in enumerate(row):
            if item is None:
                continue
            # set up padding for the current row
            fmt = '{:<%d}' % col_min_widths[i]
            print (fmt.format(item), end='  ')
        print()


class SimpleVisitor(visitor.ApiHierarchicalVisitor):
   def visit_class(self, cls):
      print(cls.name)
      for m in cls.members:
         print ('  ', m.name)


def translate_to_rst():
   api = from_html.read_api('api.html')
   SimpleVisitor(api).visit_api()


if __name__ == '__main__':
   translate_to_rst()