============
Key Bindings
============

Key bindings map key presses to commands.


File Format
***********

Key bindings are stored in ``.sublime-keymap`` files
and defined in JSON.
Key map files may be located anywhere in a package.


Naming Key Map Files
--------------------

Each platform can optionally have its own key map:

* ``Default (Windows).sublime-keymap``
* ``Default (OSX).sublime-keymap``
* ``Default (Linux).sublime-keymap``

To have the key map applied in all platforms,
name the file ``Default.sublime-keymap``.

Sublime Text will ignore any ``.sublime-keymap``
whose name doesn't follow the patterns just described.


Structure of a Key Binding
--------------------------

Key maps are arrays of key bindings.
This list presents all valid elements in a key binding.

``keys``
   An array of case-sensitive keys.
   Modifiers can be specified
   with the ``+`` sign.
   Chords can be built
   by adding elements to the array,
   e.g. ``["ctrl+k","ctrl+j"]``.
   Ambiguous chords are resolved
   with a timeout.

``command``
   Name of the command to be executed.

``args``
   Dictionary of arguments
   to be passed to ``command``.
   Keys must be the names
   of parameters to ``command``.

``context``
   Array of conditions
   that determine a particular *context*.
   All conditions must evaluate to `true`
   for the key binding to be active.
   See :ref:`context-reference` below.

Here's an example::

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
   Defaults to ``equal``.

``operand``
   The result of ``key`` is tested against this value.

``match_all``
   Requires the test to succeed
   for all selections.
   Defaults to ``false``.


Context Operands
^^^^^^^^^^^^^^^^

``auto_complete_visible``
   Returns ``true``
   if the autocomplete list
   is visible.

``has_next_field``
   Returns ``true``
   if a next snippet field
   is available.

``has_prev_field``
   Returns ``true``
   if a previous snippet field
   is available.

``num_selections``
   Returns the number of selections.

``overlay_visible``
   Returns ``true``
   if any overlay is visible.

``panel_visible``
   Returns ``true``
   if any panel is visible.

``following_text``
   Restricts the test
   to the text following the caret.

``preceding_text``
   Restricts the test
   to the text preceding the caret.

``selection_empty``
   Returns ``true``
   if the selection
   is an empty region.

``setting.x``
   Returns the value of the ``x`` setting.
   `x`` can be any string.

``text``
   Restricts the test
   to the selected text.

``selector``
   Returns the name of the current scope.

``panel_has_focus``
   Returns ``true``
   if a panel
   has input focus.

``panel``
   Returns ``true``
   if the panel given as ``operand``
   is visible.


Context Operators
^^^^^^^^^^^^^^^^^

``equal``, ``not_equal``
   Test for equality.

``regex_match``, ``not_regex_match``
   Match against a regular expression (full match).

``regex_contains``, ``not_regex_contains``
   Match against a regular expression (partial match).



Command Mode
************

Sublime Text provides a ``command_mode`` setting
to prevent key presses
from being sent to the buffer.
This is useful, for example,
to emulate Vim's modal behavior.

Key bindings not intended for command mode
should include a context like this::

    {"key": "setting.command_mode", "operand": false}

This way, plugins legitimately using command mode
will be able to define appropriate key bindings
without interference.


Bindable Keys
*************

Keys in key bindings may be specified
literally or by name.

.. XXX: Check this
If using a name doesn't work in your case,
try a literal value.

Here's the list of all valid names:

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

If you're developing a package,
keep this in mind:

* ``Ctrl+Alt+<alphanum>`` should not be used for any Windows key bindings.
* ``Option+<alphanum>`` should not be used for any OS X key bindings.

In both cases,
the user's ability
to insert non-ASCII characters
would be compromised.

End-users are free to remap
any key combination.


Order of Preference for Key Bindings
************************************

Key bindings in a key map file are evaluated
from bottom to top.
The first matching context wins.


Keeping Key Maps Organized
**************************

Sublime Text ships with default key maps
under ``Packages/Default``.
Other packages may include
key map files of their own.
The recommended storage location
for your personal key map is ``Packages/User``.

See :ref:`merging-and-order-of-precedence`
for information.


International Keyboards
***********************

Due to the way Sublime Text
maps key names to physical keys,
there might be a mismatch between the two.


Troubleshooting
***************

To enable logging
related to key maps, see:

   - `sublime.log_commands(flag)`_.
   - `sublime.log_input(flag)`_.

This may help in
debugging key maps.


.. _sublime.log_commands(flag): http://www.sublimetext.com/docs/3/api_reference.html
.. _sublime.log_input(flag): http://www.sublimetext.com/docs/3/api_reference.html
