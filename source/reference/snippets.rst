.. sublime: wordWrap false

Snippets
========

Compatibility with Textmate
***************************

Sublime Text snippets are generally compatible with Textmate snippets.

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
    Implicit keybinding for this snippet. Last key (implicit) is ``TAB``.

``scope``
    Scope selector to activate this snippet.

``description``
    User friendly description for menu item.

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
``$TM_FILENAME``            File name of the file being edited including extension.
``$TM_FILEPATH``            File path to the file being edited.
``$TM_FULLNAME``            User's user name.
``$TM_LINE_INDEX``          Column the snippet is being inserted at, 0 based.
``$TM_LINE_NUMBER``         Row the snippet is being inserted at, 1 based.
``$TM_SELECTED_TEXT``       An alias for ``$SELECTION``.
``$TM_SOFT_TABS``           ``YES`` if ``translateTabsToSpaces`` is true, otherwise ``NO``.
``$TM_TAB_SIZE``            Spaces per-tab (controlled by the ``tabSize`` option).
======================      =====================================================================

Fields
******

Mark positions to cycle through by pressing ``TAB`` or ``SHIFT + TAB``.

Syntax: ``$1`` .. ``$n``

``$0``
    Exit mark. Position at which normal text editing should be resumed. By default,
    Sublime Text implicitly sets this mark at the end of the snippet's ``content`` element.

Fields with the same name mirror each other.

Place Holders
*************

Fields with a default value.

Syntax: ``${1:PLACE_HOLDER}`` .. ``${n:PLACE_HOLDER}``

Fields and place holders can be combined and nested within other place holders.

Substitutions
**************

Syntax:

    - ``${var_name/regex/format_string/}``
    - ``${var_name/regex/format_string/options}``

``var_name``
    The field's name to base the substitution on: 1, 2, 3…
``regex``
    Perl-style regular expression: See the Boost library documentation for `regular expressions <http://www.boost.org/doc/libs/1_44_0/libs/regex/doc/html/boost_regex/syntax/perl_syntax.html>`_.
``format_string``
    See the Boost library documentation for `format strings <http://www.boost.org/doc/libs/1_44_0/libs/regex/doc/html/boost_regex/format/perl_format.html>`_.
``options``
    Optional. Any of the following:
        ``i``
            Case-insensitive regex.
        ``g``
            Replace all occurrences of ``regex``.
        ``m``
            Don't ignore newlines in the string.
