Completions
===========

Completions provide and IDE-like functionality to insert dynamic content through
the autocomplete dialog.

File Format
***********

Completions use JSON and are stored in ``.sublime-completions`` files.

Structure of a Completions List
*******************************

``scope``
	Determines whether the completions are to be sourced from this file. See
	:ref:`scopes-and-scope-selectors` for more information.

``completions``
	Array of completions (strings or triggers).

Here's an exceprt from the html completions::

	{
		"scope": "text.html - source - meta.tag, punctuation.definition.tag.begin",
	
		"completions":
		[
			{ "trigger": "a", "contents": "<a href=\"$1\">$0</a>" },
			{ "trigger": "abbr", "contents": "<abbr>$0</abbr>" },
			{ "trigger": "acronym", "contents": "<acronym>$0</acronym>" },
		]
	}

Types of Completions
********************

Simple
------

Plain strings are equivalent to an entry where the ``trigger`` is identical to
the ``contents``::

	"foo"

	# is equivalent to:

	{ "trigger": "foo", "contents": "foo" }

Normal
------

``trigger``
	Sequence of keys that will insert the ``contents``.

``contents``
	Text to be sourced in the autocomplete dialog. Can be a snippet.

How to Open the Autocomplete Dialog
***********************************

By default, it's bound to ``CTRL + SPACEBAR``.

Completions through the API
***************************

In addition to ``.sublime-snippet`` files and ``.sublime-completions``, you can
source completions from the API thanks to ``EventListener.on_query_completions``.

Order of Precedence for Completions
***********************************

The autocomplete dialog is populated from several sources, in this order of
precedence:

	* API
	* Completion files
	* Words in buffer

Additionally, snippets will compete to be completed automatically too. Snippets
take the highest precedence, but in order to trigger when pressing ``tab``,
the prefix typed in the buffer must match their trigger exctly, while
completions fuzzy match against it.

If there's only one candidate to be completed, the autocomplete dialog will be
bypassed and the word will be inserted right away.

Enabling Tab Completion for Completion Lists
********************************************

By default, the ``tab_completion`` setting is ``false``. If you want to be able
to validate the completions dialog by pressing ``TAB`` in addition to ``ENTER``,
set it to ``true``. ``tab_completion`` has no effect on triggers defined in
``.sublime-snippet`` files.