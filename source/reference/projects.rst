======================
 Projects - Reference
======================


.. seealso::

   :doc:`Documentation on projects </file_management/projects>`
      Explains how to work with projects.


Project information is saved in metadata files
that can be edited
to allow advanced configuration
other than adding or removing folders.
To edit the project file
of the currently active project
via the **Project → Edit Project** menu.
An anonymous project cannot be configured in any way,
because no .sublime-project file exists for it.


File Format
===========

=============  ===========================================
**Format**     JSON (with comments)

**Extension**  ``.sublime-project``

**Name**       Any

**Location**   Anywhere on your file system

**Content**    Metadata for projects
=============  ===========================================

Example
*******

Project metadata is split across three topmost sections:

- ``folders``, for the included folders;
- ``settings``, for project-specific settings; and
- ``build_systems``, for project-specific build systems.

.. code-block:: json
   :emphasize-lines: 2,14,18
   :linenos:

   {
       "folders":
       [
           {
               "path": "src",
               "folder_exclude_patterns": ["backup"]
           },
           {
               "path": "docs",
               "name": "Documentation",
               "file_exclude_patterns": ["*.css"]
           }
       ],
       "settings":
       {
           "tab_size": 8
       },
       "build_systems":
       [
           {
               "name": "List",
               "cmd": ["ls"]
           }
       ]
   }


Sections
========


.. sidebar:: Pattern precedence

   The include patterns are applied first,
   effectively excluding everything
   that is not matched by them.
   Afterwards,
   the exclude patterns further exclude
   files or folders from the project.

   .. TODO there is more to this, but it requires some reverse engineering
   .. TODO also find out whether and how the patterns are joined with their global pendants

**Folders**
   A list of folders
   that will be listed in the sidebar
   and defines the project scope.

   ``path``
      Required.
      The path may be relative to the project directory
      or absolute.
      Use ``.`` for the directory the project file is in.

   ``name``
      Optional.
      If present,
      it will appear in the side bar
      instead of the directory name.

   ``folder_exclude_patterns``
      Optional.
      List of wildcard patterns.
      Folders matching the wildcard patterns
      will be excluded from the project.

   ``folder_include_patterns``
      Optional.
      List of wildcard patterns.
      Folders matching the wildcard patterns
      will be included in the project.

   ``file_exclude_patterns``
      Optional.
      List of wildcard patterns.
      Files matching the wildcard patterns
      will be excluded from the project.

   ``file_include_patterns``
      Optional.
      List of wildcard patterns.
      Files matching the wildcard patterns
      will be included in the project.


   ``follow_symlinks``
      Optional.
      If enabled,
      symlinks will be followed for path resolution.


   Example:

   .. code-block:: json

      {
          "folders":
          [
              {
                  "path": ".",
                  "folder_include_patterns": ["foo"],
                  "file_exclude_patterns": ["*.html"]
              },
              {
                  "path": "foo",
                  "name": "foo <with HTML files>"
              }
          ]
      }

**Settings**
   A project may define project-specific settings
   that will only apply to files within that project.
   Project-specific settings override user settings,
   but not syntax-specific settings.

   Almost all settings can be overridden
   (excluding global settings).

   .. seealso::

      :ref:`settings-hierarchy`
         A detailed example for the order of precedence for settings.
      :doc:`Settings - Reference </reference/settings>`
         Reference of available settings.

**Build Systems**
   You can define project-specific build systems
   in a ``.sublime-project`` file.
   Build systems in projects
   follow the same rules as conventional build system,
   except a ``name`` must be specified for each.
   They will show up in the **Tools → Build Systems** menu
   and are selectable in the *Build With* popup,
   but only in that project.

   .. seealso::

      :doc:`Build Systems - Reference </reference/build_systems>`
         Documentation on build systems and their options.
