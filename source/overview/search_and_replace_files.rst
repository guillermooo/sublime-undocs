===========================
Search and Replace in Files
===========================

.. _snr-search-files:

Searching
=========

To open the search panel for files, press ``Ctrl + Shift + F``. You can use the
keyboard to control the search panel:

Toggling Options
----------------

* Regular Expressions: ``Alt + R``
* Case Sensitivity: ``Alt + C``
* Exact Match: ``Alt + W``

Search Actions
--------------

* Find Next: ``Enter``


.. _snr-search-scope-files:

Search Scope
============

The **Where** field in the search panel determines where to search. You can
define the scope of the search in several ways:

* Adding individual directories (Unix-style paths, even on Windows)
* Adding/excluding files based on a pattern
* Adding  abstract locations (``<open folders>``, ``<open files>``)

You can combine these filters separing them with commas, for example:

	/C/Users/Obama/Top Secret,-*.html,<open files>

Press the **...** button in the search panel to display a menu containing
these options.

.. xxx what kind of patterns are those?
.. xxx special locations?
.. xxx unix on windows too?
.. xxx link to reference to fulloptions


.. _snr-results-display-files:

Options to Display Results
==========================

In the search panel, you can find the following options to customize the
results format:

* Show in Separate Buffer/Output Panel
* Show Context


.. _snr-results-navigation-files:

Navigating Results
==================

If the search yields matches, you can move through the sequence like this:

* Next Match: ``F4``
* Previous Match: ``Shift + F4``
