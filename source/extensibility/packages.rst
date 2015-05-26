==========
 Packages
==========

A package is a container for resources.

.. contents::
   :depth: 3


Package Locations (and Abbreviations)
=====================================

There are three locations
for storing packages
for different purposes.

- Packages can be **folders**
  under :file:`{Data}/Packages` (short: :file:`{Packages}`)
- or **zip archives**
  with the ``.sublime-package`` extension
  located under :file:`{Data}/Installed Packages`
  (short: :file:`{Installed Packages}`)
  or any of its subdirectories.
- Additionally,
  Sublime Text provides a set of default packages
  as **zip archives**
  in :file:`{Application}/Packages` (short: :file:`{Shipped Packages}`),
  where ``Application`` refers to the folder
  that the Sublime Text executable resides.

  This folder is not intended to be modified by the user.

.. note::

   For simplicity, we will occasionally
   refer to all these directories simply as :file:`{Packages}`
   and to a package in any folder
   (``.sublime-package`` or not)
   as :file:`{Packages}/PackageName`.
   Consequently, a file inside a package
   may also be referred to as :file:`PackageName/a_file.extension`.


.. _.sublime-package:

``.sublime-package`` Packages
*****************************

Packages distributed as ``.sublime-package`` zip archives
should be considered read-only containers of resources
and never be modified manually.
Since they are usually updated as a whole,
any manual changes made to them
will be lost in the process.

If you do want to modify files in these archives,
see :ref:`overriding-packages`.


Interactions Between Packages With the Same Name
************************************************

If two packages with the same name exist
in both :file:`{Installed Packages}` and :file:`{Shipped Packages}`,
the one in :file:`{Installed Packages}` will be used
and the other ignored.

Any files in :file:`{Packages}` take precedence
over their counterpart files in a ``.sublime-package`` package
or are simply added to the package.

See also :ref:`overriding-packages`.


Package Contents
================

Typical resources found in packages include:

.. hlist::

   - build systems (``.sublime-build``)
   - color schemes (``.tmTheme``)
   - key maps (``.sublime-keymap``)
   - macros (``.sublime-macro``)
   - menus (``.sublime-menu``)
   - metadata (``.tmPreferences``)
   - mouse maps (``.sublime-mousemap``)
   - plugins (``.py``)
   - settings (``.sublime-settings``)
   - snippets (``.sublime-snippet``)
   - syntax definitions (``.tmLanguage``)
   - themes (``.sublime-theme``)

.. XXX link to respective docs
.. XXX add secondary extensions (.tmSnippet, .sublime-syntax)

Some packages may hold support files
for other packages or core features.
For example, the spell checker
uses :file:`{Installed Packages}/Language - English.sublime-package`
as a data store for English dictionaries.


Types of Packages
=================

In this guide, we categorize packages
for clarity when discussing this topic.
Sublime Text doesn't use this terminology
and you don't need to learn it.

.. glossary::

   **shipped packages**
   **default packages**
      A set of packages
      that Sublime Text ships with.
      Some of these packages are :term:`core packages`,
      while others enhance Sublime Text
      to support common programming languages out of the box.

      Examples: Default, Python, Java, C++, Markdown

      Located in :file:`{Shipped Packages}`.

   **core packages**
      Sublime Text requires these packages
      in order to function properly.

      Examples: Default, Theme - Default, Color Scheme - Default

      They are part of the shipped packages and
      located in :file:`{Shipped Packages}`.

   **user packages**
      Installed or created by the user
      to extend Sublime Text's functionality.
      They are not part of Sublime Text,
      and are always contributed by users
      or third parties.

      Example: User

      Located in :file:`{Packages}`
      and :file:`{Installed Packages}`.

   **installed packages**
      A subtype of *user packages*.

      Installed packages are ``.sublime-package`` archives
      and usually maintained by a package manager.

      Located in :file:`{Installed Packages}`.

      .. note::

         Due to the unfortunate name of this folder,
         talking about *installing*
         packages in Sublime Text
         becomes a confusing business.

         Sometimes, in this guide, by *installing* we mean
         'adding a user/third party package to Sublime Text'
         (in any form),
         and sometimes we use the term
         in its stricter sense of
         'copying a ``.sublime-package`` archive
         to :file:`{Installed Packages}`'.

   **override packages**
      A special type of *user packages*.

      Override packages serve the purpose of customizing packages
      that are distributed as ``.sublime-package`` files.
      They are effectively injected into the original package
      and do not stand-alone.

      See :ref:`overriding-packages` for details.

      Located in :file:`{Packages}`.


Note that by *third party*
we also refer to users of other
editors, notably Textmate,
as Sublime Text and Textmate
share some types of resource files
that can be reused without modification.


Managing Packages
=================

.. XXX some sentences here?

Installing Packages
*******************

.. note::

   Nowadays, regular users
   rarely need to know
   how to install packages by hand,
   as automatic package managers
   are available.

   The de facto package manager
   for Sublime Text is `Package Control`_.

   .. _Package Control: https://packagecontrol.io


Packages can be installed
in two main ways:

- by copying Sublime Text resources
  to a folder under :file:`{Packages}`, or
- by copying a ``.sublime-package`` file
  to :file:`{Installed Packages}`.


.. _disabling-packages:

Disabling Packages
******************

To temporarily disable packages,
you can add them to the ``ignored_packages`` list setting
in your :file:`{Packages}/User/Preferences.sublime-settings` file.

Changes are detected when the file is saved
and packages will be loaded or unloaded on the fly.


Enabling Packages
*****************

Similarly to :ref:`disabling-packages`,
enabling a package is a matter of
removing the package's name from the ``ignored_packages`` list setting.


Removing Packages
*****************

If you installed a package with a package manager,
you should use the method provided by the package manager
to remove it.

If you installed a package manually,
follow this procedure to safely remove a package:

1. :ref:`Disable <disabling-packages>` the package
   while Sublime Text is running.
#. Close Sublime Text.
#. Remove the package's resources from the disk.
4. Finally, you can remove the package
   from the ``ignored_packages`` list setting,
   since it doesn't exist anymore.

In addition to the resources
you have placed initially
in a :file:`{Packages}` folder or in :file:`{Installed Packages}`,
plugins may create configuration files
(such as ``.sublime-settings`` files)
or other files to store package-related data.
Usually, you will find them in the *User* package.
If you want to remove all traces of a package,
you need to find and remove these files manually.

.. warning::

   Shipped Packages are reinstated on every Sublime Text update.
   If you want to get rid of any of them,
   :ref:`disable <disabling-packages>` them instead of deleting.


.. _overriding-packages:

Customizing or Overriding Packages
==================================

Since packages in ``.sublime-package`` zip archives
:ref:`are read-only <.sublime-package>`,
you can not modify them directly.
However, Sublime Text allows you
to create an :term:`override package <override packages>`
that will effectively inject files into the original archive
without changing the archive file.

To create an override package,
just create a new folder under :file:`{Packages}`
and name it after the ``.sublime-package`` file
you want to override, without the extension.
Any file you create in this package
will take precedence over a potential counterpart file
in the original package.

Python plugins in override packages
are able to use relative imports
for accessing other modules in the ``.sublime-package`` file
as if they were part of it.

.. warning::

   Since you are always overriding entire files,
   you will not receive any updates for these overridden files
   if the original ``.sublime-package`` happens to be updated
   at some point.

.. Generally, this only works on resources
   interpreted by Sublime Text directly.
   If there are other files which the package loads
   by means of a Python plugin,
   it depends on whether the code uses
   the ``sublime.load_resource`` API or not
   (which they should).


.. _merging-and-order-of-precedence:

Merging and Order of Precedence
===============================

Package precedence is important for merging certain resources,
for example, ``.sublime-keymap`` and ``.sublime-settings`` files,
or for loading plugins (``.py``).

If an :term:`override package <override packages>` exists
for a ``.sublime-package`` package,
it will be loaded together with the ``.sublime-package`` package.

1. :file:`{Packages}/Default` is loaded.
#. All :term:`shipped packages` and :term:`installed packages`
   are joined and loaded in alphabetical order.
#. All remaining :term:`user packages`
   that did not override anything
   are loaded in alphabetical order,
   except for :file:`{Packages}/User`.
#. :file:`{Packages}/User` is loaded.


Reverting Sublime Text to Its Default Configuration
===================================================

For various reasons,
packages may cause Sublime Text to not function properly
or have bad interactions between one another.

To revert Sublime Text to its default configuration
and remove all your settings and configurations,
delete the :ref:`data directory <data-directory>`
and restart the editor.
Keep in mind
that the ``Installed Packages`` folder will be deleted too,
so you'll lose all your installed packages.

Always make sure to back up your data
before taking an extreme measure like this one!

Reverting Sublime Text to a fresh state
solves many problems
that appear to be bugs in Sublime Text
but are in fact caused by misbehaving plugins.
