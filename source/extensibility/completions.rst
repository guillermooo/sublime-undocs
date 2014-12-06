===========
Completions
===========

In the spirit of IDEs,
completions suggest terms and insert snippets.
Completions work through the completions list,
which opens automatically as you type
or by pressing :kbd:`Ctrl + Space`.

Note that, in the broader sense of
*words that Sublime Text will look up and insert for you*,
completions aren't limited to completions files,
because other sources contribute
to the list of words to be completed.
These are, namely:

* Snippets
* API-injected completions
* Buffer contents

However, the most explicit way
Sublime Text provides you to feed it completions
is by means of ``.sublime-completions`` files.
This topic deals with
the creation of a ``.sublime-completions`` file
as well as with the interactions
between all sources for completions.


File Format
===========

Completions are JSON files
with the ``.sublime-completions`` extension.
Entries in completions files can contain
either snippets-like strings or plain text.


Example
*******

Here's an example (with HTML completions):

.. code-block:: js

   {
      "scope": "text.html - source - meta.tag, punctuation.definition.tag.begin",

      "completions":
      [
         { "trigger": "a", "contents": "<a href=\"$1\">$0</a>" },
         { "trigger": "abbr\t<abbr>", "contents": "<abbr>$0</abbr>" },
         { "trigger": "acronym", "contents": "<acronym>$0</acronym>" }
      ]
   }

**scope**
   Determines when the completions list
   will be populated with this list of completions.

   See :ref:`scopes-and-scope-selectors` for more information.

**completions**
   Array of *completions*.


Types of Completions
********************

Plain Strings
-------------

Plain strings are equivalent to
an entry where the ``trigger``
is identical to the ``contents``:

.. code-block:: js

   "foo"
   // is equivalent to:
   { "trigger": "foo", "contents": "foo" }


.. _completions-trigger-based:

Trigger-based Completions
-------------------------

.. code-block:: js

   { "trigger": "foo", "contents": "foobar" },
   { "trigger": "foo\ttest", "contents": "foobar" }

**trigger**
   Text that will be displayed in the completions list
   and will cause the ``contents``
   to be inserted when chosen.

   You can use a ``\t`` tab character
   to separate the trigger from a brief description
   on what the completion is about.
   It will be displayed right-aligned,
   slightly grayed
   and does not affect the trigger itself.

**contents**
   Text to be inserted in the buffer.
   Uses the same string interpolation features
   as snippets.

   Refer to :ref:`snippet-features`.

   Because of that,
   if you want a literal ``$``,
   you have to escape it like this: ``\\$``
   (double backslashes are needed
   because we are within a JSON string).


Sources for Completions and their Priorities
============================================

These are the sources for completions
the user can control,
in the order they are prioritized:

.. py:currentmodule:: sublime_plugin


1. :doc:`/extensibility/snippets`
#. API-injected completions
   via :py:meth:`EventListener.on_query_completions`
#. ``.sublime-completions`` files

Additionally,
these other completions are folded into the final list:

4. Words in the buffer

Snippets will always win
when the current prefix
matches their tab trigger exactly.
For the rest of the completion sources,
a fuzzy match is performed.
Furthermore,
snippets always lose with fuzzy matches.

When a list of completions is shown,
snippets will still be listed alongside the other items,
even if the prefix only partially matches
the snippets' tab triggers.

.. note::

   Word completions from the buffer
   can be disabled exlicitly
   from a completions event hook.


How to Use Completions
======================

There are two methods for using completions.
Even though, when screening them,
the priority given to completions always stays the same,
the two methods produce different results,
as explained next.

Completions can be inserted in two ways:

   * through the completions list (:kbd:`Ctrl+spacebar`), or
   * By pressing :kbd:`Tab`.


The Completions List
********************

To use the completions list:

1. Press :kbd:`Ctrl+spacebar` or type something to open.
#. Optionally, press :kbd:`Ctrl+spacebar` again
   to select next entry
   or use up and down arrow keys.
#. Press :kbd:`Enter` or :kbd:`Tab` to validate selection
   (depending on the ``auto_complete_commit_on_tab`` setting)
#. Optionally, press :kbd:`Tab` repeatedly
   to insert the next possible completion.

.. note::

   If the completions list was opened explicitly,
   the current selection
   in the completions list
   can also be validated
   with any punctuation sign
   that isn't itself bound to a snippet (e.g. ``.``).

When the list of completion candidates
can be narrowed down to one unambiguous choice
given the current prefix,
this one completion will be validated automatically
the moment you trigger the completion list.


.. _completions-multi-cursor:

Completions with multiple cursors
*********************************

Sublime Text can also handle completions with multiple cursors
but will only open the completion list
when all cursors share the same text
between the current cursor positions
and the last word separator character
(e.g. ``.``  or a line break).

Working example (``|`` represents one cursor)::

   l|
   some text with l|
   l| and.l|

Not working example::

   l|
   some text with la|
   l| andl|

Selections are essentially ignored,
only the position of the cursor matters.
Thus, ``e|[-some selection] example``,
with ``|`` as the cursor and ``[...]`` as the current selection,
completes to ``example|[-some selection] example``.


:kbd:`Tab`-Completed Completions
********************************

If you want to be able to tab-complete completions,
the setting ``tab_completion`` must be set to ``true`` (default).
Snippet tab-completion is unaffected by this setting:
They will always be completed
according to their tab trigger.

With ``tab_completion`` enabled,
completion of items is always automatic.
This means, unlike the case of the completions list,
that Sublime Text will always make the decision for you.
The rules for selecting the best completion
are the same as described above,
but in case of ambiguity,
Sublime Text will insert the item it deems most suitable.
You can press the :kbd:`Tab` key multiple times
to walk through other available options.

Inserting a Literal Tab Character
---------------------------------

When ``tab_completion`` is enabled,
you can press :kbd:`Shift + Tab` to insert
a literal tab character.
