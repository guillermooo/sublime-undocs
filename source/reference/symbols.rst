=======
Symbols
=======


Overview
========

Sublime Text provides basic support
for :ref:`symbol navigation <fm-goto-symbol>`
(jumping to class and function definitions,
etc.).
Symbol navigation can be enabled
for any type of file.


Format
======

Symbols are defined  using metadata files.
Because symbol definition files
are commonly required by packages,
they are discussed in this separate page
so the information is easier to find.

Just as regular metadata files,
symbol definition files
have the ``.tmPreferences`` extension
and use the Property List format.
The file name is ignored by Sublime Text.

.. seealso::

   :doc:`metadata`
      Detailed documentation on metadata files.


Defining Symbols
================

Several symbol definition files can coexist
in the same package.
For example, two symbol definition files
could work in tandem:
one would define all symbols,
and a second one
would selectively hide some of them
that were uninteresting for users.

The symbol navigation framework in Sublime Text
is strictly text-based
and uses scope selectors
to capture symbols in source code files.
No lexical or syntactical analysis is performed.

Sublime Text features two types of symbol list:
a local symbol list (active file)
and a global symbol list (project-wide).
Using symbol definition files,
you can target the two of them.

.. XXX: ref scopes

Let's see an example
of a symbol definition file:

.. code-block:: xml
   :emphasize-lines: 7-8,11-12

   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
   <plist version="1.0">
   <dict>
      <key>name</key>
      <string>Symbol List</string>
      <key>scope</key>
      <string>source.python meta.function.python, source.python meta.class.python</string>
      <key>settings</key>
      <dict>
         <key>showInSymbolList</key>
         <integer>1</integer>
      </dict>
   </dict>
   </plist>

Using the file above,
Sublime Text would scan source code files
for scope names ``source.python meta.function.python``
and ``source.python meta.class.python``,
and text within would be indexed
as symbols.
The ``showInSymbolList`` setting tells
Sublime Text to use
the local symbol list.


Text Transformations
====================

It is possible
to apply transformations to symbols
before they are displayed to the user.
Text transformations are defined
as regular expressions
using the `Oniguruma`_ syntax.

This is an example of a text substitution:

::

   s/class\s+([A-Za-z_][A-Za-z0-9_]*.+?\)?)(\:|$)/$1/g;

In this case, a captured symbol such as ``class FooBar(object)``
would show up instead as ``FooBar(object)``
in the symbol list.


.. TODO: local symbols vs project symbols in ST show different results. Not
.. sure how it works.

And this is our previous example,
including transformations:

.. code-block:: xml
   :emphasize-lines: 15,16

   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
   <plist version="1.0">
   <dict>
      <key>name</key>
      <string>Symbol List</string>
      <key>scope</key>
      <string>source.python meta.function.python, source.python meta.class.python</string>
      <key>settings</key>
      <dict>
         <key>showInSymbolList</key>
         <integer>1</integer>
         <key>symbolTransformation</key>
         <string>
         s/class\s+([A-Za-z_][A-Za-z0-9_]*.+?\)?)(\:|$)/$1/g;
         s/def\s+([A-Za-z_][A-Za-z0-9_]*\()(?:(.{0,40}?\))|((.{40}).+?\)))(\:)/$1(?2:$2)(?3:$4…\))/g;
         </string>
      </dict>
   </dict>
   </plist>


Structure of a Symbol Definition File
=====================================

All metadata files share the same top-level structure,
which is inherited from the Property List format.


   .. code-block:: xml

      <?xml version="1.0" encoding="UTF-8"?>
      <!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
      <plist version="1.0">
      <dict>
         ...
      </dict>
      </plist>


``name``
   Optional.
   Name of the symbol definition.
   This value is ignored by Sublime Text.

.. XXX: Pretty useless, I believe.

   .. code-block:: xml

         <key>name</key>
         <string>Some arbitrary name goes here</string>

``scope``
   Comma separated list of scope names
   that Sublime Text will use
   to capture symbols in files.

   .. code-block:: xml

         <key>scope</key>
         <string>source.python meta.function.python, source.python meta.class.python</string>

``settings``
   This section contains required and optional settings.

   .. code-block:: xml

      <key>settings</key>
      <dict>
         ...
      </dict>


.. _md-symbols-settings:

``settings`` Subelements
========================

``showInSymbolList``
   Optional.

   ``0`` or ``1`` (unlike other settings).
   If ``0``,
   the corresponding symbols will be hidden instead of indexed.


   .. code-block:: xml

      <key>settings</key>
      <dict>
         <key>showInSymbolList</key>
         <integer>1</integer>
      </dict>

``showInIndexedSymbolList``
   Optional.
   Links symbols to the project symbol list.

   ``0`` or ``1`` integer (unlike other settings).
   If ``0``,
   the corresponding symbols will be hidden instead of indexed.

   .. code-block:: xml

      <key>settings</key>
      <dict>
         <key>showInIndexedSymbolList</key>
         <integer>1</integer>
      </dict>

``symbolTransformation``
   Optional.
   Semicolon-separated list of text substitutions
   expressed as regular expressions.
   The regular expressions engine used in `Oniguruma`_.

   .. code-block:: xml

      <key>settings</key>
      <dict>
         ...
         <key>symbolTransformation</key>
         <string>
         s/class\s+([A-Za-z_][A-Za-z0-9_]*.+?\)?)(\:|$)/$1/g;
         s/def\s+([A-Za-z_][A-Za-z0-9_]*\()(?:(.{0,40}?\))|((.{40}).+?\)))(\:)/$1(?2:$2)(?3:$4…\))/g;
         </string>
      </dict>

``symbolIndexTransformation``
   Optional.
   Similar to ``symbolTransformation``
   but modifies the project symbol list.


.. _Oniguruma: http://www.geocities.jp/kosako3/oniguruma/

.. TODO: Are there more settings/options?


Navigating Symbols
==================

Once symbols are defined,
you can navigate them
using standard key bindings:

- :kbd:`F12` (go to definition),
- :kbd:`Ctrl+R` (show symbols in file) and
- :kbd:`Ctrl+Shift+R` (show symbols in project).

.. seealso::

   :ref:`Goto Anything <fm-goto-symbol>`
      Browsing Symbols using the Goto Anything panel.
