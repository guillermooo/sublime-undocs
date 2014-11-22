========
Comments
========


Overview
========

Sublime Text has default commands
to comment/uncomment lines of code.
Using comment metadata files,
it's possible to make these commands
work for any type of source code.


File Format
===========

Comment metadata is stored in :file:`.tmPreferences` files
and uses the Property List format.
The file name can be arbitrary.

Because comment metadata is commonly required by packages,
it's discussed in a separate topic,
where it should be easier to find.
But note that comment metadata
is declared simply as ``shellVariables``,
just as other types of metadata.

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
   Optional. Name of the metadata file.
   This value is ignored by Sublime Text.

::

   <key>name</key>
   <string>Miscellaneous</string>

``scope``
   Required. Scope selector to determine
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


``settings`` Subelements
========================

``shellVariables``
   Required. Container for other elements.

::

   <key>shellVariables</key>
   <array>
   ...
   </array>


``shellVariables`` Subelements
==============================

**Note:** As explained in :ref:`md-shell-variables-section`,
``shellVariables`` may contain more elements,
but here we're only interested
in those related to comments.

``TM_COMMENT_START``
   Child of ``shellVariables``.
   Defines a default comment marker.
   To add a secondary comment marker,
   (usually, for block comments)
   use the name ``TM_COMMENT_START_2``.

::

   <dict>
      <key>name</key>
      <string>TM_COMMENT_START</string>
      <key>value</key>
      <string># </string>
   </dict>

``TM_COMMENT_END``
   Optional. Child of ``shellVariables``.
   Defines an end marker for a comment block.
   To add more types of comment end markers,
   use a name like ``TM_COMMENT_END_2``.

::

   <dict>
      <key>name</key>
      <string>TM_COMMENT_END</string>
      <key>value</key>
      <string>*/</string>
   </dict>


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
