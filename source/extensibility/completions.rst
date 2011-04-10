===========
Completions
===========

.. seealso::

   :doc:`Reference for completions <../reference/completions>`
        Complete documentation on all available options.

Completions provide functionality in the spirit of IDEs to suggest terms and
insert snippets. Completions work through the autocomplete list or, optionally,
by pressing :kbd:`Tab`.

Note that completions in the broader sense of *words that Sublime Text will
look up and insert for you* are not limited to completions files, because other
sources contribute to the list of words to be completed, namely:

	 * Snippets 
	 * API-injected completions
	 * Buffer contents

However, ``.sublime-completions`` files are the most explicit way Sublime Text
provides you to feed it completions. This topic deals with the creation of
``.sublime-completions`` files as well as with the interaction between all
sources for completions.


File Format
===========

Completions are JSON files with the ``.sublime-completions`` extension.
Entries in completions files can contain either snippets or plain strings.


Example
*******

Here's an excerpt from the HTML completions:

.. code-block:: js

	{
		"scope": "text.html - source - meta.tag, punctuation.definition.tag.begin",
	
		"completions":
		[
			{ "trigger": "a", "contents": "<a href=\"$1\">$0</a>" },
			{ "trigger": "abbr", "contents": "<abbr>$0</abbr>" },
			{ "trigger": "acronym", "contents": "<acronym>$0</acronym>" }
		]
	}

``scope``
	Determines when the autocomplete list will be populated with this
	list of completions. See :ref:`scopes-and-scope-selectors` for more
	information.

In the example above, we've used trigger-based completions only, but
completions files support simple completions too. Simple completions are just
plain strings. Expanding our example with a few simple completions, we'd end up
with a list like so:

.. code-block:: js

	{
		"scope": "text.html - source - meta.tag, punctuation.definition.tag.begin",
	
		"completions":
		[
			{ "trigger": "a", "contents": "<a href=\"$1\">$0</a>" },
			{ "trigger": "abbr", "contents": "<abbr>$0</abbr>" },
			{ "trigger": "acronym", "contents": "<acronym>$0</acronym>" },
			
			"ninja",
			"robot",
			"pizza"
		]
	}


Sources for Completions
=======================

Completions not only originate in ``.sublime-completions`` files. This is the
exhaustive list of sources for completions:

	* Snippets
	* API-injected completions
	* ``.sublime-completions`` files
	* Words in buffer

Priority of Sources for Completions
***********************************

This is the order in which completions are prioritized:

	* Snippets
	* API-injected completions
	* ``.sublime-completions`` files
	* Words in buffer

Snippets will always win if the current prefix matches their tab trigger
exactly. For the rest of the completions sources, a fuzzy match is performed.
Also, snippets will always lose against a fuzzy match. Note that this is only
relevant if the completion is going to be inserted automatically. When the
autocomplete list is shown, snippets will be listed along the other items, even
if the prefix only partially matches the snippets' tab triggers.

How to Use Completions
======================

There are two methods to use completions, and although the priority given to
completions when screening them is always the same, there is a difference in
the result that will be explained below.

Completions can be inserted in two ways: 

	* through the autocomplete list (:kbd:`Ctrl+spacebar`);
	* by pressing :kbd:`Tab`.


The Autocomplete List
*********************

The autocomplete list (:kbd:`Ctrl+spacebar`) may work in two ways: by bringing
up a list of suggested words to be completed, or by inserting the best match
directly.

If the choice of best completion is ambiguous, an interactive list will be
presented to the user, who will have to select an item himself. Unlike other
items, snippets in this list are displayed in this format:
``<tab_trigger> : <name>``, where ``<tab_trigger>`` and ``<name>`` are
variable.

The completion with :kbd:`Ctrl+spacebar` will only be automatic if the list of
completion candidates can be narrowed down to one unambiguous choice given the
current prefix.

:kbd:`Tab`-completed Completions
********************************

If you want to be able to tab-complete completions, the setting
``tab_completion`` must be set to ``true``. By default, ``tab_completion`` is
set to ``false``. Snippet tab-completion is unaffected by this setting, they
will always be completed according to their tab trigger.

With ``tab_completion`` enabled, completion of items is always automatic, which
means that, unlike in the case of the autocomplete list, Sublime Text will
always make a decision for you. The rules to select the best completion are the
same as above, but in case of ambiguity, Sublime Text will still insert the
item deemed most suitable.
