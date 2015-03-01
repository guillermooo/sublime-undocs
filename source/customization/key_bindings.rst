==============
 Key Bindings
==============

.. seealso::

   :doc:`Reference for key bindings </reference/key_bindings>`
      Complete documentation on key bindings.

Key bindings let you
map sequences of key presses to commands.


File Format
===========

.. TODO: Perhaps we can turn this into bullet points. Faster to read and less
..       words.
..       Like this:
..          Format: Json
..          File Name: Default(<platorm>).sublime-keymap

Key bindings are defined in JSON
and stored in ``.sublime-keymap`` files.

In the same package, separate keymap files
for Linux, OSX and Windows
may exist for better OS integration.


Example
*******

.. code-block:: json

   [
      { "keys": ["ctrl+shift+n"], "command": "new_window" },
      { "keys": ["ctrl+o"], "command": "prompt_open_file" }
   ]


Defining and Overriding Key Bindings
====================================

Sublime Text ships with default key bindings
(for example, :file:`Packages/Default/Default (Windows).sublime-keymap)`.
In order to override default key bindings
or add new ones,
use a separate keymap file
with higher precedence:
for example, :file:`Packages/User/Default (Windows).sublime-keymap`.

See :ref:`merging-and-order-of-precedence`
for more information.


Advanced Key Bindings
=====================

Simple key bindings consist
of a sequence of one or more keys mapped to a command.
However, there are more complex syntaxes
for passing arguments to commands and
restricting key bindings to specific contexts.


Passing Arguments
*****************

Use the ``args`` key
to specify arguments:

.. code-block:: json

   { "keys": ["shift+enter"], "command": "insert", "args": {"characters": "\n"} }

Here, ``\n`` is passed to the ``insert`` command
whenever :kbd:`Shift+Enter` is pressed.


Contexts
********

Contexts determine
whether a given key binding is enabled
based on the caret's position
or some other state.

.. code-block:: json

   { "keys": ["escape"], "command": "clear_fields", "context":
      [
         { "key": "has_next_field", "operator": "equal", "operand": true }
      ]
   }

This key binding translates to
*clear snippet fields and resume normal editing
if there is a next snippet field available*.
Thus, pressing :kbd:`ESC` will only
trigger this key binding
if you are cycling through snippet fields.

The same key binding
may be mapped to multiple contexts,
so a single sequence of key presses
may produce different results
at different times.


Key Chords
**********

You can create key bindings
composed of multiple keys.

.. code-block:: json

   { "keys": ["ctrl+k", "ctrl+v"], "command": "paste_from_history" }

Here, to trigger the command ``paste_from_history``,
you have to press :kbd:`Ctrl + K` first,
then release :kbd:`K`,
and finally press :kbd:`V`.

Note: This example is a default key binding,
so you can try it at any time.
