==================
Search and Replace
==================

Sublime Text features
two main types of searches:

.. toctree::
   :maxdepth: 1

	Search - Single File <search_and_replace>
	Search - Multiple Files <search_and_replace_files>


.. _snr-regexes:

Regular Expressions
===================

Search functions in Sublime Text
support regular expressions,
a powerful tool for searching and replacing text.
Regular Expressions find complex *patterns* in text.

Regular expression patterns are composed
of symbols and special constructs.
To the non-initiated,
regular expression patterns look undecipherable
because common characters double as operators
and cannot always be interpreted literally.

This is how a regular expression might look::

   (?:Sw|P)i(?:tch|s{2})\s(?:it\s)?of{2}!

The term *regular expression*
is usually shortened to *regexp* or *regex*.

To take full advantage
of the search and replace facilities in Sublime Text,
you should at least learn
the basics of regular expressions.
This guide doesn't teach you
how to use regular expressions.

The **Replace** box in a search and replace panel
also supports special symbols
called *format strings*
that look similar to regular expressions.
Format strings allow you to perform
complex text transformations
before inserting the result into the buffer.

Sublime Text uses the
Perl Compatible Regular Expressions (PCRE) engine
from the Boost library
to power regular expressions in search panels.


Using Regular Expressions in Sublime Text
=========================================

To use regular expressions in Sublime Text,
first activate them in
the corresponding search panel
by clicking on the available buttons
or using keyboard shortcuts.

If you don't activate regular expressions
before performing a search,
the search terms will be interpreted literally.

.. figure:: search-and-replace-regex-sample.png

   A search panel with the regular expressions option enabled

.. seealso::

	`Boost library documentation for regular expressions <http://www.boost.org/doc/libs/1_44_0/libs/regex/doc/html/boost_regex/syntax/perl_syntax.html>`_
		Documentation on regular expressions.

	`Boost library documentation for format strings <http://www.boost.org/doc/libs/1_44_0/libs/regex/doc/html/boost_regex/format/perl_format.html>`_
		Documentation on format strings. Note that Sublime Text additionally
		interprets :samp:`\\{n}` as :samp:`${n}`.
