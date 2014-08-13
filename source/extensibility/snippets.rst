========
Snippets
========

Whether you are coding or writing the next vampire best-seller, you're likely to
need certain short fragments of text again and again. Use snippets to save yourself
tedious typing. Snippets are smart templates that will insert text for you,
adapting it to their context.

To create a new snippet, select **Tools | New Snippet…**. Sublime Text will
present you with an skeleton for a new snippet.

Snippets can be stored under any package's folder, but to keep it simple while
you're learning, you can save them to your :file:`Packages/User` folder.

Snippets File Format
********************

Snippets typically live in a Sublime Text package. They are simplified XML files
with the extension *.sublime-snippet*. For instance, you could have a
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
to know *what* to insert, *whether* to insert and *when*. Let's see all of
these parts in turn.

``content``
    The actual snippet. Snippets can range from simple to fairly complex
    templates. We'll look at examples of both later.

    Keep the following in mind when writing your own snippets:

        - If you want to get a literal ``$``, you have to escape it like this: ``\$``.

        - When writing a snippet that contains indentation, always use tabs.
          When the snippet is inserted, the tabs will be transformed into spaces
          if the option ``translateTabsToSpaces`` is ``true``.

        - The ``content`` must be included in a ``<![CDATA[…]]>`` section.
          Snippets won't work if you don't do this!

        - The ``content`` of your snippet must not contain ``]]>`` because this
          string of characters will prematurely close the ``<![CDATA[…]]>`` section,
          resulting in an XML error. To work around this pitfall, you can insert an
          undefined variable into the string like this: ``]]$NOT_DEFINED>``. This
          modified string passes through the XML parser without closing the content
          element's ``<![CDATA[…]]>`` section, but Sublime Text will replace
          ``$NOT_DEFINED`` with an empty string before inserting the snippet into
          your document. In other words, ``]]$NOT_DEFINED>`` in your snippet file
          ``content`` will be written as ``]]>`` when you trigger the snippet.

``tabTrigger``
    Defines the sequence of keys that must be pressed to insert this snippet. After typing
    this sequence, the snippet will kick in as soon as you hit the :kbd:`Tab` key.

    A tab trigger is an implicit key binding.

``scope``
    Scope selector determining the context where the snippet will be active.
    See :ref:`scopes-and-scope-selectors` for more information.

``description``
    Used when showing the snippet in the Snippets menu. If not present, Sublime
    Text defaults to the file name of the snippet.

With this information, you can start writing your own snippets as described in
the next sections.

.. note::
    In the interest of brevity, we're only including the ``content``
    element's text in examples unless otherwise noted.


.. _snippet-features:

Snippet Features
****************

Environment Variables
---------------------

Snippets have access to contextual information in the form of environment variables.
Sublime Text automatically sets the values of the variables listed below.

You can also add your own variables to provide extra information. These custom
variables are defined in ``.sublime-options`` files.

=======================    =======================================================================
**$PARAM1, $PARAM2...**    Arguments passed to the ``insert_snippet`` command. (Not covered here.)
**$SELECTION**             The text that was selected when the snippet was triggered.
**$TM_CURRENT_LINE**       Content of the cursor's line when the snippet was triggered.
**$TM_CURRENT_WORD**       Word under the cursor when the snippet was triggered.
**$TM_FILENAME**           Name of the file being edited, including extension.
**$TM_FILEPATH**           Path to the file being edited.
**$TM_FULLNAME**           User's user name.
**$TM_LINE_INDEX**         Column where the snippet is being inserted, 0 based.
**$TM_LINE_NUMBER**        Row where the snippet is being inserted, 1 based.
**$TM_SELECTED_TEXT**      An alias for **$SELECTION**.
**$TM_SOFT_TABS**          ``YES`` if ``translate_tabs_to_spaces`` is true, otherwise ``NO``.
**$TM_TAB_SIZE**           Spaces per-tab (controlled by the ``tab_size`` option).
=======================    =======================================================================

Let's see a simple example of a snippet using variables:

.. code-block:: perl

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
snippet by pressing the :kbd:`Tab` key. Fields are used to walk you through the
customization of a snippet after it's been inserted.

.. code-block:: perl

    First Name: $1
    Second Name: $2
    Address: $3

In the example above, the cursor will jump to ``$1`` if you press :kbd:`Tab` once.
If you press :kbd:`Tab` a second time, it will advance to ``$2``, etc. You can also
move backwards in the series with :kbd:`Shift+Tab`. If you press :kbd:`Tab` after the
highest tab stop, Sublime Text will place the cursor at the end of the snippet's
content, enabling you to resume normal editing.

If you want to control where the exit point should be, use the ``$0`` mark. By
default, the exit point is the end of the snippet.

You can break out of the field cycle any time by pressing :kbd:`Esc`.

Mirrored Fields
---------------

Identical field markers mirror each other: when you edit the first one, the rest
will be populated in real time with the same value.

.. code-block:: perl

    First Name: $1
    Second Name: $2
    Address: $3
    User name: $1

In this example, "User name" will be filled out with the same value as "First Name".

Placeholders
-------------

By expanding the field syntax a little bit, you can define default values for
a field. Placeholders are useful whenever there's a general case for your snippet,
but still you still want to keep it customizable.

.. code-block:: perl

    First Name: ${1:Guillermo}
    Second Name: ${2:López}
    Address: ${3:Main Street 1234}
    User name: $1

Variables can be used as placeholders:

.. code-block:: perl

    First Name: ${1:Guillermo}
    Second Name: ${2:López}
    Address: ${3:Main Street 1234}
    User name: ${4:$TM_FULLNAME}

And you can nest placeholders within other placeholders too:

.. code-block:: perl

    Test: ${1:Nested ${2:Placeholder}}

Substitutions
-------------

In addition to the placeholder syntax, tab stops can specify more complex
operations with substitutions. Use substitutions to dynamically generate text
based on a mirrored tab stop. Of course, the tab stop you want to use as
variable has to be mirrored somewhere else in the snippet.

The substitution syntax has the following syntaxes:

    - ``${var_name/regex/format_string/}``
    - ``${var_name/regex/format_string/options}``

**var_name**
    The variable name: 1, 2, 3…

**regex**
    Perl-style regular expression: See the `Boost library documentation for
    regular expressions`_.

**format_string**
    See the `Boost library documentation for format strings`_.

**options**
    Optional. May be any of the following:
        **i**
            Case-insensitive regex.
        **g**
            Replace all occurrences of ``regex``.
        **m**
            Don't ignore newlines in the string.

.. _`Boost library documentation for regular expressions`: http://www.boost.org/doc/libs/1_44_0/libs/regex/doc/html/boost_regex/syntax/perl_syntax.html

.. _`Boost library documentation for format strings`: http://www.boost.org/doc/libs/1_44_0/libs/regex/doc/html/boost_regex/format/perl_format.html

With substitutions you can, for instance, underline text effortlessly:

.. code-block:: perl

          Original: ${1:Hey, Joe!}
    Transformation: ${1/./=/g}

    # Output:

          Original: Hey, Joe!
    Transformation: =========
