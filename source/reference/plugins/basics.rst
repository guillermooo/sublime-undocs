=================
Plugins -- Basics
=================

.. seealso::

   :doc:`API Reference <../../reference/api>`
        More information on the Python API.

   :doc:`Plugins Reference <../../reference/plugins>`
        More information about plugins.


Overview
========

This section is intended for users with programming skills.

Sublime Text can be extended
through Python plugins.
Plugins build features
by reusing existing commands
or creating new ones

.. note::

   Plugins range from the very simple
   (a single file and a single command)
   to complex, multi-file plugins.

   The most complex plugins
   are often included in
   a lager package.


Prerequisites
=============

In order to write plugins, you must be able to program in Python_.
At the time of this writing, Sublime Text used Python 3.3.3.

.. _Python: http://www.python.org


Where to Store Plugins
**********************

Sublime Text will look for plugins in these places:

* ``Installed Packages`` directory (only *.sublime-package* files)
* ``Packages`` directory
* ``Packages/<pkg_name>/`` directories

Keeping plugins directly under ``Packages`` is discouraged.


Anatomy of a Plugin
===================

This is a sample plugin::

   import sublime
   import sublime_plugin

   class MyFirstPluginCommand(sublime_plugin.TextCommand):
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


Conventions for Command Names
*****************************

Our command is named ``MyFirstPluginCommand``.
Using the ``*Command`` suffix
for command classes is customary.


Sublime Text transforms command names
by stripping the ``Command`` suffix
and separating ``PhrasesLikeThis``
with underscores, like so:
``phrases_like_this``.

Therefore, our sample plugin
must be called as follows
whenever needed::

   my_first_plugin

New commands should follow the same naming pattern.


Types of Commands
=================

You can create the following types of commands:

* Window commands (``sublime_plugin.WindowCommand``)
* Text commands (``sublime_plugin.TextCommand``)
* Application commands (``sublime_plugin.ApplicationCommand``)

When writing plugins,
consider your goal
and choose the appropriate type of command.


Shared Traits of Commands
*************************

All commands
need to implement a ``.run()`` method
in order to work.
The ``.run()`` method
can receive an arbitrarily long number
of keyword parameters.

.. note::
   Arguments to commands
   must be JSON types
   due to how Sublime Text
   serializes them internally.


Window Commands
***************

Window commands operate at the window level. This doesn't mean that you can't
manipulate views from window commands, but rather that you don't need views in
order for window commands to be available. For instance, the built-in command
``new_file`` is defined as a ``WindowCommand`` so it works even when no view
is open. Requiring a view to exist in that case wouldn't make sense.

Window command instances have a ``.window`` attribute to point to the window
instance that created them.

The ``.run()`` method of a window command doesn't require any positional
parameter.

Window commands are able to route text commands to their window's active view.

Text Commands
-------------

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

**Note:** Contrary to older versions, Sublime Text 3 doesn't allow programmatic
control over edit objects. The API is in charge of managing their life cycle.
Plugin creators must ensure that all modifying operations occur inside the
``.run`` method of new text commands. To call existing commands, you can use
``view.run_command(<cmd_name>, <args>)`` or similar API calls.

Responding to Events
--------------------

Any command deriving from ``EventListener`` will be able to respond to events.


.. _plugins-completions-example:

commands
naming
calling from where
what is a plugin
where
why
api (sync/async)
python version


events
async
completions
on query contexts
groups
layouts
