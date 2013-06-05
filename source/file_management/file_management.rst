===================================
File Navigation and File Management
===================================

.. _fm-goto-anything:

Goto Anything
=============

Goto Anything lets you **navigate files** swiftly. Open it with :kbd:`Ctrl+P`.
As you type into the input area, names of open files and files in open
directories will be searched, and a preview of the best match will be shown.
This preview is *transient*, that is, it won't become the actual active buffer
until you perform some operation on it. Transient views go away when you press
:kbd:`Esc`. You will find transient views in other situations, e.g. when
single-clicking a file in the sidebar.

Goto Anything lives up to its name --there's more to it than locating files.


Goto Anything directives
------------------------

There are a few special directives for Goto Anything which will point you to
other places than just the beginning of a file. Any of these directives can be
used in combination with file search queries and will be applied on the
currently selected file or on the file you are currently editing if you didn't

Directives are invoked with a special character, e.g. ``:``, and all text after
that will be interpreted by the directive. Example::

	island:123

This instructs Sublime Text to first search for a file that matches ``island``
and then goes to line 123.

Here is a list of the supported directives:

:samp:`@{symbol}`
    Searches for **symbol** symbol in the active buffer; bound to :kbd:`Ctrl+R`.

    Symbols usually are classes or functions but can be anything defined by the
    syntax definition. See *Symbols - Syntax Preferences* (XXX to be
    added).

:samp:`#{search}`
    Fuzzy-searches the file for **search** and highlights all occasions; bound
    to :kbd:`Ctrl+;`.

:samp:`:{line_number}`
    Goes to the specified line number or the end of the file if it exceeds the
    file; bound to :kbd:`Ctrl+G`.

Searching for symbols will only work for file types that have symbols defined
for them.


.. _fm-sidebar:

Sidebar
=======

The sidebar gives you an overview of your project. Files and folders added to
the sidebar will be available in Goto Anything and project-wide actions.
Projects and the sidebar are closely related. There's always an open project,
whether it's implicit or explicit.

To **open or close** the sidebar, press :kbd:`Ctrl+K, Ctrl+B`.

The sidebar can be navigated with the arrow keys, but first you need to give
it the **input focus** by pressing :kbd:`Ctrl+0`. To return input focus to the
buffer, press :kbd:`Esc`. Alternatively, you can use the mouse to the same
effect, but why would you?

The sidebar also provides basic file management operations through the context
menu.


.. _fm-projects:

Projects
========

Projects group sets of files and directories you need to work on as a unit.
Once you've set up your project the way that suits you by adding folders, save
it and give it a name.

To save a project, go to **Project | Save Project As...**.

To quickly switch between projects, press :kbd:`Ctrl+Alt+P`.

Project data are stored in JSON files with a *.sublime-project* extension.
Wherever there's a *.sublime-project* file, you will find an ancillary
*.sublime-workspace* file too. The second one is used by Sublime Text and you
shouldn't edit it yourself.

Project files can define settings specific to that project only. More on that
in the `official documentation`_.

.. _official documentation: http://www.sublimetext.com/docs/2/projects.html

You can open a project from the **command line** by passing the *.sublime-
project* file as an argument.

.. TODO: talk about settings related to projects
