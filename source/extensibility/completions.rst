===========
Completions
===========

.. seealso::

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
interactions between all sources for completions.


File Format
===========

Completions are JSON files with the *.sublime-completions* extension.
Entries in completions files can contain either snippets or plain strings.


Example
*******

Here's an example (with HTML completions):

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

**scope**
	Determines when the completions list will be populated with this
	list of completions. See :ref:`scopes-and-scope-selectors` for more
	information.

**completions**
	Array of *completions*.


Types of Completions
********************

Plain Strings
-------------

Plain strings are equivalent to an entry where the ``trigger`` is identical to
the ``contents``:

.. code-block:: js

	"foo"
	// is equivalent to:
	{ "trigger": "foo", "contents": "foo" }


Trigger-based Completions
-------------------------

.. code-block:: js

	{ "trigger": "foo", "contents": "foobar" }

**trigger**
	Text that will be displayed in the completions list and will cause the
	``contents`` to be inserted when chosen.

	You can use a ``\t`` tab character to separate the trigger from a brief
	description on what the completion is about, it will be displayed right-aligned and slightly grayed and does not affect the trigger itself.

**contents**
	Text to be inserted in the buffer. Can use :ref:`snippet-features`.



Sources for Completions
=======================

These are the sources for completions the user can control:

	* Snippets
	* ``.sublime-completions``
	* API-injected completions via ``EventListener.on_query_completions()``

Additionally, other completions are folded into the final list:

	* Words in the buffer


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

	* through the completions list (:kbd:`Ctrl+spacebar`), or
	* By pressing :kbd:`Tab`.


The Completions List
********************

To use the completions list:

* Press :kbd:`Ctrl+spacebar` to open
* Optionally, press :kbd:`Ctrl+spacebar` again to select next entry or use up
  and down arrow keys
* Press :kbd:`Enter` or :kbd:`Tab` to validate selection (depending on the
  ``auto_complete_commit_on_tab`` )

.. note::
	The current selection in the completions list can actually be validated with
	any punctuation sign that isn't itself bound to a snippet (e.g. ``.``).

The completions list  may work in two ways: by bringing up a list of suggested
words to be completed, or by inserting the best match directly. The automatic
insertion will only be done if the list of completion candidates can be narrowed
down to one unambiguous choice given the current prefix.

If the choice of best completion is ambiguous, an interactive list will be
presented to the user. Unlike other items, snippets in this list are displayed
in this format: :samp:`{tab_trigger}\\t{name}`.


:kbd:`Tab`-Completed Completions
********************************

If you want to be able to tab-complete completions, the setting
``tab_completion`` must be set to ``true`` (default). Snippet tab-completion
is unaffected by this setting: They will always be completed according to
their tab trigger.

With ``tab_completion`` enabled, completion of items is always automatic. This
means, unlike the case of the completions list, that Sublime Text will always
make the decision for you. The rules for selecting the best completion are the
same as described above, but in case of ambiguity, Sublime Text will insert
the item it deems most suitable.

Inserting a Literal Tab Character
---------------------------------

When ``tab_completion`` is enabled, you can press ``Shift+Tab`` to insert a
literal tab character.
