================================
Search and Replace – Single File
================================

.. _snr-search-buffer:

Searching
=========

Keyboard shortcuts related to the search panel:

==========================  ====================
**Open search panel**       Ctrl + F
Toggle regular expressions  Alt + R
Toggle case sensitivity     Alt + C
Toggle exact match          Alt + W
Find next                   Enter
Find previous               Shift + Enter
Find all                    Alt + Enter
==========================  ====================

.. _snr-incremental-search-buffer:

Incremental Search
==================

Keyboard shortcuts related to the incremental search panel:

=================================  ====================
**Open incremental search panel**  Ctrl + I
Toggle regular expressions         Alt + R
Toggle case sensitivity            Alt + C
Toggle exact match                 Alt + W
Find next                          Enter
Find previous                      Shift + Enter
Find all                           Alt + Enter
=================================  ====================

The only difference between this panel
and the regular search panel
lies in the behavior of the :kbd:`Enter` key.
In incremental searches,
it will select the next match in the file
and dismiss the search panel for you.
Choosing between this panel or the regular search panel
is a matter of preference.


.. _snr-replace-buffer:

Replacing Text
==============

Keyboard shortcuts related to the replace panel:

==========================  ====================
**Open replace panel**      Ctrl + H
Replace next                Ctrl + Shift + H
Replace all                 Ctrl + Alt + Enter
==========================  ====================


.. _snr-tips-buffer:

Tips
====


Other Ways of Searching in Files
--------------------------------

:ref:`Goto Anything <fm-goto-anything>`
provides the operator ``#``
to search in the active file.


Other Search-Related Key Bindings
---------------------------------

These key bindings work
when the search panel is hidden:

=============================================== =================
Search forward using most recent pattern        F3
Search backwards using most recent pattern      Shift + F3
Select all matches using most recent pattern    Alt + F3
=============================================== =================

You can also perform searches
based on the current selection:

=================================== ==================
Search using current selection      Ctrl + E
Replace using current selection     Ctrl + Shift + E
=================================== ==================

.. _snr-multiline-search:

Multiline Search
----------------

You can type in multiline search patterns
into search panels.
To enter newline characters,
press :kbd:`Ctrl + Enter`.

.. figure:: search-and-replace-multiline.png

   A multiline pattern

Note that search panels are resizable too.
