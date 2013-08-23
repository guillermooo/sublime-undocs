==================
Search and Replace
==================

Sublime Text features two main types of search:

.. toctree::
   :maxdepth: 1

	Search - Single File <search_and_replace>
	Search - Multiple Files <search_and_replace_files>

We'll examine them in turn, but first let's talk about a powerful tool for searching
text: regular expressions.

.. _snr-regexes:

Regular Expressions
===================

Regular Expressions find complex *patterns* in text. To take full advantage of
the search and replace facilities in Sublime Text, you should at least learn
the basics of regular expressions. In this guide we won't explain how to use
regular expressions.

Typing out *regular expression* gets boring fast, and saying it actually is
even more annoying, so instead nerds usually shorten that to *regexp* or *regex*.

This is how a regex might look::

	(?:Sw|P)i(?:tch|s{2})\s(?:it\s)?of{2}!

Regexes are known to hurt people's feelings.

To use regular expressions, first you need to activate them in the various
search panels. Otherwise, the search term will be interpreted literally.

Sublime Text uses the `Boost syntax`_ for regular expressions.

.. _Boost syntax: http://www.boost.org/doc/libs/1_47_0/libs/regex/doc/html/boost_regex/syntax/perl_syntax.html
