class SublimeApi(object):
    """
    Represents the Sublime Text Python docs from Sublime HQ.
    http://www.sublimetext.com/docs/3/api_reference.html
    """
    def __init__(self, html):
        self.html = html
        self.modules = {}


class Module(object):
    """
    Represents the documentation content of a module in the Sublime Text API.
    """
    def __init__(self, html):
        self.name = None
        self.classes = {}
        self.functions = []  # top-level funcs in the module

    def __str__(self):
        return '<Module {}>'.format(self.name)


class Class(object):
    """
    Represents the documentation of a class in the Sublime Text API.
    """
    def __init__(self, html):
        self.name = None
        self.members = []

    def __str__(self):
        return '<Class {}>'.format(self.name)


class Member(object):
    """
    A member in a class in the Sublime Text API.
    """
    def __init__(self, html):
        self.name = None
        self.return_value = None
        self.description = None

        def __str__(self):
            return '<Member {}>'.format(self.name)
