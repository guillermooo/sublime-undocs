Plugins
=======

.. seealso::

   :doc:`API Reference <../reference/api>`
        More information on the Python API.


Plugins are Python scripts implementing ``*Command`` classes from
``sublime_plugin``.


Where to Store Plugins
**********************

Sublime Text will look for plugins in these places:

* ``Packages``
* ``Packages/<pkg_name>``
* ``.sublime-package`` files

Plugin files nested deeper in ``Packages`` won't be loaded.

All plugins should live inside a folder of their own and not directly
under ``Packages``. This will spare you confusions when Sublime Text attempts
to sort packages for loading.


Conventions for Command Names
*****************************

By convention, Sublime Text command class names are suffixed with ``Command``
and written as ``NamesLikeThisCommand``.

However, command names are automatically transformed from ``NamesLikeThisCommand``
to ``name_like_this``. Thus, ``ExampleCommand`` would become ``example``,
and ``AnotherExampleCommand`` would become ``another_example``.

In names for classes defining commands, use ``NameLikeThisCommand``. To call a
command from the API, use the standardized ``name_like_this``.


Types of Commands
*****************

* ``sublime_plugin.WindowCommand``
* ``sublime_plugin.TextCommand``
* ``sublime_plugin.EventListener``

Instances of ``WindowCommand`` have a ``.window`` attribute pointing to the
window instance that created them. Similarly, instances of ``TextCommand``
have a ``.view`` attribute.

Shared Traits for Commands
--------------------------

All commands must implement a ``.run()`` method.

All commands can receive an arbitrarily long number of keyword arguments that
must be valid JSON types.


How to Call Commands from the API
*********************************

Depending on the type of command, use a reference to a ``View`` or a ``Window``
and call ``<object>.run_command('command_name')``. In addition to the command's
name, ``.run_command`` accepts a dictionary whose keys are the names of valid
parameters for said command::

   window.run_command("echo", {"Tempus": "Irreparabile", "Fugit": "."})


Command Arguments
*****************

All user-provided arguments to commands must be valid JSON types.


Text Commands and the ``edit`` Object
*************************************

Text commands receive an ``edit`` object passed to them by Sublime Text.

All actions done within an ``edit`` are grouped as a single undo action.
Callbacks such as ``on_modified()`` and ``on_selection_modified()`` are called
when the edit is finished.

.. XXX: Is the above true?

Contrary to earlier versions of Sublime Text, the ``edit`` object's life time is
now managed solely by the editor. Plugin authors must ensure to perform all
editing operations within the ``run()`` method of text commands so that macros
and repeating commands work as expected.

To call other commands from your own commands, use the ``run_command()``
function.


Responding to Events
********************

Any subclass of ``EventListener`` will be able to respond to events. You cannot
make a class derive both from ``EventListener`` and from any other type of
command.

.. sidebar:: A Word of Warning about ``EventListener``

	Expensive operations in event listeners can cause Sublime Text to become
	unresponsive, especially in events triggered frequently, like
	``on_modified()`` and ``on_selection_modified()``. Be careful of how much
	work is done in these and don't implement events you don't need, even if
	they just ``pass``.


Sublime Text and the Python Standard Library
********************************************

Sublime Text ships with a trimmed down standard library.


Automatic Plugin Reload
***********************

Sublime Text will reload topmost Python modules as they change (perhaps
because you are editing a *.py* file within *Packages*). By contrast, Python
subpackages won't be reloaded automatically, and this can lead to confusion
while you're developing plugins. Generally speaking, it's best to restart
Sublime Text after you've made changes to plugin files, so all changes can take
effect.


Multithreading
**************

Only the ``set_timeout()`` function is safe to call from different threads.

.. XXX: Is this still true?
