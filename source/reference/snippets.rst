.. sublime: wordWrap false

Snippets
========

Compatibility with Textmate
***************************

Generally, Sublime Text snippets are compatible with Textmate snippets.

File Format
***********

Snippet files are XML files with the ``sublime-snippet`` extension.

.. code-block:: xml

    <snippet>
        <content><![CDATA[]]></content>
        <tabTrigger></tabTrigger>
        <scope></scope>
        <description></description>
    </snippet>

``content``
    Actual snippet content.

``tabTrigger``
    Implicit key binding for this snippet. The last key (implicit) is ``TAB``.

``scope``
    Scope selector to activate this snippet.

``description``
    Friendly description to be used when the snippet is shown as a menu item.

Escape Sequences
****************

``\$``
    Literal ``$``.

Environment Variables
*********************

======================      =====================================================================
``$PARAM1 .. $PARAMn``      Arguments passed to the ``insertSnippet`` command.
``$SELECTION``              The text that was selected when the snippet was triggered.
``$TM_CURRENT_LINE``        Content of the line the cursor was in when the snippet was triggered.
``$TM_CURRENT_WORD``        Current word under the cursor when the snippet was triggered.
``$TM_FILENAME``            Filename of the file being edited including extension.
``$TM_FILEPATH``            Path to the file being edited.
``$TM_FULLNAME``            User's user name.
``$TM_LINE_INDEX``          Column where the snippet is being inserted, 0 based.
``$TM_LINE_NUMBER``         Row where the snippet is being inserted, 1 based.
``$TM_SELECTED_TEXT``       An alias for ``$SELECTION``.
``$TM_SOFT_TABS``           ``YES`` if ``translateTabsToSpaces`` is true, otherwise ``NO``.
``$TM_TAB_SIZE``            Spaces per-tab (controlled by the ``tabSize`` option).
======================      =====================================================================

Fields
******

Marked positions to cycle through, by pressing ``TAB`` or ``SHIFT + TAB``.

Syntax: ``$1`` .. ``$n``

``$0``
    Exit mark. The position where normal text editing should be resumed. By default,
    Sublime Text implicitly sets this mark at the end of the snippet's ``content`` element.

Fields with the same name mirror each other.

Placeholders
*************

Fields with a default value.

Syntax: ``${1:PLACE_HOLDER}`` .. ``${n:PLACE_HOLDER}``

Fields and placeholders can be combined, and nested within other placeholders.

Substitutions
**************

Syntax:

    - ``${var_name/regex/format_string/}``
    - ``${var_name/regex/format_string/options}``

``var_name``
    The name of the field to base the substitution on: 1, 2, 3...
``regex``
    Perl-style regular expression: See the Boost library documentation for more on
    `regular expressions <http://www.boost.org/doc/libs/1_44_0/libs/regex/doc/html/boost_regex/syntax/perl_syntax.html>`_.
``format_string``
    See the Boost library documentation for more on
    `format strings <http://www.boost.org/doc/libs/1_44_0/libs/regex/doc/html/boost_regex/format/perl_format.html>`_.
``options``
    Optional. Any of the following:
        ``i``
            Case-insensitive ``regex``.
        ``g``
            Replace all occurrences of ``regex``.
        ``m``
            Don't ignore newlines in the string.
