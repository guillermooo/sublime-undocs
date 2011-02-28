Basic Concepts
==============

.. Keep Sublime Text 2 here and use Sublime Text in the rest of the docs.

While reading these pages, you will come across several forms of *shorthand writing*
and assumptions. Here we explain those in full in addition to describing fundamental
aspects of Sublime Text 2.

Data Directory
**************

Sublime Text 2 stores nearly all of the interesting files for users under the
data directory. This is a platform-dependent location:

* **Windows**: ``%APPDATA%\Sublime Text 2``
* **OS X**: ``~/Library/Application Support/Sublime Text 2``
* **Linux**: ``~/.Sublime Text 2``

.. note::
	If you're running a portable installation of Sublime Text 2, the data
	directory will be inside the ``Data`` directory of your installation.

The Packages/Path
^^^^^^^^^^^^^^^^^

This is a location within the data directory that we'll keep referring to in
these pages. You can obtain it by means of an API call:``sublime.packages_path()``.
In this guide, we refer to this location as ``Packages``, the *packages path*
or the *packages folder*.

The ``User`` Package
^^^^^^^^^^^^^^^^^^^^

``Packages/User`` is a catch-all directory for custom plugins, snippets, macros,
etc. Consider it your personal area in the packages folder.

Sublime Text 2 will never overwrite the contents of the ``Packages/User``
during upgrades.

The Python Console
******************

Sublime Text 2 has an embedded Python interpreter. You will find yourself turning
to it often in order to inspect Sublime Text 2 settings and quickly test API calls
while you're writing plugins.

To open the Python console, press ``CTRL + ```.

Your System's Python vs Sublime Text 2 Embedded Python
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sublime Text 2 comes with its own Python interpreter and it's separate from your
system's Python installation. This embedded interpreter is intended only to
interact with the plugin API, not for general development.

TextMate Compatibility
**********************

Sublime Text 2 is compatible with TextMate snippets, color schemes,
``.tmLanguage`` files and ``.tmPreferences`` files.

Be Sublime, My Friend
*********************

Borrowing from `Bruce Lee's wisdom`_, Sublime Text 2 can be bent and twisted in
many ways to become your perfect weapon. In skilled hands, it can defeat an
army of ninjas without breaking a sweat. Empty your mind. Be sublime, my friend.

.. _Bruce Lee's wisdom: http://www.youtube.com/watch?v=7ijCSu87I9k&feature=related