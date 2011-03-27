Completions
===========

.. seealso::

   :doc:`Reference for completions <../reference/completions>`
        Complete documentation on all available options.

Completions provide and IDE-like functionality to autocomplete words, insert
snippets or suggest dynamic content, all through the autocomplete list.


File Format
***********

Completions are JSON files with the ``.sublime-completions`` extension.


Example
-------

Here's an excerpt from the HTML completions::

	{
		"scope": "text.html - source - meta.tag, punctuation.definition.tag.begin",
	
		"completions":
		[
			{ "trigger": "a", "contents": "<a href=\"$1\">$0</a>" },
			{ "trigger": "abbr", "contents": "<abbr>$0</abbr>" },
			{ "trigger": "acronym", "contents": "<acronym>$0</acronym>" }
		]
	}

``scope`` determines when the autocomplete list will be populated with this
list of completions. See :ref:`scopes-and-scope-selectors` for more information.

How to Open the Autocomplete List
*********************************

By default, it's bound to ``CTRL + SPACEBAR``.