Plugins
=======

.. seealso::

   :doc:`API Reference <../reference/api>`
        More information on the Python API.


Plugins are Python scripts implementing ``*Command`` classes from ``sublime_plugin``.

Where to Store Plugins
**********************

Sublime Text 2 will look for plugins in these places:

* ``Packages``
* ``Packages/<pkg_name>``

Any plugin nested deeper in ``Packages`` won't be loaded.

All plugins should live inside a directory of their own and not directly
under ``Packages``.


Conventions for Command Names
*****************************

Sublime Text 2 command class names are suffixed by convention with ``Command`` and
written as ``CamelCasedPhrases``.

However, Sublime Text 2 transforms the class name from ``CamelCasedPhrases`` to
``camel_cased_phrases``. So ``ExampleCommand`` would turn into ``example``
and ``AnotherExampleCommand`` would turn into ``another_example``.

For class definition names, use ``CamelCasedPhrasesCommand``;
to call a command from the API, use the normalized name (``camel_cased_phrases``).


Types of Commands
*****************

* ``sublime_plugin.ApplicationCommand``
* ``sublime_plugin.WindowCommand``
* ``sublime_plugin.TextCommand``
* ``sublime_plugin.EventListener``

Instances of ``WindowCommand`` have a ``.window`` attribute pointing to the
window instance that created them. Similarly, instances of ``TextCommand``
have a ``.view`` attribute.

Shared Traits for Commands
--------------------------

All commands must implement a ``.run()`` method.
All commands can receive and arbitrarily long number of keyword arguments,
but they must be valid JSON types.


How to Call Commands from the API
*********************************

Use a reference to a ``View`` or a ``Window``, or ``sublime`` depending on
the type of command, and call ``object.run_command('command_name')``.
In addition, you can pass a dictionary where keys are names of parameters
to ``command_name``. ::

   window.run_command("echo", {"Tempus": "Irreparabile", "Fugit": "."})


 Command Arguments
 *****************

 All user-provided arguments to commands must be valid JSON types. Only
 Sublime Text can pass other types of arguments to commands (such as edit
 objects, view instances, etc.).


Text Commands and the ``edit`` Object
*************************************

The two API functions of interest are ``view.begin_edit()``, which takes an optional command name and an optional dictionary of arguments, and ``view.end_edit()``, which finishes the edit.

All actions done within an edit are grouped as a single undo action. Callbacks such as ``on_modified()`` and ``on_selection_modified()`` are called when the edit is finished.

It's important to call ``view.end_edit()`` after each ``view.begin_edit()``, otherwise the buffer will be in an inconsistent state. An attempt will be made to fix it automatically if the edit object gets collected, but that often doesn't happen when you expect, and will result in a warning printed to the console. In other words, you should always bracket an edit in a ``try..finally`` block.

The command name passed to ``begin_edit()`` is used for repeat, macro recording, and for describing the action when undoing/redoing it. If you're making an edit outside of a ``TextCommand``, you should almost never supply a command name.

If you have created an edit object, and call a function that creates another one, that's fine: the edit is only considered finished when the outermost call to ``end_edit()`` runs.

As well as grouping modifications, you can use edit objects for grouping changes to the selection, so they're undone in a single step.


Responding to Events
********************

Any subclass of ``EventListener`` will be able to respond to events. You cannot
make a class derive from both ``EventListener`` and any other type of command.

.. sidebar:: A Word of Warning about ``EventListener``

	Expensive operations in event listeners can cause Sublime Text 2 to become
	unresponsive, especially in events triggered frequently, like ``on_modified``
	and ``on_selection_modified``. Be careful of how much work is done in those
	and do not implement events you don't need, even if they just ``pass``.


Python and the Standard Library
*******************************

Sublime Text ships with a trimmed down standard library. Notable missing
modules are the *gtk*, *multiprocessing* and *sqlite3* modules.


Automatic Plugin Reload
***********************

Sublime Text will automatically reload top-level Python modules from packages
as they change (perhaps because you are editing a *.py* file). Note that
Python subpackages won't be reloaded; this can lead to confusion while
developing plugins. Generally, it's best to restart Sublime Text after you've
made changes to plugin files so all changes take effect.


Multithreading
**************

Only the ``.set_timeout()`` function is safe to call from different threads.
