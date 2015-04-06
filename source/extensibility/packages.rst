========
Packages
========

A package is a container for resources.
Packages can be folders under ``Packages``,
or zip archives under ``<Data>/Installed Packages``
with the ``.sublime-package`` extension.

Typical resources found in packages include:

.. hlist::

   - build systems (``.sublime-build``)
   - key maps (``.sublime-keymap``)
   - macros (``.sublime-macro``)
   - menus (``.sublime-menu``)
   - plugins (``.py``)
   - settings (``.sublime-settings``)
   - snippets (``.sublime-snippet``)
   - syntax definitions (``.tmLanguage``)
   - metadata (``.tmPreferences``)
   - themes (``.sublime-theme``)

Some packages may hold support files
for other packages or core features.
For example, the spell checker
uses ``Packages/Language - English.sublime-package``
as a data store for English dictionaries.


The *Installed Packages* Folder
*******************************

You will find this folder
in ``<Data>/Installed Packages``.
It contains ``.sublime-package`` archives.


Types of Packages
*****************

In this guide, we categorize packages
for clarity when discussing this topic.
Sublime Text doesn't use this terminology
and you don't need to learn it.

**core packages**
   Sublime Text requires these packages
   in order to work.
   Located in ``<Data>/../Packages``.

**shipped packages**
   Included in every installation,
   though technically not required.
   They enhance Sublime Text out of the box.
   May have been contributed by users or
   third parties.
   Located in ``<Data>/../Packages``.

**user packages**
   Installed by the user
   to extend Sublime Text's functionaility.
   They are not part of Sublime Text,
   and are always contributed by users
   or third parties.
   Located in ``<Data>/Packages``
   and ``<Data>/Installed Packages``.

**installed packages**
   Packages stored under
   ``<Data>/Installed Packages`` as ``.sublime-package`` archives.
   A type of *user package*.

   .. note::

      Due to the unfortunate name of this folder,
      talking about *installing*
      packages in Sublime Text
      becomes a confusing business.

      Sometimes, in this guide, by *instaling* we mean
      'adding a user/third party package to Sublime Text'
      (in any form),
      and sometimes we use the term
      in its stricter sense of
      'copying a ``.sublime-package`` archive
      to ``<Data>/Installed Packages``'.

Note that by *third party*
we mainly refer to users of other
editors, such as Textmate,
as Sublime Text and Textmate
share some types of resource files
that can be reused without modification.


Installing Packages
*******************

.. note::

   Nowadays, regular users
   rarely need to know
   how to install packages by hand,
   as automatic package managers
   are available.

   The de facto package manager
   for Sublime Text is Package Control.

Packages can be installed
in two main ways:

- by copying Sublime Text resources
  to  a folder under ``Packages``, or
- by copying a ``.sublime-package``
  to ``<Data>/Installed Packages``

.. note::

   In this guide,
   *installed packages* sometimes refers strictly
   to ``.sublime-package`` archives residing
   in the ``<Data>/Installed Packages`` directory.

   Sublime Text can restore any package
   located in ``<Data>/Installed Packages``, but
   not every package located under ``Packages``.


.. _installation-of-sublime-packages:

Installation of ``.sublime-package`` Archives
---------------------------------------------

Copy the ``.sublime-package`` archive
to the ``<Data>/Installed Packages`` folder
and restart Sublime Text.
If the ``<Data>/Installed Packages`` folder
doesn't exist, you can create it.

Note that ``.sublime-package`` files
are just ``.zip`` archives with a custom file extension.


Packages and Magic
******************

Sublime Text deals with packages without much hidden magic. There are two
notable exceptions: Macros defined in any package automatically appear under
**Tools | Macros | <Your Package>**, and snippets from any package appear
under **Tools | Snippets | <Your Package>**.

However, Sublime Text follows some rules for packages. For instance,
``Package/User`` will never be clobbered during updates to the software.

.. sidebar:: The ``User`` Package

   Usually, unpackaged resources are stored in ``Packages/User``. If you
   have a few loose snippets, macros or plugins, this is a good place to keep
   them.


.. _merging-and-order-of-precedence:

Merging and Order of Precedence
-------------------------------

*Packages/Default* and *Packages/User* receive special treatment when
merging files (e.g. *.sublime-keymap* and *.sublime-settings* files).
Before merging can take place, the files have to be arranged in some order. To
that end, Sublime Text sorts them alphabetically by name, with the exception
of the *Default* and *User* folders. Files contained in *Default* will
always go to the front of the list, and those in *User*, to the end.


Ignored Packages
****************

To temporarily disable packages,
you can add them to the ``ignored_packages`` list
in your ``Packages/User/Preferences.sublime-settings`` file.


Restoring Packages
******************

Sublime Text keeps a copy of all installed packages so it can recreate them as
needed. This means it can reinstall core packages, shipped packages and,
potentially, user packages alike. However, only user packages installed as
``sublime-packages`` are added to its registry of installed packages. Packages
installed in alternative ways will be lost completely if you delete them.


Reverting Sublime Text to Its Default Configuration
---------------------------------------------------

To revert Sublime Text to its default configuration, delete the data directory
and restart the editor. Keep in mind that the ``Installed Packages`` folder will
be deleted too, so you'll lose all your installed packages.

Always make sure to back up your data before taking an extreme measure like
this one.

Reverting Sublime Text to a fresh state solves many problems that appear to be
due to bugs in Sublime Text but are in fact caused by misbehaving plugins.
