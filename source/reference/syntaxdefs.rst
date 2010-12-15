.. sublime: wordWrap false

Syntax Definitions
==================

As explained below, _sds are stored in Plist files, but we'll be using JSON
for the examples. See :ref:`syntaxdefs` for more information about converting
JSON into Plist.

.. warning::
    This topic is a draft and may contain wrong information.

Compatibility with Textmate
***************************

Sublime Text syntax definitions are generally compatible with Textmate snippets.

File Format
***********

Snippet files Plist format with the ``tmLanguage`` extension. Here's an example
in JSON:

.. code-block:: js

  { "name": "Sublime Snippet (Raw)",
    "scopeName": "source.ssraw",
    "fileTypes": ["ssraw"],
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
              "1": { "name": "keyword.control.ssraw" },
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

``name``
    Descriptive name for the syntax definition. Shows up in the syntax definition dropdown menu
    located in the bottom right of Sublime Text interface. It's usually the name of the programming
    language or equivalent.

``scopeName``
    Name of the top-level scope for this syntax definition. Either ``source.<lang>`` or ``text.<lang>``.
    Use ``source`` for programming languages and ``text`` for everything else.

``fileTypes``
    And array of file type extensions for which this syntax should be automatically activated.
    Include the extensions without the leading dot.

``uuid``
    Unique indentifier for this _sd. Currently ignored.

``foldingStartMarker``
    Currently ignored. Used for code folding.

``foldingStopMarker``
    Currently ignored. Used for code folding.

``patterns``
    Array of patterns to match against the buffer's text.

``repostitory``
    Array of patterns abstracted out from the patterns element. Useful to keep
    the _sd tidy as well as for specialized uses like recursive patterns. Optional.


The Patterns Array
******************

Elements contained in the ``patterns`` array.

``match``
    Contains the following elements:

    ============    ==================================================
    ``match``       Pattern to search for.
    ``name``        Scope name to be assigned to matches of ``match``.
    ``comment``     Optional. For information only.
    ``captures``    Optional. Refinement of ``match``. See below.
    ============    ==================================================

    In turn, ``captures`` can contain *n* of the following pairs of elements:

    ========      ==================================
    ``0..n``      Name of the group referenced.
    ``name``      Scope to be assigned to the group.
    ========      ==================================

    Examples:

    .. code-block:: js

        // Simple

        { "name": "constant.character.escape.ssraw",
          "match": "\\\\(\\$|\\>|\\<)"
          "comment". "Sequences like \$, \> and \<"
        }

        // With captures

        { "match": "\\$(\\d+)",
          "name": "keyword.ssraw",
          "captures": {
              "1": { "name": "constant.numeric.ssraw" }
           },
          "comment": "Tab stops like $1, $2..."
        }

``include``
    Includes items in the repository, other _sds or the current one.

    References:

        =========       ===========================
        $self           The current _sd.
        #itemName       itemName in the repository.
        source.js       External _sds.
        =========       ===========================

    Examples:

    .. code-block:: js

        // Requires presence of DoubleQuotedStrings element in the repository.
        { "include": "#DoubleQuotedStrings" }

        // Recursively includes the current _sd.
        { "include": "$self" }

        // Includes and external _sd.
        { "include": "source.js" }

``begin .. end``
    Defines a scope potentially spanning multiple lines

    Contains the following elements:

        =================       ================================================
        ``begin``               The start marker pattern.
        ``end``                 The end marker pattern.
        ``name``                Scope name for the whole region.
        ``beginCaptures``       ``captures`` for ``begin``. See ``captures``.
        ``endCaptures``         ``captures`` for ``end``. See ``captures``.
        ``patterns``            ``patterns`` to be matched against the content.
        ``contentName``         Scope name for the content excluding the markers.
        =================       ================================================

    Example:

    .. code-block:: js

        { "name": "variable.complex.ssraw",
          "begin": "(\\$)(\\{)([0-9]+):",
          "beginCaptures": {
              "1": { "name": "keyword.control.ssraw" },
              "3": { "name": "constant.numeric.ssraw" }
           },
           "patterns": [
              { "include": "$self" },
              { "name": "string.ssraw",
                "match": "."
              }
           ],
           "end": "\\}"
        }

Repository
**********

Can be referenced from ``patterns`` or from itself in an ``include`` element.
See ``include`` for more information.

The repository can contain the following elements:

  - Simple elements:

    .. code-block:: js

      "elementName": {
        "match":  "some regexp",
        "name":   "some.scope.somelang"
      }

  - Complex elements:

    .. code-block:: js

      "elementName": {
        "patterns": [
          { "match":  "some regexp",
            "name":   "some.scope.somelang"
          },
          { "match":  "other regexp",
            "name":   "some.other.scope.somelang"
          }
        ]
      }

Examples:

.. code-block:: js

    "repository": {
      "numericConstant": {
        "patterns": [
          { "match":  "\\d*(?<!\\.)(\\.)\\d+(d)?(mb|kb|gb)?",
            "name":   "constant.numeric.double.powershell",
            "captures": {
              "1": { "name": "support.constant.powershell" },
              "2": { "name": "support.constant.powershell" },
              "3": { "name": "keyword.other.powershell" }
              }
          },
          { "match":  "(?<!\\w)\\d+(d)?(mb|kb|gb)?(?!\\w)",
            "name":   "constant.numeric.powershell",
            "captures": {
              "1": { "name": "support.constant.powershell" },
              "2": { "name": "keyword.other.powershell" }
              }
          }
        ]
      },
      "scriptblock": {
        "begin":  "\\{",
        "end":    "\\}",
        "name":   "meta.scriptblock.powershell",
        "patterns": [
          { "include": "$self" }
        ]
      },
    }


Escape Sequences
****************

Be sure to escape JSON/XML sequences as needed.

.. EXPLAIN