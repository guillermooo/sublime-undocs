===========
Completions
===========

.. seealso::

   :doc:`Reference for completions <../reference/completions>`
        Complete documentation on all available options.

Completions provide functionality in the spirit of IDEs to autocomplete words,
insert snippets or suggest dynamic content, all through the autocomplete list
or by pressing :kbd:`Tab`.


File Format
===========

Completions are JSON files with the ``.sublime-completions`` extension.
Completions files can contain either snippets or plain strings.

Note  that completions in the broader sense of *words that Sublime Text will
look up and insert for you* are not limited to completions files, because other
sources contribute to the list of words to be completed. Namely, we're
referring to API-injected completions, snippets and the buffer's contents.
However, ``.sublime-completions`` files are the most explicit way Sublime Text
provides you to feed it completions.


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
plain strings. Expanding our example with simple completions, we'd end up with
a list like so:

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

How to Use Autocompletions
==========================

.. warning:: This is a draft.

Completions can be inserted in two ways: by pressing :kbd:`Tab` or through
the autocomplete list (:kbd:`Ctrl+spacebar`). Completions lead a tough life,
where only the fittest of several competing species survives. We'll see how
the drama unfolds in the next sections.

:kbd:`Tab`-completed Completions
********************************

Completions can only be :kbd:`Tab`-completed if the setting
``tab_completion`` is ``true``. If it is, Sublime Text will insert the best
completion candidate into the view. Note that *candidate* here not only refers
to completions sourced from ``.sublime-completions`` files, but to completions
injected via API, to snippets, and to words in the current buffer too. If that
sounds complex, it's because it is.

When you press :kbd:`Tab` under these circumstances, all hell will break loose.
Well, no, actually there's priorities to completions: first come API-injected
completions, then completions files and lastly, words in the buffer. But life's
never easy: snippets want to claim their place among completions too. And, in
fact, they will always win if you complete against their *exact* tab trigger.
As a corollary to this, they will always lose when you :kbd:`Tab`-complete
against an inexact tab trigger, and one of the other completions enumerated
above will snatch the coveted to-be-completed status.

If that didn't make you want to switch off ``tab_completion``, then you might
want to switch it on, because it's disabled by default.

What happens if ``tab_completion`` is set to ``false``? In that case, only
snippets will qualify to be :kbd:`Tab`-completed. Snippets seem to be at the
top of the food chain in Sublime Text. With ``tab_completion`` off, then,
the rest of the completions will only be available through the autocomplete
list.

The Autocomplete List
*********************

The autocomplete list is bound to :kbd:`Ctrl+spacebar`. Let's remember that
completions not only originate in ``.sublime-completions`` files. Thus, when
you open the autocomplete list, it will get populated following the same order
of precedence as outlined in the previous section. However, if Sublime Text
can narrow down the list of candidates to a single one, it will bypass the
autocomplete list altogether and it will insert the winning completion
straight away.

Snippets in the autocomplete list look different than the rest of the
completions: they follow the display pattern ``<tab_trigger> : <name>``, where
``<tab_trigger>`` and ``<name>`` are variable.

To sum up: Not all completions are born equal, but they all have a place in
Sublime Text, although it might not always be the one you were expecting.
