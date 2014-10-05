============
Installation
============

The process of installing Sublime Text is different for each platform.

Make sure to read the `conditions for use`_ on the official site. **Sublime Text
is not free**.

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

Download and open the *.dmg* file, and then drag the Sublime Text 3 bundle
into the *Applications* folder.

To create a `symbolic link` to use at the command line.

::

    ln -s  "/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl" /usr/local/bin/subl


Linux
=====

You can download the package and uncompress it manually. Alternatively, you
can use the command line.


Ubuntu
******

**For i386**

::

    cd ~
    wget http://c758482.r82.cf2.rackcdn.com/sublime-text_build-3047_i386.deb

**For x64**

::

    cd ~
    wget http://c758482.r82.cf2.rackcdn.com/sublime-text_build-3047_amd64.deb

Other Linux Distributions
*************************

**For i386**

::

    cd ~
    wget http://c758482.r82.cf2.rackcdn.com/sublime_text_3_build_3047_x32.tar.bz2
    tar vxjf sublime_text_3_build_3047_x32.tar.bz2

**For x64**

::

    cd ~
    wget http://c758482.r82.cf2.rackcdn.com/sublime_text_3_build_3047_x64.tar.bz2
    tar vxjf sublime_text_3_build_3047_x64.tar.bz2

Now we should move the uncompressed files to an appropriate location.

::

    sudo mv Sublime\ Text\ 3 /opt/


Lastly, we create a `symbolic link` to use at the command line.

::

    sudo ln -s /opt/Sublime\ Text\ 3/sublime_text /usr/bin/sublime


In Ubuntu, if you also want to add Sublime Text to the Unity luncher, read on.

First we need to create a new file.

::

    sudo sublime /usr/share/applications/sublime.desktop


Then copy the following into it.

::

    [Desktop Entry]
    Version=3.0
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

If you've registered your copy of Sublime Text, but every time you open it
you're asked to enter your license, you should try running this command.

::

    sudo chown -R username:username /home/username/.config /sublime-text-3

Just replace `username` with your account's username. This should fix the
permission error in the case that you opened up Sublime Text as root when you
first entered the license.


Living Dangerously... or Not
============================

Sublime Text has three release *channels*:

* `Stable`_ (default)
* `Dev`_
* `Nightly`_

.. _Stable: http://www.sublimetext.com/3
.. _Dev: http://www.sublimetext.com/dev
.. _Nightly: http://www.sublimetext.com/nightly

Furthermore, there are separate channels
for the Sublime Text 3 Beta,
which is only available to registered users.

* `3-Beta <http://www.sublimetext.com/3>`_ (comparable to *Nightly*)
* `3-Dev <http://www.sublimetext.com/3dev>`_

.. XXX: So many channels for ST3, really? Check this.

If you are working on a NASA project
or are on a tight deadline,
keep using the stable releases
and stop reading here.
**Stable releases** are better tested
and more reliable for everyday use
than the others.
**The majority of users will want
to use stable releases only.**

The *dev* and *nightly* channels are unstable, which likely means that builds
published through them will contain bugs and not work reliably.
They are updated more often than stable releases.

**Dev builds** are available for everyone
and are released inbetween stable releases.
While not quite ready for everyday use yet,
they showcase new features in a mostly unbroken fashion.

Finally, **nightly builds** are the bleeding edge, with frequent updates and
also frequent problems of various degrees of severity. They are fun to try
out, but do so at your own risk. Nightly builds are **only available for
registered users**.
