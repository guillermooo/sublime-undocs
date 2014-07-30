.. warning::

   Want even better documentation for Sublime Text?

   We are starting a new round of writing and editing to improve this guide in many ways. If you find it useful, please `support us <https://www.bountysource.com/teams/st-undocs/fundraiser>`_.

   |AmountRaised|

============
Key Bindings
============

Key bindings map key presses to commands.


File Format
***********

Key bindings are stored in ``.sublime-keymap`` files and defined in JSON. All
key map filenames need to follow this pattern: ``Default (<platform>).sublime-keymap``.
Otherwise, Sublime Text will ignore them.


Platform-Specific Key Maps
--------------------------

Each platform gets its own key map:

* ``Default (Windows).sublime-keymap``
* ``Default (OSX).sublime-keymap``
* ``Default (Linux).sublime-keymap``

Separate key maps exist to abide by different vendor-specific `HCI <http://en.wikipedia.org/wiki/Human%E2%80%93computer_interaction>`_ guidelines.


Structure of a Key Binding
--------------------------

Key maps are arrays of key bindings. Below you'll find valid elements in key bindings.

``keys``
	An array of case-sensitive keys to be pressed. Modifiers can be specified
	with the ``+`` sign. Chords are built by adding elements to the array,
	e.g. ``["ctrl+k","ctrl+j"]``. Ambiguous chords are resolved with a timeout.

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
----------------------

``key``
	Name of a context operand to query.

``operator``
	Type of test to perform against ``key``.

``operand``
	Value against which the result of ``key`` is tested.

``match_all``
	Requires the test to succeed for all selections. Defaults to ``false``.

Context Operands
^^^^^^^^^^^^^^^^

``auto_complete_visible``
	Returns ``true`` if the autocomplete list is visible.

``has_next_field``
	Returns ``true`` if a next snippet field is available.

``has_prev_field``
	Returns ``true`` if a previous snippet field is available.

``num_selections``
	Returns the number of selections.

``overlay_visible``
	Returns ``true`` if any overlay is visible.

``panel_visible``
	Returns ``true`` if any panel is visible.

``following_text``
	Restricts the test just to the text following the caret.

``preceding_text``
	Restricts the test just to the text preceding the caret.

``selection_empty``
	Returns ``true`` if the selection is an empty region.

``setting.x``
	Returns the value of the ``x`` setting. ``x`` can be any string.

``text``
	Restricts the test just to the selected text.

``selector``
	Returns the current scope.

``panel_has_focus``
	Returns ``true`` if the current focus is on a panel.

``panel``
	Returns ``true`` if the panel given as operand is visible.

Context Operators
^^^^^^^^^^^^^^^^^

``equal``, ``not_equal``
	Test for equality.

``regex_match``, ``not_regex_match``
	Match against a regular expression.

``regex_contains``, ``not_regex_contains``
	Match against a regular expression (containment).



Command Mode
************

Sublime Text provides a ``command_mode`` setting to prevent key presses from
being sent to the buffer. This is useful when emulating Vim's modal behavior.


Bindable Keys
*************

Keys may be specified literally or by name. Here's the list of valid names:

* ``up``
* ``down``
* ``right``
* ``left``
* ``insert``
* ``home``
* ``end``
* ``pageup``
* ``pagedown``
* ``backspace``
* ``delete``
* ``tab``
* ``enter``
* ``pause``
* ``escape``
* ``space``
* ``keypad0``
* ``keypad1``
* ``keypad2``
* ``keypad3``
* ``keypad4``
* ``keypad5``
* ``keypad6``
* ``keypad7``
* ``keypad8``
* ``keypad9``
* ``keypad_period``
* ``keypad_divide``
* ``keypad_multiply``
* ``keypad_minus``
* ``keypad_plus``
* ``keypad_enter``
* ``clear``
* ``f1``
* ``f2``
* ``f3``
* ``f4``
* ``f5``
* ``f6``
* ``f7``
* ``f8``
* ``f9``
* ``f10``
* ``f11``
* ``f12``
* ``f13``
* ``f14``
* ``f15``
* ``f16``
* ``f17``
* ``f18``
* ``f19``
* ``f20``
* ``sysreq``
* ``break``
* ``context_menu``
* ``browser_back``
* ``browser_forward``
* ``browser_refresh``
* ``browser_stop``
* ``browser_search``
* ``browser_favorites``
* ``browser_home``

Modifiers
---------

* ``shift``
* ``ctrl``
* ``alt``
* ``super`` (Windows key, Command key...)

Warning about Bindable Keys
---------------------------

If you're developing a package, keep this in mind:

* ``Ctrl+Alt+<alphanum>`` should not be used for any Windows key bindings.
* ``Option+<alphanum>`` should not be used for any OS X key bindings.

In both cases, the user's ability to insert non-ASCII characters would be
compromised.

If you are the end-user, you are free to remap those key combinations.


Keeping Key Maps Organized
**************************

Sublime Text ships with default key maps under ``Packages/Default``. Other
packages may include their own key map files. The recommended storage location
for your personal key map is ``Packages/User``.

See :ref:`merging-and-order-of-precedence` for information about how Sublime
Text sorts files for merging.


International Keyboards
***********************

Due to the way Sublime Text maps key names to physical keys, there might be a
mismatch between the two.


Troubleshooting
***************

.. TODO: fix formatting for API cross-ref.

To enable command logging, see `sublime.log_commands(flag)`_. This may help in
debugging key maps.

.. _sublime.log_commands(flag): http://www.sublimetext.com/docs/2/api_reference.html

.. warning::

   Want even better documentation for Sublime Text?

   We are starting a new round of writing and editing to improve this guide in many ways. If you find it useful, please `support us <https://www.bountysource.com/teams/st-undocs/fundraiser>`_.

   |AmountRaised|

.. |AmountRaised| image:: https://www.bountysource.com/badge/team?team_id=841&style=raised
   :target: https://www.bountysource.com/teams/st-undocs/fundraiser
