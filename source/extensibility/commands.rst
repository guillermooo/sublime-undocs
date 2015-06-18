========
Commands
========

.. warning::

   Development of Sublime Text has moved on to version 3.

   As a result,
   **this branch for Sublime Text 2
   will not be updated any more**.
   Please select the ``latest`` branch
   in the panel on the bottom left
   and consider updating Sublime Text.


Commands are ubiquitous in Sublime Text: key bindings, menu items and macros
all work through the command system. They are found in other places too.

Some commands are implemented in the editor's core, but many of them are
provided as python plugins. Every command can be called from a python plugin.

Command Dispatching
*******************

Normally, commands are bound to the application object, a window object or a
view object. Window objects, however, will dispatch commands based on input
focus, so you can issue a view command from a window object and the correct
view instance will be found for you.

Anatomy of a Command
********************

Commands have a name separated by underscores, like ``hot_exit`` and can take
a dictionary of arguments whose keys must be strings and whose values must
be JSON types. Here's a few examples of commands run from the Python console::

   view.run_command("goto_line", {"line": 10})
   view.run_command('insert_snippet', {"contents": "<$SELECTION>"})
   view.window().run_command("prompt_select_project")


.. seealso::

   :doc:`Reference for commands <../reference/commands>`
        Command reference.