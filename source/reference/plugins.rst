Plugins
=======

.. seealso::

   :doc:`API Reference <../reference/api>`
        More information on the Python API.


Plugins are Python scripts implementing ``*Command`` classes from ``sublime_plugin``.

Where to Store Plugins
**********************

Sublime Text 2 will look for plugins in these places:

* ``Package``
* ``Packages/<pkg_name>``

Any plugin nested deeper in ``Packages`` won't be loaded.


Conventions for Command Names
*****************************

Sublime Text 2 command class names are suffixed by convention with ``Command`` and
written as ``CamelCasedPhrases``.

However, Sublime Text 2 transforms the class name from ``CamelCasedPhrases`` to
``camel_cased_phrases``. So ``ExampleCommand`` would turn into ``example``
and ``AnotherExampleCommand`` would turn into ``another_example``.

For class definition names, use ``CamelCasedPhrasesCommand``;
to call a command from the API, use the transformed name (``camel_cased_phrases``).


Types of Commadns
*****************

* ``sublime_plugin.ApplicationCommand``
* ``sublime_plugin.WindowCommand``
* ``sublime_plugin.TextCommand``
* ``sublime_plugin.EventListener``

Shared Traits for Commands
--------------------------

All commands must implement a ``.run()`` method.
All commands can receive and arbitrarily long number of keyword arguments.


How to Call Commands from the API
*********************************

Use a reference to a ``View``, a ``Window`` or ``sublime`` depending on
the type of command, and call ``object.run_command('command_name')``.
In addition, you can pass a dictionary where keys are names of parameters
to ``command_name``.


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

Any subclass of ``EventListener`` will be able to respond to events.

.. sidebar:: A Word of Warning about ``EventListener``

	Expensive operations in event listeners can cause Sublime Text 2 to become
	unresponsive, especially in events triggered frequently, like ``on_modified``
	and ``on_selection_modified``. Be careful of how much work is done in those
	and do not implement events you don't need, even if they just ``pass``.
