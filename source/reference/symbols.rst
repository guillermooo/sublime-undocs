=======
Symbols
=======


Overview
========

Sublime Text provides basic support
for symbol navigation
(jumping to class and function definitions,
etc.).


Format
======

Symbol definition files have the :file:`.tmPreferences` extension
and use the Property List format.
Their file can be arbitrary.


Defining Symbols
================

Several symbol definition files can coexist
in the same package.
For example, two symbol definition files
could work in tandem:
one would define symbols in general,
and a second one would hide some symbols
that are uninteresting for users.

The symbol navigation framework in Sublime Text
uses scope selectors
to capture symbols in source code files.

Let's see an example:

.. code-block:: xml

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

.. TODO: Is that so (below)?

Note that the ``showInSymbolList`` setting is required.

It is also possible
to apply transformations
to symbols
before they are displayed to the user.
Text transformations are defined
as regular expressions.
The regular expression engine used is `Oniguruma`_.

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


.. _Oniguruma: http://www.geocities.jp/kosako3/oniguruma/


Structure of a Symbol Definition File
=====================================

This is the full list of valid
elements in a symbol definition file.

Symbol files are in the Property List format,
so they share this top-level structure:

::

   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
   <plist version="1.0">
   <dict>
      ...
   </dict>
   </plist>


``name``
   Optional. Name of the symbol definition.
   This value is ignored by Sublime Text.

.. XXX: Pretty useless, I believe.

::

      <key>name</key>
      <string>Some arbitrary name goes here</string>

``scope``
   Comma separated list of scope names
   that Sublime Text will use
   to capture symbols in files.

::

      <key>scope</key>
      <string>source.python meta.function.python, source.python meta.class.python</string>

``settings``
   This section contains required and optional settings.

::

   <key>settings</key>
   <dict>
      ...
   </dict>

Valide elements inside ``settings``:

``showInSymbolList``
   ``0`` or ``1``. If ``0``, the corresponding symbols
   will be hidden instead of indexed.

::

   <key>settings</key>
   <dict>
      <key>showInSymbolList</key>
      <integer>1</integer>
   </dict>

``showInIndexedSymbolList``
   Links symbols to the global symbol list.
   ``0`` or ``1``. If ``0``, the corresponding symbols will be hidden
   instead of indexed.

::

   <key>settings</key>
   <dict>
      <key>showInIndexedSymbolList</key>
      <integer>1</integer>
   </dict>

``symbolTransformation``
   Optional. Semicolon-separated list
   of text substitutions expressed as regular expressions.
   The regular expressions engine used in `Oniguruma`_.

::

   <key>settings</key>
   <dict>
      ...
      <key>symbolTransformation</key>
      <string>
      s/class\s+([A-Za-z_][A-Za-z0-9_]*.+?\)?)(\:|$)/$1/g;
      s/def\s+([A-Za-z_][A-Za-z0-9_]*\()(?:(.{0,40}?\))|((.{40}).+?\)))(\:)/$1(?2:$2)(?3:$4…\))/g;
      </string>
   </dict>

.. TODO: Are there more settings/options?


Navigating Symbols
==================

Once symbols are defined,
you can navigate them
using standard key bindings: **F12** (go to definition),
**Ctrl+R** (show symbols in file),
and **Ctrl+Shift+R**
(show symbols in project).
