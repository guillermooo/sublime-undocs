========
Settings
========

Sublime Text stores configuration data in *.sublime-settings* files.
Flexibility comes at the price of a slightly complex system for applying
settings. However, here's a rule of thumb:

Always place your personal settings files under *Packages/User* to guarantee
they will take precedence over any other conflicting settings files.

With that out of the way, let's unveil, to please masochistic readers,
the mysteries of how settings work.


Format
======

Settings files use JSON and have the *.sublime-settings* extension.


Types of Settings
=================

The purpose of each *.sublime-settings* file is determined by its name. These
names can be descriptive (like *Preferences (Windows).sublime-settings*
or *Minimap.sublime-settings*), or they can be related to what the settings
file is controlling. For example, file type settings need to carry the name
of the *.tmLanguage* syntax definition for the file type. Thus, for the
 *.py* file type, whose syntax definition is contained in *Python.tmLanguage*,
 the corresponding settings file would be called *Python.sublime-settings*.

Also, some settings files only apply to specific platforms. This can be
inferred from the filenames: *Preferences (Windows).sublime-settings*,
*Preferences (Linux).sublime-settings*, etc.

**This is important:** Platform-specific settings files in the *Packages/User*
folder are ignored. In this way, you can be sure that a single Platform-specific
settings file will override all others.


How to Access and Edit Common Settings Files
============================================

Unless you need very fine-grained control over settings, you can access the main
configuration files through the **Preferences | Settings - User** and
**Preferences | Settings - More** menu items. Editing **Preferences - Settings Default**
isn't a smart thing to do, because changes will be reverted with every update
to the software. However, you can use that file for reference: it contains comments
explaining the purpose of all available global and file type settings.


Order of Precedence of *.sublime-settings* Files
==================================================

The same settings file (such as *Python.sublime-settings*) can appear in multiple
places. All settings defined in identically named files will be merged together
and overwritten according to predefined rules. See
:ref:`merging-and-order-of-precedence` for more information.

Let us remember again that any given settings file in *Packages/User* ultimately
overrides every other settings file of the same name.

In addition to settings files, Sublime Text maintains *session* data---settings
for the particular set of files being currently edited. Session data is updated
as you work on files, so if you adjust settings for a particular file in any
way (mainly through API calls), they will be recorded in the session and will
take precedence over any applicable *.sublime-settings* files.

To check the value of a setting for a particular file being edited, use
*view.settings().get(<setting_name>)* from the console.

Finally, it's also worth noting that some settings may be automatically adjusted
for you. Keep this in mind if you're puzzled about some setting's value. For
instance, this is the case for certain whitespace-related settings and the
``syntax`` setting.

Below, you can see the order in which Sublime Text would process a
hypothetical hierarchy of settings for Python files on Windows:

- *Packages/Default/Preferences.sublime-settings*
- *Packages/Default/Preferences (Windows).sublime-settings*
- *Packages/User/Preferences.sublime-settings*
- *Packages/Python/Python.sublime-settings*
- *Packages/User/Python.sublime-settings*
- Session data for the current file
- Auto adjusted settings


Global Editor Settings and Global File Settings
===============================================

These settings are stored in *Preferences.sublime-settings* and
*Preferences (<platform>).sublime-settings* files. The defaults can be
found in *Packages/Default*.

Valid names for *<platform>* are ``Linux``, ``OSX``, and ``Windows``.


File Type Settings
==================

If you want to target a specific file type, name the *.sublime-settings* file
after the file type's syntax definition. For example, if our syntax definition
was called *Python.tmLanguage*, we'd need to call our settings file
*Python.sublime-settings*.

Settings files for specific file types usually live in packages, like
*Packages/Python*, but there can be multiple settings files in separate
locations for the same file type.

Similarly to global settings, one can establish platform-specific settings for
file types. For example, *Python (Linux).sublime-settings* would be
consulted only under Linux.

Also, let us stress that, under *Packages/User*, only *Python.sublime-settings*
would be read, but not any *Python (<platform>).sublime-settings* variants.

Regardless of its location, any file-type-specific settings file has precedence
over every global settings file affecting the file type.


Where to Store User Settings (Once Again)
=========================================

Whenever you want to save settings, especially if they should be preserved
between software updates, place the corresponding *.sublime-settings* file in
*Packages/User*.
