# Contribution guidelines


## Issue

Even though it's very unlikely,
please search through the existing issues
and look for existing similar ones
before submitting your own.


## Pull request

Please try to group related changes into single pull requests
and great additional ones if necessary.


### `.rst` Style guidelines

Please note that
some files might not follow all these guidelines yet
since we established them at a later point.
If you encounter inconsistencies,
please report or file a pull request to fix them.

#### Line Width

All lines must be 80 characters long or less.

When writing text,
try to split it using [semantic linefeeds][].
As an example,
this file does it as well.

[semantic linefeeds]: http://rhodesmill.org/brandon/2012/one-sentence-per-line/

#### Enumerations

- Unnumbered enumerations should use the following hierarchy:

  ```rst
  -
     *
  ```

- Numbered enumerations should use `#.` when possible:

  ```rst
  #. This will be the first entry, but we might change this in the future.
  #. Using ``#.`` allows us to swap lines without having to change the numbers.
  ```

#### Indentation

Generally, blocks are indented by 3 spaces
but visual indentation is preferred.

*Examples:*

```rst
- This sentence can be split
  using a semantic linefeed
  which we mentioned earlier.

1. The very same thing applies to this line
   but it uses a three-spaces indent instead.

.. This is a multi-line comment,
   properly indented.
   Yeah.

.. directive::
   :option:

   Text will be here.

:Hello: This field has a short field name,
        so aligning the field body
        with the first line
        is feasible.

:Number-of-African-swallows-required-to-carry-a-coconut:
   It would be very difficult
   to align the field body
   with the left edge
   of the first line.
   It's mostly preferable
   not to begin the body
   on the same line as the marker.
```

The [Wrap Plus][] package helps with this,
but currently not with definition lists.

[Wrap Plus]: https://sublime.wbond.net/packages/Wrap%20Plus

#### Headers

The following header styles should be used in the displayed order.
For technical reasons you **must** follow the exact hierarchy,
e.g. h3 must come after h2 or higher and **not** after h1.

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

File paths (relative or absolute) are specified like this:

    :file:`{Packages}/SomePackage/somefile.ext`

`{variables}` may be used arbitrarily,
but the following path prefixes are known:

- `{Data}`
- `{Packages}`
- `{User}`
- `{Default}`

All paths use forward slashes
unless designated specifically for Windows.

File extensions (when referring to file types) look like:

    ``.ext``

#### Shortcut Keys

Except for the special OSX bindings site,
all shortcut keys use the `:kbd:` role:

```
:kbd:`Ctrl + T`
```

All key parts are written in TitleCase
and all key bindings should refer to the default for Windows.

#### Sublime Text-specific

- Commands in the command palette are referenced as follows:

  ```rst
  **Preferences: Settings - User**
  ```

- Menu items (in the main menu by default) are specified like so (notice `→`):

  ```rst
  *Preferences → Package Settings → ...*
  ```

#### Comments

The following comment "keywords" may be used
*at the beginning* of a comment
to mark a section for a revisit:

- XXX
- TODO
