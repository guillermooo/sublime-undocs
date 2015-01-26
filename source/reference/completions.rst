=================
Completions Files
=================

.. seealso::

   :doc:`/extensibility/completions`
      Introduction to the different types of completions


Note that completions aren't limited to completions files,
because other sources contribute
to the completions list
(see above).
However, the most explicit way
Sublime Text provides you to feed it completions
is by means of ``.sublime-completions`` files.

This topic only deals with
the format of a ``.sublime-completions`` file.


File Format
===========

Completions are JSON files
with the ``.sublime-completions`` extension.
Entries in completions files can contain
either snippet-like strings or plain text.


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
   to add a *hint* for the preceding trigger.
   The hint will be displayed right-aligned,
   slightly grayed
   and does not affect the trigger itself.

**contents**
   Text to be inserted in the buffer.
   Supports the same string interpolation features
   as snippets.

   Refer to :ref:`snippet-features`.

   .. note::

      If you want a literal ``$``,
      you have to escape it like this: ``\\$``
      (double backslashes are needed
      because we are within a JSON string).
