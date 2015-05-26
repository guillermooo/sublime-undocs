==============
Basic Concepts
==============


Overview
========

To fully understand the rest of this guide,
you need to be familiar
with the concepts presented in this section.


General Conventions
===================

This guide is written from the perspective of a Windows user.
Most instructions will only require trivial changes
to work on other platforms.

Unless otherwise noted,
relative paths (for example, :file:`Packages/User`)
start at `the Data Directory`_.

We assume default key bindings
when indicating keyboard shortcuts.
If you are using a non-US-English keyboard layout,
some key bindings may not match your layout.
This is due to the way Sublime Text
processes key strokes internally.


Mastering Sublime Text Takes Time
=================================

Mastering Sublime Text requires time and practice.
Luckily, it's built around
a handful of concepts
that make for a consistent
system once all the pieces come together.

This guide will teach you
how to use and configure Sublime Text.

Sublime Text is a versatile editor for programmers,
but you don't need to be one
in order to use it,
and you don't need
to configure it extensively to be productive—it's an efficient tool out of the box.
Hackers, however, will appreciate
all the customization and extensibility opportunities.

In the following paragraphs,
we'll outline key aspects
that you'll get familiar with
after you've spent some time using the editor.

.. _data-directory:

The *Data* Directory
====================

Nearly all of the interesting files for users
live under the *data directory*.
The data directory is
a platform-dependent location:

* **Windows**: :file:`%APPDATA%\\Sublime Text 3`
* **OS X**: :file:`~/Library/Application Support/Sublime Text 3`
* **Linux**: :file:`~/.config/sublime-text-3`

If you're using the **portable version** (Windows only),
look for :file:`{Application}/Data`.
Here, ``Application``
refers to the directory
to which you've extracted
the compressed portable files
and where the executable resides.

Note that the :file:`Data` directory
only exists with that name
in the portable version.
In full installations,
it is one of the locations
indicated above.


The *Packages* Directory
========================

This is a key directory
located under the data directory.
All resources for supported programming
and markup languages
are stored here.

(More on *packages* and *resources* :doc:`later </extensibility/packages>`.)


You can access the packages directory
from the main menu (**Preferences → Browse Packages...**),
by means of an API call (``sublime.packages_path()``),
and by other means
that will be explained in later topics.

In this guide, we refer to the packages folder
as *Packages*, *packages path*, *packages folder* or *packages directory*.


The *User* Package
******************

:file:`{Packages}/User` is a catch-all directory
for custom plugins, snippets, macros, etc.
Consider it your personal area
in the packages folder.
Additionally, it will contain
most of your personal application or plugin settings.

Updates to Sublime Text will never
overwrite the contents of :file:`{Packages}/User`.


Sublime Text is Programmable
============================

This information is useful for programmers.
Other users just need to know
that Sublime Text
enables users with programming skills
to add their own features to the editor.

Sublime Text exposes its internals
via an Application Programming Interface (API)
that programmers can interact with using
the Python programming language.
An embedded Python interpreter is included
in the editor.
The embedded interpreter is useful
to inspect the editor's settings
and to quickly test API calls
while developing plugins.

Sublime Text and plugins output information
to a *console*.
To open the console,
press :kbd:`Ctrl+\``
or select **View → Show Console**
from the main menu.

Here's the Python console in Sublime Text:

.. image:: basic-concepts-console.png


Your System's Python vs the Sublime Text 3 Embedded Python
**********************************************************

Sublime Text 3 comes with its own Python interpreter
that's separate
from your system's Python interpreter
(if available).

The embedded interpreter is only intended
to interact with the plugin API,
not for general development.


Packages, Plugins, Resources and Other Terms
============================================

Almost every aspect of Sublime Text
can be extended or customized.
You can modify the editor's behavior,
add macros and snippets, extend menus
and much more.
You can even create whole new features
using the editor's API to build complex
plugins.

Sublime Text's vast flexibility is the reason
why you will learn
about so many configuration files:
there simply must be a place
to specify all available preferences and settings.

Configuration files in Sublime Text
are text files
that conform to a predefined structure or *format*:
JSON predominates,
but you'll find XML files too.
For the more advanced
extensibility options,
Python source code files are used.

In this guide, for brevity,
we sometimes refer collectively to all these
disparate configuration files as *resources*.

Sublime Text will look for resources
inside the packages folder.
We'll talk at length about *packages* later,
but the short version is that,
to keep things tidy,
Sublime Text has a notion of a *package*,
that is, a folder (or zip archive)
that contains resources
that belong together
(maybe they help
compose emails faster,
write HTML efficiently,
enhance the coding experience for C, Ruby, Go...).


Textmate Compatibility
======================

This information is useful
for Textmate users
who are now using Sublime Text.

Textmate is an editor for the Mac.

Sublime Text compatibility with Textmate bundles
is good excluding commands,
which are incompatible.
Additionally, Sublime Text requires
all syntax definitions to have the *.tmLanguage* extension,
and all preferences files
to have the *.tmPreferences* extension.
In particular, this means that *.plist* files
will be ignored,
even if they are located
under a *Syntaxes* or *Preferences* subdirectory.


vi/Vim Emulation
================

This information is useful for Vim users
who are now using Sublime Text.

vi is an ancient modal editor
that lets the user perform all operations
from the keyboard.
Vim, a modern version of vi,
is still in widespread use.

Sublime Text provides vi emulation
through the *Vintage* package.
The Vintage package is *ignored* by default.
Learn more about Vintage_
in the official documentation.

An evolution of Vintage, called Vintageous_,
offers a better vi/Vim editing experience
and is updated more often than Vintage.
Vintageous_ is an open source project.

.. _Vintage: http://www.sublimetext.com/docs/3/vintage.html
.. _Vintageous: http://guillermooo.bitbucket.org/Vintageous


emacs Emulation
===============

This information is useful
for emacs users who are
now using Sublime Text.

emacs is another popular
editor for programmers.

Sublime Text does not offer
any built-in emacs emulation,
but you can try third-party packages
created by other Sublime Text users.
