===================================
File Navigation and File Management
===================================

.. _fm-goto-anything:

Goto Anything
=============

Goto Anything lets you **navigate files** swiftly. Open it with :kbd:`Ctrl+P`.
As you type into the input area, names of open files and files in :ref:`open
directories <fm-projects-folders>` will be searched, and a preview of the best match will be shown.
This preview is *transient*, that is, it won't become the actual active buffer
until you perform some operation on it. Transient views go away when you press
:kbd:`Esc`. You will find transient views in other situations, e. g. when
single-clicking a file in the sidebar.

Goto Anything lives up to its name --there's more to it than locating files.


.. _fm-goto-directives:

Goto Anything directives
------------------------

There are a few special directives for Goto Anything which will point you to
other places than just the beginning of a file. Any of these directives can be
used in combination with file search queries and will be applied on the
currently selected file or on the file you are currently editing if you haven't
specified any filename search term.

Directives are invoked with a special character, e. g. ``:``, and all text after
that will be interpreted by the directive. Example::

    island:123

This instructs Sublime Text to first search for a file that matches ``island``
and then goes to line 123.

Here is a list of the supported directives:

:samp:`@{symbol}`
    Searches for **symbol** symbol in the active buffer; bound to :kbd:`Ctrl+R`.

    Symbols usually are classes or functions but can be anything defined by the
    syntax definition. See *Symbols - Syntax Preferences* (XXX to be added). In
    return, they might not be defined at all and searching for symbols will fail
    in this case.

:samp:`#{search}`
    Fuzzy-searches a word in the file matching **search** and highlights all
    occurrences; bound to :kbd:`Ctrl+;`.

:samp:`:{line_number}`
    Goes to the specified line number or the end of the file if it exceeds the
    limit; bound to :kbd:`Ctrl+G`.


.. _fm-sidebar:

Sidebar
=======

The sidebar gives you an overview of your project. Files and folders added to
the sidebar will be available in `Goto Anything`_ and project-wide actions.
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
it and give it a name. Project files use the *.sublime-project* extension.

.. _fm-projects-folders:

You can add and remove folders to a project with the **Project** menu and the
side bar's context menu. Futhermore, you can drag folders onto a window and they
will be added automatically.

To save a project, choose **Project | Save Project As...**.

To quickly switch between projects, press :kbd:`Ctrl+Alt+P`. Alernatively you
can browse **Projects | Recent Projects**.

You can open a project from the **command line** by passing the
*.sublime-project* file as an argument.



Project Definitions
-------------------

Project definitions are stored in JSON files with a *.sublime-project*
extension. Wherever there's a *.sublime-project* file, you will find an
ancillary *.sublime-workspace* file too, which contains user specific data, such
as the open files and the modifications to each. The latter is used by Sublime
Text and you shouldn't edit it yourself.

Project definitions support three top level sections: ``folders``, for the
included folders, ``settings``, for settings overrides, and
``build_systems``, for project-specific build systems. An example:

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
    Each folder must have a ``path``, and may optionally have a
    ``folder_exclude_patterns`` and ``file_exclude_patterns`` setting. The path
    may be relative to the project directory or an absolute path. Folders
    may also be given a ``name`` setting, to set how they're displayed on the
    side bar.

**Settings**
    A project may define project-specific settings which only apply to (open)
    files within that project. Project-specific settings override regular user
    settings but not syntax-specific settings.

    You can override almost all settings (excluding global settings).

    .. seealso::

        :ref:`settings-hierarchy`
            A detailed example for the order of precedence for settings.
        :doc:`Settings - Reference </reference/settings>`
            Reference of available settings.

**Build Systems**
    You can define project-specific build systems in a project definition. In
    addition to regular build systems, a ``name`` must be specified for each
    one. Build systems listed here will be available via the regular **Tools |
    Build Systems** menu.

    .. seealso::

        :doc:`Build Systems - Reference </reference/build_systems>`
            Documentation on build systems and their options.