Syntax Definitions
==================

Syntax definitions make Sublime Text aware of programming and markup languages.
Most noticeably, they work together with colors to provide syntax highlighting.
Syntax definitions define *scopes* that divide the text in a buffer into named
regions. Several editing features in Sublime Text make extensive use of
this fine-grained contextual information.

Essentially, syntax definitions consist of regular expressions used to find
text, as well as more or less arbitrary, dot-separated strings called *scopes*
or *scope names*. For every occurrence of a given regular expression, Sublime
Text gives the matching text its corresponding *scope name*.


Prerequisites
*************

In order to follow this tutorial, you will need to install AAAPackageDev_, a
package intended to ease the creation of new syntax definitions for Sublime
Text. Follow the installation notes in the "Getting Started" section of the
readme.

.. _AAAPackageDev: https://github.com/SublimeText/AAAPackageDev


File format
***********

Sublime Text uses `property list`_ (Plist) files to store syntax definitions.
However, because editing XML files is a cumbersome task, we'll use YAML_ instead
and convert it to Plist format afterwards. This is where the AAAPackageDev
package (mentioned above) comes in.

.. _property list: http://en.wikipedia.org/wiki/Property_list
.. _YAML: http://en.wikipedia.org/wiki/YAML

.. note::
    If you experience unexpected errors during this tutorial, chances are
    AAAPackageDev or YAML is to blame. Don't immediately think your problem is
    due to a bug in Sublime Text.

By all means, do edit the Plist files by hand if you prefer to work in XML, but
always keep in mind their differing needs in regards to escape sequences, many
XML tags etc.


.. _scopes-and-scope-selectors:

Scopes
******

Scopes are a key concept in Sublime Text. Essentially, they are named text
regions in a buffer. They don't do anything by themselves, but Sublime Text
peeks at them when it needs contextual information.

For instance, when you trigger a snippet, Sublime Text checks the scope bound to
the snippet and looks at the caret's position in the file. If the caret's
current position matches the snippet's scope selector, Sublime Text fires it
off. Otherwise, nothing happens.

.. sidebar:: Scopes vs Scope Selectors

    There's a slight difference between *scopes* and *scope selectors*: Scopes
    are the names defined in a syntax definition, while scope selectors are used
    in items like snippets and key bindings to target scopes. When creating a
    new syntax definition, you care about scopes; when you want to constrain a
    snippet to a certain scope, you use a scope selector.

Scopes can be nested to allow for a high degree of granularity. You can drill
down the hierarchy very much like with CSS selectors. For instance, thanks to
scope selectors, you could have a key binding activated only within single
quoted strings in Python source code, but not inside single quoted strings in
any other language.

Sublime Text inherits the idea of scopes from Textmate, a text editor for Mac.
`Textmate's online manual`_ contains further information about scope selectors
that's useful for Sublime Text users too. Especially Color Schemes make
excessive usage of scopes to style every aspect of a language in the desired
color.

.. _`Textmate's online manual`: http://manual.macromates.com/en/scope_selectors


How Syntax Definitions Work
***************************

At their core, syntax definitions are arrays of regular expressions paired with
scope names. Sublime Text will try to match these patterns against a buffer's
text and attach the corresponding scope name to all occurrences. These pairs of
regular expressions and scope names are known as *rules*.

Rules are applied in order, one line at a time. Rules are applied in the
following order:

    1. The rule that matches at the first position in a line
    2. The rule that comes first in the array

.. XXX: What are those exceptions mentioned below?

Each rule consumes the matched text region, which therefore will be excluded
from the next rule's matching attempt (save for a few exceptions). In practical
terms, this means that you should take care to go from more specific rules to
more general ones when you create a new syntax definition. Otherwise, a greedy
regular expression might swallow parts you'd like to have styled differently.

Syntax definitions from separate files can be combined, and they can be
recursively applied too.


Your First Syntax Definition
****************************

By way of example, let's create a syntax definition for Sublime Text snippets.
We'll be styling the actual snippet content, not the whole ``.sublime-snippet``
file.

.. note::
    Since syntax definitions are primarily used to enable syntax highlighting,
    we'll use the phrase *to style* to mean *to break down a source code file
    into scopes*. Keep in mind, however, that colors are a different thing from
    syntax definitions and that scopes have many more uses besides syntax
    highlighting.

Here are the elements we want to style in a snippet:

    - Variables (``$PARAM1``, ``$USER_NAME``\ ...)
    - Simple fields (``$0``, ``$1``\ ...)
    - Complex fields with placeholders (``${1:Hello}``)
    - Nested fields (``${1:Hello ${2:World}!}``)
    - Escape sequences (``\\$``, ``\\<``\ ...)
    - Illegal sequences (``$``, ``<``\ ...)

Here are the elements we don't want to style because they are too complex for
this example:

    - Variable Substitution (``${1/Hello/Hi/g}``)

.. note::
    Before continuing, make sure you've installed the AAAPackageDev package as
    explained above.

Creating A New Syntax Definition
--------------------------------

To create a new syntax definition, follow these steps:

  - Go to **Tools | Packages | Package Development | New Syntax Definition**
  - Save the new file in your :file:`Packages/User` folder as a ``.YAML-tmLanguage`` file.

You now should see a file like this:

.. code-block:: yaml

    # [PackageDev] target_format: plist, ext: tmLanguage
    ---
    name: Syntax Name
    scopeName: source.syntax_name
    fileTypes: []
    uuid: 0da65be4-5aac-4b6f-8071-1aadb970b8d9

    patterns:
    -
    ...

Let's examine the key elements.

``name``
    The name that Sublime Text will display in the syntax definition drop-down list.
    Use a short, descriptive name. Typically, you will use the name of the programming
    language you are creating the syntax definition for.

``scopeName``
    The top level scope for this syntax definition. It takes the form
    ``source.<lang_name>`` or ``text.<lang_name>``. For programming languages,
    use ``source``. For markup and everything else, use ``text``.

``fileTypes``
    This is a list of file extensions (without the leading dot). When opening
    files of these types, Sublime Text will automatically activate this syntax
    definition for them.

``uuid``
    This is a unique identifier for this syntax definition. Each new syntax
    definition gets its own uuid. Even though Sublime Text itself ignores it,
    don't modify this.

``patterns``
    A container for your patterns.

For our example, fill the template with the following information::

    # [PackageDev] target_format: plist, ext: tmLanguage
    ---
    name: Sublime Snippet (Raw)
    scopeName: source.ssraw
    fileTypes: [ssraw]
    uuid: 0da65be4-5aac-4b6f-8071-1aadb970b8d9

    patterns:
    -
    ...

.. note::
    YAML is not a very strict format, but can cause headaches when you don't
    know its conventions. It supports single and double quotes, but you may also
    omit them as long as the content does not create another YAML literal. If
    the conversion to Plist fails, take a look at the output panel for more
    information on the error. We'll explain later how to convert a syntax
    definition in YAML to Plist. This will also cover the first commented line
    in the template.

    The ``---`` and ``...`` are optional.


Analyzing Patterns
******************

The ``patterns`` array can contain several types of elements. We'll look at some
of them in the following sections. If you want to learn more about patterns,
refer to Textmate's online manual.

Matches
-------

Matches take this form:

.. code-block:: yaml

    match: (?i:m)y \s+[Rr]egex
    name: string.format
    comment: This comment is optional.


.. sidebar:: Regular Expressions' Syntax In Syntax Definitions

    Sublime Text uses Oniguruma_'s syntax for regular expressions in syntax
    definitions. Several existing syntax definitions make use of features
    supported by this regular expression engine that aren't part of perl-style
    regular expressions, hence the requirement for Oniguruma.

    .. _Oniguruma: http://www.geocities.jp/kosako3/oniguruma/doc/RE.txt


``match``
    A regular expression Sublime Text will use to find matches.

``name``
    The name of the scope that should be applied to any occurrences of ``match``.

``comment``
    An optional comment about this pattern.

Let's go back to our example. It looks like this:

.. code-block:: yaml

    # [PackageDev] target_format: plist, ext: tmLanguage
    ---
    name: Sublime Snippet (Raw)
    scopeName: source.ssraw
    fileTypes: [ssraw]
    uuid: 0da65be4-5aac-4b6f-8071-1aadb970b8d9

    patterns:
    -
    ...


That is, make sure the ``patterns`` array is empty.

Now we can begin to add our rules for Sublime snippets. Let's start with simple
fields. These could be matched with a regex like so:

.. code-block:: perl

    \$[0-9]+
    # or...
    \$\d+

We can then build our pattern like this:

.. code-block:: yaml

    name: keyword.other.ssraw
    match: \$\d+
    comment: Tab stops like $1, $2...

.. sidebar:: Choosing the Right Scope Name

    Naming scopes isn't obvious sometimes. Check the `Textmate naming
    conventions`_ for guidance on scope names. AAAPackageDev automatically
    provides completions for scope names according to these conventions. It is
    important to re-use the basic categories outlined there if you want to
    achieve the highest compatibility with existing colors.

    Color schemes have hardcoded scope names in them. They could not possibly
    include every scope name you can think of, so they target the standard ones
    plus some rarer ones on occasion (like for CSS or Markdown). This means that
    two color schemes using the same syntax definition may render the text
    differently!

    Bear in mind too that you should use the scope name that best suits your
    needs or preferences. It'd be perfectly fine to assign a scope like
    ``constant.numeric`` to anything other than a number if you have a good
    reason to do so.

    .. _Textmate naming conventions: https://manual.macromates.com/en/language_grammars#naming_conventions

And we can add it to our syntax definition too:

.. code-block:: yaml

    # [PackageDev] target_format: plist, ext: tmLanguage
    ---
    name: Sublime Snippet (Raw)
    scopeName: source.ssraw
    fileTypes: [ssraw]
    uuid: 0da65be4-5aac-4b6f-8071-1aadb970b8d9

    patterns:
    - comment: Tab stops like $1, $2...
      name: keyword.other.ssraw
      match: \$\d+
    ...

.. note::
    You should use two spaces for indent. This is the recommended indent for
    YAML and lines up with lists like shown above.

We're now ready to convert our file to ``.tmLanguage``. Syntax definitions use
Textmate's ``.tmLanguage`` extension for compatibility reasons. As explained
above, they are simply Plist XML files.

Follow these steps to perform the conversion:

    - Make sure that ``Automatic`` is selected in **Tools | Build System**, or
      select ``Convert to ...``
    - Press :kbd:`F7`
    - A ``.tmLanguage`` file will be generated for you in the same folder as
      your ``.YAML-tmLanguage`` file
    - Sublime Text will reload the changes to the syntax definition

In case you are wondering why AAAPackageDev knows what you want to convert your
file to: It's specified in the first commente line.

You have now created your first syntax definition. Next, open a new file and
save it with the extension ``.ssraw``. The buffer's syntax name should switch to
"Sublime Snippet (Raw)" automatically, and you should get syntax highlighting if
you type ``$1`` or any other simple snippet field.

Let's proceed to creating another rule for environment variables.

.. code-block:: yaml

    comment: Variables like $PARAM1, $TM_SELECTION...
    name: keyword.other.ssraw
    match: \$[A-Za-z][A-Za-z0-9_]+

Repeat the above steps to update the ``.tmLanguage`` file.

Fine Tuning Matches
-------------------

You might have noticed, for instance, that the entire text in ``$PARAM1`` is
styled the same way. Depending on your needs or your personal preferences, you
may want the ``$`` to stand out. That's where ``captures`` come in. Using
captures, you can break a pattern down into components to target them
individually.

Let's rewrite one of our previous patterns to use ``captures``:

.. code-block:: yaml

    comment: Variables like $PARAM1, $TM_SELECTION...
    name: keyword.other.ssraw
    match: \$([A-Za-z][A-Za-z0-9_]+)
    captures:
      '1': {name: constant.numeric.ssraw}

Captures introduce complexity to your rule, but they are pretty straightforward.
Notice how numbers refer to parenthesized groups left to right. Of course, you
can have as many capture groups as you want.

.. note::
    Writing ``1`` on a new line and pressing tab will autocomplete to ``'1':
    {name: }`` thanks to AAAPackageDev.

Arguably, you'd want the other scope to be visually consistent with this one.
Go ahead and change it too.

.. note::
    As with ususal regular expressions and substítutions, the capture group
    ``'0'`` applies to the whole match.

Begin-End Rules
---------------

Up to now we've been using a simple rule. Although we've seen how to dissect patterns
into smaller components, sometimes you'll want to target a larger portion of your
source code that is clearly delimited by start and end marks.

Literal strings enclosed by quotation marks or other delimiting constructs are
better dealt with by begin-end rules. This is a skeleton for one of these rules::

    name:
    begin:
    end:

Well, at least in their simplest version. Let's take a look at one that
includes all available options:

.. code-block:: yaml

    name:
    contentName:
    begin:
    beginCaptures:
      '0': {name: }
      # ...
    end:
    endCaptures:
      '0': {name: }
      # ...
    patterns:
    - name:
      match:
    # ...

Some elements may look familiar, but their combination might be daunting. Let's
inspect them individually.

``name``
    Just like with simple captures this sets the following scope name to the
    whole match, including ``begin`` and ``end`` marks. Effectively, this will
    create nested scopes for ``beginCaptures``, ``endCaptures`` and ``patterns``
    defined within this rule. Optional.

``contentName``
    Unlike the ``name`` this only applies a scope name to the enclosed text.
    Optional.

``begin``
    Regex for the opening mark for this scope.

``end``
    Regex for the end mark for this scope.

``beginCaptures``
    Captures for the ``begin`` marker. They work like captures for simple
    matches. Optional.

``endCaptures``
    Same as ``beginCaptures`` but for the ``end`` marker. Optional.

``patterns``
    An array of patterns to match **only** against the begin-end's content; they
    aren't matched against the text consumed by ``begin`` or ``end`` themselves.
    Optional.

We'll use this rule to style nested complex fields in snippets:

.. code-block:: yaml

    name: variable.complex.ssraw
    contentName: string.other.ssraw
    begin: '(\$)(\{)([0-9]+):'
    beginCaptures:
      '1': {name: keyword.other.ssraw}
      '3': {name: constant.numeric.ssraw}
    end: \}
    patterns:
    - include: $self
    - name: support.other.ssraw
      match: .

This is the most complex pattern we'll see in this tutorial. The ``begin`` and
``end`` keys are self-explanatory: they define a region enclosed between
``${<NUMBER>:`` and ``}``. We need to wrap the begin pattern into quotes because
otherwise the trailing ``:`` would indicate the parser to expect another
dictionary key. ``beginCaptures`` further divides the begin mark into smaller
scopes.

The most interesting part, however, is ``patterns``. Recursion, and the
importance of ordering, have finally made their appearance here.

We've seen above that fields can be nested. In order to account for this, we
need to style nested fields recursively. That's what the ``include`` rule does
when we furnish it the ``$self`` value: it recursively applies our **entire
syntax definition** to the text captured by our begin-end rule. This portion
excludes the text individually consumed by the regexes for ``begin`` and
``end``.

Remember, matched text is consumed; thus, it is excluded from the next match
attempt and can't be matched again.

To finish off complex fields, we'll style placeholders as strings. Since we've
already matched all possible tokens inside a complex field, we can safely tell
Sublime Text to give any remaining text (``.``) a literal string scope. Note
that this doesn't work if we made the pattern greedy (``.+``) because this
includes possible nested references.

.. note::
    We could've used ``contentName: string.other.ssraw`` instead of the last
    pattern but this way we introduce the importance of ordering and how matches
    are consumed.

Final Touches
-------------

Lastly, let's style escape sequences and illegal sequences, and then we can wrap up.

.. code-block:: yaml

    - comment: Sequences like \$, \> and \<
      name: constant.character.escape.ssraw
      match: \\[$<>]

    - comment: Unescaped and unmatched magic characters
      name: invalid.illegal.ssraw
      match: '[$<>]'

The only hard thing here is not forgetting that ``[]`` enclose arrays in YAML and thus must be wrapped in quotes.
Other than that, the rules are pretty straightforward if you're familiar with
regular expressions.

However, you must take care to place the second rule after any others matching
the ``$`` character, since otherwise it will be consumed and result in every
following expression not matching.

Also, even after adding these two additional rules, note that our recursive
begin-end rule from above continues to work as expected.

At long last, here's the final syntax definition:

.. code-block:: yaml

    # [PackageDev] target_format: plist, ext: tmLanguage
    ---
    name: Sublime Snippet (Raw)
    scopeName: source.ssraw
    fileTypes: [ssraw]
    uuid: 0da65be4-5aac-4b6f-8071-1aadb970b8d9

    patterns:
    - comment: Tab stops like $1, $2...
      name: keyword.other.ssraw
      match: \$(\d+)
      captures:
        '1': {name: constant.numeric.ssraw}

    - comment: Variables like $PARAM1, $TM_SELECTION...
      name: keyword.other.ssraw
      match: \$([A-Za-z][A-Za-z0-9_]+)
      captures:
        '1': {name: constant.numeric.ssraw}

    - name: variable.complex.ssraw
      begin: '(\$)(\{)([0-9]+):'
      beginCaptures:
        '1': {name: keyword.other.ssraw}
        '3': {name: constant.numeric.ssraw}
      end: \}
      patterns:
      - include: $self
      - name: support.other.ssraw
        match: .

    - comment: Sequences like \$, \> and \<
      name: constant.character.escape.ssraw
      match: \\[$<>]

    - comment: Unescaped and unmatched magic characters
      name: invalid.illegal.ssraw
      match: '[$<>]'
    ...

There are more available constructs and code reuse techniques using a
"repository", but the above explanations should get you started with the
creation of syntax definitions.

.. note::
    If you previously used JSON for syntax definitions you are still able to do
    this because AAAPackageDev is backwards compatible.

    If you want to consider switching to YAML (either from JSON or directly from
    Plist), it provides a command named ``AAAPackageDev: Convert to YAML and
    Rearrange Syntax Definition`` which will automatically format the resulting
    YAML in a pleasurable way.

.. seealso::

    :doc:`/reference/syntaxdefs`
        Reference for snytax definitions
