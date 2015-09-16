==========
 Projects
==========

Projects group sets of files and folders
to keep your work organized.
They sport project-specific settings or build systems
and you can quickly switch between them
to continue working where you left off.

Adding folders to a project is necessary for
:ref:`fm-goto-anything` and project-wide Goto Definition.

There is always an active project,
even if you haven't created one.
This is called an *Anonymous Project*
and limited in functionality.
New windows always use an anonymous project
when they first open.

Project metadata is stored in JSON files
with a ``.sublime-project`` extension.
Wherever there's a ``.sublime-project`` file,
you will find an ancillary ``.sublime-workspace`` file too.
The second one contains session data
and you shouldn't edit it.
(More on workspaces later.)

.. note::

   Generally speaking,
   it's fine to commit ``.sublime-project`` files
   to a source code repository,
   but always be mindful of what you store in them.


Creating a Project
==================

Start with an anonymous project
by opening a new window
or closing any active project
with the **Project → Close Project** menu.

You can add and remove folders to/from a project
using the **Project** menu
or the side bar's context menu.
If you drag a folder onto a Sublime Text window,
it will be added to the project too.

To save an anonymous project,
go to **Project → Save Project As...**.

After the project is saved,
you can edit it by hand and further customize it.


Opening Projects
================

Using the main menu,
you can open or switch projects
by selecting **Projects → Open Recent**,
**Projects → Switch Project…**
or **Projects → Quick Switch Project…**.

Switching will close the current project
and open the specified in the same window
whereas opening will open a new window
and open the project there.

Keyboard shortcuts related to projects:

+----------------------------------+-----------------------+
| **Quick Switch Project…**        | Ctrl + Alt + P        |
+----------------------------------+-----------------------+

Additionally,
you can open a project from the **command line**
by passing the ``.sublime-project`` file as an argument
to the ``subl`` command line helper
included with Sublime Text.


More Configurability
====================

Along with more options for individual directories,
projects can have specific build systems or settings overrides.

.. seealso::

    :doc:`/reference/projects`
        Documentation on project file format and options.


Settings Related to the Sidebar and Projects
============================================

``binary_file_patterns``
    A list of wildcards.
    Files matching these wildcards will show up in the side bar,
    but will be excluded from Goto Anything
    and Find in Files.

.. TODO: binary_file_patterns also applies to projects, right?


Workspaces
==========

Workspaces hold sessions data
associated with a project,
which includes information
about the opened files, the pane layout or find history.
A project can have multiple sessions
(or workspaces) in parallel.

A common use case is
to work on different features
within *the same project*
that require different files each
and you want to switch between them quickly.
In this case you'll want to have
a second workspace available.
Writing tests could be an example for this.

Workspaces behave very much like projects.
To create a new workspace,
select **Project → New Workspace for Project**.
To save the active workspace,
select **Project → Save Workspace As...**.

Workspaces metadata is stored in JSON files
with the ``.sublime-workspace`` extension
and will not be covered in detail
because it is not supposed to be edited by hand.

To switch between different workspaces,
use :kbd:`Ctrl+Alt+P`,
exactly as you do with projects.

As with projects, you can open a workspace
from the **command line**
by passing the desired ``.sublime-workspace`` file
as an argument to the ``subl`` command line helper
included with Sublime Text.

.. warning::

    Unlike ``.sublime-project`` files,
    ``.sublime-workspace`` files
    are not meant to be shared or edited manually.
    **You should never commit ``.sublime-workspace`` files
    into a source code repository.**
