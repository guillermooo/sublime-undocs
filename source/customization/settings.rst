========
Settings
========

Sublime Text stores configuration data in *.sublime-settings* files.
Flexibility comes at the price of a slightly complex system for applying
settings. However, here's a rule of thumb:

Always place your personal settings files under *Packages/User* to guarantee
that they will take precedence over any other conflicting settings files.

With that out of the way, let's unveil the mysteries of how settings work, to
the enjoyment of masochistic readers.


Format
======

Settings files use JSON and have the *.sublime-settings* extension.


Types of Settings
=================

The purpose of each *.sublime-settings* file is determined by its name. These
names can be descriptive (like :file:`Preferences (Windows).sublime-settings` or
:file:`Minimap.sublime-settings`), or they can be related to what the settings
file is controlling. For example, file type settings need to carry the name of
the *.tmLanguage* syntax definition for the file type. Thus, for the *.py* file
type, whose syntax definition is contained in :file:`Python.tmLanguage`, the
corresponding settings files would be called :file:`Python.sublime-settings`.

.. XXX does this also work for custom .sublime-settings files?

Also, some settings files only apply for specific platforms. This can be
inferred from the file names, e.g.
:file:`Preferences ({platform}).sublime-settings`. Valid names for *platform*
are ``Windows``, ``Linux``, ``OSX``.

This is **important**: Platform-specific settings files in the
:file:`Packages/User` folder are ignored. This way, you can be sure a single
settings file overrides all the others.

Settings changes are usually updated in real time but you might have to restart
Sublime Text in order to load *new* settings files.


How to Access and Edit Common Settings Files
============================================

Unless you need very fine-grained control over settings, you can access the main
configuration files through the **Preferences | Settings - User** and
**Preferences | Settings - More** menu items. You should not edit **Preferences | Settings - Default**,
because changes will be reverted with every update to the software. However, you
can use that file for reference: it contains comments explaining the purpose of all
available global and file type settings.


Order of Precedence of *.sublime-settings* Files
==================================================

The same settings file (such as :file:`Python.sublime-settings`) can appear in
multiple places. All settings defined in identically named files will be merged
together and overwritten according to predefined rules. See
:ref:`merging-and-order-of-precedence` for more information.

Let us remember again that any given settings file in :file:`Packages/User`
ultimately overrides every other settings file of the same name.

In addition to settings files, Sublime Text maintains *session* data --settings
for the particular set of files being currently edited. Session data is updated
as you work on files, so if you adjust settings for a particular file in any
way (mainly through API calls), they will be recorded in the session and will
take precedence over any applicable *.sublime-settings* files.

To check a setting's current value for a particular file, use
:samp:`view.settings().get("{setting_name}")` from the console.

Lastly, it's also worth noting that some settings may be adjusted automatically
for you. Keep this in mind if you're puzzled about some setting's value. For
instance, this is the case for certain whitespace-related settings and the
``syntax`` setting.

See `The Settings Hierarchy`_ for a full example of the order of precedence.


Global Editor Settings and Global File Settings
===============================================

These settings are stored in file:`Preferences.sublime-settings` and
:file:`Preferences ({platform}).sublime-settings` files. The defaults can be
found in :file:`Packages/Default`.

Valid names for *platform* are ``Windows``, ``Linux``, ``OSX``.


File Type Settings
==================

If you want to target a specific file type, name the *.sublime-settings* file
after the file type's syntax definition. For example, if our syntax definition
was called :file:`Python.tmLanguage`, we'd need to call our settings file
`Python.sublime-settings`.

.. XXX does the tmLanguage's "name" key have any effect on this?

Settings files for specific file types usually live in packages, like
:file:`Packages/Python`, but there can be multiple settings files for the same
file type in separate locations.

Similarly to global settings, one can establish platform-specific settings for
file types. For example, :file:`Python (Linux).sublime-settings` would only be
consulted under Linux.

Also, let us emphasize that under :file:`Pakages/User` only
:file:`Python.sublime-settings` would be read, but not any
:file:`Python ({platform}).sublime-settings` variant.

Regardless of its location, any file-type-specific settings file has precedence
over a global settings file affecting the same filet type.


.. _settings-hierarchy:

The Settings Hierarchy
======================

Below, you can see the order in which Sublime Text would process a
hypothetical hierarchy of settings for Python files on Windows:

- :file:`Packages/Default/Preferences.sublime-settings`
- :file:`Packages/Default/Preferences (Windows).sublime-settings`
- :file:`Packages/AnyOtherPackage/Preferences.sublime-settings`
- :file:`Packages/AnyOtherPackage/Preferences (Windows).sublime-settings`
- :file:`Packages/User/Preferences.sublime-settings`
- Settings from the current project
- :file:`Packages/Python/Python.sublime-settings`
- :file:`Packages/Python/Python (Windows).sublime-settings`
- :file:`Packages/User/Python.sublime-settings`
- Session data for the current file
- Auto-adjusted settings


Where to Store User Settings (Once Again)
=========================================

Whenever you want to save settings, especially if they should be preserved
between software updates, place the corresponding *.sublime-settings* file in
:file:`Packages/User`.
