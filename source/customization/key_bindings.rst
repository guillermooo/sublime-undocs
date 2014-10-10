============
Key Bindings
============

.. seealso::

   :doc:`Reference for key bindings </reference/key_bindings>`
        Complete documentation on key bindings.

Key bindings let you
map sequences of key presses to actions.


File Format
===========

.. TODO: Perhaps we can turn this into bullet points. Faster to read and less
..       words.
..       Like this:
..       	Format: Json
..				File Name: Default(<platorm>).sublime-keymap

Key bindings are defined in JSON
and stored in *.sublime-keymap* files.
In order to integrate better with each platform,
there are separate key map files
for Linux, OSX and Windows.
Only key maps for the corresponding platform
will be loaded.

Example
*******

Here's an excerpt from the default key map for Windows::

	[
		{ "keys": ["ctrl+shift+n"], "command": "new_window" },
		{ "keys": ["ctrl+o"], "command": "prompt_open_file" }
	]


Defining and Overriding Key Bindings
====================================

Sublime Text ships with a default key map
(for example, :file:`Packages/Default/Default (Windows).sublime-keymap)`.
In order to override the key bindings defined there,
or to add new ones,
you can store them in a separate key map
of higher precedence:
for example :file:`Packages/User/Default (Windows).sublime-keymap`.

See :ref:`merging-and-order-of-precedence`
for more information
on how Sublime Text sorts files for merging.


Advanced Key Bindings
=====================

Simple key bindings consist
of a key combination and a command to be executed.
However, there are more complex syntaxes
for passing arguments and contextual awareness.


Passing Arguments
*****************

Arguments are specified
in the ``args`` key::

		{ "keys": ["shift+enter"], "command": "insert", "args": {"characters": "\n"} }

Here, ``\n`` is passed to the ``insert`` command
when you press :kbd:`Shift+Enter`.


Contexts
********

Contexts determine
whether a given key binding will be enabled
based on the caret's position
or some other state.

::

	{ "keys": ["escape"], "command": "clear_fields", "context":
		[
			{ "key": "has_next_field", "operator": "equal", "operand": true }
		]
	}

This key binding translates to
*clear snippet fields and resume normal editing
if there is a next field available*.
Thus, unless you are cycling through snippet fields,
pressing :kbd:`ESC` will **not**
trigger this key binding.
(However, something else might occur instead
if :kbd:`ESC` happens to be bound to a different context too---
and that's likely to be the case for :kbd:`ESC`.)


Keys combinations
*****************

You can create a key binding
which will be triggered only
if a combination of multiple keys
is stroked in sequence.
To use it, you just have
to add a second value in the ``keys`` array::

	{ "keys": ["ctrl+k", "ctrl+v"], "command": "paste_from_history" }

Here, to trigger the command ``paste_from_history``,
you have to press :kbd:`Ctrl` + :kbd:`k` first,
release the key :kbd:`k`,
then press the key :kbd:`v`.

Note: this example is a default key binding,
so you don't need to add it to your config file
and you can try it right now!
