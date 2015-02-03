"""
Translates a Sublime Text settings file in Json format to a yaml representation.
"""

from collections import namedtuple
import sys


setting_data = namedtuple('setting_data', 'comment key value')

EOF = '<EOF>'


class State(object):
    '''
    Keeps track of the translator's state.
    '''
    def __init__(self, content):
        '''
        @content
          Input being processed.
        '''
        self.content = content
        self.idx = -1 # current idx into @content
        self.start = 0 # we'll emit starting here

    def next_char(self):
        self.idx += 1
        if self.idx >= len(self.content):
            self.idx -= 1
            return EOF
        return self.content[self.idx]

    def consume(self, c):
        '''
        @c
          Expected character.

        Try to consume @c or raise an error if it isn't the next item in the
        input.
        '''
        cc = self.next_char()
        if c !=  cc:
            raise ValueError ('unexpected consumed char: %s' % cc)

    def find_next(self, what):
        while True:
            c = self.next_char()
            if c == what or c == EOF:
                return c

    def skip(self, chars):
        '''
        Skips over @chars but does not ignore them for emitting.

        @chars
          A list of characters.
        '''
        while True:
            c = self.next_char()
            if c not in chars:
                self.backup()
                break

    def at_eof(self):
        '''
        Are we done yet?
        '''
        return self.idx >= len(self.content)

    def mark_start(self):
        '''
        Start a span for .emit()ting.
        '''
        self.start = self.idx

    def backup(self):
        self.idx -= 1

    def ignore(self):
        '''
        Ignore the current span of text that would be .emit()ted.
        '''
        self.start = self.idx

    def emit(self):
        '''
        Return a span of text starting at .start and ending at .idx.
        '''
        value = self.content[self.start:self.idx]
        self.ignore()
        return value


class JsonTranslator(object):
    '''
    Reads in a Sublime Text Json file with comments and returns a list
    of (comment, key, value) items.
    '''

    def __init__(self, content):
        """
        @content
          The input to be translated.
        """
        self.state = State(content)

    def go_to_start(self):
        c = self.state.find_next('{')
        if c == EOF:
            raise ValueError('bad document')

    def parse_comment(self):
        self.state.mark_start()
        while True:
            self.state.find_next('\n')
            self.state.skip(['\n', ' ', '\t'])
            c = self.state.next_char()
            if c == EOF:
                raise ValueError('bad comment')
            elif c == '/':
                continue
            elif c == '"':
                self.state.backup()
                comment = self.state.emit()
                break

        return comment

    def parse(self):
        self.go_to_start()

        comm = None
        key = None
        value = None

        items = []
        while True:
            c = self.state.next_char()
            if c == '/':
                comm = self.parse_comment()

            elif c == EOF:
                break

            elif c == '"':
                _ = self.state.next_char()
                self.state.mark_start()
                if self.state.find_next('"') == EOF:
                    raise ValueError('bad document')

                key = self.state.emit()

                if self.state.find_next(':') == EOF:
                    raise ValueError('bad document')
                self.state.skip([' ', '\t'])
                self.state.ignore()
                if self.state.find_next('\n') == EOF:
                    raise ValueError('bad document')

                value = self.state.emit().strip()
                if value.endswith(','):
                    value = value[:-1]

            if key and value:
                items.append(setting_data(comm, key, value))
                comm = None
                key = None
                value = None

        return items


if __name__ == '__main__':
    content = None
    with open('Default.sublime-settings', 'rt') as f:
        content = f.read()

    if not content:
        sys.exit(1)

    s = JsonTranslator(content)
    data = s.parse()
    for it in data:
        print ("-")
        try:
            print('  comment: |')
            lines = it.comment.split('\n')
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                print ('    %s' % line)
        except:
            print('  comment: ""')
        print('  description: insert description here')
        print('  name:', it.key)
        print('  value:', it.value)
