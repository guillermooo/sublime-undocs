==============
Metadata Files
==============


Overview
========

Metadata files can be used to control several aspects of Sublime Text.

Here's an example of an advanced metadata file:

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


File Format
===========

Metadata files have the :file:`.tmPreferences` extension and use the
Property List format. The file name can be arbitrary.


Structure of a Metadata File
============================

All metadata files share the same top-level structure.

.. code-block:: xml

   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
   <plist version="1.0">
   <dict>
      ...
   </dict>
   </plist>

These are all valid elements
in a metadata file:

``name``
   Optional. Name of the metadata.
   This value is ignored by Sublime Text.

::

   <key>name</key>
   <string>Shell Variables</string>

``scope``
   Optional. Scope selector to determine
   in which context the metadata should be active.

::

   <key>scope</key>
   <string>source.python</string>

``settings``
   Required. Container for other elements.

::

   <key>settings</key>
   <dict>
   ...
   </dict>


Subelements of ``settings``
===========================

The ``settings`` element can contain
multiple types of subelements for different purposes.


.. _md-shell-variables-section:


Shell Variables (Child of ``settings``)
---------------------------------------

Metadata defining variables available in snippets.

``shellVariables``
   Required. Container for other elements.

::

   <key>shellVariables</key>
   <array>
   </array>


``shellVariables`` Subelements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

These are all valid elements
to define variables.


``SOME_VARIABLE_NAME``
   Child of ``shellVariables``.
   Arbitrary name.

::

   <dict>
      <key>name</key>
      <string>BOOK_OPENING</string>
      <key>value</key>
      <string>Once upon a time...</string>
   </dict>


Indentation Options (Children of ``settings``)
----------------------------------------------

Indentation options control aspects of  the auto indentation mechanism.

``increaseIndentPattern``
   Regex. If it matches on the current line,
   the next line will be indented one level further.

::

      <key>increaseIndentPattern</key>
      <string>insert regex here</string>

``decreaseIndentPattern``
   Regex. If it matches on the current line,
   the next line will be unindented one level.

::

      <key>decreaseIndentPattern</key>
      <string>insert regex here</string>

``bracketIndentNextLinePattern``
   Regex. If it matches on the current line,
   only the next line will be indented one level further.

::

      <key>bracketIndentNextLinePattern</key>
      <string>insert regex here</string>

``disableIndentNextLinePattern``
   Regex. If it matches on the current line,
   the next line will not be indented further.

::

      <key>disableIndentNextLinePattern</key>
      <string>insert regex here</string>

``unIndentedLinePattern``
   Regex. The autoindenter will ignore
   lines matching this regex
   when computing the next line's indentation level.

::

      <key>unIndentedLinePattern</key>
      <string>insert regex here</string>


Completions Options (Child of ``settings``)
-------------------------------------------

Completion options control aspects of the completions mechanism.

``cancelCompletion``
   Regex. If it matches on the current line,
   supresses the autocomplete popup.

::

      <key>cancelCompletion</key>
      <string>regex</string>


Related API Functions
=====================

To extract metadata information from plugin code,
you can use the ``view.meta_info(key, point)``
API call.


.. seealso::

    :doc:`comments`
      Metadata defining comment markers.

    :doc:`symbols`
      Metadata defining indexable symbols