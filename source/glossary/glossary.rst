.. _glossary:

========
Glossary
========

.. glossary::

    buffer
        Data of a loaded file and additional metadata, associated with one or
        more views. The distinction between *buffer* and *view* is technical.
        Most of the time, both terms can be used interchangeably.

    view
        Graphical display of a buffer. Multiple views can show the same buffer.

    plugin
        A feature impemented in Python, which can consist of a single command
        or multiple commands. It can be contained in one *.py* file or many
        *.py* files.

    package
        This term is ambiguous in the context of Sublime Text, because it can
        refer to a Python package (unlikely), a folder inside ``Packages``
        or a *.sublime-package* file. Most of the time, it means a folder
        inside ``Packages`` containing resources that belong together, which build
        a new feature or provide support for a programming or markup language.

    panel
        An input/output widget, such as a search panel or the output panel.

    overlay
        An input widget of a special kind. For example, Goto Anything is an overlay.
