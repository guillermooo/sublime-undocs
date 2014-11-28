# Contribution Guidelines


## Issue

Even though it's very unlikely,
please search through the existing issues
and look for existing similar ones
before submitting your own.


## Pull request

Please try to group related changes into single pull requests
and create additional ones if necessary.


### `.rst` Style guidelines

Not all the files in this project
follow these guidelines yet,
as we established them
after a large portion of this guide had been written already.
If you find any style inconsistencies,
please file a report or send a pull request to fix them.

#### Line Widths

Lines MUST NOT be longer than 80 characters,
except for tables, urls and code blocks.

Split the text using [semantic linefeeds][].
This file can serve as an example.

[semantic linefeeds]: http://rhodesmill.org/brandon/2012/one-sentence-per-line/

#### Enumerations

- Unnumbered lists SHOULD use the following hierarchy:

  ```rst
  -
     *
  ```

- Numbered lists SHOULD use `#.` when possible:

  ```rst
  #. This is the first item,
     but it may change places
     in the future.
  #. Using ``#.``,
     we can swap lines around
     without worrying about numbering.
  ```

#### Indentation

Blocks SHOULD be indented by 3 spaces,
but visual indentation is preferred.

*Examples:*

```rst
- This sentence can be split
  using a semantic linefeed,
  as mentioned earlier.

#. The very same thing applies to this line,
   but it uses a three-spaces indent instead.

.. This is a multiline comment,
   properly indented.
   Yeah.

.. directive::
   :option:

   Text goes here.

:Hello: This field has a short field name,
        so aligning the body text
        with the first line
        is ok.

:Number-of-African-swallows-required-to-carry-a-coconut:
   It would be awkward
   to align the field's body
   with the right edge
   of the first line.

   In this case
   it's discouraged
   to begin a field's body 
   on the same line as the marker.
```

#### Headings

The following heading styles
MUST be used in the displayed order
for technical reasons
(e.g. h3 must come after h2 or higher,
and **not** after h1).

```rst
===========
 Heading 1
===========

Heading 2
=========

Heading 3
*********

Heading 4
---------
```

#### File Paths

File paths (relative or absolute)
MUST be specified like this:

    :file:`{Packages}/SomePackage/somefile.ext`

Variable parts (`{name}`) may be used freely,
but you will come across these frequently:

- `{Data}`
- `{Packages}`
- `{User}`
- `{Default}`

All paths MUST be written with forward slashes
unless they are meant to be used in Windows.

File extensions (when referring to file types)
MUST be written like this:

    ``.ext``

#### Shortcut Keys

Except for the special OS X bindings site,
all shortcut keys use the `:kbd:` role:

```
:kbd:`Ctrl + T`
```

All key names are written in TitleCase
and all key bindings MUST refer
to the default for Windows.

#### Sublime Text-specific

- Commands in the command palette
  MUST be written as follows:

  ```rst
  **Preferences: Settings - User**
  ```

- Menu items (in the main menu by default)
  MUST be written as follows (notice the `→`):

  ```rst
  *Preferences → Package Settings → ...*
  ```

#### Comments

The following comment 'keywords' may be used
*at the beginning* of a comment
to mark a section for review:

- XXX
- TODO

Examples:

```rst
.. TODO
   - Add some screenshots

.. XXX Does anyone really need this?
```
