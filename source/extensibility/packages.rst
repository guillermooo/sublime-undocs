Packages
========

Packages are simply directories under ``Packages``. They exist mainly for
organizational purposes and have no bearing in how resources within them work
except in a few cases that will be explained later.

This is an exhaustive list of Sublime Text resources than can be found inside
a package:
	
    - build systems (``.sublime-build``)
    - key maps (``.sublime-keymap``)
    - macros (``.sublime-macro``)
    - menus (``.sublime-menu``)
    - plugins (``.py``)
    - preferences (``.tmPreferences``)
    - settings (``.sublime-settings``)
    - syntax definitions (``.tmLanguage``)
    - snippets (``.sublime-snippet``)
    - themes (``sublime-theme``)

Some of them may include support files for other packages or built-in functionality
too. Such is the case of the dictionaries used by the spell-checker
(e. g. ``Packages\Language - English``).

Types of Packages
*****************

In order to talk about packages, we're going to divide them in groups:

**core packages**
	Sublime Text requires these packages in order to work.

**shipped packages**
	Sublime Text includes these packages in every installation, although they are not
	technically required. Shipped packages enhance Sublime Text out of the box and
	very often they have been contributed by users or other third parties.

**user packages**
	These packages are installed by the user to further extend Sublime Text. They
	are not part of any Sublime Text installation and are always contributed by
	users or other third parties.

**installed package**
	Any package of any type that Sublime Text can restore if deleted.

Let's emphasize that this artificial division is for the sake of clarity in this guide.
Sublime Text makes no distinction between these types of packages internally.

Restoring of Packages
*********************

Sublime Text keeps a copy of all installed packages so it can recreate them when
needed. This means it will be able to reinstall core packages, shipped packages
and user packages alike. However, only user packages installed as a ``sublime-package``
are added to the registry of installed packages. Packages installed in alternative
ways will be completely lost if you delete them.

Reverting Sublime Text to its Default Configuration
---------------------------------------------------

To revert Sublime Text to its default configuration (plus installed packages),
delete the data directory and restart the editor. Keep in mind, though, that
``Packages\User`` is not an installed package and you will lose its contents if
you delete it.

In any case, make sure to back things up before taking an extreme measure like
this.

Installation of Packages
************************

There are three main ways to install packages:

	- ``.sublime-package`` archives
	- version control systems
	- copy-pasting of files

Ultimately, installing a package consists simply in placing the directory
containing Sublime Text resources under ``Packages``. The only thing that
changes from one system to another is how you copy these files.

.. sidebar:: Installing Packages vs Installed Packages
	
	Note that installing a package doesn't actually make that package an
	installed package. *Installed packages* are ``.sublime-package`` archives
	residing in the ``Installed Packages`` folder. *To install a package*
	means to copy it to ``Packages``.

	Packages installed as ``.sublime-package`` archives get added automatically
	to ``Installed Packages``, so they are very convenient.

Installation of Packages with ``.sublime-package`` Archives
-----------------------------------------------------------

To install a ``.sublime-package``, simply double-click on it. Sublime Text will
take care of the rest.

.. note::
	This method will only work with full installations. If you're using a
	portable installation, copy the ``.sublime-package`` to the ``Installed Packages``
	directory manually and restart Sublime Text.

Installation of Packages from a Version Control System
------------------------------------------------------

Explaining how to use version control systems (VCSs) is outside the scope of
this guide, but there are many user packages available for free on public
repositories like Google Code, GitHub and Bitbucket.

Manual Installation
-------------------

Simply copy and paste a directory containing Sublime Text resources to``Packages``.

Packages and Magic
******************

There's little invisible magic involved in the way Sublime Text deals with packages.
One notable exception is that macros defined in any package appear under
**Tools | Macros | <Your Package>**.

As mentioned at the begninning, however, there are some packages that Sublime
Text treats especially. For instance, ``Package\User`` will never be clobbered
during a software update.

.. sidebar:: The ``User`` Package

	Usually, unpackaged resources are stored in the ``User`` package. If you
	have a few loose snippets, macros or plugins, this is a good place to keep
	them.

Merging and Order of Preference
-------------------------------

``Packages\Default`` and ``Packages\User`` also receive a special treament when
merging files (e. g. ``.sublime-keymap`` and ``.sublime-settings`` files). Before
the merging can take place, the files have to be arranged in an order. To that end,
Sublime Text sorts them by name, but ``Default`` and ``User`` are special: ``Default``
will always go to the front of the list, and ``User`` to the end.

The ``Installed Packages`` Directory
************************************

You will find this directory in the data directory. It contains a copy of every
``sublime-package`` installed. Used to restore ``Packages``.

The ``Pristine Packages`` Directory
***********************************

You will find this directoy in the data directory. It contains a copy of every
shipped and core package. Used to restore ``Packages``.