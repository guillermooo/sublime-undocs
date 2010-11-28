Commands
========

.. WARNING::
    This topic is a draft and could contain wrong information!

Commands are the basic building blocks underlying Sublime Text's automation
facilities. They can be built-in or custom. Commands can take parameters and can
be bound to a view, a window or the Sublime Text application.

Built-in commands
*****************

See `official documentation for commands`_.

.. _official documentation for commands: http://www.sublimetext.com/docs/commands

Custom commands
***************

Custom commands are created with python plugins.

Naming conventions for custom commands
--------------------------------------

Command names are written in *camelCase* and are always suffixed with *Command*
(e. g. ``MyNewCommand``, ``NukeCommand``, ``DuplicateLineCommand``).

Sublime Text will unify all command names by removing the *Command* suffix and
lowercasing the initial letter. Following with the previous examples, you would
call them like this (with ``view.runCommand`` or a similar API call):

    - ``myNew``
    - ``nuke``
    - ``duplicateLine``

Otherwise, Sublime Text wouldn't find them and would fail silently.
