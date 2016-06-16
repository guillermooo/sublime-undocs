====================
Settings – Reference
====================

.. warning::

   This page may contain outdated or incomplete information.
   You can see a description of most available settings in the
   default settings file (**Preferences → Settings - Default** or
   :file:`Default/Preferences.sublime-settings`).

.. seealso::

   :doc:`Customization - Settings </customization/settings>`
      A detailed overview on settings in Sublime Text and their order of
      precedence.


Global Settings
===============

.. FIXME: Wrong information

Global settings can only be modified
in :file:`Preferences.sublime-settings` and :file:`Preferences (<platform>).sublime-settings`
(where ``<platform>`` can be any of ``Linux``, ``OSX`` or ``Windows``)
and, where indicated, also in :file:`.sublime-project` files.

.. XXX obviously, some settings are missing here ... but do we really need to
.. include all the settings with a brief description? That's what the comments
.. in the default settings are for, actually.

.. include:: /_includes/settings_global.g.txt


File Settings
=============

Whitespace and Indentation
**************************

.. include:: /_includes/settings_file.g.txt

Visual Settings
***************

.. include:: /_includes/settings_visual.g.txt

Automatic Behavior
******************

.. include:: /_includes/settings_automatic.g.txt

System and Miscellaneous Settings
*********************************

.. include:: /_includes/settings_system.g.txt


Build and Error Navigation Settings
***********************************

.. include:: /_includes/settings_build.g.txt


File and Directory Settings
***************************

.. include:: /_includes/settings_filesystem.g.txt


Input Settings
**************

.. include:: /_includes/settings_input.g.txt
