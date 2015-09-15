=======
 Menus
=======

.. seealso::

   :doc:`Reference for menus </reference/menus>`
      Reference for menu creation.

Sublime Text provides several menus
that can be modified,
most notably by adding menu items.


File Format
===========

=============  ===========================================
**Format**     JSON (with comments)

**Extension**  ``.sublime-menu``

**Name**       One out of the list of available menus.
               See :ref:`menu-types` for the complete list
               and what menu they represent.

**Location**   Any

**Content**    A list of "menu item" objects.
=============  ===========================================

Example
*******

The following is an excerpt
from the default :file:`Main.sublime-menu` file.

.. code-block:: json

   [
       {
           "caption": "Edit",
           "mnemonic": "E",
           "id": "edit",
           "children":
           [
               { "command": "undo", "mnemonic": "U" },
               { "command": "redo_or_repeat", "mnemonic": "R" },
               {
                   "caption": "Undo Selection",
                   "children":
                   [
                       { "command": "soft_undo" },
                       { "command": "soft_redo" }
                   ]
               },
               { "caption": "-", "id": "clipboard" },
               { "command": "copy", "mnemonic": "C" },
               { "command": "cut", "mnemonic": "t" },
               { "command": "paste", "mnemonic": "P" },
               { "command": "paste_and_indent", "mnemonic": "I" },
               { "command": "paste_from_history", "caption": "Paste from History" }
           ]
       }
   ]


Images
******

.. figure:: images/context_menu_default.png
   :class: shadowed
   :figclass: float-left
   :figwidth: 50%

   The default context menu in the editing area.

.. figure:: images/context_menu_modified.png
   :class: shadowed
   :figclass: float-left
   :figwidth: 50%

   A modified context menu in the editing area.


.. _menu-types:

Available Menus
===============

The file name
of a ``.sublime-menu`` file
specifies the menu in the application
to be modified.

The following menus are available:

========================   ===============
     File/Menu Name          Description
========================   ===============
**Main**                   Main menu

**Context**                Context menu in the editing area

**Find in Files**          Appears when clicking the "…" button
                           in the :doc:`Find in Files
                           </search_and_replace/search_and_replace_files>` panel

**Side Bar**               Context menu for each node in the sidebar

**Side Bar Mount Point**   Additional context menu items
                           for the top-level nodes in the sidebar

**Tab Context**            Context menu of the tab bar

**Widget Context**         Context menu of input fields
                           in all kinds of widgets,
                           including Command Palette, Goto Anything,
                           the find panels
                           and those opened by APIs
========================   ===============

Additionally,
the following four menus open
when their column in the status bar
is clicked:

- **Encoding**
- **Line Endings**
- **Indentation**
- **Syntax**

.. figure:: images/statusbar_menu.gif
   :class: shadowed

   Demonstration of a status bar menu.


.. _menu-items:

Menu Items
==========

A menu item can either
invoke a command (with arguments)
when it is selected
or have a sub-menu.

The available properties are:

- a command name,
- arguments for the command,
- an ID,
- a caption,
- a mnemonic and
- a sub-menu.

In order to function properly,
it must provide *at least* either out of

- a command name,
- a caption and a sub-menu or
- just a caption or
- an ID (see below).

When parsing a menu item,
the following rules apply:

#. The presence of a sub-menu
   overrides the command and its arguments,
   making it effectively non-existent.
   It also overrides the :ref:`separator caption <menu-separators>`.

#. If no caption is provided,
   a caption is inferred
   from the command's ``description`` method.
   If neither caption nor command are provided,
   the caption is an empty string.

#. The character used for the mnemonic
   must be contained in the item's caption.
   Mnemonics are case-sensitive.

#. Menu items referencing
   commands that can not be found
   are disabled.

#. Menu items can be hidden or disabled
   by the command.

.. TODO add refs to Command methods


.. _menu-separators:

Separators
**********

Separators are menu items
with the caption ``-``
and no sub-menu.
They are commonly used
to group menu items with similar purposes
or with a shared thematic.
Separators can not call commands,
but the presence of a sub-menu
converts the separator item into a regular item
with a single hyphen as its caption.

For rendering,
multiple consecutive separators are reduced to one
and separators at the beginning or the end of a menu
are not displayed.


.. _menu-merging:

Menu Merging
============

Generally,
``.sublime-menu`` files are loaded in package load order.
Menu files with the same name are concatenated
by extending the menu item list
with all items in the file,
unless IDs are involved.
See below for this case.

Menu files in the same package are loaded lexicographically
in the root folder,
after which the sub folders are traversed similarly.

As a special case,
menu items from the *User* package
in the standard non-ID section
are always inserted after any standard items
from other packages.


.. _item-ids:

Item IDs
========

When a menu item specifies an ID,
a separate section within the menu is searched for
and, if it does not exist,
created at the very end of the menu.
*This is a forward lookup only.*
The ID determines the section's name
and the menu item with the ID
will be the first item in this section.
All following items in the file
will then be appended to the ID's section,
until another item with an ID is specified.

If two menu items
from different ``.sublime-menu`` files
reference the same item via ID,
Sublime Text will override the previously defined item's parameters
with the new parameters,
if there are any.
Child elements in a sub menu are appended
and do not override.
All following items are then appended to the ID's section,
until another item with an ID is specified.

Common practice is
to assign IDs to separators
and items having a sub-menu,
to allow other packages or the user themselves
to easily customize the menu.
Separators always mark the beginning of a section,
while it is required to address the exact same menu item
in order to append items to its sub-menu.

.. note::

   Due to the strict forward lookup
   it is possible to have
   *multiple different items with the same ID*
   in one menu.

   Because of the potential confusion this may cause
   it is discouraged.

   Example:
   The following three IDs
   are defined in a menu, in order:
   ``test, test2, test``.

   The item with the second "test" ID
   can then be targeted
   using the following ID combinations:
   ``test, test2, test``; ``test, test`` or ``test2, test``.


Sub-Menus
=========

Every menu item can have a sub-menu,
where hovering the item
reveals the items grouped behind it.
Sub-menus are independent menus
with their own ID hierarchy.

In order to extend a sub-menu
from a different menu file,
an ID must be specified in both occasions
to target the correct item.


The Main Menu
=============

Unlike all other menus,
the Main Menu's root menu
represents the menu items in the menu bar,
for example "File" and "Help".
Other than that,
there is no notable difference.


Interface For Commands
======================

Each menu item can be dynamically

#. hidden,
#. disabled,
#. checked, or
#. assigned a different caption.

For this,
commands may provide method endpoints in their class.
The endpoints are called with the same arguments
as the actual command would be
(except for ``edit`` in ``TextCommand`` s),
however they may also accept no parameters at all.

#. ``is_visible``
#. ``is_enabled``
#. ``is_checked``
#. ``description``

Note that these are also relevant
for the command palette
to an extent.

.. seealso::

   `Official API Documentation on the Command endpoints`__

   .. __: http://www.sublimetext.com/docs/3/api_reference.html#sublime_plugin.ApplicationCommand


Context Menus in the Side Bar
=============================

The **Side Bar** and **Side Bar Mount Point** menus
are different to the others
in that they have **contextual information** available
regarding the selected item(s).
The selected items in the sidebar,
both directories and files,
are passed as a list to the specified command
in a ``files`` argument.
