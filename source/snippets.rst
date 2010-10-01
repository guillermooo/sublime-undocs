Snippets
========

Whether you are coding or writing the next vampire best-seller, you're likely to
need certain short fragments of text again and again. Use snippets to save yourself
tedious typing. Snippets are smart templates that will insert text for you and
adapt it to their context.

To create a new snippet, select ``Tools > New Snippet``. Sublime Text will
present you with an skeleton for a new snippet.

Snippets can be stored under any package's folder, but to keep it simple while
you're learning, you can save them to your ``Packages\User`` folder. For now,
think of packages as folders. That's what they are, after all.

Snippets file format
********************

Snippets typically live in a Sublime Text package. They are simplified XML files
with the extension ``sublime-snippet``. For instance, you could have a
`greeting.sublime-snippet` inside an `Email` package.

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

`content`
    The actual snippet. Snippets can range from simple to fairly complex
    templates. We'll look at examples of both later.

    .. note::
        Note that the content is included in a ``<![CDATA[…]]>`` section.
        Snippets won't work if you don't do this!

    .. note::
        If you want the get a literal ``$``, you have to escape it like this: ``\$``.

    .. note::
        When writing a snippet that contains indentation, always use tabs. The
        tabs will be transformed into spaces when the snippet is inserted if the
        option ``translateTabsToSpaces`` is set to ``true``.

`tabTrigger`
    Defines the sequence of keys you want to type to let Sublime Text you want
    to insert this snippet. The snippet will kick in as soon as you hit the
    ``tab`` key after entering the predefined sequence.

    .. note::
        This is not the only way to tell Sublime Text how you want to insert your
        snippet, but we'll talk about that some other time. For now, let's just
        say that the other method is more flexible as well as a bit more complex.

`scope`
    Scopes won't be explained here, but they are a core concept of Sublime Text.
    Basically, scopes are named ranges of text. Based on grammars, Sublime Text
    know what to name different parts of a text.

`description`
    Used when showing the snippet in the Snippets menu. If not present, Sublime Text
    defaults to the name of the snippet.

With this information, you can start writing your own snippets. We'll see next
how to go about this.

    .. note::
        In the interest of brevity, we're only including the ``content``
        element's text in examples unless stated otherwise.

Snippet resources
*****************

Automatic variables
-------------------

Snippets have access to contextual and environmental information in the form
of variables.

======================    ====================================================================================
**PARAM1, PARAM2 …**      Arguments passed to the ``insertSnippet`` command. (Not covered here.)
**SELECTION**             The text that was selected when the snippet was triggered.
**TM_CURRENT_LINE**       Content of the line the cursor was in when the snippet was triggered.
**TM_CURRENT_WORD**       Current word under the cursor when the snippet was triggered.
**TM_FILENAME**           Filne name of the file being edited including extension.
**TM_FILEPATH**           File path to the file being edited.
**TM_FULLNAME**           User's User name.
**TM_LINE_INDEX**         Column the snippet is being inserted at, 0 based.
**TM_LINE_NUMBER**        Row the snippet is being inserted at, 1 based.
**TM_SELECTED_TEXT**      An alias for **SELECTION**.
**TM_SOFT_TABS**          ``YES`` if ``translateTabsToSpaces`` is true, otherwise ``NO``.
**TM_TAB_SIZE**           Spaces per-tab (controlled by the ``tabSize`` option).
======================    ====================================================================================

Let's see a simple example of a snippet using variables:

.. code-block:: c

    ====================================
    USER NAME:          $TM_FULLNAME
    FILE NAME:          $TM_FILENAME
     TAB SIZE:          $TM_TAB_SIZE
    SOFT TABS:          $TM_SOFT_TABS
    ====================================

    # Output (except hash symbols and leading spaces):
    # ====================================
    # USER NAME:          guillermo
    # FILE NAME:          test.txt
    #  TAB SIZE:          4
    # SOFT TABS:          YES
    # ====================================


Tab stops
---------

With the help of special marks, you can cycle through positions within the
snippet by pressing the ``tab`` key. Tab stops are used to walk you through
the customization of a snippet once it's been inserted.

.. code-block:: c

    First Name: $1
    Second Name: $2
    Address: $3

In the example above, the cursor will jump to ``1$`` if you press ``tab`` once.
If you press ``tab`` a second time, it will advance to ``$2``, etc. You can also
move backwards in the series with ``shift+tab``. If you press ``tab`` after the
highest tab stop, by default Sublime Text will place the cursor at the end of the
snippet so that you can resume normal editing.


    .. note::
        If you want to control where the exit point should be, use the ``$0`` mark.

Mirrored tab stops
------------------

Identical tab stop marks mirror each other: when you edit the first one, the rest
will be populated with the same value in real time.

.. code-block:: c

    First Name: $1
    Second Name: $2
    Address: $3
    User name: $1

In this example, "User name" will be filled out with the same value as "First Name".

Place holders
-------------

By expanding the tab stop syntax a little bit, you can define default values for
every tab stop. If there's a general case for your template and you will only
need to customize it occasionally, it makes sense to use place holders for the
most likely text you will need.

.. code-block:: c

    First Name: ${1:Guillermo}
    Second Name: ${2:López}
    Address: ${3:Main Street 1234}
    User name: $1

Of course, you can use variables as place holders too:

.. code-block:: c

    First Name: ${1:Guillermo}
    Second Name: ${2:López}
    Address: ${3:Main Street 1234}
    User name: ${4:$TM_FULLNAME}

You can have any number of substitutions in your snippets. Substitutions can
mirror each other too.

.. code-block:: c

    Hello ${1:John}! This is ${2:Frank}. You owe me ${3:100}\$. I know where you
    live, $1.
