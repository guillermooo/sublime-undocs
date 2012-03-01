==============
Basic Concepts
==============

Here we'll explain concepts that the reader needs to be familiar with in order
to fully understand the contents of this guide.

Conventions in This Guide
==========================

This guide is written from the perspective of a Windows user, but most
instructions should only require trivial changes to work on other platforms.

Relative paths (e. g. *Packages/User*) start at the *data directory* unless
otherwise noted. The *data directory* is explained further below.

We assume default key bindings when indicating keyboard shortcuts. Due to the
way Sublime Text maps keys to commands, **some key bindings won't match your
locale's keyboard layout**.


With Great Power Comes Lots of Questions
========================================

Sublime Text is a very extensible and customizable editor. It does many things
out of the box, but if you spend some time tailoring it to your exact needs,
it will give you superpowers. This guide will teach you all you need to know
to configure Sublime Text.

In the following paragraphs, we'll outline some aspects that won't click in
your mind until you've spent some time using Sublime Text. Keep exploring the
editor and looking around in this guide, and everything will fall into place
at some point.

Sublime Text is undeniably a versatile tool for programmers, but you don't
need to be one to use it, or even to configure it to make it the perfect tool
for your writing. If you're a hacker, however, you are about to spend the
remainder of your day playing around with this editor.


The *Data* Directory
====================

Sublime Text 2 stores nearly all of the interesting files for users under the
data directory. This is a platform-dependent location:

* **Windows**: *%APPDATA%\\Sublime Text 2*
* **OS X**: *~/Library/Application Support/Sublime Text 2*
* **Linux**: *~/.config/sublime-text-2*

For **portable installations**, look inside *Sublime Text 2/Data*. Here, the
*Sublime Text 2* part refers to the directory to which you've extracted the
contens of the compressed file containing Sublime Text 2.

Note that only for portable installations does a directory named *Data* exist.
For the other types of installation, the data directory is the location
indicated above.

The *Packages* Directory
==============================

This is a **key directory**: all resources for supported programming and
markup languages are stored here. A *package* is a directory containing
related files having a special meaning to Sublime Text.

You can access the packages directory from the Sublime Text 2 menu
(**Preferences | Browse Packages...**), or by means of an api call:
``sublime.packages_path()``. In this guide, we refer to this location as
*Packages*, *packages path*, *packages folder* or *packages directory*.

The ``User`` Package
^^^^^^^^^^^^^^^^^^^^

*Packages/User* is a catch-all directory for custom plugins, snippets,
macros, etc. Consider it your personal area in the packages folder. Sublime
Text 2 will never overwrite the contents of *Packages/User* during upgrades.


The Python Console and the Python API
=====================================

This information is especially interesting for programmers. For the rest of
Sublime Text 2 users, you just need to know that Sublime Text enables users
with programming skills to add their own features to the editor. (So go learn
how to program; it's great fun!)

Sublime Text 2 comes with an embedded Python interpreter. It's an useful tool
to inspect Sublime Text 2 settings and to quickly test API calls while you're
writing plugins.

To open the Python console, press ``Ctrl+``` or select **View | Show Console**
in the menu.

Confused? Let's try again more slowly:

*Python* is a programming language known to be easy for beginners and very
powerful at the same time. *API* is short for ‘Application Programming
Interface', which is a fancy way of saying that Sublime Text 2 is prepared to
be programmed by the user. Put differently, Subime Text gives the user access
to its internals through Python. Lastly, a *console* is a little window inside
Sublime Text which lets you type in short snippets of Python code and run them.
The console also shows text output by Sublime Text or its plugins.

Your System's Python vs the Sublime Text 2 Embedded Python
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

On **Windows** and **Linux**, Sublime Text 2 comes with its own Python
interpreter and it's separate from your system's Python installation.

On **OS X**, the system Python is used instead. Modifying your system version
of Python, such as replacing it with the MacPorts version, can cause problems
for Sublime Text.

The embedded interpreter is intended only to interact with the plugin API, not
for general development.


Packages, Plugins, Resources and Other Things That May Not Make Sense to You Now
================================================================================

For now, just keep in mind that almost everything in Sublime Text can be adapted
to your needs. This vast flexibility is the reason why you will learn about so
many settings files: there simply must be a place to specify all your preferences.

Configuration files in Sublime Text let you change the editor's behavior, add
macros, snippets or create new features --where *feature* means ‘anything you can
think of'. Ok, maybe not *anything*, but Sublime Text definitely hands you over
a good deal of control.

These settings files are simply text files following a special structure or
*format*: JSON dominates, but you'll find XML files too.

In this guide, we refer collectively to all these disparate configuration
files as *resources*. Sublime Text will look for resources inside the packages
directory. To keep things tidy, the editor has a notion of a *package*, which
is a directory containing resources that belong together (maybe they all help
write emails faster or code in a certain programming language).


Textmate Compatibility
======================

This information is mainly useful for Textmate users who are now using Sublime
Text. Textmate was an editor for the Mac.

Sublime Text 2 is fairly compatible with Textmate bundles with the notable
exception of commands. Additionally, Sublime Text requires all syntax
definitions to have the *.tmLanguage* extension, and all preferences files to
have the *.tmPreferences* extension. This means that *.plist* files will be
ignored, even if they are located under a *Syntaxes* or *Preferences*
subdirectory.


Vi Emulation
============

This information is mainly useful for dinosaurs and people who like to drop
the term RSI in conversations. Vi is an ancient modal editor that lets the
user perform all operation from the keyboard. Vim, a modern version of vi,
is still in widespread use.

Sublime Text provides vi emulation through the *Vintage* package. The Vintage
package is *ignored* by default. Read more about Vintage_ in the official
documentation.

.. _Vintage: http://www.sublimetext.com/docs/2/vintage.html


Be Sublime, My Friend
=====================

Borrowing from `Bruce Lee's wisdom`_, Sublime Text 2 can become almost anything
you need it to be. In skilled hands, it can defeat an army of ninjas without
your breaking a sweat. So... empty your mind; be sublime, my friend.

.. _Bruce Lee's wisdom: http://www.youtube.com/watch?v=iO3sBulXpVw
