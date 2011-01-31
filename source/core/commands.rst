Commands
========

.. WARNING::
    This topic is a draft and could contain wrong information!

Commands are the basic building blocks underlying Sublime Text's automation
facilities. Key bindings, menu items, toolbar buttons and macros all work through
the command system.

Commands can take parameters and can be bound to a view, a window or the Sublime
Text application.

There are built-in and python commands. Built-in commands are included in the
editor's core and python commands are defined as plugins (python scripts). Within
python commands, there are shipped commands, included by default, and user
commands, added by the user. Don't read too much into these categorization, it's
merely there for the sake of clarity in these help files--Sublime Text doesn't
care about the differences.


Built-in commands
*****************

**The official documentation only covers Sublime Text v1 at the moment. The main
difference between Sublime Text 1 and Sublime Text 2 is naming conventions.
Sublime Text 1 used to use ``camelCase``, but Sublime Text 2 uses underscores to
separate words: ``fire_gun``. Most of the time, if a command is implemented and
documented for Sublime Text 1, it may work by changing its name accordingly.**

See `official documentation for commands`_.

.. _official documentation for commands: http://www.sublimetext.com/docs/commands

Custom commands
***************

Custom commands are created with python plugins.

Naming conventions for custom commands
--------------------------------------

Command names are written in *CamelCase* and are always suffixed with *Command*
(e. g. ``MyNewCommand``, ``NukeCommand``, ``DuplicateLineCommand``).

Sublime Text will unify all command names by removing the *Command* suffix and
separating words with underscores. Following with the previous examples, you
would call them like this (with ``view.run_command`` or a similar API call):

    - ``my_new``
    - ``nuke``
    - ``duplicate_line``

Otherwise, Sublime Text wouldn't find them and would fail silently.


Using Commands
**************

There are many ways to use commands, but if you just want to try out one of them,
you can use the python console (``CTRL + ~``).

.. code-block:: python

    # UNTESTED view command
    view.run_command("goto_line", {"line": 7})

    # UNTESTED window command
    view.window().run_command("show_minimap", {"key": True})

Note that commands take arguments passed as a dictionary; not ``**kwargs``.


Exploring Python Commands
*************************

Shipped commands can be found in many packages under the ``Packages`` folder.
In ``Packages/Default`` you'll find many python commands that are used frequently.



UNSORTED COMMANDS (WORK IN PROGRESS)
************************************

auto_complete
build
clear_fields
close_file
copy
cut
decrease_font_size
delete_word
duplicate_line
exec
expand_selection
find_all_under
find_next
find_prev
find_under
find_under_expand
find_under_prev
focus_group
hide_auto_complete
hide_overlay
hide_panel
increase_font_size
indent
insert
insert_snippet
join_lines
left_delete
move
move_to
move_to_group
new_file
new_window
next_field
next_result
next_view
next_view_in_stack
paste
paste_and_indent
prev_field
prev_result
prev_view
prev_view_in_stack
prompt_open_file
prompt_save_as
prompt_select_project
redo
redo_or_repeat
reindent
right_delete
run_macro
run_macro_file
save
scroll_lines
select_all
select_lines
set_layout
show_overlay
show_panel
show_scope_name
single_selection
slurp_find_string
slurp_replace_string
soft_redo
soft_undo
sort_lines
split_selection_into_lines
swap_line_down
swap_line_up
switch_file
toggle_comment
toggle_full_screen
toggle_overwrite
toggle_record_macro
toggle_side_bar
transpose
undo
unindent

