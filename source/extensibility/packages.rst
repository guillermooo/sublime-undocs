==========
 Packages
==========

A package is a container for resources.


Package Locations (and Abbreviations)
=====================================

There are three locations
for storing packages
for different purposes.

- Packages can be **folders**
  under :file:`{Data}/Packages` (short: :file:`{Packages}`)
- or **zip archives**
  under :file:`{Data}/Installed Packages` (short: :file:`{Installed Packages}`)
  with the ``.sublime-package`` extension.
- Additionally,
  Sublime Text provides a set of default packages
  as **zip archives**
  in :file:`{Application}/Packages` (short: :file:`{Shipped Packages}`),
  where ``Application`` refers to the folder
  that the ST binary resides in.

Zip archives in :file:`{Installed Packages}`
(or :file:`{Shipped Packages}`)
can optionally be in any number of subdirectories.

For simplicity we will, on occasions,
collectively refer to all these directories by :file:`{Packages}`
and refer to a package in any folder
(``.sublime-package`` or not)
by :file:`{Packages}/Package Name`.
Consequently, a file inside a package
may also be referred to as :file:`{Package Name}/a_file.extension`.


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

**shipped packages** (or *default packages*)
   A set of packages
   that Sublime Text ships with by default.
   They are included in every installation,
   though technically not required
   and enhance Sublime Text out of the box.

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

   Packages stored under :file:`{Installed Packages}`
   as ``.sublime-package`` archives.

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

Note that by *third party*
we also refer to users of other
editors, notably Textmate,
as Sublime Text and Textmate
share some types of resource files
that can be reused without modification.


Installing Packages
===================

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
  to a folder under ``Packages``, or
- by copying a ``.sublime-package`` file
  to :file:`{Installed Packages}`

.. note::

   In this guide,
   *installed packages* sometimes refers strictly
   to ``.sublime-package`` archives residing
   in the :file:`<Data>/Installed Packages` directory.


.. _installation-of-sublime-packages:

Installation of ``.sublime-package`` Archives
*********************************************

Copy the ``.sublime-package`` archive
to the ``<Data>/Installed Packages`` folder
and restart Sublime Text.
If the ``<Data>/Installed Packages`` folder
doesn't exist, you can create it.

Note that ``.sublime-package`` files
are just ``.zip`` archives with a custom file extension.


Packages and Magic
==================

Sublime Text deals with packages without much hidden magic. There are two
notable exceptions: Macros defined in any package automatically appear under
**Tools → Macros → <Your Package>**, and snippets from any package appear
under **Tools → Snippets → <Your Package>**.

However, Sublime Text follows some rules for packages. For instance,
``Package/User`` will never be clobbered during updates to the software.

.. sidebar:: The ``User`` Package

   Usually, unpackaged resources are stored in ``Packages/User``. If you
   have a few loose snippets, macros or plugins, this is a good place to keep
   them.


.. _merging-and-order-of-precedence:

Merging and Order of Precedence
*******************************

*Packages/Default* and *Packages/User* receive special treatment when
merging files (e.g. *.sublime-keymap* and *.sublime-settings* files).
Before merging can take place, the files have to be arranged in some order. To
that end, Sublime Text sorts them alphabetically by name, with the exception
of the *Default* and *User* folders. Files contained in *Default* will
always go to the front of the list, and those in *User*, to the end.


Ignored Packages
================

To temporarily disable packages,
you can add them to the ``ignored_packages`` list
in your ``Packages/User/Preferences.sublime-settings`` file.


Restoring Packages
==================

Sublime Text keeps a copy of all installed packages so it can recreate them as
needed. This means it can reinstall core packages, shipped packages and,
potentially, user packages alike. However, only user packages installed as
``sublime-packages`` are added to its registry of installed packages. Packages
installed in alternative ways will be lost completely if you delete them.


Reverting Sublime Text to Its Default Configuration
***************************************************

To revert Sublime Text to its default configuration, delete the data directory
and restart the editor. Keep in mind that the ``Installed Packages`` folder will
be deleted too, so you'll lose all your installed packages.

Always make sure to back up your data before taking an extreme measure like
this one.

Reverting Sublime Text to a fresh state solves many problems that appear to be
due to bugs in Sublime Text but are in fact caused by misbehaving plugins.
