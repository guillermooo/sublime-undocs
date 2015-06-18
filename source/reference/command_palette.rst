===============
Command Palette
===============

.. warning::

   Development of Sublime Text has moved on to version 3.

   As a result,
   **this branch for Sublime Text 2
   will not be updated any more**.
   Please select the ``latest`` branch
   in the panel on the bottom left
   and consider updating Sublime Text.


The command palette is fed entries with ``.sublime-commands`` files.


File Format (``.sublime-commands`` Files)
=========================================

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
   Arguments to pass to ``command``. Note that to locate the packages folder
   you need to use a snippet-like variable: ``${packages}`` or $packages. This
   differs from other areas of the editor due to different implementations in
   the lower layers.


How to Use the Command Palette
==============================

#. Press :kbd:`Ctrl+Shift+P`
#. Select command

Entries are filtered by current context. Not all entries will be visible at all
times.