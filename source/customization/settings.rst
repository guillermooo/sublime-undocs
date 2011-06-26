========
Settings
========

Sublime Text uses ``.sublime-settings`` files to store configuration data.
Settings control many aspects of the editor, from visual layout to file type
settings.


Format
======

Settings files use JSON and have the ``.sublime-settings`` extension. The purpose
of a ``.sublime-settings`` file is determined by its name. For example,
``Python.sublime-settings`` controls settings for Python files, whereas
``Minimap.sublime-settings`` controls the minimap settings, etc.

.. XXX This belongs in a file of its own.


Types of Settings
=================

As mentioned above, there are several types of ``.sublime-settings`` files
controlling several aspects of the editor. In this section only file type
settings are explained.


File Settings
=============

A hierarchy of ``.sublime-settings`` files controls settings specific to a file
type. Therefore, the location of settings matters. As it's always the case when
merging files of any kind, Sublime Text gives the top priority to files in the
``User`` package. See the section :ref:`merging-and-order-of-precedence` for
more information.

In addition, there's yet another layer of settings that overrides the others:
the *session*. Session data is updated as you work on a file, so if you adjust
settings for a file in any way (mainly through API calls), they will be
recorded in the session and will take precedence over any ``.sublime-settings``
files. Calls to ``obj.settings().get()`` always return the value in effect for
``obj``.

When untangling the applicable settings for a file at any time, one must also
keep in mind that Sublime Text adjusts settings automatically in some
situations. For example, if ``auto_detect_indentation`` is on, the value a call
to ``view.settings().get('tab_size')`` returns might appear unexpected,
especially if you've explicitly set ``tab_size`` moments earlier.

Below, you can see the order in which Sublime Text would process a
hypothetical hierarchy of settings for Python on Windows:

- :file:`Packages/Default/Base File.sublime-settings`
- :file:`Packages/Default/Base File (Windows).sublime-settings`
- :file:`Packages/User/Base File.sublime-settings`
- :file:`Packages/Python/Python.sublime-settings`
- :file:`Packages/User/Python.sublime-settings`
- *Session data for the current file*
- *Auto adjusted settings*


Global File Type Settings
=========================

There are two types of global settings files affecting file types:

- :file:`Base File.sublime-settings` and
- :file:`Base File (<platform>).sublime-settings`.

:file:`Base File` is always in effect for all platforms, whereas
:file:`Base File (<platform>)` only applies to the named platform. Multiple
:file:`Base File` and :file:`Base File (<platform>)` files can coexist with
the exception of ``Packages/User``. From ``Packages/User``, only :file:`Base File`
will be read. This is so there is only one global file that overrides all the
other ones.

Legal values for ``<platform>`` are: ``Linux``, ``OSX`` and ``Windows``.


Settings Specific to a File Type
================================

If you want to target a specific file type in a ``.sublime-settings`` file, give
it the name of the applicable syntax definition for said file type. Note you
have to use the syntax definition's *file name*, not a *scope name*. For example,
if our syntax definition was called :file:`Python.tmLanguage`, we'd need to call
our settings file :file:`Python.sublime-settings`.

Settings files for specific file types usually live in packages, like :file:`Packages/Python`, but there can be multiple settings files for the same file
type in separate locations. Similarly to global settings, one can establish
platform-specific settings for file types. For example,
``Python (Linux).sublime-settings`` would only be consulted under Linux. Also,
under ``Pakages/User`` only ``Python.sublime-settings`` would be read, but not
``Python (<platform>).sublime-settings``.

Regardless of its location, any file-type-specific settings file has precedence
over every global settings file affecting file types.


Where to Store User Settings
============================

Whenever you want to persist settings, especially if they should be preserved
between upgrades, place the relevant ``.sublime-settings`` file in :file:`Packages/User`.
This is the recommended place to store user settings.

You can nevertheless save settings files under other subdirectories of ``Packages``.
For example, ``Packages/ZZZ/Python.sublime-settings`` would override
``Packages/Python/Python.sublime-settings`` by virtue of alphabetical order.
However, ``Packages/User/Python.sublime-settings`` would continue to have the
highest precedence for the Python file type settings.
