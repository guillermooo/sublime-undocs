Completions
===========

Completions provide an IDE-like functionality to insert dynamic content through
the completions list or by pressing :kbd:`Tab`.

File Format
***********

Completions are JSON files with the ``.sublime-completions`` extension.

Structure of a Completions List
*******************************

``scope``
	Determines whether the completions are to be sourced from this file. See
	:ref:`scopes-and-scope-selectors` for more information.

``completions``
	Array of completions.

Here's an excerpt from the html completions::

	{
		"scope": "text.html - source - meta.tag, punctuation.definition.tag.begin",

		"completions":
		[
			{ "trigger": "a", "contents": "<a href=\"$1\">$0</a>" },
			{ "trigger": "abbr", "contents": "<abbr>$0</abbr>" },
			{ "trigger": "acronym", "contents": "<acronym>$0</acronym>" }

		]
	}


Types of Completions
********************

Plain Strings
-------------

Plain strings are equivalent to an entry where the ``trigger`` is identical to
the ``contents``::

	"foo"

	# is equivalent to:

	{ "trigger": "foo", "contents": "foo" }

Trigger-based Completions
-------------------------

``trigger``
	Text that will be displayed in the completions list and will cause the
	``contents`` to be inserted when validated.

``contents``
	Text to be inserted in the buffer. Can use snippet features.


Sources for Completions
***********************

These are the sources for completions the user can control:

	* ``.sublime-completions``
	* ``EventListener.on_query_completions()``

Additionally, other completions are folded into the final list:

	* Snippets
	* Words in the buffer

Priority of Sources for Completions
-----------------------------------

	* Snippets
	* API-injected completions
	* ``.sublime-completions`` files
	* Words in buffer

Snippets will only be automatically completed against an exact match of their
tab trigger. Other sources for completions are filtered with a case insensitve
fuzzy search instead.


The Completions List
*********************

To use the completions list:

	* Press :kbd:`Ctrl+spacebar` to open
	* Optionally, press :kbd:`Ctrl+spacebar` again to select next entry
	* Press :kbd:`Enter` or :kbd:`Tab` to validate selection

.. note::
	The current selection in the completions list can in fact be validated with
	any punctuation sign that isn't itself bound to a snippet.

Snippets show up in the completions list following the pattern:
``<tab_trigger> : <name>``. For the other completions, you will see just the
text to be inserted.

If the list of completions can be narrowed down to one choice, the autocomplete
dialog will be bypassed and the corresponding content will be inserted right
away according to the priority rules stated above.


Enabling and Disabling Tab Completion for Completions
*****************************************************

The ``tab_completion`` setting is ``true`` by default. Set it to ``false`` if
you want :kbd:`Tab` to stop sourcing the most likely completion. This setting
has no effect on triggers defined in ``.sublime-snippet`` files, so snippets
will always be inserted after a :kbd:`Tab`.

With ``tab_completion`` on, the same order of priority stated above applies,
but, unlike the case of the completions list, Sublime Text always will
insert a completion, even if faced with an ambiguous choice.

Inserting a Literal Tab
-----------------------

If ``tab_completion`` is ``true``, you can press ``Shift+Tab`` after a prefix
to insert a literal tab character.
