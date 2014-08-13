
===========
Completions
===========

.. seealso::

   :doc:`Reference for completions <../reference/completions>`
      Complete documentation on all available options.
   `Sublime Text Documentation <http://www.sublimetext.com/docs/2/tab_completion.html>`_
   	Official documentation on this topic.

In the spirit of IDEs, completions suggest terms and insert snippets.
Completions work through the completions list or, optionally, by pressing
:kbd:`Tab`.

Note that, in the broader sense of *words that Sublime Text will look up and
insert for you*, completions aren't limited to completions files, because other
sources contribute to the list of words to be completed, namely:

	 * Snippets
	 * API-injected completions
	 * Buffer contents

However, the most explicit way Sublime Text provides you to feed it
completions is by means of ``.sublime-completions`` files. This topic deals
with the creation of a ``.sublime-completions`` file as well as with the
interactions among all sources for completions.


File Format
===========

Completions are JSON files with the ``.sublime-completions`` extension.
Entries in completions files can contain either snippets or plain strings.


Example
*******

Here's an excerpt from Sublime Text's HTML completions:

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
	Determines when the completions list will be populated with this
	list of completions. See :ref:`scopes-and-scope-selectors` for more
	information.

In the example above, we've only used trigger-based completions, but
completions files support simple completions too. Simple completions are just
plain strings. Expanding our example with a few simple completions results
in a list like this:

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

Completions not only originate in ``.sublime-completions`` files. Here is the
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
	* Words in the buffer

Snippets will always win if the current prefix matches their tab trigger
exactly. For the rest of the completion sources, a fuzzy match is performed.
Furthermore, snippets always lose with fuzzy matches.

But this is relevant only when the completion is inserted automatically. When
a list of completions is shown, snippets will still be listed alongside the
other items, even if the prefix only partially matches the snippets' tab
triggers.

How to Use Completions
======================

There are two methods for using completions. Even though, when screening them, the
priority given to completions always stays the same, the two methods produce
different results, as explained next.

Completions can be inserted in two ways:

	* Through the completions list (:kbd:`Ctrl+spacebar`).
	* By pressing :kbd:`Tab`.


The Completions List
********************

The completions list (:kbd:`Ctrl+spacebar`) does its work in two ways: by bringing
up a list of suggested words to be completed, or by inserting the best match
directly.

If the choice of best completion is ambiguous, an interactive list will be
presented to the user, who then will have to select an item himself. Unlike other
items, snippets in this list are displayed in the format:
``<tab_trigger> : <name>``, where ``<tab_trigger>`` and ``<name>`` are
variable.

Using :kbd:`Ctrl+spacebar`, the completion choice will be automatic only if the list of
completion candidates can be narrowed down to one unambiguous choice, given the
current prefix.

:kbd:`Tab`-Completed Completions
********************************

If you want to be able to tab-complete completions, the setting
``tab_completion`` must be ``true``, which is the default.
Snippets' tab-completion is unaffected by this setting: they
always will be completed, or not, according to their tab trigger.

With ``tab_completion`` enabled, completion of items is always automatic. This
means, unlike the case of the completions list, that Sublime Text will always
make the decision for you. The rules for selecting the best completion are the
same as described above, but in case of ambiguity, Sublime Text will insert
the item it deems most suitable.

Inserting a Literal Tab Character
---------------------------------

When ``tab_completion`` is enabled, you can press ``Shift+Tab`` to insert a
literal tab character.


