Key Bindings
============

Key bindings map key presses to commands.

File Format
***********

Key bindings are stored in ``.sublime-keymap`` files and defined in JSON. All
key map file names need to follow this pattern: ``Default (Platform).sublime-keymap``.
Otherwise, Sublime Text will ignore them.

Platform-Specific Key Maps
**************************

Each platform gets its own key map:

* ``Default (Windows).sublime-keymap``
* ``Default (OSX).sublime-keymap``
* ``Default (Linux).sublime-keymap``

Separate key maps exist to abide by different vendor-specific `HCI <http://en.wikipedia.org/wiki/Human%E2%80%93computer_interaction>`_ guidelines.

Keeping Key Maps Organized
**************************

Sublime Text ships with default key maps under ``Packages/Default``. Other
packages may include their own key map files. The recommended storage location
for your personal key map is ``Packages/User``.

See :ref:`merging-and-order-of-preference` for information about how Sublime
Text sorts files for merging.

Structure of a Key Binding
**************************

Key maps are arrays of key bindings. Below you'll find valid elements in key bindings.

``keys``
	An array of case-sensitive keys to be pressed. Modifiers can be specified
	with the ``+`` sign. Chords are built by adding elements to the array,
	e. g. ``["ctrl+k","ctrl+j"]``. Ambiguous chords are resolved with a timeout.

``command``
	Name of the command to be executed.

``args``
	Dictionary of arguments to be passed to ``command``. Keys must be the names
	of parameters to ``command``.

``context``
	Array of contexts to selectively enable the key binding. All contexts must
	be true for the key binding to trigger. See :ref:`context-reference` below.

Here's an example illustrating most of the features outlined above::

	{ "keys": ["shift+enter"], "command": "insert_snippet", "args": {"contents": "\n\t$0\n"}, "context":
		[
			{ "key": "setting.auto_indent", "operator": "equal", "operand": true },
			{ "key": "selection_empty", "operator": "equal", "operand": true, "match_all": true },
			{ "key": "preceding_text", "operator": "regex_contains", "operand": "\\{$", "match_all": true },
			{ "key": "following_text", "operator": "regex_contains", "operand": "^\\}", "match_all": true }
		]
	}

.. _context-reference:

Structure of a Context
**********************

``key``
	Name of a context operand to query.

``operator``
	Type of test to perform against ``key``.

``operand``
	Value against which the result of ``key`` is tested.

``match_all``
	Requires the test to succeed for all selections. Defaults to ``false``.

Context Operands
----------------

``auto_complete_visible``
	Returns ``true`` if the autocomplete dialog is visible.

``has_next_field``
	Returns ``true`` if there's a next snippet field available.

``has_prev_field``
	Returns ``true`` if there's a previous snippet field available.

``num_selections``
	Returns the number of selections.

``overlay_visible``
	Returns ``true`` if any overlay is visible.

``panel_visible``
	Returns ``true`` if any panel is visible.

``following_text``
	Restricts the test to the text following the caret.

``preceding_text``
	Restricts the test to the text preceding the caret.

``selection_empty``
	Returns ``true`` if the selection is an empty region.

``setting.x``
	Returns the value of the ``x`` setting. ``x`` can be any string.

``text``
	Restricts the test to the line the caret is in.

``selector``
	Returns the current scope.

Operators
---------

``equal``, ``not_equal``
	Test for equality.

``regex_contains``, ``not_regex_contains``
	Match against a regular expression.

Command Mode
************

Sublime Text provides a ``command_mode`` setting to prevent key presses from
being sent to the buffer. This is useful to emulate Vim's modal behavior.

Bindable Keys
*************

Keys may be specified literally or by name. Below you'll find a list of available
names (and some literals). This list isn't exhaustive.

* ``0-9``
* ``A-Z``
* ``a-z``
* ``backquote``
* ``backspace``
* ``break``
* ``delete``
* ``enter``
* ``equals``
* ``escape``
* ``f1-f12``
* ``forward_slash``
* ``home``, ``end``
* ``insert``
* ``left, up, right, down``
* ``minus``
* ``pageup, pagedown``
* ``plus``
* ``right_bracket``, ``left_bracket``
* ``semicolon``
* ``space``
* ``tab``

Modifiers
---------

* ``shift``
* ``ctrl``
* ``alt``
* ``super`` (Windows key, Command key...)

International Keyboards
***********************

Due to the way Sublime Text maps key names to physical keys, there might be a
mismatch between the two.

Troubleshooting
***************

.. TODO: fix formatting for API cross-ref.

See `sublime.log_commands(flag)`_  to enable command logging. It may help when
debugging key maps.

.. _sublime.log_commands(flag): http://www.sublimetext.com/docs/2/api_reference.html