==============
Metadata Files
==============


Overview
========

Metadata are parameters
that can be assigned to certain text sections
using scope selectors.

.. XXX ref scope selectors

These paremeters can be used for many purposes;
for example:

- specifying the current comment markers,
  even within embedded source code,
  so that you can toggle comments in any syntax,
- defining rules for auto-indentation,
- marking symbols that Sublime Text will allow you to
  :ref:`browse to quickly <fm-goto-symbol>`.

.. Link to the separate comment and symbol sections from here

Furthermore, snippets can access metadata
declared in the ``shellVariables`` setting,
which allows you to create a snippet
that has different contents
depending on where it's used.


File Format
===========

Metadata files have the ``.tmPreferences`` extension and use the
Property List format. The file name can be arbitrary.

Metadata files are inherited from TextMate.

Here's an example of a metadata file:

.. code-block:: xml

   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
   <plist version="1.0">
   <dict>
      <key>name</key>
      <string>JavaScript Metadata</string>
      <key>scope</key>
      <string>source.js</string>
      <key>settings</key>
      <dict>
         <key>decreaseIndentPattern</key>
         <string>^(.*\*/)?\s*\}.*$</string>
         <key>increaseIndentPattern</key>
         <string>^.*\{[^}"']*$</string>

         <key>bracketIndentNextLinePattern</key>
         <string>(?x)
         ^ \s* \b(if|while|else)\b [^;]* $
         | ^ \s* \b(for)\b .* $
         </string>
      </dict>
      <dict>
         <key>shellVariables</key>
         <array>
            <dict>
               <key>name</key>
               <string>TM_COMMENT_START</string>
               <key>value</key>
               <string>// </string>
            </dict>
            <dict>
               <key>name</key>
               <string>TM_COMMENT_START_2</string>
               <key>value</key>
               <string>/*</string>
            </dict>
            <dict>
               <key>name</key>
               <string>TM_COMMENT_END_2</string>
               <key>value</key>
               <string>*/</string>
            </dict>
         </array>
      </dict>
      <key>uuid</key>
      <string>BC062860-3346-4D3B-8421-C5543F83D11F</string>
   </dict>
   </plist>


Structure of a Metadata File
============================

All metadata files share the same top-level structure,
which is inherited from the Property List format.

.. code-block:: xml

   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
   <plist version="1.0">
   <dict>
      ...
   </dict>
   </plist>

The following top-level keys are used in a metadata file;
all others are ignored.

``name``
   Optional.
   Name of the metadata.

   This value is ignored by Sublime Text.

   .. code-block:: xml

      <key>name</key>
      <string>Shell Variables</string>

``scope``
   Required.
   Scope selector to determine
   in which context the metadata should be active.

   .. XXX: refer to scopes here

   .. code-block:: xml

      <key>scope</key>
      <string>source.python</string>

``settings``
   Required.
   Container for other elements.

   .. code-block:: xml

      <key>settings</key>
      <dict>
         ...
      </dict>

``uuid``
   Optional.
   A unique identifier for this file.

   This value is ignored by Sublime Text.

   .. code-block:: xml

      <key>uuid</key>
      <string>BC062860-3346-4D3B-8421-C5543F83D11F</string>


Subelements of ``settings``
===========================

The ``settings`` element can contain
subelements for different purposes,
which will be grouped in the following sections.

Some have certain functionality associated with them,
while others can only be accessed via the :ref:`API <md-api>`.


Indentation Options (Children of ``settings``)
----------------------------------------------

Indentation options control aspects of the auto-indentation mechanism.

``increaseIndentPattern``
   Regex.
   If it matches on the current line,
   the next line will be indented one level further.

   .. code-block:: xml

      <key>increaseIndentPattern</key>
      <string>insert regex here</string>

``decreaseIndentPattern``
   Regex.
   If it matches on the current line,
   the next line will be unindented one level.

   .. code-block:: xml

      <key>decreaseIndentPattern</key>
      <string>insert regex here</string>

``bracketIndentNextLinePattern``
   Regex.
   If it matches on the current line,
   only the next line will be indented one level further.

   .. code-block:: xml

      <key>bracketIndentNextLinePattern</key>
      <string>insert regex here</string>

``disableIndentNextLinePattern``
   Regex.
   If it matches on the current line,
   the next line will not be indented further.

   .. code-block:: xml

      <key>disableIndentNextLinePattern</key>
      <string>insert regex here</string>

``unIndentedLinePattern``
   Regex.
   The auto-indenter will ignore
   lines matching this regex
   when computing the next line's indentation level.

   .. code-block:: xml

      <key>unIndentedLinePattern</key>
      <string>insert regex here</string>


Completions Options (Child of ``settings``)
-------------------------------------------

Completion options control aspects of the completions mechanism.

``cancelCompletion``
   Regex.
   If it matches on the current line,
   supresses the autocomplete popup.

   .. code-block:: xml

      <key>cancelCompletion</key>
      <string>insert regex here</string>


Symbol Definitions (Child of ``settings``)
------------------------------------------

Documentation for symbol definitions
was moved to a separate page:
:ref:`Symbol Definition settings <md-symbols-settings>`.


.. _md-shell-variables:

Shell Variables (Child of ``settings``)
---------------------------------------

Shell variables are used for different purposes
and can be accessed from snippets.

.. XXX: uncomment once reference exists

.. .. seealso::

..   :doc:`snippets`
      Using shell variables in snippets.

Note that shell variables are defined
as dictionaries in an array,
and thus have a different format
from ``settings`` subelements.

``shellVariables``
   Container for "shell variables".

   .. code-block:: xml

      <key>shellVariables</key>
      <array>
         ...
      </array>


``shellVariables`` Subelements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Subelements of ``shellVariables`` are
dictionaries with ``name`` and ``value`` keys.

.. code-block:: xml

   <dict>
      <key>name</key>
      <string>BOOK_OPENING</string>
      <key>value</key>
      <string>Once upon a time...</string>
   </dict>


.. seealso::

   :ref:`Comments <md-comments-shellvariables>`
      Shell variables defining comment markers.


.. _md-api:

Related API Functions
=====================

To extract metadata information from plugin code,
you can use the ``view.meta_info(key, point)``
API call.

.. XXX: add reference to view.meta_info(key, point)
