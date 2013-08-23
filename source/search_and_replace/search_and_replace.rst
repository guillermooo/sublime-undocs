================================
Search and Replace - Single File
================================

.. _snr-search-buffer:

Searching
=========

To open the **search panel** for buffers, press ``Ctrl + F``. Some options in
the search panel and search actions can be controlled with the keyboard:

==========================	===========
Toggle Regular Expressions	``Alt + R``
Toggle Case Sensitivity   	``Alt + C``
Toggle Exact Match       	``Alt + W``
Find Next					``Enter``
Find Previous				``Shift + Enter``
Find All					``Alt + Enter``
==========================	===========

.. _snr-incremental-search-buffer:

Incremental Search
==================

The **incremental search panel** can be brought up with ``Ctrl + I``. The only
difference with the regular search panel lies in the behavior of the ``Enter``
key: in incremental searches, it will select the next match in the buffer and
dismiss the search panel for you. Choosing between this panel or the regular
search panel is mainly a matter of preference.


.. _snr-replace-buffer:

Replacing Text
==============

You can open the replace planel with ``Ctrl + H``.

==========================	======================
Replace All:				``Ctrl + Alt + Enter``
==========================	======================

.. xxx no key binding for replacing once?


.. _snr-tips-buffer:

Tips
====

Other Ways of Searching in Buffers
----------------------------------

.. todo: link to goto anything section

Goto Anything provides the operator ``#`` to search in the current
buffer. The search term will be the part following the ``#`` operator.

Other Key Bindings to Search in Buffers
---------------------------------------

These key bindings work when the search panel is hidden.

===============================================	==============
Search Forward Using Most Recent Pattern 		``F3``
Search Backwards Using Most Recent Pattern		``Shift + F3``
Select All Matches Using Most Recent Pattern	``Alt + F3``
===============================================	==============

.. search under cursor ??

Multiline Search
----------------

You can type a multiline search pattern. To enter a newline character, press
``Ctrl + Enter`` in the search panel. Note that the search panel is resizable
too.
