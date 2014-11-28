========
Comments
========


Overview
========

Sublime Text has default commands
to comment or uncomment lines of code.
Using **metadata files**,
it's possible to make these commands
work for any type of source code.

Because metadata for comment markers is commonly required by packages,
it's discussed in this separate document,
where it should be easier to find.


.. seealso::

   :doc:`metadata`
      More detailed documentation on metadata.


File Format
===========

Metadata files have the :file:`.tmPreferences` extension and use the
Property List format. The file name can be arbitrary.

Metadata files are inherited from TextMate.

Let's see a basic example:

.. code-block:: xml

   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
   <plist version="1.0">
   <dict>
      <key>name</key>
      <string>Miscellaneous</string>
      <key>scope</key>
      <string>source.python</string>
      <key>settings</key>
      <dict>
         <string></string>
         <key>shellVariables</key>
         <array>
            <dict>
               <key>name</key>
               <string>TM_COMMENT_START</string>
               <key>value</key>
               <string># </string>
            </dict>
         </array>
      </dict>
   </dict>
   </plist>


Structure of a Comment Metadata File
====================================

All comment metadata files
share the same top-level structure:

.. code-block:: xml

   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
   <plist version="1.0">
   <dict>
      ...
   </dict>
   </plist>


Top-level Elements
==================

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

   In most cases you want this to be your syntax's base scope.

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


``settings`` Subelements
========================

``shellVariables``
   Required (for comment markers).
   Container for other elements.

   .. code-block:: xml

      <key>shellVariables</key>
      <array>
         ...
      </array>


.. _md-comments-shellvariables:

``shellVariables`` Subelements
==============================

.. note::

   As explained in :ref:`md-shell-variables`,
   ``shellVariables`` may contain more elements,
   but here we're only interested
   in those related to comments.

``TM_COMMENT_START``
   Defines a default comment marker.

   To add a secondary comment marker,
   (usually, for block comments)
   use the name ``TM_COMMENT_START_2``.


   .. code-block:: xml

      <dict>
         <key>name</key>
         <string>TM_COMMENT_START</string>
         <key>value</key>
         <string># </string>
      </dict>

``TM_COMMENT_END``
   Optional.
   Defines an end marker for a comment block.

   If this is omitted,
   ``TM_COMMENT_START`` will be treated as a line comment marker.

   To add more types of comment end markers,
   use a name like ``TM_COMMENT_END_2``.

   .. code-block:: xml

      <dict>
         <key>name</key>
         <string>TM_COMMENT_END</string>
         <key>value</key>
         <string>*/</string>
      </dict>

``TM_COMMENT_DISABLE_INDENT``
   Optional.
   Disables indentation for the ``TM_COMMENT_START``
   marker.

   For targetting the ``TM_COMMENT_START/END_2`` group,
   use ``TM_COMMENT_START_2``.

   .. code-block:: xml

      <dict>
         <key>name</key>
         <string>TM_COMMENT_END</string>
         <key>value</key>
         <string>*/</string>
      </dict>


Example
=======

Here's a more complete example
using some of the features just discussed:

.. code-block:: xml

   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
   <plist version="1.0">
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


Related Keyboard Shortcuts
==========================

Once comment metadata has been defined,
you can use default Sublime Text key bindings
to comment/uncomment lines of code.

- To toggle a line comment, press :kbd:`Ctrl+/`
- To toggle a block comment, press :kbd:`Ctrl+Shift+/`
