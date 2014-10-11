===================================
File Navigation and File Management
===================================

.. _fm-goto-directives:

Goto Anything
=============

Use Goto Anything
to **navigate your project's files** swiftly.
(More about projects later.)

To open Goto Anything,
press :kbd:`Ctrl+P`.
As you type into the input area,
names of open files and files in :ref:`open directories <fm-projects-folders>`
will be searched,
and a preview of the best match
will be shown.
This preview is *transient*;
that is, it won't become the actual active view
until you perform some operation on it.
Transient views go away when you press :kbd:`Esc`.
You will find transient views in other situations,
for example when single-clicking a file in the sidebar.

Goto Anything lives up to its name
--there's more to it than locating files.


Goto Anything Operators
-----------------------

Goto Anything understands a handful of operators.
Any of them can be used
in combination with file search queries.

Example::

	island:123

This instructs Sublime Text
to first search for a file
that matches ``island``
and then go to line 123.


Supported Operators
-------------------

:samp:`@{symbol}`
    Searches for **symbol** symbol in the active buffer;
    bound to :kbd:`Ctrl+R`.

    Symbols usually are classes or functions,
    but can target any scope present
    in the syntax definition.
    See *Symbols - Syntax Preferences*
    (XXX to be added).
    If no symbols are defined,
    the search will simply fail.

.. (XXX to be added).

:samp:`#{term}`
    Fuzzy-searches a word in the file matching **term**
    and highlights all instances;
    bound to :kbd:`Ctrl+;`.

:samp:`:{line_number}`
    Goes to the specified line number
    or the end of the file
    if it exceeds the file limit;
    bound to :kbd:`Ctrl+G`.

.. note::
	Searching for symbols will only work
    if the active file type
    has symbols defined for it.
    Symbols are defined in *.tmLanguage* files.

.. todo: Explain how to create symbols.

.. _fm-sidebar:

Sidebar
=======

The sidebar gives you an overview
of the active project.
Files and folders added to the sidebar
will be available in `Goto Anything`_
and project-wide actions
(like project-wide searches).

Projects and the sidebar are closely related.
It's important to note
that there's always an active project,
whether it's explicit or implicit.

To **toggle** the sidebar,
press :kbd:`Ctrl+K, Ctrl+B`.

The sidebar can be navigated
with the arrow keys,
but first you need to give it the **focus**
by pressing :kbd:`Ctrl+0`.
To return the focus to the view,
press :kbd:`Esc`.
Alternatively, you can use the mouse
to the same effect.

Files opened from the sidebar
create *semi-transient* views.
Unlike transient views, *semi-transient* views
show up as a new tab.
You will be able to tell semi-transient views from other views
because their tab text is shown in italics.
When a new semi-transient view is opened,
any existing semi- transient view in the same pane
gets automatically closed.

The sidebar provides basic file management operations
through its context menu.

.. _fm-projects:

Projects
========

Projects group sets of files and folders
to keep your work organized.
Set up a project by adding folders in a way
that suits you,
and then save your new configuration.

.. _fm-projects-folders:

You can add and remove folders to a project
with the **Project** menu
and the side bar's context menu.
Alternatively,
you can drag a folder onto a window
and it will be added automatically.

To save a project,
go to **Project | Save Project As...**.

To switch projects quickly,
press :kbd:`Ctrl+Alt+P`.
Using the menu,
you can select **Projects | Recent Projects**.

Project data are stored in JSON files
with a *.sublime-project* extension.
Wherever there's a *.sublime-project* file,
you will find an ancillary *.sublime-workspace* file too.
The second one is used by Sublime Text
and you shouldn't edit it yourself.

Project files can define settings specific to that project.
More information in the `official documentation`_.

.. _official documentation: http://www.sublimetext.com/docs/2/projects.html

.. todo: add settings example here.

You can open a project from the **command line**
by passing the *.sublime- project* file as an argument
to the Sublime Text executable.

Project files are meant
to be committed to source code repositories.


Project Definitions
-------------------

Project definitions are stored in JSON files
with a *.sublime-project* extension.
Wherever there's a *.sublime-project* file,
you will find an ancillary *.sublime-workspace* file too,
which contains user specific data,
such as the open files and the modifications to each.
The latter is used by Sublime Text
and isn't meant to be edited by users.

Project definitions support three top level sections:
``folders``, for the included folders, ``settings``, for settings overrides,
and ``build_systems``, for project-specific build systems.

.. sourcecode:: javascript

    {
        "folders":
        [
            {
                "path": "src",
                "folder_exclude_patterns": ["backup"]
            },
            {
                "path": "docs",
                "name": "Documentation",
                "file_exclude_patterns": ["*.css"]
            }
        ],
        "settings":
        {
            "tab_size": 8
        },
        "build_systems":
        [
            {
                "name": "List",
                "cmd": ["ls"]
            }
        ]
    }


**Folders**
    Each folder must have a ``path``,
    and may optionally have a ``folder_exclude_patterns``
and ``file_exclude_patterns`` setting.
    The path may be relative to the project directory,
    or an absolute path.
    Folders may also be given a ``name``
    that will appear in the side bar.

**Settings**
    A project may define project-specific settings
    that will only apply to files within that project.
    Project-specific settings override regular user settings,
    but not syntax-specific settings.

    Almost all settings can be overridden
    (excluding global settings).

    .. seealso::

        :ref:`settings-hierarchy`
            A detailed example for the order of precedence for settings.
        :doc:`Settings - Reference </reference/settings>`
            Reference of available settings.

**Build Systems**
    You can define project-specific build systems in a project definition.
    In addition to regular build systems,
    a ``name`` must be specified for each one.
    Build systems listed here will be available
    via the regular **Tools | Build Systems** menu.

    .. seealso::

        :doc:`Build Systems - Reference </reference/build_systems>`
            Documentation on build systems and their options.


Notable Settings Related to The Sidebar and Projects
====================================================

These options control which files
are shown in the sidebar
and included in project-wide actions,
such as searching files.

	folder_exclude_patterns
	file_exclude_patterns
	binary_file_patterns

To see a detailed description of their purpose,
open the default settings file
(*Default/Preferences.sublime-settings*)
via the Command Palette (`Ctrl+P`).


Workspaces
==========

Workspaces can be seen as different *views*
into the same project.
For example, you may want
to have only a selected few files open
while working on *Feature A*.
Or perhaps you use a different pane layout
when you're writing tests, etc.
Workspaces help in these situations.

**Workspaces behave very much like projects.
To create a new workspace,
select **Project | New Workspace for Project.
To save the active workspace,
select **Project | Save Workspace As....

Workspaces data is stored in JSON files
with the *.sublime-workspace* extension.

Contrary to *.sublime-project* files,
*.sublime-workspace* files
**are not** meant to be shared or edited manually.
**Never** commit *.sublime-workspace* files
into a source code repository.

To switch between different workspaces,
use :kbd:`Ctrl+Alt+P`,
exactly as you do with projects.

As with projects, you can open a workspace
from the **command line**
by passing the desired *.sublime-workspace* file
as an argument to the Sublime Text executable.


Panes
=====

Panes are groups of views.
In Sublime Text you can have
multiple panes open at the same time.

To create a new pane,
press :kbd:`Ctrl+K, Ctrl+Up`.
To close a pane, press :kbd:`Ctrl+K, Ctrl+Down`.

Further pane management commands
can be found under **View | Layout**
and related submenus.
