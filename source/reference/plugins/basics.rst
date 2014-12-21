=================
Plugins -- Basics
=================


Prerequisites
=============

This section is intended
for users with programming skills.

In order to write plugins,
you must be able to program in Python_.
At the time of this writing,
Sublime Text used Python 3.3.3.

.. _Python: http://www.python.org


Overview
========

Sublime Text can be extended
through Python plugins.
Plugins build features
by reusing existing commands
or creating new ones.

.. note::

   Plugins range from the very simple
   (a single file and a single command)
   to complex, multi-file plugins.
   The more complex plugins
   are often included in
   a larger package.


What's a Command?
=================

A command is a basic unit of functionality
in Sublime Text.
Most editor actions are encapsulated
as commands:
moving the caret; editing operations
like deleting, inserting characters, etc;
but also creating buffers,
new windows; showing panels...

As mentioned earlier,
plugins reuse or create commands.
In concrete terms,
commands are simply Python classes
that can be called
from different places,
like the plugin API, menu files, macros,
key maps, etc.

Some commands take optional
or mandatory arguments.

Here's an example of a command call
from a window object::

   window.run_command("echo", {"Hello": "World"})

We'll see examples
of creating commands
in later sections.


Where to Store Plugin Files
===========================

Sublime Text will look for Python files
containing plugins
in these places:

* ``Packages`` directory
* ``Packages/<pkg_name>/`` directories
* ``Installed Packages`` directory (only *.sublime-package* files)

Keeping plugins directly under ``Packages``
is discouraged.


Anatomy of a Plugin
===================

This is a sample plugin::

   import sublime
   import sublime_plugin


   class InsertHelloWorldCommand(sublime_plugin.TextCommand):
       def __init__(self, *args, **kwargs):
           super().__init__(*args, **kwargs)

       def run(self, edit):
           self.view.insert(edit, 0, 'hello world!')


The ``sublime`` and the ``sublime_plugin`` modules
are provided by Sublime Text;
they are not part
of the Python standard library.

As mentioned earlier,
plugins reuse or create *commands*.
Commands are
an essential building block in Sublime Text.
Commands are simply Python classes
that can be called
from different places,
like the plugin API, menu files, macros, etc.

Sublime Text commands derive from the ``*Command`` classes defined in
``sublime_plugin`` (more on this later).

The rest of the code in our example is concerned with particulars of
``TextCommand`` or the API. We'll discuss those topics in later sections.


Naming Conventions for ``*Command`` Subclasses
**********************************************

Our previous command is named ``InsertHelloWorldCommand``.
Using the ``Command`` suffix
for command classes is customary.


Sublime Text transforms command names
by stripping the ``Command`` suffix
and separating ``PhrasesLikeThis``
with underscores, like so:
``phrases_like_this``.

Therefore, our sample plugin
must be called as follows
whenever needed::

   insert_hello_world

New commands should follow the same naming pattern.


Types of Commands
=================

You can create the following types of commands:

* Window commands (``sublime_plugin.WindowCommand``)
* Text commands (``sublime_plugin.TextCommand``)
* Application commands (``sublime_plugin.ApplicationCommand``)

Additionally, you can create
classes that respond to editor events
by deriving from ``sublime_plugin.EventListener``.

We'll discuss each type of command
in later sections.

When writing plugins,
consider your goal
and choose the most appropriate type of command.


The ``.run()`` Method in Commands
*********************************

All commands
need to implement a ``.run()`` method
in order to work.
The ``.run()`` method
can receive an arbitrarily long number
of keyword parameters.

.. XXX: about params, can ApplicationCommand's receive
..      params?

.. note::
   Arguments to commands
   must be JSON types
   due to how Sublime Text
   serializes them internally.


Window Commands
***************

Window commands operate
at the window level.
Therefore, you don't need views
in order for window commands
to be available.
For instance,
the built-in command ``new_file``
is defined as a ``WindowCommand``
so it works
even when no view is open.
Requiring a view to exist
in that case
wouldn't make sense.

Window command instances have a ``.window`` attribute to point to the window
instance that created them.

The ``.run()`` method of a window command doesn't require any positional
parameter.

Despite not requiring an active view,
window commands are able
to route text commands
to their window's active view,
so it's possible to call
a ``TextCommand`` from a ``WindowCommand``.


Text Commands
*************

Text commands operate at the view level, so they require a view to exist
in order to be available.

Text command instances have a ``.view`` attribute pointing to the view instance
that created them.

The ``.run()`` method of text commands requires an ``edit`` instance as
its first positional argument.


Text Commands and the ``edit`` Object
-------------------------------------

The edit object groups modifications to the view so that undo and macros work
sensibly.

Plugin creators must ensure that all modifying operations occur inside the
``.run()`` method of new text commands. To call existing commands, you can use
``view.run_command(<cmd_name>, <args>)`` or similar API calls.


Responding to Events
====================

Any subclass of ``EventListener`` will be able to respond to events. You cannot
make a class derive both from ``EventListener`` and from any other type of
command.

.. warning::

   Expensive operations in event listeners can cause Sublime Text to become
   unresponsive, especially in events triggered frequently, like
   ``.on_modified()`` and ``.on_selection_modified()``. Be careful of how much
   work is done in these and don't implement events you don't need, even if
   they just ``pass``.


How to Call Commands from the API
=================================

Depending on the type of command,
use a reference to a ``View`` or a ``Window``
and call ``<object>.run_command('command_name')``.
In addition to the command's name,
``.run_command()`` accepts a dictionary
whose keys are the names
of valid parameters for said command::

   window.run_command("echo", {"Tempus": "Irreparabile", "Fugit": "."})

.. XXX: check the following

Application commands can be called
either from the command line
or using ``sublime.run_command()``.

Sublime Text and the Python Standard Library
============================================

Sublime Text ships with a trimmed down standard library.
Not all modules are available from a plugin.


Automatic Plugin Reload
=======================

Sublime Text will reload top-level Python modules as they change (perhaps
because you are editing a *.py* file within *Packages*). By contrast, Python
subpackages won't be reloaded automatically, and this can lead to confusion
while you're developing plugins. Generally speaking, it's best to restart
Sublime Text after you've made changes to plugin files, so all changes can take
effect.


.. commands
.. naming
.. calling from where
.. what is a plugin
.. where
.. why
.. api (sync/async)
.. python version


.. events
.. async
.. completions
.. on query contexts
.. groups
.. layouts

.. seealso::

   :doc:`API Reference <../../reference/api>`
        More information on the Python API.

   :doc:`Plugins Reference <../../reference/plugins>`
        More information about plugins.
