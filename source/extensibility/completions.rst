===========
Completions
===========

.. seealso::

	`Sublime Text Documentation <http://www.sublimetext.com/docs/2/tab_completion.html>`_
		Official documentation on this topic.

Completions provide functionality in the spirit of IDEs to suggest terms and
insert snippets. Completions work through the completions list or, optionally,
by pressing :kbd:`Tab`.

Note that completions in the broader sense of *words that Sublime Text will
look up and insert for you* are not limited to completions files, because other
sources contribute to the list of words to be completed, namely:

	 * Snippets
	 * API-injected completions
	 * Buffer contents

However, *.sublime-completions* files are the most explicit way Sublime Text
provides you to feed it completions. This topic deals with the creation of
*.sublime-completions* files as well as with the interaction between all
sources for completions.


File Format
===========

Completions are JSON files with the *.sublime-completions* extension.
Entries in completions files can contain either snippets or plain strings.

Here's an example (with HTML completions):

.. code-block:: js

	{
		"scope": "text.html - source - meta.tag, punctuation.definition.tag.begin",

		"completions":
		[
			{ "trigger": "a", "contents": "<a href=\"$1\">$0</a>" },
			{ "trigger": "abbr", "contents": "<abbr>$0</abbr>" },
			{ "trigger": "acronym", "contents": "<acronym>$0</acronym>" },
			{ "trigger": "script\t<script src=\"...\" />",
			  "contents": "<script src=\"$1\" />" },

			"ninja",
			"robot",
			"pizza"
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


.. _completions-trigger-based:

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

.. py:currentmodule:: sublime_plugin

* :doc:`/extensibility/snippets`
* *.sublime-completions*
* API-injected completions via :py:meth:`EventListener.on_query_completions`

Additionally, other completions are folded into the final list:

* Words in the buffer

Priority of Sources for Completions
***********************************

This is the order in which completions are prioritized:

* Snippets
* API-injected completions
* *.sublime-completions* files
* Words in buffer

Snippets will always win if the current prefix matches their tab trigger
exactly. For the rest of the completions sources, a fuzzy match is performed.
Also, snippets will always lose against a fuzzy match. Note that this is only
relevant if the completion is going to be inserted automatically. When the
completions list is shown, snippets will be listed along the other items, even
if the prefix only partially matches the snippets' tab triggers.

How to Use Completions
======================

There are two methods for using completions. Even though, when screening them, the
priority given to completions always stays the same, the two methods produce
different results, as explained next.

Completions can be inserted in two ways:

	* through the completions list (:kbd:`Ctrl+spacebar`), and
	* by pressing :kbd:`Tab`.


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


.. _completions-multi-cursor:

Completions with multiple cursors
*********************************

Sublime Text can also handle completions with multiple cursors but will only
open the completion list when all cursors share the same prefix.

Working example (``|`` represents one cursor)::

	l|
	some text with l|
	l| and.l|

Not working example::

	l|
	some text with la|
	l| andl|

Selections are essentially ignored, only the position of the cursor matters.
Thus, ``e|[-some selection] example``, with ``|`` as the cursor and ``[...]`` as
the current selection, completes to ``example|[-some selection] example``.


:kbd:`Tab`-completed Completions
********************************

If you want to be able to tab-complete completions, the setting
``tab_completion`` must be set to ``true`` (default). Snippet tab-completion is
unaffected by this setting: They will always be completed according to their tab
trigger.

With ``tab_completion`` enabled, completion of items is always automatic, which
means that, unlike in the case of the completions list, Sublime Text will
always make a decision for you. The rules to select the best completion are the
same as above, but in case of ambiguity, Sublime Text will still insert the
item deemed most suitable.

Inserting a Literal Tab Character
---------------------------------

When ``tab_completion`` is enabled, you can press ``Shift+Tab`` to insert a
literal tab character.