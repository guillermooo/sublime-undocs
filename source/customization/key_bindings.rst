.. warning::

   Want even better documentation for Sublime Text? You can  `help <https://www.bountysource.com/teams/st-undocs/fundraiser>`_.

============
Key Bindings
============

.. seealso::

   :doc:`Reference for key bindings <../reference/key_bindings>`
        Complete documentation on key bindings.

Key bindings let you map sequences of key presses to actions.

File Format
===========

Key bindings are defined in JSON and stored in ``.sublime-keymap`` files. In
order to integrate better with each platform, there are separate key map files
for Linux, OSX and Windows. Only key maps for the corresponding platform will
be loaded.

Example
*******

Here's an excerpt from the default key map for Windows::

	[
		{ "keys": ["ctrl+shift+n"], "command": "new_window" },
		{ "keys": ["ctrl+o"], "command": "prompt_open_file" }
	]

Defining and Overriding Key Bindings
====================================

Sublime Text ships with a default key map (for example,
:file:`Packages/Default/Default (Windows).sublime-keymap)`. In order to
override the key bindings defined there, or to add new ones, you can store
them in a separate key map of higher precedence: for example
:file:`Packages/User/Default (Windows).sublime-keymap`.

See :ref:`merging-and-order-of-precedence` for more information on how
Sublime Text sorts files for merging.

Advanced Key Bindings
=====================

Simple key bindings consist of a key combination and a command to be executed.
However, there are more complex syntaxes for passing arguments and
contextual awareness.

Passing Arguments
*****************

Arguments are specified in the ``args`` key::

		{ "keys": ["shift+enter"], "command": "insert", "args": {"characters": "\n"} }

Here, ``\n`` is passed to the ``insert`` command when you press :kbd:`Shift+Enter`.

Contexts
********

Contexts determine whether a given key binding will be enabled based on the
caret's position or some other state.

::

	{ "keys": ["escape"], "command": "clear_fields", "context":
		[
			{ "key": "has_next_field", "operator": "equal", "operand": true }
		]
	}

This key binding translates to *clear snippet fields and resume normal editing
if there is a next field available*. Thus, unless you are cycling through snippet
fields, pressing :kbd:`ESC` will **not** trigger this key binding. (However,
something else might occur instead if :kbd:`ESC` happens to be bound to a
different context too---and that's likely to be the case for :kbd:`ESC`.)
.. warning::

   Want even better documentation for Sublime Text? You can  `help <https://www.bountysource.com/teams/st-undocs/fundraiser>`_.

