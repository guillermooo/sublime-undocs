Snippets
========

Whether you are coding in a programming language or simply writing, you're
likely to need certain short fragments again and again. Snippets save you this
tedious typing by inserting smart templates that adapt to the context in which
you are writing. All this will become clearer once you gain even a superficial
understanding about this feature.

The easiest way to create a new snippet is by selecting the ``New Snippet``
command from Sublime Text's ``Tools`` menu. This will present you with an skeleton
for a new snippet.

You can store snippets under any package folder, but for the purposes of this
tutorial, you can save them under you `User` package.

Snippets file format
********************

Snippets typically live under a Sublime Text pacakge folder. They are simplified
XML files with the extension sublime-snippet. So, for instance, you could have
a `greeting.sublime-snippet` under an `Email` package. For the time being, think
of packages as folders. That's what they are, after all.

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

The `snippet` element contains all the information Sublime Text needs to know
*what* to insert, *where* to insert it and *how*. Let's see all of these parts
in turn.

`content`
    The actual snippet. Snippets can range from simple to fairly complex
    templates. We'll look at examples of both later.

    .. note::
        Note that the content is included in a ``<![CDATA[...]]`` section.
        Snippets won't work if you don't do this!

    .. note::
        If you want the get a literal ``$``, you have to escape it like this: ``\$``.

`tabTrigger`
    Defines the sequence of keys you want to type to let Sublime Text you want
    to insert this snippet. The snippet will kick in as soon as you hit the
    `tab` key after entering the predefined sequence.

    NOTE: This is not the only way to tell st- how you want to insert your
    snippet, but we'll talk about that some other time. For now, let's just say
    that the other method is both more flexible are a bit more complex.

`scope`
    Scopes won't be explained here, but they are a core concept of Sublime Text.
    Basically, scopes are named ranges of text. Based on grammars, Sublime Text
    know what to name different parts of a text.

`description`
    I don't know what descriptions are for, but I will investigate.

With this information, you can start writing your own snippets. We'll see next
how to go about this.

Snippet resources
=================

Automatic variables
*******************

Every snippet has access to metainformation about the file it's being triggered
on in the form of variables.

======================    ====================================================================================
**SELECTION**             The text that was selected when the snippet was triggered.
**PARAM1, PARAM2...**     Arguments passed to the `insertSnippet` command. (Not covered here.)
**TM_SELECTED_TEXT**      ???
**TM_LINE_INDEX**         ???
**TM_LINE_NUMBER**        Line where the cursor was in when the snippet was triggered.
**TM_FILEPATH**           File path to the file you are editing.
**TM_FILENAME**           Filne name of the file you are editing.
**TM_CURRENT_WORD**       Current word under the cursor when the snippet was triggered.
**TM_CURRENT_LINE**       Holds the content of the line the cursor was in when the snippet was triggered.
**TM_FULLNAME**           ???
**TM_TAB_SIZE**           ???
**TM_SOFT_TABS**          ???
======================    ====================================================================================

Substitutions
*************

You can define stop points to cycle through with the `tab` key in your snippet.
You can also put placeholder text in each of them. That way you can decide
whether to leave the placeholder or change it after you've inserted the snippet.

.. code-block:: c

    Hello ${1:John}!

You can have any number of substitutions in your snippets. Substitutions can
mirror each other too.

.. code-block:: c

    Hello ${1:John}! This is ${2:Frank}. You owe me ${3:100}\$. I know where you
    live, $1.


Complex substitutions
*********************
