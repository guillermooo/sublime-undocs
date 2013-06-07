================================
Search and Replace - Single File
================================

.. _snr-search-buffer:

Searching
=========

To open the **search panel** for buffers, press :kbd:`Ctrl + F`. Some options in
the search panel and search actions can be controlled with the keyboard:

==========================	====================
Toggle Regular Expressions	:kbd:`Alt + R`
Toggle Case Sensitivity   	:kbd:`Alt + C`
Toggle Exact Match       	:kbd:`Alt + W`
Find Next					:kbd:`Enter`
Find Previous				:kbd:`Shift + Enter`
Find All					:kbd:`Alt + Enter`
==========================	====================

.. _snr-incremental-search-buffer:

Incremental Search
==================

The **incremental search panel** can be brought up with :kbd:`Ctrl + I`. The only
difference with the regular search panel lies in the behavior of the :kbd:`Enter``
key: in incremental searches, it will select the next match in the buffer and
dismiss the search panel for you. Choosing between this panel or the regular
search panel is mainly a matter of preference.


.. _snr-replace-buffer:

Replacing Text
==============

You can open the replace planel with :kbd:`Ctrl + H`.

==========================	=========================
Replace All:				:kbd:`Ctrl + Alt + Enter`
==========================	=========================

.. XXX no key binding for replacing once?


.. _snr-tips-buffer:

Tips
====

Other Ways of Searching in Buffers
----------------------------------

:ref:`Goto Anything <fm-goto-anything>` provides the operator ``#`` to search in
the current buffer, see :ref:`fm-goto-directives`.

Other Key Bindings to Search in Buffers
---------------------------------------

These keybindings work when the search panel is hidden.

===============================================	=================
Search Forward Using Most Recent Pattern 		:kbd:`F3`
Search Backwards Using Most Recent Pattern		:kbd:`Shift + F3`
Select All Matches Using Most Recent Pattern	:kbd:`Alt + F3`
===============================================	=================

.. XXX search under cursor ??

.. _snr-multiline-search:

Multiline Search
----------------

You can type a multiline search pattern. To enter a newline character, press
:kbd:`Ctrl + Enter` in the search panel. Note that the search panel is resizable
too.
