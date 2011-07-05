========
Packages
========

Packages are simply directories under ``Packages``. They exist mainly for
organizational purposes, but Sublime Text follows a few rules when dealing with
them. More on this later.

Here's a list of typical resources living inside packages:
	
    - build systems (``.sublime-build``)
    - key maps (``.sublime-keymap``)
    - macros (``.sublime-macro``)
    - menus (``.sublime-menu``)
    - plugins (``.py``)
    - preferences (``.tmPreferences``)
    - settings (``.sublime-settings``)
    - syntax definitions (``.tmLanguage``)
    - snippets (``.sublime-snippet``)
    - themes (``.sublime-theme``)

Some packages may include support files for other packages or core
features. For example, the spell checker uses :file:`Packages\Language - English`
as a data store for English dictionaries.


Types of Packages
*****************

In order to talk about packages in this guide, we'll divide them in groups.
This division is artificial and for the sake of clarity in this topic. Sublime
Text doesn't use it in any way.

**core packages**
	Sublime Text requires these packages in order to work.

**shipped packages**
   Sublime Text includes these packages in every installation, although they are
   not technically required. Shipped packages enhance Sublime Text out of the
   box. They may have been contributed by users or third parties.

**user packages**
   These packages are installed by the user to further extend Sublime Text.
   They are not part of any Sublime Text installation and are always contributed
   by users or third parties.

**installed packages**
	Any package that Sublime Text can restore if deleted.

Let's emphasize again that you don't need to memorize this classification.
Also, it's worth noting that by *third party* we mainly refer to other editors'
users, like Textmate's.


Installation of Packages
************************

There are two main ways to install packages:

	- ``.sublime-package`` files
	- version control systems

Ultimately, installing a package consists simply in placing a directory
containing Sublime Text resources under ``Packages``. The only thing that
changes from one system to another is how you copy these files.

.. sidebar:: Installing Packages vs Installed Packages
	
   Note that installing a package doesn't actually make that package an
   installed package. *Installed packages* are ``.sublime-package`` files
   residing in the ``Installed Packages`` directory. In this guide, we use
   *to install a package* to mean to copy a package to ``Packages``.

   Sublime Text can restore any package located in ``Installed Packages``, but
   not every package located in ``Packages``.

.. _installation-of-sublime-packages:

Installation of ``.sublime-package`` Files
------------------------------------------

Copy the ``.sublime-package`` file to the ``Installed Packages`` directory
and restart Sublime Text. If the ``Installed Packages`` doesn't exist, you can
create it.

Note that ``.sublime-package`` files are simply ``.zip`` archives with a custom
file extension.

Installation of Packages from a Version Control System
------------------------------------------------------

Explaining how to use version control systems (VCSs) is outside the scope of
this guide, but there are many user packages available for free on public
repositories like Google Code, GitHub and Bitbucket.

Also, there is a `Sublime Text organization`_ at GitHub open to contributors.

.. _Sublime Text organization: http://github.com/SublimeText


Packages and Magic
******************

There's little invisible magic involved in the way Sublime Text deals with packages.
Two notable exceptions are that macros defined in any package appear under
**Tools | Macros | <Your Package>**, and snippets from any package appear under
**Tools | Snippets | <Your Package>**.

As mentioned at the beginning, however, there are some rules for packages.
For instance, ``Package/User`` will never be clobbered during updates of the
software.

.. sidebar:: The ``User`` Package

	Usually, unpackaged resources are stored in ``Packages/User``. If you
	have a few loose snippets, macros or plugins, this is a good place to keep
	them.

.. _merging-and-order-of-precedence:

Merging and Order of Precedence
-------------------------------

``Packages/Default`` and ``Packages/User`` also receive a special treatment when
merging files (e. g. ``.sublime-keymap`` and ``.sublime-settings`` files). Before
the merging can take place, the files have to be arranged in an order. To that end,
Sublime Text sorts them alphabetically by name with the exception of files
contained in ``Default`` and ``User``: ``Default`` will always go to the front
of the list, and ``User`` to the end.


Restoring Packages
******************

Sublime Text keeps a copy of all installed packages so it can recreate them when
needed. This means it will be able to reinstall core packages, shipped packages
and user packages alike. However, only user packages installed as a ``sublime-package``
are added to the registry of installed packages. Packages installed in alternative
ways will be completely lost if you delete them.

Reverting Sublime Text to Its Default Configuration
---------------------------------------------------

To revert Sublime Text to its default configuration, delete the data directory
and restart the editor. Keep in mind, though, that the ``Installed Packages``
directory will be deleted too, so you will lose all installed packages.

Always make sure to back up your data before taking an extreme measure like this
one.


The ``Installed Packages`` Directory
************************************

You will find this directory in the data directory. It contains a copy of every
``sublime-package`` installed. Used to restore ``Packages``.


The ``Pristine Packages`` Directory
***********************************

You will find this directoy in the data directory. It contains a copy of every
shipped and core package. Used to restore ``Packages``.