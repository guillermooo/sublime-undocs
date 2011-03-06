Completions
===========

Completions provide and IDE-like functionality to autocomplete words, insert
snippets or suggest dynamic content, all through the autocomplete dialog. They
can be thought of as a more flexible way to insert snippets.

File Format
***********

Completions use JSON and are stored in ``.sublime-completions`` files.

Example
*******

Here's an excerpt from the html completions::

	{
		"scope": "text.html - source - meta.tag, punctuation.definition.tag.begin",
	
		"completions":
		[
			{ "trigger": "a", "contents": "<a href=\"$1\">$0</a>" },
			{ "trigger": "abbr", "contents": "<abbr>$0</abbr>" },
			{ "trigger": "acronym", "contents": "<acronym>$0</acronym>" },
		]
	}

``scope`` determines when the autocomplete dialog will be populated with this
list of completions. See :ref:`scopes-and-scope-selectors` for more information.

How to Open the Autocomplete Dialog
***********************************

By default, it's bound to ``CTRL + SPACEBAR``.