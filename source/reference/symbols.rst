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

The symbol navigation framework in Sublime Text
is strictly text-based.
No lexical or syntactical analysis is performed.


Format
======

Symbols are defined  using metadata files.
Because symbol definition files
are commonly required by packages,
they are discussed separately in this page
for convenience.

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

Sublime Text features two types of symbol list:
a local symbol list (active file)
and a global symbol list (project-wide).
Using symbol definition files,
you can target both individually.

Symbol definition files use scope selectors
to capture symbols in source code files.

Several symbol definition files can coexist
in the same package.
For example, two symbol definition files
could work in tandem:
one would define all symbols,
and a second one
could selectively hide some of them
if they were uninteresting for users.

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
Symbol transformations consist of text substitutions
defined as regular expressions
using the `Oniguruma`_ syntax.

This is an example of a text substitution:

::

   s/class\s+([A-Za-z_][A-Za-z0-9_]*.+?\)?)(\:|$)/$1/g;

In this case, a captured symbol such as ``class FooBar(object)``
would show up as ``FooBar(object)``
in the symbol list.

Let's expand our previous example
to use a symbol transformation:

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

These are all the valid elements in a symbol definition file:

``name``
   Optional.
   Name of the symbol definition.
   Ignored by Sublime Text.

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
   A container for settings.

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
   Links symbols to the local symbol list.
   Valid values are ``0`` or ``1``.
   If ``0``,
   the corresponding symbols
   will not be displayed.

   .. code-block:: xml

      <key>showInSymbolList</key>
      <integer>1</integer>

``showInIndexedSymbolList``
   Optional.
   Links symbols to the global symbol list.
   Valid values are ``0`` or ``1``.
   If ``0``,
   the corresponding symbols
   will not be displayed.

   .. code-block:: xml

      <key>showInIndexedSymbolList</key>
      <integer>1</integer>

``symbolTransformation``
   Optional.
   Targets the local symbol list.
   Semicolon-separated list of text substitutions
   expressed as regular expressions
   using the `Oniguruma`_ syntax.
   Whitespace between substitution instructions
   is ignored.

   .. code-block:: xml

      <key>symbolTransformation</key>
      <string>
         s/class\s+([A-Za-z_][A-Za-z0-9_]*.+?\)?)(\:|$)/$1/g;
         s/def\s+([A-Za-z_][A-Za-z0-9_]*\()(?:(.{0,40}?\))|((.{40}).+?\)))(\:)/$1(?2:$2)(?3:$4…\))/g;
      </string>

``symbolIndexTransformation``
   Optional.
   Targets the global symbol list.
   Semicolon-separated list of text substitutions
   expressed as regular expressions
   using the `Oniguruma`_ syntax.
   Whitespace between substitution instructions
   is ignored.

   .. code-block:: xml

      <key>symbolIndexTransformation</key>
      <string>
         s/class\s+([A-Za-z_][A-Za-z0-9_]*.+?\)?)(\:|$)/$1/g;
         s/def\s+([A-Za-z_][A-Za-z0-9_]*\()(?:(.{0,40}?\))|((.{40}).+?\)))(\:)/$1(?2:$2)(?3:$4…\))/g;
      </string>

.. _Oniguruma: http://www.geocities.jp/kosako3/oniguruma/

.. TODO: Are there more settings/options?


Navigating Symbols
==================

Once symbols are defined,
you can navigate them
using standard key bindings:

===================  ========================
:kbd:`F12`           Go to definition
:kbd:`Ctrl+R`        Show local symbol list
:kbd:`Ctrl+Shift+R`  Show global symbol list
===================  ========================

.. seealso::

   :ref:`Goto Anything <fm-goto-symbol>`
      Browsing symbols using Goto Anything.
