===================
 Menus - Reference
===================

.. seealso::

   :doc:`Documentation on menus </customization/menus>`
      Explains how menus work and what you can do


File Format
===========

=============  ===========================================
**Format**     JSON (with comments)

**Extension**  ``.sublime-menu``

**Name**       One out of the list of available menus.
               See :ref:`menu-types` for the complete name list
               and what menu they represent.

**Location**   Any under :file:`{Packages}`

**Content**    A list of :ref:`menu-item-objects`
=============  ===========================================


Example
*******

The following is an excerpt
from the default :file:`Main.sublime-menu` file.

.. code-block:: json
   :linenos:

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


.. _menu-item-objects:

"Menu Item" objects
===================

:ref:`Menu items <menu-items>` may have the following properties.

Unless you are referencing an existing item via ID,
each menu item must define either
``children``, ``command`` or ``caption``.

``command``
   Name of the command to be called
   when the menu item is selected.

``args``
   Object of arguments to the command.
   For **Side Bar** and **Side Bar Mount Point** menus,
   this is extended by a ``files`` argument
   that contains all selected items in the sidebar as a list.

``caption``
   Text to be displayed in the menu.
   A single hyphen (``-``) turns the item
   into a :ref:`menu separator <menu-separators>`.

``children``
   List of :ref:`menu-item-objects` that are displayed
   when the item is hovered.
   Overrides existence of ``command`` property.

``mnemonic``
   A single character used for menu accelerators.
   The character must be contained in the caption
   and is case-sensitive.

``id``
   A unique string identifier for the menu item.
   This can be used to extend menu sections or sub-menu
   or to alter a menu item entirely.

   Refer to the :ref:`main documentation <item-ids>` on how this works.
