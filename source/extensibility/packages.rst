========
Packages
========

Packages are simply folders under :file:``Packages``. They exist mainly for
organizational purposes, but Sublime Text follows a few rules when dealing with
them. More on this later.

Here's a list of the typical resources living inside packages:

    - build systems (``.sublime-build``)
    - key maps (``.sublime-keymap``)
    - macros (``.sublime-macro``)
    - menus (``.sublime-menu``)
    - plugins (``.py``)
    - syntax preferences (``.tmPreferences``)
    - settings (``.sublime-settings``)
    - syntax definitions (``.tmLanguage``)
    - snippets (``.sublime-snippet``)
    - themes (``.sublime-theme``)

Some packages may include support files for other packages or core
features. For example, the spell checker uses :file:`Packages\Language - English`
as a data store for English dictionaries.


Types of Packages
*****************

In this guide, in order to talk about packages, we divide them into groups.
This division is artificial, and just useful for clarity when discussing this topic.
Sublime Text doesn't use this division in any way.

**core packages**
	Sublime Text requires these packages in order to work.

**shipped packages**
   Sublime Text includes these packages in every installation, though
   technically they are not required.
   These shipped packages enhance Sublime Text out of the
   box. They may have been contributed by users or third parties.

**user packages**
   Packages installed by the user to extend Sublime Text's functionaility.
   They are not part of any Sublime Text installation, and always are contributed
   by users or third parties.

**installed packages**
   Any package that, if deleted, Sublime Text will be able to restore.

Let's emphasize again that you don't need to memorize this classification.

Also, it's worth noting that by *third party* we mainly refer to users of other
editors, such as Textmate.


Installation of Packages
************************

There are two main ways to install packages:

    - *.sublime-package* files
    - version control systems

Ultimately, installing a package is simply a matter of copying a folder
containing Sublime Text resources to :file:``Packages``. The only thing that
changes from one system to another is how you copy these files.

.. sidebar:: Installing Packages vs Installed Packages

   Note that "installing a package" actually doesn't make that package a Sublime Text
   installed package. *Installed packages* are *.sublime-package* files
   residing in the ``Installed Packages`` folder. In this guide, we use
   *install a package* to mean copying a package to :file:``Packages``.

   Sublime Text can restore any package located in ``Installed Packages``, but
   can't automatically restore the packages located in ``Packages``.

.. _installation-of-sublime-packages:

Installation of ``.sublime-package`` Files
------------------------------------------

Copy the ``.sublime-package`` file to the ``Installed Packages`` folder
and restart Sublime Text. If the ``Installed Packages`` folder doesn't exist, you can
create it.

Note that ``.sublime-package`` files simply are ``.zip`` archives with a custom
file extension.

Installation of Packages from a Version Control System
------------------------------------------------------

Explaining how to use version control systems (VCSs) is outside the scope of
this guide, but there are many user packages available free of charge on public
repositories like Google Code, GitHub and Bitbucket.

Also, a `Sublime Text organization`_ at GitHub is open to contributors.

.. _Sublime Text organization: http://github.com/SublimeText


Packages and Magic
******************

Sublime Text deals with packages quite simply, without much hidden magic.
There are two notable exceptions: Macros defined in any package automatically appear under
**Tools | Macros | <Your Package>**, and snippets from any package appear under
**Tools | Snippets | <Your Package>**.

However, as mentioned at the beginning, Sublime Text follows some rules for packages.
For instance, ``Package/User`` will never be clobbered during updates to the
software.

.. sidebar:: The ``User`` Package

    Usually, unpackaged resources are stored in ``Packages/User``. If you
    have a few loose snippets, macros or plugins, this is a good place to keep
    them.

.. _merging-and-order-of-precedence:

Merging and Order of Precedence
-------------------------------

``Packages/Default`` and ``Packages/User`` also receive special treatment when
merging files (e. g. ``.sublime-keymap`` and ``.sublime-settings`` files).
Before merging can take place, the files have to be arranged in some order. To
that end, Sublime Text sorts them alphabetically by name, with the exception
of the folders ``Default`` and ``User``. Files contained in ``Default`` will
always go to the front of the list and, those in ``User``, to the end.


Restoring Packages
******************

Sublime Text keeps a copy of all installed packages so it can recreate them as
needed. This means it can reinstall core packages, shipped packages
and, potentially, user packages alike. However, only user packages installed as
``sublime-packages``
are added to its registry of installed packages. Packages installed in alternative
ways will be lost completely if you delete them.

Reverting Sublime Text to Its Default Configuration
---------------------------------------------------

To revert Sublime Text to its default configuration, delete the data directory
and restart the editor. Keep in mind, though, that the ``Installed Packages``
folder will be deleted too, so you'll lose all your installed packages.

Always make sure to back up your data before taking an extreme measure like
this one.


The ``Installed Packages`` Directory
************************************

You will find this folder in the data directory. It contains a copy of every
``sublime-package`` installed. It is used to restore ``Packages``.


The ``Pristine Packages`` Directory
***********************************

You will find this folder in the data directory. It contains a copy of every
shipped and core package. It is used to restore ``Packages``.
