=============
Color Schemes
=============


Overview
========

Color schemes define the colors
used to highlight source code in Sublime Text views.


File Format
===========

Color scheme files use the Property List format
and have the .tmTheme extension.
The file names of color scheme files
are displayed in the Preferences --> Color Scheme menu.

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
   Generally speaking, it is much simpler
   to create a new color scheme
   than a new UI theme.


Where to Store Color Schemes
============================

You can keep color scheme files anywhere under Packages
(even inside directories nested multiple levels deep).
Most frequently, you will find color schemes
inside their own directory.

By convention, directories containing color scheme files
have the ‘Color Scheme - ‘- prefix.
For example: Color Scheme - Default.


Selecting a Color Scheme
************************

You can change the current color scheme
by means of the Preferences > Color Scheme menu.
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
   See Subelements of Settings for more information.

``uuid``
   Optional.
   A unique identifier for the file. Ignored by Sublime Text.


Subelements of Settings
***********************

Sublime Text supports
the following color scheme settings:

Global Settings

Not associated with any scope.
These settings affect global visual items in the view.

``activeGuide``
   XXX

``background``
   Backgound color of the view.

``bracketContentsForeground``
   Color of bracketed sections of text.

``bracketContentsOptions``
   XXX

``bracketsForeground``
   Foreground color for brackets.

``bracketsOptions``
   XXX

``caret``
   Color of the caret.

``findHighlight``
   Color of the current search match.

``findHighlightForeground``
   Foreground color of the current search match.

``foreground``
   Foreground color for the view.

``guide``
   XXX

``gutter``
   Background color of the gutter.

``gutterForeground``
   Foreground color of the gutter.

``inactiveSelection``
   Color of inactive selections (inactive view).

``invisibles``
   Color of whitespace characters
   when they are displayed
   (see SETTING_TO_CHANGE_WHITESPACE_VISIBILITY).

   IT DOESN’T SEEM TO DO THIS

``lineHihglight``
   Color of the line the caret is in
   (see SETTING TO ENABLE LINE HILITIN).

``selection``
   Color of the selection regions.

``selectionBackground``
   Background color of the selection regions.

``selectionBorder``
   Color of the selection regions’ border.

``shadow``
   XXX

``shadowWidth``
   XXX

``stackGuide``
   XXX

``tagsForeground``
   Foreground color for tags.

``tagsOptions``
   XXX

``highlight``
   XXX

``highlightForeground``
   XXX

``Scoped Settings``
   Associated with a particular scope.

``name``
   Descriptive name of the item.

``scope``
   Target scope name.

``settings``
   Container for settings.

   Valid settings are:

``fontStyle``
   Style of the font. Any of AAA, BBB, CCC.

``foreground``
   Foreground color.

``background``
   Background color.

   Sublime Text Settings Related to Color Schemes

``color_scheme``
   Path to a color scheme file
   relative to the Data folder
   (example: Packages/User/Color Schemes - Custom/Fictitious.tmTheme).
