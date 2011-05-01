==============
Basic Concepts
==============

In these pages we use several forms of *shorthand* and make a few
assumptions. Below we explain them in full, in addition to describing
fundamental aspects of the Sublime Text 2 editor. All this information will
enable you to understand better the content of this guide.

The :file:`Data` Directory
==========================

Sublime Text 2 stores nearly all of the interesting files for users under the
data directory. This is a platform-dependent location:

* **Windows**: :file:`%APPDATA%\\Sublime Text 2`
* **OS X**: :file:`~/Library/Application Support/Sublime Text 2`
* **Linux**: :file:`~/.Sublime Text 2`
* **Portable Installation**: :file:`Sublime Text 2/Data`

The :file:`Packages` Directory
==============================

This is a location within the data directory that we'll keep referring to again
and again. You can obtain it by means of an API call:
``sublime.packages_path()``. In this guide, we refer to this location
as ``Packages``, *packages path* or *packages folder*.

The ``User`` Package
^^^^^^^^^^^^^^^^^^^^

:file:`Packages/User` is a catch-all directory for custom plugins, snippets,
macros, etc. Consider it your personal area in the packages folder. Sublime
Text 2 will never overwrite the contents of ``Packages/User`` during upgrades.

The Python Console
==================

Sublime Text 2 has an embedded Python interpreter. You will find yourself
turning to it often in order to inspect Sublime Text 2 settings and to quickly
test API calls while you're writing plugins.

To open the Python console, press :kbd:`Ctrl+`` or select **View | Show Console**
in the menu.

Your System's Python vs Sublime Text 2 Embedded Python
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sublime Text 2 comes with its own Python interpreter and it's separate from
your system's Python installation. This embedded interpreter is intended only
to interact with the plugin API, not for general development.

Textmate Compatibility
======================

Sublime Text 2 is compatible with Textmate snippets, color schemes,
``.tmLanguage`` files and ``.tmPreferences`` files.

Be Sublime, My Friend
=====================

Borrowing from `Bruce Lee's wisdom`_, Sublime Text 2 can become almost anything
you need it to be. In skilled hands, it can defeat an army of ninjas without
your breaking a sweat. Empty your mind. Be sublime, my friend.

.. _Bruce Lee's wisdom: http://www.youtube.com/watch?v=OW-cnizLDEE