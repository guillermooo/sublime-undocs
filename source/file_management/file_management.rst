===================================
File Navigation and File Management
===================================

Goto Anything
=============

Use Goto Anything to **navigate your project's files** swiftly. (More about
projects later.)

To open Goto Anything, press :kbd:`Ctrl+P`. As you type into the input area,
all file names of files open within the editor (and of files in added folders
too) will be searched, and a preview of the best match will be shown. This
preview is *transient*; that is, it won't become the actual active view until
you perform some operation on it. Transient views go away when you press
:kbd:`Esc`. You will see transient views in other situations too.

But Goto Anything lives up to its name---there's more to it than searching
files:

To perform a **fuzzy text search** using Goto Anything, append ``#`` and
keep typing, like this:

::

	isl#trsr

This makes Sublime Text perform a fuzzy search for *trsr* in files whose name
loosely matches *isl*. For example, you could find the word *treasure* inside
a file named *island*.

To perform a fuzzy search in the current view, press :kbd:`Ctrl+;`.

Fuzzy searches can detect transposed characters for clumsy fingers.

And there's more:

To **search symbols** in the current view, press :kbd:`Ctrl+R`. As in the case
of ``#``, the ``@`` operator can be used after file names too.

To **go to a line number**, press :kbd:`Ctrl+G`. Again, the operator ``:`` can
be used after file names, just as ``#`` and ``@``.

Searching for symbols will only work if the active file type has symbols
defined for it. Symbols are defined in *.tmLanguage* files.

.. todo: Explain how to create symbols.


Sidebar
=======

The sidebar gives an overview of the active project. Files and folders added
to the sidebar will be available in Goto Anything as well as for project-wide
actions (like project-wide searches).

Projects and the sidebar are very closely related. It's important to note that
there's always an active project, whether it's explicit or implicit.

To **toggle** the sidebar, press :kbd:`Ctrl+K, Ctrl+B`.

The sidebar can be navigated with the arrow keys, but first you need to give
it the **focus** by pressing :kbd:`Ctrl+0`. To return the focus to the view,
press :kbd:`Esc`. Alternatively, you can use the mouse to the same effect.

Files opened from the sidebar create *semi-transient* views. Unlike transient
views, *semi-transient* views show up as a new tab. You will be able to tell
semi-transient views from other views because their tab text is shown in
italics. When a new semi-transient view is opnened, any existing semi-
transient view in the same pane gets automatically closed.

The sidebar provides basic file management operations through its context
menu.


Projects
========

Projects group sets of files and folders to keep your work organized. Set up a
project by adding folders in a way that suits you, and then save your new
configuration.

To save a project, go to **Project | Save Project As...**.

To switch projects quickly, press :kbd:`Ctrl+Alt+P`.

Project data is stored in JSON files with a `.sublime-project` extension.
Wherever there's a `.sublime-project` file, you may find one or more
`.sublime-workspace` files. Workspaces are explained later.

Project files can define settings specific to that project. More
information in the `official documentation`_.

.. _official documentation: http://www.sublimetext.com/docs/2/projects.html

.. todo: add settings example here.

You can open a project from the **command line** by passing the *.sublime-
project* file as an argument to the Sublime Text executable.


Workspaces
==========

Workspaces can be seen as different *views* into the same project. For
example, you may want to have only a selected few files open while working on
*Feature A*. Or perhaps you use a different pane layout when you're writing
tests, etc. Workspaces help in these situations.

**Workspaces behave very much like projects. To create a new workspace, select
**Project | New Workspace for Project. To save the current workspace, select
**Project | Save Workspace As....

Workspaces data is stored in JSON files with the *.sublime-workspace*
extension.

Contrary to *.sublime-project* files, *.sublime-workspace* files **are not**
meant to be shared or edited manually. **Never** commit *.sublime-workspace*
files into a source code repository.

To switch between different workspaces, use :kbd:`Ctrl+Alt+P`, exactly as you
do with projects.

As with projects, you can open a workspace from the **command line** by
passing the desired *.sublime-workspace* file as an argument to the Sublime
Text executable.


Panes
=====

Panes are groups of Views. In Sublime Text you can have multiple panes open
at the same time.

To create a new pane, press :kbd:`Ctrl+K, Ctrl+Up`. To destroy a pane,
press :kbd:`Ctrl+K, Ctrl+Down`.

To find further pane management commands, look under **View | Layout** and
related submenus.
