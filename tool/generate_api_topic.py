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
   def visit_module(self, m):
      # if m.name != 'sublime':
      #    return
      print('- {}:'.format(m.name))

      for f in m.functions:
         # if f.name != 'xarch()':
         #    continue
         self.visit_function(f)

      for (_, cls) in m.classes.items():
         self.visit_class(cls)

   def visit_class(self, cls):
      print ('  - name: {}'.format (cls.name))
      print ('    type: class')
      print ('    parameters: add params')
      print ('    description: add description')
      if cls.members:
         print ('    members:')
      for m in cls.members:
         self.visit_function(m, indent='    ', typ='method')

   def visit_function(self, f, typ='function', indent='  '):
      print ()
      print ('{0}- name: {1}'.format(indent, f.name))
      print ('{0}  type: {1}'.format(indent, typ))
      print ('{0}  parameters: add params'.format(indent))
      if f.return_value.strip() != 'None':
         print ('{0}  return_value: {1}'.format(indent, f.return_value))
      print ('{0}  description: |'.format(indent))
      # print ('{0}    {1}'.format(indent, f.description))
      self.wrap(f.description, indent='    ' + indent)

   def wrap(self, text, indent):
      lines = text.split('\n')
      for line in lines:
         print('{0}{1}'.format(indent, line.strip()))


def translate_to_rst():
   api = from_html.read_api('api.html')
   SimpleVisitor(api).visit_api()


if __name__ == '__main__':
   translate_to_rst()