Syntax Definitions
==================

.. warning::
  This topic is a draft and might contain inaccurate information.

Syntax definitions make Sublime Text aware of different languages. Most prominently,
syntax definitions work together with colors to style source code. Because syntax
definitions carve scopes in a source code file, however, they provide a fundamental
contextual reference to Sublime Text's editing features.

Simplifying, Sublime Text uses the rules defined in syntax definitions to find matches in
the buffer's text and gives occurrences names (*scopes*). Scopes are then used to determine
the course of action when actions defined in package items like snippets or commands are triggered.

Prerequisites
*************

In order to follow this tutorial, you will need to install GrammarDev_, a package
intended to ease the creation of new syntax definitions.

.. _GrammarDev: http://bitbucket.org/guillermooo/grammardev

File format
***********

.. XXX insert link to WPedia

Sublime Text uses `property list`_ files (plist) to store syntax definitions.

.. _`property list`: http://en.wikipedia.org/wiki/Property_list

Because editing xml files is a cumbersome task, we'll be using json instead
and converting it to plist afterwards. This is where the GrammarDev package
mentioned above comes in.

.. note::
    If you experience unexpected errors during this tutorial, chances are
    GrammarDev is to blame. Don't immediately think your problem is due to a
    bug in Sublime Text.

By all means, do edit the plist files by hand if you prefer to work in xml, but
keep always in mind the differing needs with regards to escape sequences, etc.

Scopes
******

Scopes are a key concept in Sublime Text. Essentially, they are named text regions
in your source code file. Scopes identify elements in text based on regular expressions.
They don't do anything by themselves, but Sublime Text refers back to them when
it needs a contextual reference.

For instance, when you trigger a snippet, Sublime Text checks the scope the snippet's
bound to and looks at the caret's position in the file. If the caret's current
scope matches the snippet's scope selector, Sublime Text fires the snippet off.
Otherwise, nothing happens.

Scopes can be nested to allow for a high degree of granularity. You can drill down
the hierarchy very much like with CSS selectors. For instance, thanks to scope
selectors, you could have a keybinding activated only within single quoted strings
in python source code, but not inside single quoted strings in any other language.

Sublime Text implements the idea of scopes from Texmate, a text editor for Mac.
`Textmate's online manual`_ contains further information about scopes that is useful for
Sublime Text users too.

.. _`Textmate's online manual`: http://manual.macromates.com/en/

.. note::
  Sublime Text provides a hook to override the scope matching look-up chain,
  allowing you to add user-defined scopes.

How Syntax Definitions Work
****************************

At their core, syntax definitions are arrays of regular expressions paired with
scope names. Sublime Text will try to match these patterns against a buffer's text
and atthach the scope name to all occurrences. These regexp-name pairs are known
as *rules*.

Rules are applied in order, one line at a time. Each rule consumes the matched
text region, i.e., it will be excluded from the next rule's matching attempt
(save for a few exceptions). In practical terms, this means that, when you create
a new syntax definition, you should take care to go from more specific rules
to more general ones. Otherwise, a greedy regular expression might swallow parts
you'd like to have scoped differently.

Syntax definitions from separate files can be combined, and they can be recursively
applied too.

Your First Syntax Definition
****************************

By way of example, let's create a syntax definition for Sublime Text snippets.
We'll be styling the actual snippet content, not the ``sublime-snippet`` file.

.. note::
  Since syntax definitions are primarily used to activate syntax highlighting for
  source code, we'll use *to style* with the meaning *to break down a source code
  file into scopes*. However, keep in mind that colors are a different thing to
  syntax definitions and that scopes have many more uses besides syntax higlighting.

These are the elements we want to style in snippets:

    - Variables (**$PARAM1**, **$USER_NAME**...)
    - Simple tab stops (**$0**, **$1**...)
    - Complex tab stops with place holders (**${1:Hello}**)
    - Nested tab stops (**${1:Hello ${2:World}!**)
    - Escape sequences (**\$**, **\<**...)
    - Illegal sequences (**$**, **<**...)

.. note::
    Before continuing, make sure you've installed the GrammarDev package.

Creating A New Syntax Definition
--------------------------------

To create a new syntax definition, follow these steps:

  - Hit ``CTRL + ~`` to open the Sublime Text python console
  - Type ``view.runCommand("newSyntaxDef")``
  - Save the new file to your ``Packages\User`` folder as **Sublime Snippets (Raw).JSON-tmLanguage**

You should now see a file like this::

  { "name": "Untitled",
    "scopeName": "source.untitled",
    "fileTypes": ["ff", "fff"],
    "foldingStartMarker": "\\\\{\\\\s*$",
    "foldingStopMarker": "^\\\\s*\\\\}",
    "patterns": [
       { "name": "keyword.untitled",
         "match": "\\\\b(if|while|for|return)\\\\b"
       },
       { "name": "string.quoted.double.untitled",
         "begin": "\\\"",
         "beginCaptures": {
           "0": { "name": "definition.string.quoted.double.untitled" }
          },
          "end": "\\\"",
          "patterns": [
             { "name": "constant.character.escape.untitled",
               "match": "\\\\."
             }
          ]
       }
    ],
    "uuid": "ca03e751-04ef-4330-9a6b-9b99aae1c418"
  }


**uuid**
    Located at the end, this is a string uniquely identifying this syntax definition. You
    shouldn't need to modify it.

**name**
    The name that Sublime Text will display in the syntax definition drop-down menu (bottom right).
    Use a short, descriptive name. Normally, you will be using the programming
    language's name you are creating the grammar for.

**scopeName**
    The top level scope for this grammar. It takes the form ``source.<lang_name>`` or
    ``text.<lang_name>``. For programming languages, use ``source``. For markup
    and everything else, ``text``.

**fileTypes**
    This is a list of file extensions. When opening one of these files, Sublime Text will
    apply this syntax definition to it.

**foldingStartMarker**
    XXX. Optional.

**foldingStopMarker**
    XXX. Optional.

**patterns**
    Container for your patterns.

For our example, fill in the template with the following information::

    {   "name": "Sublime Snippet (Raw)",
        "scopeName": "source.ssraw",
        "fileTypes": ["ssraw"],
        "foldingStartMarker": "\\\\{\\\\s*$",
        "foldingStopMarker": "^\\\\s*\\\\}",
        "patterns": [
        ],
        "uuid": "ca03e751-04ef-4330-9a6b-9b99aae1c418"

.. note::
    Json is a very restrictive format, so make sure to get all the commas and
    quotes right.

Analyzing Patterns
******************

Patterns can contain several types of elements. We'll look at some of them in
the folllowing sections. If you want to learn more about patterns, check out
Textmate's online manual.

Matches
-------

They take this form::

    { "match": "[Mm]y \s+[Rr]egex",
      "name": "string.ssraw",
      "comment": "This comment is optional."
    }

**match**
    A regular expression Sublime Text will use to try and find matches.

**name**
    Name of the scope that should be applied to the matches of match.

**comment**
    An optional comment about this pattern.

Let's go back to our example. Make it look like this::

    { "name": "Sublime Snippet (raw)",
      "scopeName": "source.ssraw",
      "fileTypes": ["ssraw"],
      "foldingStartMarker": "\\\\{\\\\s*$",
      "foldingStopMarker": "^\\\\s*\\\\}",
      "patterns": [
      ],
      "uuid": "ca03e751-04ef-4330-9a6b-9b99aae1c418"
    }

That is, make sure the patterns array is empty.

Now we can begin to add our rules for Sublime snippets. Let's start with simple
tab stops. These could be matched with a regex like so::

    \$[0-9]+
    # or...
    \$\d+

However, because we're writing our regex in json, we need to account for json's
own escaping rules. Thus, our previous example becomes::

    \\$\\d+

With escaping out of the way, we can build our pattern like this::

    { "match": "\\$\\d+",
      "name": "keyword.source.ssraw",
      "comment": "Tab stops like $1, $2..."
    }

.. note::
    Naming scopes isn't obvious sometimes. Check the Textmate online manual
    for guidance on scope names. It is important to re-use the basic categories
    outlined there if you want to achieve the highest compatibility with existing
    colors. Colors have hardcoded scopes names in them. They could not possibly
    include every scope name you can think of, so they target the standard ones
    plus some rarer ones on occasion. This means that two colors using the same
    syntax definition may render the text differently!

    Bear in mind too that you should use the scope name that best suits a given
    pattern. It is perfectly fine to assign a scope like ``constant.numeric`` to
    anything other than a number if you have a good reason to do so.

And we can add it to our syntax definition too::

    {   "name": "Sublime Snippet (raw)",
        "scopeName": "source.ssraw",
        "fileTypes": ["ssraw"],
        "foldingStartMarker": "\\\\{\\\\s*$",
        "foldingStopMarker": "^\\\\s*\\\\}",
        "patterns": [
            { "match": "\\$\\d+",
              "name": "keyword.source.ssraw",
              "comment": "Tab stops like $1, $2..."
            }
        ],
        "uuid": "ca03e751-04ef-4330-9a6b-9b99aae1c418"
    }

We're now ready to convert our file to tmLanguage.

Follow these steps:

    - Press ``CTRL + SHIFT + G``
    - A tmLanguage file will be created for you
    - Close and reopen Sublime Text so all your changes can take effect

.. note::
    Sublime Text cannot reload syntax definitions automatically when they're modified.

You have now created your first syntax definition. Now create a new file and save it with the
extension ``ssraw``. The syntax name should switch to "Sublime Snippet (Raw)"
automatically, and you should see some color if you type ``$1`` or any other
simple tab stop.

Let's proceed to creating another rule for automatic variables.

::

    { "match": "\\$[A-Za-z][A-Za-z0-9_]+",
      "name": "keyword.source.ssraw",
      "comment": "Variables like $PARAM1, $TM_SELECTION..."
    }

Repeat the steps above to update the tmLanguage file and restart Sublime Text.

Fine Tuning Matches
-------------------

You might have noticed that the entire text in $PARAM1, for instance, is styled
the same way. Depending on your needs or your personal preferences, you may want
the $ to stand out from the rest. That's where captures come in. Using captures,
you can break a pattern downp into components and target them individually.

Let's rewrite one of our previous patterns to use captures::

    { "match": "\\$([A-Za-z][A-Za-z0-9_]+)",
      "name": "keyword.ssraw",
       "captures": {
           "1": { "name": "constant.numeric.ssraw" }
       },
      "comment": "Variables like $PARAM1, $TM_SELECTION..."
    }

Captures introduce complexity to your pattern, but they are pretty straightforward.
Notice how numbers refer to parenthesized groups left to right. Of course, you can
have as many capture groups as you want.

Arguably, you'd want the other scope to be visually consistent with this one.
Go ahead and change it too.

Up to now we've been matching up pretty simple pieces of text. We've seen how
to dissect these into smaller components, but sometimes you'll want to target
a larger portion of your source code defined by start and end marks.

Begin..End Rules
----------------

Literal strings enclosed in quotation marks and other delimited constructs are
better dealt with with begin..end rules. This is a skeleton for one of these rules::

      { "name": "",
        "begin": "",
        "end": ""
      }

Well, that's the simpler version. Let's take a look at one including all available
options::

       { "name": "",
         "begin": "",
         "beginCaptures": {
           "0": { "name": "" }
         },
         "end": "",
         "endCaptures": {
           "0": { "name": "" }
         },
         "patterns": [
            {  "name": "",
               "match": ""
                         }
         ],
         contentName: ""
       }

**begin**
    Regex for the opening mark for this scope.

**end**
    Regex for the end mark for this scope.

**beginCaptures**
    Captures for the begin marker. Work as captures for simple matches. Optional.

**endCaptures**
    Same as beginCaptures but for the end marker. Optional.

**contentName**
    Scope for the whole matched region, from the begin marker to the end marker,
    inclusive. This will effectively create nested scopes for beginCaptures,
    endCaptures and patterns defined within this rule. Optional.

**patterns**
    An array of patterns to match against the begin..end content. They are not
    matched up against the text consumed by **begin** or **end**.

An example for our syntax definition::

    { "name": "variable.complex.ssraw",
       "begin": "(\\$)(\\{)([0-9]+):",
       "beginCaptures": {
           "1": { "name": "keyword.ssraw" },
           "3": { "name": "constant.numeric.ssraw" }
       },
       "patterns": [
           { "include": "$self" },
           {  "name": "string.ssraw",
              "match": "."
           }
       ],
       "end": "\\}"
    }

This is the most complex pattern we'll see in the tutorial. The begin and end
keys are pretty simple: They define a region enclosed between ``${<NUMBER>:`` and ``}``.
``beginCaptures`` further divides the begin mark into smaller scopes.

The most interesting part, however, is ``patterns``. Recursion and the
importance of ordering have finally made an appearance here.

We've seen further above that tab stops can be nested. In order to account for
this, we need to recursively style nested tab stops. That's what the ``include``
rule does when furnished the ``$self`` value: it recursively applies our entire
grammar to the portion of text contained in our begin..end rule.

Remember that matched up text is consumed and is excluded from the next match
attempt. The same holds true for recursively styled grammars.

To finish off complex tab stops, we want to style place holders as strings. Since
we've already matched up all possible tokens inside a complex tabstop, we can
safely tell Sublime Text to give any remaining text (``.``) a literal string scope.

Final Touches
-------------

Lastly, let's style escape sequences and illegal sequeces, and wrap up.

::

        {  "name": "constant.character.escape.ssraw",
           "match": "\\\\(\\$|\\>|\\<)"
        },

        {  "name": "invalid.ssraw",
           "match": "(\\$|\\<|\\>)"
        }

The only hard thing here is getting the number of escape characters right. Other
than that, the rules are pretty straightforward if you're familiar with
regular expressions.

However, you must take care to put the second rule after any others matching
the ``$`` character, since otherwise you may not get the desired result.

And here's the final syntax definition::

  {   "name": "Sublime Snippet (Raw)",
      "scopeName": "source.ssraw",
      "fileTypes": ["ssraw"],
      "foldingStartMarker": "\\{\\s*$",
      "foldingStopMarker": "^\\s*\\}",
      "patterns": [
          { "match": "\\$(\\d+)",
            "name": "keyword.ssraw",
            "captures": {
                "1": { "name": "constant.numeric.ssraw" }
             },
            "comment": "Tab stops like $1, $2..."
          },

          { "match": "\\$([A-Za-z][A-Za-z0-9_]+)",
            "name": "keyword.ssraw",
            "captures": {
                "1": { "name": "constant.numeric.ssraw" }
             },
            "comment": "Variables like $PARAM1, $TM_SELECTION..."
          },

          { "name": "variable.complex.ssraw",
            "begin": "(\\$)(\\{)([0-9]+):",
            "beginCaptures": {
                "1": { "name": "keyword.ssraw" },
                "3": { "name": "constant.numeric.ssraw" }
             },
             "patterns": [
                { "include": "$self" },
                { "name": "string.ssraw",
                  "match": "."
                }
             ],
             "end": "\\}"
          },

          { "name": "constant.character.escape.ssraw",
            "match": "\\\\(\\$|\\>|\\<)"
          },

          { "name": "invalid.ssraw",
            "match": "(\\$|\\>|\\<)"
          }
      ],
      "uuid": "ca03e751-04ef-4330-9a6b-9b99aae1c418"
  }

There are more available constructs and code reuse techniques, but the above
explanations should get you started on the creation of syntax definitions.
