============
Installation
============

Make sure to read the `conditions for use`_
on the official site.
**Sublime Text is not free**.

The process of installing Sublime Text
is different for each platform.

.. _conditions for use: http://www.sublimetext.com/buy


32 bits or 64 bits?
===================


OS X
****

You can ignore this section:
there is only one version
of Sublime Text for OS X.


Windows
*******

You should be able to run
the 64-bit version
if you are using a modern version Windows.
If you are having trouble running the 64-bit version,
try the 32-bit version.


Linux
*****

Run this command
in your terminal
to check your operating system's type::

    uname -m


Windows
=======

Portable or Not Portable?
*************************

Sublime Text comes in two flavors for Windows:
normal, and portable.
Most users should be better served by
a normal installation.
Use the portable version only
if you know you need it.

**Normal installations** separate data
between two folders:
the installation folder proper,
and the *data directory*
(user-specific directory for data;
explained later in this guide).
Normal installations
also integrate Sublime Text
with File Explorer.

**Portable installations** keep all files
needed by Sublime Text
in a single folder.
This folder can be moved around
and the editor will still work.


How to Install the Normal Version of Sublime Text
*************************************************

#. Download the installer
#. Double click on the installer


How to Install the Portable Version of Sublime Text
***************************************************

#. Download the compressed files
#. Unzip them to a folder of your choice

You will find the *sublime_text.exe* executable
inside that folder.

OS X
====

#. Download *.dmg* file
#. Open *.dmg* file
#. Drag the Sublime Text 3 bundle
   into the *Applications* folder

To create a `symbolic link`
to use at the command line
issue the following command
at the terminal::


    ln -s  "/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl" /usr/local/bin/subl


Linux
=====

You can download the package
and uncompress it manually.
Alternatively,
you can use the command line.


Ubuntu
******

**For i386**

::

    cd ~
    wget http://c758482.r82.cf2.rackcdn.com/sublime-text_build-3083_i386.deb

**For x64**

::

    cd ~
    wget http://c758482.r82.cf2.rackcdn.com/sublime-text_build-3083_amd64.deb


Other Linux Distributions
*************************

**For i386**

::

    cd ~
    wget http://c758482.r82.cf2.rackcdn.com/sublime_text_3_build_3083_x32.tar.bz2
    tar vxjf sublime_text_3_build_3083_x32.tar.bz2

**For x64**

::

    cd ~
    wget http://c758482.r82.cf2.rackcdn.com/sublime_text_3_build_3083_x64.tar.bz2
    tar vxjf sublime_text_3_build_3083_x64.tar.bz2

Now we should move the uncompressed files
to an appropriate location.

::

    sudo mv Sublime\ Text\ 3 /opt/


Lastly, we create a `symbolic link`
to use at the command line.

::

    sudo ln -s /opt/Sublime\ Text\ 3/sublime_text /usr/bin/sublime


In Ubuntu, if you also want to add Sublime Text
to the Unity luncher, read on.

First we need to create a new file.

::

    sudo sublime /usr/share/applications/sublime.desktop


Then copy the following into it.

::

    [Desktop Entry]
    Version=1.0
    Name=Sublime Text 3
    # Only KDE 4 seems to use GenericName, so we reuse the KDE strings.
    # From Ubuntu's language-pack-kde-XX-base packages, version 9.04-20090413.
    GenericName=Text Editor

    Exec=sublime
    Terminal=false
    Icon=/opt/Sublime Text 3/Icon/48x48/sublime_text.png
    Type=Application
    Categories=TextEditor;IDE;Development
    X-Ayatana-Desktop-Shortcuts=NewWindow

    [NewWindow Shortcut Group]
    Name=New Window
    Exec=sublime -n
    TargetEnvironment=Unity

If you've registered your copy of Sublime Text,
but every time you open it
you're asked to enter your license,
you should try running this command.

::

    sudo chown -R username:username /home/username/.config /sublime-text-3

Just replace `username` with your account's username.
This should fix the permission error
in the case that you opened up Sublime Text as root
when you first entered the license.


Release Channels
================

At the time of this writing,
two major versions of Sublime Text exist:
Sublime Text 2 and Sublime Text 3.
Generally speaking, Sublime Text 3
is the better choice.
Even though it's technically in beta,
it's as stable as Sublime Text 2
and has more features.

Use Sublime Text 2 only
if you have found issues
running Sublime Text 3
or you depend on any package
not available for Sublime Text 3.


Getting Sublime Text 3
**********************

Sublime Text 3 currently has two release *channels*:

* `Beta`_ (default, recommended)
* `Dev`_

.. _Beta: http://www.sublimetext.com/3
.. _Dev: http://www.sublimetext.com/3dev

**Beta releases** are better tested
and more reliable for everyday use
than development builds.
**The majority of users should only
use beta releases.**

The *dev* channel is unstable:
dev builds may contain bugs
and not work reliably.
Dev builds are updated more often
than beta releases.

**Dev builds are only available
to registered users.**


Getting Sublime Text 2
**********************

We recommend Sublime Text 3,
but if you have chosen to use Sublime Text 2
you can download it `here`_.

.. _here: http://www.sublimetext.com/2
