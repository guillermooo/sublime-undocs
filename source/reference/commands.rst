========
Commands
========

Overview
========

.. named actions, used everywhere, take json arguments

This list of commands is a work in progress.


.. _cmd-about-paths:

About Paths in Command Arguments
================================

Some commands take paths as parameters. Among these, some support snippet-like
syntax, while others don't. A command of the first kind would take a parameter
like :file:`${packages}/SomeDir/SomeFile.ext` whereas a command of the second kind
would take a parameter like :file:`Packages/SomeDir/SomeFile.ext`.

Generally, newer commands support the snippet-like syntax.

Commands expect UNIX-style paths if not otherwise noted, even on
Windows (e. g. :file:`/c/Program Files/Sublime Text 2/sublime_plugin.py`).

Often, relative paths in arguments to commands are assumed to start at the
``Data`` directory.

Variables in Paths as Arguments
-------------------------------

The same variables available to build systems are expanded in arguments to
commands. See :ref:`build-system-variables` for more information.


.. TODO: split into Window and Text (and Application) commands since they behave
.. differently and require other call mechanisms when called from a plugin

.. _cmd-list:

Commands
========

.. py:currentmodule:: sublime

.. note::

	This list is still incomplete. While there are a few commands that are just
	not useful to a user (or even package developer) there are also a few undocumented
	commands or commands without a discription.

**build**
	Runs a build system.

	- **variant** [String]: Optional. The name of the variant to be run.

**set_build_system**
	Changes the current build system.

	- **file** [String]: Path to the build system. If empty, Sublime Text tries
	  to automatically find an appropriate build systems from specified
	  selectors.
	- **index** [Int]: Used in the **Tools | Build System** menu but otherwise
	  probably not useful.

**new_build_system**
	Creates a new buffer and inserts a build system template.

**toggle_save_all_on_build**
	Toggles whether all open files should be saved before starting the build.

**run_macro_file**
	Runs a *.sublime-macro* file.

	- **file** [String]: Relative path to the macro file.

**insert_snippet**
	Inserts a snippet from a string or *.sublime-snippet* file.

	- **contents** [String]: Snippet as a string to be inserted. Remember that
	  backslashes ``\`` have to be escaped, like in every other JSON string.
	- **name** [String]: Relative :ref:`path <cmd-about-paths>` to the *.sublime-snippet* file to be
	  inserted.

	.. seealso::

		:doc:`/extensibility/snippets`
			Documentation on snippets and their variable features.

**insert**
	Inserts a string.

	- **characters** [String]: String to be inserted.

**move**
	Advances the caret by predefined units.

	- **by** [Enum]: Values: *characters*, *words*, *word_ends*, *subwords*,
	  *subword_ends*, *lines*, *pages*, *stops*.
	- **forward** [Bool]: Whether to advance or reverse in the buffer.
	- **word_begin** [Bool]
	- **empty_line** [Bool]
	- **punct_begin** [Bool]
	- **separators** [Bool]

**move_to**
	Advances the caret to predefined locations.

	- **to** [Enum]: Values: *bol*, *eol*, *bof*, *eof*, *brackets*.
	- **extend** [Bool]: Whether to extend the selection. Defaults to ``false``.

**switch_file**
	Switches between two files with the same name and different extensions.

	- **extensions** [String]: Extensions (without leading dot) for which
	  switching will be enabled.

**open_file**
	Opens the specified file.

	- **file** [String]: Absolute or relative :ref:`path <cmd-about-paths>`
	  to the file to be opened. Relative paths will originate from the recently
	  accessed directory (e.g. the directory of the currently opened file).
	- **contents** [String]: This string will be written to the new buffer if
	  the file does not exist.

**open_dir**
	Opens the specified directory with the default file manager.

	- **dir** [String]: The directory to open.

**open_file_settings**
	Opens the syntax-specific user settings file for the current syntax.

**new_window**
	Opens a new window.

**close_window**
	Closes the active window.

**close**
	Closes the active view.

**close_file**
	Closes the active view and, under certain circumsances, the whole
	application.
	XXX Sounds kinda wrong.

**exit**
	Exits the whole application with all open windows.

**reopen_last_file**
	Reopens the last closed file.

**save**
	Saves the active file.

	- **encoding** [String]: The file encoding to save as.

**prompt_save_as**
	Prompts for a new file name and saves the active file.

**save_project_as**
	Prompts for a new file name and saves the current project.

**prompt_select_project**
	Opens a popup with recently accessed projects where you can fuzzy-search.

**prompt_open_project**
	Prompts for a project file to open as a project.

**close_project**
	Closes the current project.

**prompt_add_folder**
	Prompts for a folder to add to the current project.

**close_folder_list**
	Removes all folders from the current project.

**refresh_folder_list**
	Reloads all folders in the current project and updates the side bar.

**toggle_sidebar**
	Shows or hides the sidebar.

**toggle_show_open_files**
	Shows ot hides the open files in the sidebar.

**toggle_status_bar**
	Shows or hides the status bar.

**toggle_full_screen**
	Toggles full screen mode on or off.

**toggle_distraction_free**
	Toggles distraction free mode on or off.

**toggle_tabs**
	Shows or hides the tab bar.

**toggle_menu**
	Shows or hides the menu bar.

**toggle_minimap**
	Shows or hides the minimap.

**left_delete**
	Deletes the character right before the caret.

**right_delete**
	Deletes the character right after the caret.

**undo**
	Undoes the latest action.

**redo**
	Reapplies the latest undone action.

**redo_or_repeat**
	Performs the latest action again.

.. XXX does this mean selections?

**soft_undo**
	Undoes each action stepping through granular edits.

**soft_redo**
	Redoes each action stepping through granular edits.

**cut**
	Removes the selected text and sends it to the system clipboard. Put
	differently, it cuts.

**copy**
	Sends the selected text to to the system clipboard.

**paste**
	Inserts the clipboard contents after the caret.

	- **clipboard** [String]: May be *selection*. XXX what other values are
	  allowed?

**paste_and_indent**
	Inserts the clipboard contents after the caret and indents contextually.

**select_lines**
	Adds a line to the current selection.

	- **forward** [Bool]: Whether to add the next or previous line. Defaults to
	  ``true``.

**scroll_lines**
	Scrolls lines in the view.

	- **amount** [Float]: Positive values scroll lines down and negative values
	  scroll lines up.

**prev_view**
	Switches to the previous view.

**next_view**
	Switches to the next view.

**next_view_in_stack**
	Switches to the most recently active view.

**previous_view_in_stack**
	Switches to the view that was active before the most recently active view.

.. XXX I don't think this is very clear or even true.

**select_all**
	Select the view's content.

**split_selection_into_lines**
	Unsurprisingly, it splits the selection into multiple selections, one on
	each line.

**single_selection**
	Collapses multiple selections into a single selection.

**clear_fields**
	Breaks out of the active snippet field cycle.

**hide_panel**
	Hides the active panel.

	- **cancel** [Bool]: Notifies the panel to restore the selection to what it
	  was when the panel was opened. (Only incremental find panel.)

**hide_overlay**
	Hides the active overlay. Show the overlay using the show_overlay command.

**hide_auto_complete**
	Hides the auto complete list.

**insert_best_completion**
	| Inserts the best completion that can be inferred from the current context.
	| XXX Probably useless. XXX

	- **default** [String]: String to insert failing a best completion.

**replace_completion_with_next_completion**
	XXX Useless for users. XXX

**reindent**
	Corrects indentation of the selection with regular expressions set in the
	syntax's preferences. The base indentation will be that of the line before
	the first selected line.
	Sometimes does not work as expected.

**indent**
	Increments indentation of selection.

**unindent**
	Unindents selection.

**detect_indentation**
	Guesses the indentation from the current file.

**next_field**
	Advances the caret to the text snippet field in the current snippet field
	cycle.

**prev_field**
	Moves the caret to the previous snippet field in the current snippet field
	cycle.

**commit_completion**
	| Inserts into the buffer the item that's currently selected in the auto
	  complete list.
	| XXX Probably not useful for users. XXX

**toggle_overwrite**
	Toggles overwriting on or off.

**expand_selection**
	Extends the selection up to predefined limits.

	- **to** [Enum]: Values: *bol*, *hardbol*, *eol*, *hardeol*, *bof*, *eof*,
	  *brackets*, *line*, *tag*, *scope*, *indentation*.

**close_tag**
	Surrounds the current inner text with the appropiate tags.

**toggle_record_macro**
	Starts or stops the macro recorder.

**run_macro**
	Runs the macro stored in the macro buffer.

**save_macro**
	Prompts for a fiel path to save the macro in the macro buffer to.

**show_overlay**
	Shows the requested overlay. Use the **hide_overlay** command to hide it.

	- **overlay** [Enum]:
		The type of overlay to show. Possible values:

		- *goto*: Show the :ref:`Goto Anything <fm-goto-anything>` overlay.
		- *command_palette*: Show the :doc:`../extensibility/command_palette`.

	- **show_files** [Bool]: If using the goto overlay, start by displaying
	  files rather than an empty widget.
	- **text** [String]: The initial contents to put in the overlay.

**show_panel**
	Shows a panel.

	- **panel** [Enum]: Values: *incremental_find*, *find*, *replace*,
	  *find_in_files*, *console* or *output.<panel_name>*.
	- **reverse** [Bool]: Whether to search backwards in the buffer.
	- **toggle** [Bool]: Whether to hide the panel if it's already visible.

**find_next**
	Finds the next occurrence of the current search term.

**find_prev**
	Finds the previous occurrence of the current search term.

**find_under**
	Finds the next occurrence of the current selection or the current word.

**find_under_prev**
	Finds the previous occurrence of the current selection or the current word.

**find_under_expand**
	Adds a new selection based on the current selection or expands the
	selection to the current word.

**find_under_expand_skip**
	Adds a new selection based on the current selection or expands the
	selection to the current word while removing the current selection.

**find_all_under**
	Finds all occurrences of the current selection or the current word.

**slurp_find_string**
	Copies the current selection or word into the "find" field of the find
	panel.

**slurp_replace_string**
	Copies the current selection or word into the "replace" field of the find
	and replace panel.

**next_result**
	Advance to the next captured result.

**prev_result**
	Move to the previous captured result.

**toggle_setting**
	Toggles the value of a boolean setting. This value is view-specific.

	- **setting** [String]: The name of the setting to be toggled.

**set_setting**
	Set the value of a setting. This value is view-specific.

	- **setting** [String]: The name of the setting to changed.
	- **value** [*]: The value to set to.

**set_line_ending**
	Changes the line endings of the current file.

	- **type** [Enum]: *windows*, *unix*, *cr*

**next_misspelling**
	Advance to the next misspelling

**prev_misspelling**
	Move to the previous misspelling.

**swap_line_down**
	Swaps the current line with the line below.

**swap_line_up**
	Swaps the current line with the line above.

**toggle_comment**
	Comments or uncomments the active lines, if available.

	- **block** [Bool]: Whether to prefer a block comment.

**join_lines**
	Joins the current line with the next one.

**duplicate_line**
	Duplicates the current line or selections if any.

**auto_complete**
	Opens the auto complete list.

**replace_completion_with_auto_complete**
	XXX Useless for users. XXX

**show_scope_name**
	Shows the name for the caret's scope in the status bar.

.. _cmd-exec:

**exec**
	Runs an external process asynchronously. On Windows, GUIs are supressed.

	``exec`` is the default command used by build systems, thus it provides
	similar functionality. However, a few options in build systems are taken
	care of by Sublime Text internally so they list below only contains
	parameters accepted by this command.

	- **cmd** [[String]]
	- **file_regex** [String]
	- **line_regex** [String]
	- **working_dir** [String]
	- **encoding** [String]
	- **env** [{String: String}]
	- **path** [String]
	- **shell** [Bool]
	- **kill** [Bool]: If ``True`` will simply terminate the current build
	  process. This is invoked via *Build: Cancel* command from the
	  :ref:`Command Palette <ext-command-palette-overview>`.
	- **quiet** [Bool]: If ``True`` prints less information about running the
	  command.

	.. seealso::

		:ref:`Arbitrary Options for build systems <build-arbitrary-options>`
			Detailed documentation on all other available options.


**transpose**
	Makes stuff dance (swap places).

**sort_lines**
	Sorts lines.

	- **case_sensitive** [Bool]: Whether the sort should be case sensitive.

**sort_selection**
	Sorts lines in selection.

	- **case_sensitive** [Bool]: Whether the sort should be case sensitive.

**permute_lines**
	XXX

	- **operation** [Enum]: *reverse*, *unique*, *shuffle* ...?

**permute_selection**
	XXX

	- **operation** [Enum]: *reverse*, *unique*, *shuffle* ...?

**set_layout**
	Changes the group layout of the current window. This command uses the same
	pattern as :py:meth:`Window.set_layout`, see there for a list and
	explanation of parameters.

**focus_group**
	Gives focus to the top-most file in the specified group.

	- **group** [Int]: The group index to focus. This is determined by the order
	  of ``cells`` items from the current layout (see :py:meth:`Window.set_layout`).

**move_to_group**
	Moves the current file to the specified group.

	- **group** [Int]: The group index to focus. See **focus_group** command.

**select_by_index**
	Focusses a certain tab in the current group.

	- **index** [Int]: The tab index to focus.

**next_bookmark**
	Select the next bookmarked region.

**prev_bookmark**
	Select the previous bookmarked region.

**toggle_bookmark**
	Sets or unsets a bookmark for the active region(s). (Bookmarks can be
	accessed via the regions API using ``"bookmarks"`` as the key.)

**select_bookmark**
	Selects a bookmarked region in the current file.

	- **index** [Int]

**clear_bookmarks**
	Removes all bookmarks.

**select_all_bookmarks**
	Selects all bookmarked regions.

**wrap_lines**
	Wraps lines. By default, it wraps lines at the first ruler's column.

	- **width** [Int]: Specifies the column at which lines should be wrapped.

**upper_case**
	Makes the selection upper case.

**lower_case**
	Makes the selection lower case.

**title_case**
	Capitalizes the selection's first character and turns the rest into lower
	case.

**swap_case**
	Swaps the case of each character in the selection.

**set_mark**
	XXX

**select_to_mark**
	XXX

**delete_to_mark**
	XXX

**swap_with_mark**
	XXX

**clear_bookmarks**
	XXX

	- **name** [String]: e.g. ``"mark"``.

**yank**
	XXX

**show_at_center**
	Scrolls the view to show the selected line in the middle of the view and
	adjusts the horizontal scrolling if necessary. Only focusses on the first
	selection if multiple selections have been made

**increase_font_size**
	Increases the font size.

**decrease_font_size**
	Decreases the font size.

**reset_font_size**
	Resets the font size to the default

	*Note*: This essentially removes the entry from your User settings, there
	might be other places where this has been "changed".

**fold**
	Folds the current selection and displays ``…`` instead. Unfold arrows are
	added to the lines where a region has been folded.

**unfold**
	Unfolds all folded regions in the selection.

**fold_by_level**
	Scans the whole file and folds everything with an indentation level of
	``level`` or higher. This does not unfold already folded regions if you
	first fold by level 2 and then by 3, for example.

	- **level** [Int]: The level of indentation that should be folded.

**fold_tag_attributes**
	Folds all tag attributes in XML files, only leaving the tag's name and the
	closing bracket visible.

**unfold_all**
	Unfolds all folded regions.

**context_menu**
	Shows the context menu.

**open_recent_file**
	Opens a recently closed file.

	- **index** [Int]

**open_recent_folder**
	Opens a recently closed folder.

	- **index** [Int]

**open_recent_project**
	Opens a recently closed project.

	- **index** [Int]

**clear_recent_files**
	Deletes records of recently accessed files and folders.

**clear_recent_projects**
	Deletes records of recently accessed projects.

**reopen**
	Reopens the current file.

	- **encoding** [String]: The file encoding the file should be reopened with.

**clone_file**
	Clones the current view into the same tab group, both sharing the same
	buffer. That means you can drag one tab to another group and every update to
	one view will be visible in the other one too.

**revert**
	Undoes all unsaved changes to the file.

**expand_tabs**
	XXX

	- **set_translate_tabs** [Bool]

**unexpand_tabs**
	XXX

	- **set_translate_tabs** [Bool]

**new_plugin**
	Creates a new buffer and inserts a plugin template (a text command).

**new_snippet**
	Creates a new buffer and inserts a snippet template.

**open_url**
	Opens the specified url with the default browser.

	- **url** [String]

**show_about_window**
	I think you know what this does.

.. Some regex-related and search-related commands missing. They don't seem to
.. be too useful at all.


Discovering Commands
====================

There are several ways to discover a command's name in order to use it as a key
binding, in a macro, as a menu entry or in a plugin.

- Browsing the default key bindings at **Preferences | Key Bindings - Default**.
  If you know the key binding whose command you want to inspect you can just
  search for it using the :doc:`search panel
  </search_and_replace/search_and_replace>`. This, of course, also works in the
  opposite direction.

- ::

	``sublime.log_commands(True)``

  Running the above in the console will tell Sublime Text to print the command's
  name in the console whenever a command is run. You can practically just enter
  this, do whatever is needed to run the command you want to inspect and then
  look at the console. It will also print the passed arguments so you can
  basically get all the information you need from it. When you are done, just
  run the function again with ``False`` as parameter.

- Inspecting *.sublime-menu* files. If your command is run by a menu item,
  browse the default menu file at :file:`Packages/Default/Main.sublime-menu`.
  You will find them quick enough once you take a look at it, or see the :doc:`menu documentation </customization/menus>`.

.. XXX link menu docs when they are done

- Similar to menus you can do exactly the same with *.sublime-command* files.
  See :doc:`/extensibility/completions` for some documentation on completion
  files.
