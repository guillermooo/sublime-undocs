===============
Command Palette
===============

.. seealso::

   :doc:`Reference for Command Palette <../reference/command_palette>`
      Complete documentation on the command palette options.


.. _ext-command-palette-overview:

Overview
========

The *command palette* is an interactive list bound to :kbd:`Ctrl+Shift+P` whose
purpose is to execute commands. The command palette is fed entries with
commands files. Usually, commands that don't warrant creating a key binding of
their own are good candidates for inclusion in a ``.sublime-commands`` file.


File Format (Commands Files)
============================

Commands files use JSON and have the ``.sublime-commands`` extension.

Here's an excerpt from ``Packages/Default/Default.sublime-commands``::

   [
       { "caption": "Project: Save As", "command": "save_project_as" },
       { "caption": "Project: Close", "command": "close_project" },
       { "caption": "Project: Add Folder", "command": "prompt_add_folder" },

       { "caption": "Preferences: Default File Settings", "command": "open_file", "args": {"file": "${packages}/Default/Base File.sublime-settings"} },
       { "caption": "Preferences: User File Settings", "command": "open_file", "args": {"file": "${packages}/User/Base File.sublime-settings"} },
       { "caption": "Preferences: Default Global Settings", "command": "open_file", "args": {"file": "${packages}/Default/Global.sublime-settings"} },
       { "caption": "Preferences: User Global Settings", "command": "open_file", "args": {"file": "${packages}/User/Global.sublime-settings"} },
       { "caption": "Preferences: Browse Packages", "command": "open_dir", "args": {"dir": "$packages"} }
   ]

``caption``
   Text for display in the command palette.
``command``
   Command to be executed.
``args``
   Arguments to pass to ``command``.


How to Use the Command Palette
==============================

#. Press :kbd:`Ctrl+Shift+P`
#. Select command

The command palette filters entries by context, so whenever you open it, you
won't always see all the commands defined in every ``.sublime-commands`` file.
