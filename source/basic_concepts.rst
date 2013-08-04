==============
Basic Concepts
==============

Overview
========

To fully understand the rest of this guide, you need to be familiar with the
concepts presented in this section.


Conventions
===========

Written from the perspective of a Windows user, most instructions will only
require trivial changes to work on other platforms.

Relative paths, like *Packages/User*, start at the *data directory* unless
otherwise noted. The *data directory* is explained further below.

We assume default key bindings when indicating keyboard shortcuts. If you're
using a non-English keyboard layout, note that **some key bindings won't match
your locale's keyboard**. This is due to the way Sublime Text maps keys to
commands.


With Great Power Comes A Lot of Questions
=========================================

Unquestionably a versatile tool for programmers, you don't need to be one in
order to use Sublime Text, or even to configure it extensively. If you're a
hacker, however, you are in for a great many pleasant surprises.

Sublime Text can be infinitely customized and extended. You can start using it
efficiently out of the box, but spending some time tailoring it to your exact
needs will pay off great dividends.

This guide will teach you how to configure Sublime Text.

You won't master Sublime Text in a day, but it's built on a handful of
pervasive ideas that make for a consistent and easily understandable system.

In the following paragraphs, we'll outline a few key aspects that won't click
in your mind until you've spent some time using the editor. Keep
experimenting, keep looking around in this guide, and, eventually, everything
will fall into place.


The *Data* Directory
====================

Nearly all of the interesting files for users live under the data directory.
This is a platform-dependent location:

.. XXX I'm using the portable installation, so double check this.

* **Windows**: *%APPDATA%\\Sublime Text 3*
* **OS X**: *~/Library/Application Support/Sublime Text 3*
* **Linux**: *~/.config/sublime-text-3*

For **portable installations**, look inside *Sublime Text 3/Data*. Here, the
*Sublime Text 3* part refers to the directory to which you've extracted the
compressed portable files.

Note that only in portable installations does a directory named *Data* exist.
For the remaining installation types, the data directory is the location
indicated above.


The *Packages* Directory
==============================

This is a **key directory**: all resources for supported programming and
markup languages are stored here. A *package* is a directory containing
related files having a special meaning for Sublime Text.

You can access the packages directory from the main menu
(**Preferences | Browse Packages...**), or by means of an API call:
``sublime.packages_path()``. In this guide, we refer to this location as
*Packages*, *packages path*, *packages folder* or *packages directory*.

The ``User`` Package
^^^^^^^^^^^^^^^^^^^^

*Packages/User* is a catch-all directory for custom plugins, snippets,
macros, etc. Consider it your personal area in the packages folder. Sublime
Text will never overwrite the contents of *Packages/User* during upgrades.


The Python Console and the Python API
=====================================

This information is especially interesting for programmers. For other users,
you just need to know that Sublime Text enables users with programming skills
to add their own features to the editor. (So go learn how to program; it's
great fun!)

Sublime Text comes with an embedded Python interpreter. It's an useful tool
to inspect the editor's settings and to quickly test API calls while
developing plugins.

To open the Python console, press ``Ctrl+``` or select **View | Show Console**
from the main menu.

Confused? Let's try again more slowly:

*Python* is a programming language known to be easy for beginners and very
powerful at the same time. *API* is short for 'Application Programming
Interface', which is a fancy way of saying that Sublime Text 3 is prepared to
be programmed by the user. Put differently, Subime Text gives the user access
to its internals through Python. Finally, a *console* is a little window
inside Sublime Text that lets you type in short snippets of Python code and
run them. The console also shows text output by Sublime Text or its plugins.

Your System's Python vs the Sublime Text 3 Embedded Python
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. XXX Double check this
On **Windows** and **Linux**, Sublime Text 3 comes with its own Python
interpreter and it's separate from your system's Python installation.

On **OS X**, the system Python is used instead. Modifying your system version
of Python, such as replacing it with the MacPorts version, can cause problems
for Sublime Text.

The embedded interpreter is intended only to interact with the plugin API, not
for general development.


Packages, Plugins, Resources and Other Things That May Not Make Sense to You Now
================================================================================

Almost every aspect of Sublime Text can be tweaked, extended or customized.
This is all you need to understand for now. Well, that and that this vast
flexibility is the reason why you'll learn about so many configuration files:
there simply must be a place to specify all your preferences.

Among other things, you can modify the editor's behavior, add macros and
snippets, extend menus... and even create whole new features --where *feature*
means 'anything you can think of'. OK, right, there might be things you can't
do, but you're definitely spoiled for choice.

These configuration files are simple text files following a special structure
or *format*: JSON predominates, but you'll find XML files and Python files
too.

In this guide, for brevity we refer collectively to all these disparate
configuration files as *resources*.

Sublime Text will look for resources inside the packages folder. To keep
things tidy, the editor has a notion of a *package*, which is a folder
containing resources that belong together (maybe they all help compose emails
faster, write HTML efficiently, enhance the coding experience for C, Ruby,
Go...).


Textmate Compatibility
======================

This information is mainly useful for Textmate expats who've found a new home
in Sublime Text. Textmate is an editor for the Mac.

Sublime Text compatibility with Textmate bundles is good excluding commands,
which are incompatible. Additionally, Sublime Text requires all syntax
definitions to have the *.tmLanguage* extension, and all preferences files to
have the *.tmPreferences* extension. This means that *.plist* files will be
ignored, even if they are located under a *Syntaxes* or *Preferences*
subdirectory.


Vi/Vim Emulation
================

This information is mainly useful for dinosaurs and people who like to drop
the term RSI in conversations. Vi is an ancient modal editor that lets the
user perform all operations from the keyboard. Vim, a modern version of vi,
is still in widespread use.

Sublime Text provides vi emulation through the *Vintage* package. The Vintage
package is *ignored* by default. Read more about Vintage_ in the official
documentation.

An evolution of Vintage called Vintageous_ offers a better Vi editing
experience and is updated more often than Vintage. Vintageous_ is an open
source project, just as Vintage_.

.. _Vintage: http://www.sublimetext.com/docs/3/vintage.html
.. _Vintageous: http://guillermooo.bitbucket.org/Vintageous


Emacs
=====

This information is hardly useful for anyone. Emacs is... Well, nobody really
knows what emacs is, but some people edit text with it.

If you are an emacs user, you're probably not reading this.


Be Sublime, My Friend
=====================

Borrowing from `Bruce Lee's wisdom`_, Sublime Text can become almost anything
you need it to be. In skilled hands, blah, blah, blah.

Empty your mind; be sublime, my friend.

.. _Bruce Lee's wisdom: http://www.youtube.com/watch?v=7ijCSu87I9k
