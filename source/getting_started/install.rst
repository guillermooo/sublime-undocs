============
Installation
============

The process of installing Sublime Text is different for each platform.

Make sure to read the `conditions for use`_ on the official site. Sublime Text
is not free.

.. _conditions for use: http://www.sublimetext.com/buy

32 bits or 64 bits?
===================

Choose the 64-bit version if you're running a 64-bit operating system,
otherwise the 32-bit version.

On **Windows**, if in doubt, choose the 32-bit version. Modern 64-bit
versions of Windows can run 32-bit software.

On **Linux** run this command in your terminal to check your operating
system's type::

	uname -m

For **OS X**, you can ignore this section: there is only one version of
Sublime Text for OS X.

Windows
=======

Portable or Not Portable?
-------------------------

Sublime Text comes in two flavors for Windows: normal, and portable. If you
need the portable installation, you probably know already. Otherwise, go with
the normal one.

**Normal installations** separate data between two folders: the installation
folder proper, and the *data directory*. These concepts are explained later
in this guide. Normal installations also integrate Sublime Text with the
Windows context menu.

**Portable installations** will keep all files Sublime Text needs to run in
one single folder. You can then move this folder around and the editor will
still work.

How to Install the Normal Version of Sublime Text
-------------------------------------------------

Download the installer, doubleclick on it and follow the onscreen
instructions.

How to Install the Portable Version of Sublime Text
----------------------------------------------------

Download the package and uncompress it to a folder of your choice. You will
find the *sublime_text.exe* executable inside that folder.

OS X
====

Download and open the *.dmg* file, and then drag the Sublime Text 2 bundle
into the *Applications* folder.

Linux
=====

You can download the package and uncompress it manually. Alternatively, you
can use the command line:

::

	cd /path/to/your/apps
	wget http://url/to/sublime.tar.bz2
	tar vxjf sublime.tar.bz2

If you want, you can also create a symbolic link to the executable for
convenience::

	sudo ln -s /path/to/sublime_text /usr/bin/subl

Living Dangerously... or Not
============================

Sublime Text has three release *channels*:

* `Stable`_ (default)
* `Dev`_
* `Nightly`_

.. _Stable: http://www.sublimetext.com/2
.. _Dev: http://www.sublimetext.com/dev
.. _Nightly: http://www.sublimetext.com/nightly

Furthermore, there are separate channels for the Sublime Text 3 Beta which is only available to users who own a licence:

* `3-Beta <http://www.sublimetext.com/3>`_ (comparable to *Nightly*)
* `3-Dev <http://www.sublimetext.com/3dev>`_

If you are working on a NASA project or are on a tight deadline, keep using the
stable releases and stop reading here. **Stable releases** are better tested and
more reliable for everyday use than the others. **The majority of users will
want to use stable releases only.**

The *dev* and *nightly* channels are unstable, which means that builds
published through them are likely to contain bugs and to not work reliably.
They are updated more often than stable releases.

**Dev builds** are available for everyone and are released inbetween stable
releases. While not quite ready for everyday use yet, they showcase new features
in a mostly unbroken fashion.

Lastly, **nightly builds** are the bleeding edge, with frequent updates and
also frequent problems of various degrees of severity. They are fun to try
out, but do so at your own risk. Nighlty builds are **only available for
registered users**.
