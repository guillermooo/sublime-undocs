========
Settings
========

Sublime Text uses ``.sublime-settings`` files to store configuration data. Settings
control many aspects of the editor, from visual layout to file type options.
The purpose of ``.sublime-settings`` files is determined by their name. The sections
below deal with settings files in detail.

.. XXX This belongs in a file of its own.

File Settings
=============

A hierarchy of ``.sublime-settings`` files controls settings specific to a file
type. Therefore, the location of settings matters. As it's always the case when
merging files of any kind, Sublime Text gives the top priority to files in the ``User``
package. See the section :ref:`merging-and-order-of-preference` for more information.

The above notwithstanding, there's yet another layer of settings that overrides
the others: the *session*. Session data is updated as you work on a file, so if
you adjust settings for a file in any way (mainly through API calls), they
will be recorded in the session and will take precedence over any
``.sublime-settings`` files. Calls to ``obj.settings().get`` always return the value in effect
for ``obj`` at the time it was called.

Another thing to keep in mind when untangling the applicable settings for a file at any
time is that Sublime Text adjusts settings behind your back in some
situations. For example, if ``auto_detect_indentation`` is on, you might be
confused by the value a call to ``view.settings().get('tab_size')`` returns, especially
if you've explicitly set ``tab_size`` moments earlier.

For example, this is the order in which Sublime Text would process a
hypothetical hierarchy of settings for Python on Windows:

- :file:`Packages/Default/Base File.sublime-settings`
- :file:`Packages/Default/Base File (Windows).sublime-settings`
- :file:`Packages/User/Base File.sublime-settings`
- :file:`Packages/User/Base File (Windows).sublime-settings`
- :file:`Packages/Python/Python.sublime-settings`
- :file:`Packages/User/Python.sublime-settings`
- *Session data for the current file*
- *Auto adjusted settings*

Global File Type Settings
=========================

There are two types of global settings files affecting file types:
:file:`Base File` and :file:`Base File (Platform)`. :file:`Base File` is always in effect for all
platforms, whereas the second one only applies to the named platform. Multiple
:file:`Base File` and :file:`Base File (Platform)` files can coexist.

Settings Specific to a File Type
================================

If you want to target a specific file type in a ``.sublime-settings`` file, give it
the name of the applicable syntax definition for said file type. Note you have
to use the syntax definition's *file name*, not a *scope name*. For example, if our syntax
definition was called :file:`Python.tmLanguage`, we'd need to call our settings file
:file:`Python.sublime-settings`. Settings files for specific file types usually live in
packages, like :file:`Packages/Python`, but there can be multiple settings files for
the same file type in separate locations.

Where to Store User Settings
============================

Whenever you want to persist settings, especially if they should be preserved
between upgrades, place the relevant ``.sublime-settings`` file in :file:`Packages/User`.