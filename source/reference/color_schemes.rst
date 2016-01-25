=============
Color Schemes
=============

.. contents::
   :local:
   :depth: 2

Overview
========

Color schemes define the colors
used to highlight source code in Sublime Text views
and to style different elements
found in the editing area:
background, foreground, selection, caret...


File Format
===========

Color scheme files use the Property List format
and have the .tmTheme extension.

The file format of color scheme files
is inherited from Textmate.

.. note::

   Sublime Text uses the .tmTheme extension for color scheme files
   to maintain compatibility with Textmate.
   Rather confusingly, Sublime Text also has a notion
   of a user interface (UI) theme.
   A UI theme is a set of styles and decorations
   to alter the look of the editor’s UI.
   It’s important to remember
   that UI themes and color schemes
   are two different customization mechanisms.
   Generally speaking, it is far less complex
   to create a new color scheme
   than it is to create a new UI theme.


Where to Store Color Schemes
============================

You can keep color scheme files anywhere under Packages
(even inside directories nested multiple levels deep).

By convention, directories containing
a set of color scheme files
have the *Color Scheme -* prefix.
For example: *Color Scheme - Default*.

The file names of all available color schemes
are displayed in the **Preferences → Color Scheme** menu.


Selecting a Color Scheme
************************

You can change the current color scheme
by means of the **Preferences → Color Scheme** menu.

A common way of selecting a color scheme
is by associating it to a type of file
using the file-type-specific settings.
For example, for the Python file type (``syntax_file`` == :file:`Python.tmLanguage`),
we'd use the :file:`Python.sublime-settings` file
and, within, set ``color_scheme`` to some color scheme file.

For more information about settings, see :doc:`settings`.


Structure of a Color Scheme File
================================

Color scheme files are based
on the Property List format.
All color scheme files share
the same topmost structure.

Colors can be expressed in the
following formats: ``#RRGGBB``, ``#RGB``.

Most elements controlling colors
accept an alpha channel value:
``#RRGGBBAA``.

.. contents:: Contents
   :local:

Topmost Elements in Color Schemes Files
*****************************************

.. code-block:: xml

   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
   <plist version="1.0">
   <dict>
      <key>name</key>
      <string>Monokai</string>
      <key>settings</key>
      <array>
      ... INSERT AWESOME COLORS HERE ...
      </array>
      <key>uuid</key>
      <string>D8D5E82E-3D5B-46B5-B38E-8C841C21347D</string>
   </dict>
   </plist>

``name``
   Optional.
   Name of the color scheme.
   Ignored by Sublime Text.

``uuid``
   Optional.
   A unique identifier for the file.
   Ignored by Sublime Text.


Subelements of Settings
***********************

Sublime Text supports
the following color scheme settings:


Global Settings
---------------

Not associated with any scope.
These settings affect global visual items
in the editing area.

Global settings go inside a ``<dict>`` element
within the topmost ``<array>``.

.. code-block:: xml

   <array>
      <dict>
         <key>settings</key>
         <dict>
            <key>background</key>
            <string>#272822</string>
            <key>caret</key>
            <string>#F8F8F0</string>
            ...
         </dict>
      </dict>
   ...
   </array>


Global Settings Ordered by Type
-------------------------------


General
^^^^^^^

``foreground``
   Foreground color for the view.

``background``
   Backgound color of the view.

``invisibles``
  Ignored.

``caret``
   Color of the caret.

``lineHighlight``
   Color of the line the caret is in.
   Only used when the ``higlight_line`` setting is set to ``true``.


Brackets
^^^^^^^^

``bracketContentsForeground``
   Color of bracketed sections of text
   when the caret is in a bracketed section.
   Only applied when the ``match_brackets`` setting
   is set to `true`.

``bracketContentsOptions``
   Controls certain options
   when the caret is in a bracket section.
   Only applied when the ``match_brackets`` setting
   is set to ``true``.

   Options: ``underline``, ``stippled_underline``, ``squiggly_underline``.
   The `underline` option indicates
   that the text should be drawn
   using the given color, not just the underline.

``bracketsForeground``
   Foreground color of the brackets
   when the caret is next to a bracket.
   Only applied when the ``match_brackets`` setting
   is set to ``true``.

``bracketsForeground``
   Background color of the brackets
   when the caret is next to a bracket.
   Only applied when the ``match_brackets`` setting
   is set to ``true``.

``bracketsOptions``
   Controls certain options
   when the caret is next to a bracket.
   Only applied when the ``match_brackets`` setting
   is set to ``true``.

   Options: ``underline``, ``stippled_underline``, ``squiggly_underline``.
   ``underline`` indicates the text should be drawn
   using the given color, not just the underline.


Tags
^^^^

``tagsForeground``
   Color of tags when the caret is next to a tag.
   Only used when the ``match_tags`` setting
   is set to ``true``.

``tagsOptions``
   Controls certain options
   when the caret is next to a tag.
   Only applied when the ``match_tags`` setting
   is set to ``true``.

   Options: ``underline``, ``stippled_underline``, ``squiggly_underline``.
   ``underline`` indicates the text should be drawn
   using the given color,
   not just the underline.


Find
^^^^

``findHighlight``
   Background color of regions matching the current search.

``findHighlightForeground``
   Foreground color of regions matching the current search.


Gutter
^^^^^^

``gutter``
   Background color of the gutter.

``gutterForeground``
   Foreground color of the gutter.


Selection
^^^^^^^^^

``selection``
   Color of the selection regions.

``selectionBackground``
   Background color of the selection regions.

``selectionBorder``
   Color of the selection regions’ border.

``inactiveSelection``
   Color of inactive selections (inactive view).


Guides
^^^^^^

``guide``
   Color of the guides displayed to indicate nesting levels.

``activeGuide``
   Color of the guide lined up with the caret.
   Only applied if the ``indent_guide_options`` setting
   is set to ``draw_active``.

``stackGuide``
   Color of the current guide's parent guide level.

   Only used if the ``indent_guide_options`` setting
   is set to ``draw_active``.


Highlighted Regions
^^^^^^^^^^^^^^^^^^^

``highlight``
   Background color for regions added via ``sublime.add_regions()``
   with the ``sublime.DRAW_OUTLINED`` flag added.

``highlightForeground``
   Foreground color for regions added via ``sublime.add_regions()``
   with the ``sublime.DRAW_OUTLINED`` flag added.


Shadow
^^^^^^

``shadow``
   Color of the shadow effect when the buffer is scrolled.

``shadowWidth``
   Width ot the shadow effect when the buffer is scrolled.


Scoped Settings
---------------

Settings associated with a particular scope.

.. code-block:: xml

   <array>
      ...
      <dict>
         <key>name</key>
         <string>Comment</string>
         <key>scope</key>
         <string>comment</string>
         <key>settings</key>
         <dict>
            <key>foreground</key>
            <string>#75715E</string>
         </dict>
      </dict>
      ...
   </array>


``name``
   Descriptive name of the item.

``scope``
   Target scope name.

``settings``
   Container for settings.

   Valid settings are:

``fontStyle``
   Style of the font.

   Options: ``bold``, ``italic``.

``foreground``
   Foreground color.

``background``
   Background color.


Sublime Text Settings Related to Color Schemes
==============================================

View Settings
*************

``color_scheme``
   Path to a color scheme file
   relative to the Data folder
   (example: :file:`Packages/Color Scheme - Default/Monokai.tmTheme`).
