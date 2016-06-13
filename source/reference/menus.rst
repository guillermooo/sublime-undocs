===================
 Menus - Reference
===================

.. seealso::

   :doc:`Documentation on menus </customization/menus>`
      Explains how menus work and what you can do


File Format
===========

.. include:: /_includes/menus_summary_table.g.txt


Example
*******

The following is an excerpt
from the default :file:`Main.sublime-menu` file.

.. literalinclude:: ../common/menus-example-0.txt
   :language: json


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
