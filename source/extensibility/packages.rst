.. warning::

   Want even better documentation for Sublime Text? You can  `help <https://www.bountysource.com/teams/st-undocs/fundraiser>`_.

========
Packages
========

Packages are simply folders under ``Packages``, or zip archives with the
`.sublime-package` extension saved under ``Installed Packages``. 

Here's a list of typical resources that can be found inside packages:

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

Some packages may include support files for other packages or core features.
For example, the spell checker uses *$PATH_TO_SUBLIME_TEXT\Packages\Language -
English.sublime-package* as a data store for English dictionaries.


Types of Packages
*****************

In this guide, we classify packages under different categories. This
classification is artificial and useful just for clarity when discussing this
topic. Sublime Text doesn't use this classification in any way.

**core packages**
	Required packages for proper functioning.

**shipped packages**
  Included in every installation, though technically not required. They
  enhance Sublime Text out of the box. May have been contributed by users or
  third parties.

**user packages**
  Installed by the user to extend Sublime Text's functionaility. They are not
  part of any Sublime Text installation, and are always contributed by users
  or third parties.

**installed packages**
  Packages stored under *Installed Packages* as *.sublime-package*\ 's

It's worth noting that by *third party* we mainly refer to users of other
editors, such as Textmate.


Package Installation
*********************

Ultimately, installing a package is simply a matter of copying a folder
containing Sublime Text resources to ``Packages``, or a *.sublime-package*
file to *Installed Packages*. The only thing that varies is how you obtain
and copy these files.

.. sidebar:: Installing Packages vs Installed Packages

   Note that "installing a package" actually doesn't make that package a Sublime Text
   installed package. *Installed packages* are ``.sublime-package`` files
   residing in the ``Installed Packages`` folder. In this guide, we use
   *install a package* to mean either copying a package to ``Packages`` or
   a *.sublime-package* file to *Installed Packages*. We hope to come up with
   a less confusing terminology in the future to explain this!

.. XXX - I'm not sure this is still true.
   Sublime Text can restore any package located in ``Installed Packages``, but
   can't automatically restore the packages located in ``Packages``.

.. _installation-of-sublime-packages:

Installation of ``.sublime-package`` Files
------------------------------------------

Copy the ``.sublime-package`` file to the ``Installed Packages`` folder and
restart Sublime Text. If the ``Installed Packages`` folder doesn't exist, you
can create it.

Note that ``.sublime-package`` files simply are ``.zip`` archives with a custom
file extension.

Installation of Packages from a Version Control System
------------------------------------------------------

Explaining how to use version control systems (VCSs) is outside the scope of
this guide, but there are many user packages available free of charge on public
repositories like GitHub and Bitbucket.

Also, a `Sublime Text organization`_ at GitHub is open to contributors.

.. _Sublime Text organization: http://github.com/SublimeText


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

To temporarily disable packages, you can add them to the `ignored_packages` list
in your *Packages/User/Preferences.sublime-settings* file.


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


The ``Installed Packages`` Directory
************************************

You will find this folder in the data directory. It contains a copy of every
``sublime-package`` installed. It is used to restore ``Packages``.
.. warning::

   Want even better documentation for Sublime Text? You can  `help <https://www.bountysource.com/teams/st-undocs/fundraiser>`_.

