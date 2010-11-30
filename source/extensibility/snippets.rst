Snippets
========

Whether you are coding or writing the next vampire best-seller, you're likely to
need certain short fragments of text again and again. Use snippets to save yourself
tedious typing. Snippets are smart templates that will insert text for you and
adapt it to their context.

To create a new snippet, select **Tools | New Snippet**. Sublime Text will
present you with an skeleton for a new snippet.

Snippets can be stored under any package's folder, but to keep it simple while
you're learning, you can save them to your ``Packages\User`` folder. For now,
think of packages as folders. That's what they are, after all.

Snippets File Format
********************

Snippets typically live in a Sublime Text package. They are simplified XML files
with the extension ``sublime-snippet``. For instance, you could have a
``greeting.sublime-snippet`` inside an ``Email`` package.

The structure of a typical snippet is as follows (including the default hints
Sublime Text inserts for your convenience):

.. code-block:: xml

    <snippet>
        <content><![CDATA[Type your snippet here]]></content>
        <!-- Optional: Tab trigger to activate the snippet -->
        <tabTrigger>xyzzy</tabTrigger>
        <!-- Optional: Scope the tab trigger will be active in -->
        <scope>source.python</scope>
        <!-- Optional: Description to show in the menu -->
        <description>My Fancy Snippet</description>
    </snippet>

The ``snippet`` element contains all the information Sublime Text needs in order
to know *what* to insert, *whether* to insert it and *when*. Let's see all of
these parts in turn.

**content**
    The actual snippet. Snippets can range from simple to fairly complex
    templates. We'll look at examples of both later.

    Keep the following in mind when writing your own snippets:

        - If you want the get a literal ``$``, you have to escape it like this: ``\$``.

        - When writing a snippet that contains indentation, always use tabs. The
          tabs will be transformed into spaces when the snippet is inserted if the
          option ``translateTabsToSpaces`` is set to ``true``.

    .. note::
        The **content** must be included in a ``<![CDATA[…]]>`` section.
        Snippets won't work if you don't do this!

**tabTrigger**
    Defines the sequence of keys you will press to insert this snippet. The
    snippet will kick in as soon as you hit the ``tab`` key after typing this
    sequence.

    A tab trigger is an implicit key binding.

.. XXX Link to commands
    .. note::
        There are other ways to cause Sublime Text to insert snippets via
        commands.

**scope**
    Scope selector determining the context where the snippet will be active.
    See `Scope and Scope Selectors` for more information.

.. XXX Link to section mentioned.

**description**
    Used when showing the snippet in the Snippets menu. If not present, Sublime Text
    defaults to the name of the snippet.

With this information, you can start writing your own snippets as described in
the next sections.

.. note::
    In the interest of brevity, we're only including the ``content``
    element's text in examples unless stated otherwise.

Snippet Resources
*****************

Environment Variables
---------------------

Snippets have access to contextual information in the form of environment variables.
Sublime Text sets the values of the variables listed below automatically.

You can also add your own variables to provide extra information. These custom
variables are defined in ``sublime-options`` files.

======================    ====================================================================================
**$PARAM1, $PARAM2 …**      Arguments passed to the ``insertSnippet`` command. (Not covered here.)
**$SELECTION**             The text that was selected when the snippet was triggered.
**$TM_CURRENT_LINE**       Content of the line the cursor was in when the snippet was triggered.
**$TM_CURRENT_WORD**       Current word under the cursor when the snippet was triggered.
**$TM_FILENAME**           File name of the file being edited including extension.
**$TM_FILEPATH**           File path to the file being edited.
**$TM_FULLNAME**           User's user name.
**$TM_LINE_INDEX**         Column the snippet is being inserted at, 0 based.
**$TM_LINE_NUMBER**        Row the snippet is being inserted at, 1 based.
**$TM_SELECTED_TEXT**      An alias for **$SELECTION**.
**$TM_SOFT_TABS**          ``YES`` if ``translateTabsToSpaces`` is true, otherwise ``NO``.
**$TM_TAB_SIZE**           Spaces per-tab (controlled by the ``tabSize`` option).
======================    ====================================================================================

Let's see a simple example of a snippet using variables::

    ====================================
    USER NAME:          $TM_FULLNAME
    FILE NAME:          $TM_FILENAME
     TAB SIZE:          $TM_TAB_SIZE
    SOFT TABS:          $TM_SOFT_TABS
    ====================================

    # Output:
    ====================================
    USER NAME:          guillermo
    FILE NAME:          test.txt
     TAB SIZE:          4
    SOFT TABS:          YES
    ====================================


Fields
------

With the help of field markers, you can cycle through positions within the
snippet by pressing the ``TAB`` key. Fields are used to walk you through the
customization of a snippet once it's been inserted.

::

    First Name: $1
    Second Name: $2
    Address: $3

In the example above, the cursor will jump to ``$1`` if you press ``TAB`` once.
If you press ``TAB`` a second time, it will advance to ``$2``, etc. You can also
move backwards in the series with ``SHIFT + TAB``. If you press ``TAB`` after the
highest tab stop, Sublime Text will place the cursor at the end of the snippet's
content so that you can resume normal editing.

If you want to control where the exit point should be, use the ``$0`` mark.

You can break out of the field cycle any time by pressing ``ESC``.

Mirrored Fields
---------------

Identical field markers mirror each other: when you edit the first one, the rest
will be populated with the same value in real time.

::

    First Name: $1
    Second Name: $2
    Address: $3
    User name: $1

In this example, "User name" will be filled out with the same value as "First Name".

Place Holders
-------------

By expanding the field syntax a little bit, you can define default values for
a field. Place holders are useful when there's a general case for your snippet
but you still want to keep its customization convenient.

::

    First Name: ${1:Guillermo}
    Second Name: ${2:López}
    Address: ${3:Main Street 1234}
    User name: $1

Variables can be used as place holders:

::

    First Name: ${1:Guillermo}
    Second Name: ${2:López}
    Address: ${3:Main Street 1234}
    User name: ${4:$TM_FULLNAME}

And you can nest place holders within other place holders too:

::

    Test: ${1:Nested ${2:Placeholder}}

Substitutions
-------------

.. WARNING::
    This section is a draft and may contain inaccurate information.

In addition to the place holder syntax, tab stops can specify more complex operations
with substitutions. Use substitutions to dynamically generate text based on a mirrored
tab stop.

The substitution syntax has the following syntaxes:

    - ``${var_name/regex/format_string/}``
    - ``${var_name/regex/format_string/options}``

**var_name**
    The variable name: 1, 2, 3...

**regex**
    Perl-style regular expression: See the `Boost library reference for regular expressions <http://www.boost.org/doc/libs/1_44_0/libs/regex/doc/html/boost_regex/syntax/perl_syntax.html>`_.

**format_string**
    See the `Boost library reference for format strings <http://www.boost.org/doc/libs/1_44_0/libs/regex/doc/html/boost_regex/format/perl_format.html>`_.

**options**
    Optional. May be any of the following:
        **i**
            Case-insensitive regex.
        **g**
            Replace all occurrences of ``regex``.
        **m**
            Don't ignore newlines in the string.

With substitutions you can, for instance, underline text effortlessly:

::

          Original: ${1:Hey, Joe!}
    Transformation: ${1/./=/g}

    # Output:

          Original: Hey, Joe!
    Transformation: =========
