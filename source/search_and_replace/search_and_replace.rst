================================
Search and Replace - Single File
================================

.. _snr-search-buffer:

Searching
=========

To open the **search panel** for buffers, press :kbd:`Ctrl + F`. Some options
and actions available through this panel can be controlled from the keyboard:

==========================  ====================
Toggle Regular Expressions  :kbd:`Alt + R`
Toggle Case Sensitivity     :kbd:`Alt + C`
Toggle Exact Match          :kbd:`Alt + W`
Find Next                   :kbd:`Enter`
Find Previous               :kbd:`Shift + Enter`
Find All                    :kbd:`Alt + Enter`
==========================  ====================

.. _snr-incremental-search-buffer:

Incremental Search
==================

The **incremental search panel** can be brought up with :kbd:`Ctrl + I`. The only
difference with the regular search panel lies in the behavior of the :kbd:`Enter``
key. In incremental searches, it will select the next match in the file and dismiss
the search panel for you. Choosing between this panel or the regular search
panel is mainly a matter of preference.


.. _snr-replace-buffer:

Replacing Text
==============

To open the replace planel, press :kbd:`Ctrl + H`. Some actions available through
this panel can be controlled from the keyboard.

==========================  =========================
Replace All:                :kbd:`Ctrl + Alt + Enter`
Replace Next:               :kbd:`Ctrl + Shift + H`
==========================  =========================


.. _snr-tips-buffer:

Tips
====


Other Ways of Searching in Files
--------------------------------

:ref:`Goto Anything <fm-goto-anything>` provides the operator ``#`` to search in
the current buffer.


Other Search-Related Key Bindings
---------------------------------

These key bindings work when the search panel is hidden.

=============================================== =================
Search Forward Using Most Recent Pattern        :kbd:`F3`
Search Backwards Using Most Recent Pattern      :kbd:`Shift + F3`
Select All Matches Using Most Recent Pattern    :kbd:`Alt + F3`
=============================================== =================

.. XXX search under cursor ??

.. _snr-multiline-search:

Multiline Search
----------------

You can type in multiline search patterns into search panels. To enter newline
characters, press :kbd:`Ctrl + Enter`. Note that search panels are resizable.
