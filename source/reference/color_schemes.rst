=============
Color Schemes
=============


Overview
========

Color schemes define the colors
used to highlight source code in Sublime Text views
and the colors use for different elements
found in the editing area:
background, foreground, selection, caret, etc.


File Format
===========

Color scheme files use the Property List format
and have the .tmTheme extension.
The file names of color scheme files
are displayed in the **Preferences → Color Scheme** menu.

The file format of color schemes
is inherited from Textmate.

.. note::

   Sublime Text uses the .tmTheme extension for color scheme files
   to maintain compatibility with Textmate.
   Confusingly, Sublime Text also has a notion
   of a user interface (UI) theme.
   A UI theme is a set of styles and decorations
   to alter the look of the editor’s UI.
   It’s important to remember
   that UI themes and color schemes
   are two different customization mechanisms.
   Generally speaking, it is far less complex
   to create a new color scheme
   than to create a new UI theme.


Where to Store Color Schemes
============================

You can keep color scheme files anywhere under Packages
(even inside directories nested multiple levels deep).
Most frequently, you will find color schemes
inside their own directory.

By convention, directories containing color scheme files
have the *Color Scheme -*  prefix.
For example: *Color Scheme - Default*.


Selecting a Color Scheme
************************

You can change the current color scheme
by means of the **Preferences → Color Scheme** menu.
Using settings files or plugins,
you can create advanced color scheme selection mechanisms
to change the color scheme
depending on the file type, time of day, etc.


Structure of a Color Scheme File
================================

Color scheme files are based
on the Property List format.
All color scheme files share
the same top-level structure.

.. insert top-level example here

``name``
   Optional.
   Name of the color scheme.
   Ignored by Sublime Text.

``settings``
   Array of dict elements.
   See :ref:`Subelements of Settings` for more information.

``uuid``
   Optional.
   A unique identifier for the file. Ignored by Sublime Text.


Subelements of Settings
***********************

Sublime Text supports
the following color scheme settings:


Global Settings
---------------

Not associated with any scope.
These settings affect global visual items in the editing area.

``activeGuide``
   Color of the guide lined up with the caret.
   Only used if the ``indent_guide_options`` setting
   is set to ``draw_active``.

``background``
   Backgound color of the view.

``bracketContentsForeground``
   Color of bracketed sections of text
   when the caret is in a bracket section.
   Only used when the ``match_brackets`` setting
   is set to `true`.

``bracketContentsOptions``
   XXX when the caret is in a bracket section.
   Only used when the ``match_brackets`` setting
   is set to ``true``.

   Options: ``underline``, ``stippled_underline``, ``squiggly_underline``.
   `underline` indicates the text should be drawn
   using the given color, not just the underline.

``bracketsForeground``
   Foreground color of the brackets
   when the caret is next to a bracket.
   Only used when the ``match_brackets`` setting
   is set to ``true``.

``bracketsForeground``
   Background color of the brackets
   when the caret is next to a bracket.
   Only used when the ``match_brackets`` setting
   is set to ``true``.

``bracketsOptions``
   XXX

   Options: ``underline``, ``stippled_underline``, ``squiggly_underline``.
   ``underline`` indicates the text should be drawn
   using the given color, not just the underline.

``caret``
   Color of the caret.

``findHighlight``
   Background color of regions matching the current search.

``findHighlightForeground``
   Background color of regions matching the current search.

``foreground``
   Foreground color for the view.

``guide``
   Color of the guides displayed to mark nesting levels.

``gutter``
   Background color of the gutter.

``gutterForeground``
   Foreground color of the gutter.

``inactiveSelection``
   Color of inactive selections (inactive view).

``invisibles``
  Ignored by Sublime Text.

``lineHihglight``
   Color of the line the caret is in.
   Only used when the ``higlight_line`` setting is set to ``true``.

``selection``
   Color of the selection regions.

``selectionBackground``
   Background color of the selection regions.

``selectionBorder``
   Color of the selection regions’ border.

``shadow``
   Color of the shadow effect when the buffer is scrolled.

``shadowWidth``
   Width ot the shadow effect when the buffer is scrolled.

``stackGuide``
   XXX
   Only used if the ``indent_guide_options`` setting
   is set to ``draw_active``.

``tagsForeground``
   Color of tags when the caret is next to a tag.
   Only used when the ``match_brackets`` setting
   is set to ``true``.

``tagsOptions``
   XXX when the caret is next to a tag.
   Only used when the ``match_brackets`` setting
   is set to ``true``.

   Options: ``underline``, ``stippled_underline``, ``squiggly_underline``.
   ``underline`` indicates the text should be drawn
   using the given color,
   not just the underline.

``highlight``
   Background color for reggions added via ``sublime.add_regions()``
   with the ``sublime.DRAW_OUTLINED`` flag added.

``highlightForeground``
   Foreground color for reggions added via ``sublime.add_regions()``
   with the ``sublime.DRAW_OUTLINED`` flag added.


Scoped Settings
---------------

Associated with a particular scope.


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

``color_scheme``
   Path to a color scheme file
   relative to the Data folder
   (example: Packages/User/Color Schemes - Custom/Fictitious.tmTheme).
