Packages
========

Packages are simply directories under ``Packages``. They exist mainly for organizational
purposes and bear no especial meaning to Sublime Text except in a few cases that will be
explained later.

Inside packages, you will normally find Sublime Text resources: snippets, macros, plugins,
themes, settings, menus, preferences, build systems or key maps. However, some of them
include support files for other packages or built-in functionality, for instance in the
case of the spell-checking functionality (e.g. ``Packages\Language - English``).

Types of Packages
*****************

In order to talk about packages, we're going to divide them in groups:

**core packages**
	Sublime Text requires these packages in order to work.

**shipped packages**
	Sublime Text includes these packages in every installation, although they are not
	technically required. Shipped packages enhance Sublime Text out of the box and they
	might have been contributed by users or other third parties.

**user packages**
	These are installed by the user to further extend Sublime Text. They are not included
	with any Sublime Text installation. These packages are always contributed by users or
	other third parties.

Let's emphasize that this artificial division is for the sake of clarity in this guide.
Sublime Text makes no distinction between these types of packages internally.

Recreation of Packages
**********************

Sublime Text has a self-healing mechanism to recover deleted packages. It keeps a copy of
all installed packages so it can recreate them when needed. This means it will be able to
reinstall core packages, shipped packages and user packages alike. However, only user
packages installed as ``sublime-package`` are added to the installed packages registry.
Packages installed in alternative ways will be completely lost if you delete them.

Instalation of Packages
***********************

There are three ways to install packages: ``sublime-package`` archives, version control
systems, and plain copy-paste of files. Ultimately, installing a package consists simply in
placing the directory containing Sublime Text resources under the ``Packages`` folder. The
only thing that changes from one system to another is how you copy this files.

Installation of Packages with ``sublime-package`` Archives
----------------------------------------------------------

To install a ``sublime-package``, simply double-click on it. Sublime Text will take care
of the rest.

.. note::
	This system will only work with full installations as opposed to portable installations.

Installation of Packages from a Version Control System
------------------------------------------------------

Explaining how to use version control systems (VCSs) is outside the scope of this guide.
However, there are many user packages available for free on public repositories like
Google Code, GitHub and Bitbucket.

Manual Installation
-------------------

Simply copy and paste a directory containing Sublime Text resources to the ``Packages``
directory.

Packages and Magic
******************

As mentioned before, there are some packages that Sublime Text treats especially. For
instance, macros stored in the ``User`` package will show up under **Tools | Macros | User**.
Also, Sublime Text won't clobber your installation's ``User`` package when you update the
software.

Conventions about Package Names
*******************************

Usually, unpackaged resources are stored in the ``User`` package. If you have a few loose
snippets, macros or plugins, this is a good place to keep them.

Package names are written with upper case initial.

Specific Rules about Resources and Packages
*******************************************

Resource type-specific behavior is highlighted in the particular resource reference section.
For example, plugins nested more than two levels deep from ``Packages`` are not picked up by
Sublime Text.

Installed Packages
******************

You will find this directory under ``%APPDATA%\Sublime Text X``. It contains a copy of every
``sublime-package`` installed.

.. note::
	If you're using a portable version of Sublime Text, you can place here any ``sublime-package``
	and it will be installed the next time you start Sublime Text.

Pristine Packages
*****************

You will find this directoy under ``%APPDATA%\Sublime Text X``. It contains a copy of every
shipped package. They are used to recreate the ``Packages`` folder when any of the packages
contained in there is deleted.
