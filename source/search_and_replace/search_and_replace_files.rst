===================================
Search and Replace - Multiple Files
===================================

.. _snr-search-files:

Searching
=========

To open the search panel for files, press ``Ctrl + Shift + F``. You can use the
keyboard to control the search panel and some search actions:

==========================	===========
Toggle Regular Expressions	``Alt + R``
Toggle Case Sensitivity		``Alt + C``
Toggle Exact matches		``Alt + W``
Find Next					``Enter``
==========================	===========

.. _snr-search-scope-files:

Search Scope
============

The **Where** field in the search panel determines where to search. You can
define the scope of the search in several ways:

* Adding individual directories (Unix-style paths, even on Windows)
* Adding/excluding files based on a pattern
* Adding  symbolic locations (``<open folders>``, ``<open files>``)

You can combine these filters separating them with commas, for example:

	/C/Users/Joe/Top Secret,-*.html,<open files>

Press the **...** button in the search panel to display a menu containing
these options.

.. xxx what kind of patterns are those?
.. xxx special locations?
.. xxx unix on windows too?
.. xxx link to reference to fulloptions

.. _snr-results-format-files:

Results Format
==============

In the search panel, you can find the following options to customize the
results format:

* Show in Separate Buffer/Output Panel
* Show Context


.. _snr-results-navigation-files:

Navigating Results
==================

If the search yields matches, you can move through the sequence using the
following key bindings:

================	==============
Next match			``F4``
Previous match		``Shift + F4``
================	==============
