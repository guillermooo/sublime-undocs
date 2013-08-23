Commands
********

Overview
========

.. named actions, used everywhere, take json arguments
This list of commands is a work in progress.


About Paths in Command Arguments
================================

Some commands take paths as parameters. Among these, some support snippet-like
syntax, while others don't. A command of the first kind would take a parameter
like *${packages}/SomeDir/SomeFile.Ext* whereas a command of the second kind
would take a parameter like *Packages/SomeDir/SomeFile.Ext*.

Generally, newer commands support the snippet-like syntax.

Often, relative paths in arguments to commands are assumed to start at the
``Data`` directory.

Variables in Paths as Arguments
-------------------------------

The same variables available to build systems are expanded in arguments to
commands. See :ref:`build-system-variables` for more information.


Commands
========

**build**
	Runs a build system.

	- **variant** [String]: Optional. The name of the variant to be run.

**run_macro_file**
	Runs a *.sublime-macro* file.

	- **file** [String]: Path to the macro file.

**insert_snippet**
	Inserts a snippet from a string or *.sublime-snippet* file.

	- **contents** [String]: Snippet as a string to be inserted.
	- **name** [String]: Path to the *.sublime-snippet* file to be inserted.

**insert**
	Inserts a string.

	- **characters** [String]: String to be inserted.

**move**
	Advances the caret by predefined units.

	- **by** [Enum]: Values: *characters*, *words*, *word_ends*, *subwords*, *subword_ends*, *lines*, *pages*, *stops*.
	- **forward** [Bool]: Whether to advance or reverse in the buffer.
	- **word_begin** [Bool]
	- **empty_line** [Bool]
	- **punct_begin** [Bool]
	- **separators** [Bool]

**move_to**
	Advances the caret to predefined locations.

	- **to** [Enum]: Values: *bol*, *eol*, *bof*, *eof*, *brackets*.
	- **extend** [Bool]: Whether to extend the selection. Defaults to ``false``.

**new_window**
	Opens a new window.

**close_window**
	Closes the active window.

**switch_file**
	Switches between two files with the same name and different extensions.

	- **extensions** [[String]]: Extensions (without leading dot) for which switching will be enabled.

**close**
	Closes the active view.

**close_file**
	Closes the active view and, under certain circumsances, the whole application.
	XXX Sounds kinda wrong.

**save**
        Saves the active file.

**prompt_save_as**
        Prompts for a new file name and saves the active file.

**toggle_sidebar**
	Shows or hides the sidebar.

**toggle_full_screen**
	Toggles full screen mode on or off.

**toggle_distraction_free**
	Toggles distraction free mode on or off.

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

**paste_and_indent**
	Inserts the clipboard contents after the caret and indents contextually.

**select_lines**
	Adds a line to the current selection.

	- **forward** [Bool]: Whether to add the next or previous line. Defaults to
	  ``true``.

**scroll_lines**
	Scrolls lines in the view.

	- **amount** [Float]: Positive values scroll lines down and negative values scroll lines up.

**prev_view**
	Switches to the previous view.

**next_view**
	Switches to the next view.

**next_view_in_stack**
	Switches to the most recently active view.

**previous_view_in_stack**
	Switches to the view that was active before the most recently active view.
	I don't think this is very clear or even true.

**select_all**
	Select the view's content.

**split_selection_into_lines**
	Unsurprisingly, it splits the selection into lines.

**single_selection**
	Collapses multiple selections into a single selection.

**clear_fields**
	Breaks out of the active snippet field cycle.

**hide_panel**
	Hides the active panel.

	- **cancel** [Bool]: Notifies the panel to restore the selection to what it
	was when the panel was opened. (Only incremental find panel.)

**hide_overlay**
	Hides the active overlay.  Show the overlay using the show_overlay command.

**hide_auto_complete**
	Hides the auto complete list.

**insert_best_completion**
	Inserts the best completion that can be inferred from the current context.
	XXX Probably useless. XXX

	- **default** [String]: String to insert failing a best completion.

**replace_completion_with_next_completion**
	XXX Useless for users. XXX

**reindent**
	XXX ??? XXX

**indent**
	Increments indentation.

**next_field**
	Advances the caret to the text snippet field in the current snippet field
	cycle.

**prev_field**
	Moves the caret to the previous snippet field in the current snippet field
	cycle.

**commit_completion**
	Inserts into the buffer the item that's currently selected in the auto
	complete list. XXX Probably not useful for users. XXX

**unindent**
	Unindents.

**toggle_overwrite**
	Toggles overwriting on or off.

**expand_selection**
	Extends the selection up to predifined limits.

	- **to** [Enum]: Values: bol, hardbol, eol, hardeol, bof, eof, brackets, line.

**find_under_expand**
	Adds a new selection based on the current selection or expands the
	selection to the current word.

**close_tag**
	Surrounds the current inner text with the appropiate tags.

**toggle_record_macro**
	Starts or stops the macro recorder.

**run_macro**
	Runs the macro stored in the macro buffer.

**show_overlay**
	Shows the requested overlay. Use the **hide_overlay** command to hide it.

	- **overlay** [Enum]:
                The type of overlay to show. Possible values:

		- *goto*: Show the `Goto Anything <http://docs.sublimetext.info/en/latest/file_management/file_management.html#goto-anything>`_ overlay.
		- *command_palette*: Show the `command palette <http://docs.sublimetext.info/en/latest/extensibility/command_palette.html>`_.

	- **show_files** [Bool]: If using the goto overlay, start by displaying files rather than an empty widget.
	- **text** [String]: The initial contents to put in the overlay.

**show_panel**
	Shows a panel.

	- **panel** [Enum]: Values: incremental_find, find, replace, find_in_files, console
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
	Toggles the value of a boolean setting.

	- **setting** [String]: The name of the setting to be toggled.

**next_misspelling**
	Advance to the next misspelling

**prev_misspelling**
	Move to the previous misspelling.

**swap_line_down**
	Swaps the current line with the line below.

**swap_line_up**
	Swaps the current line with the line above.

**toggle_comment**
	Comments or uncomments the active lines.

	- **block** [Bool]: Whether to use a block comment.

**join_lines**
	Joins the current line with the next one.

**duplicate_line**
	Duplicates the current line.

**auto_complete**
	Opens the auto comeplete list.

**replace_completion_with_auto_complete**
	XXX Useless for users. XXX

**show_scope_name**
	Shows the name for the caret's scope in the status bar.

**exec**
	Runs an external process asynchronously.

	XXX Document all options.

**transpose**
	Makes stuff dance.

**sort_lines**
	Sorts lines.

	- **case_sensitive** [Bool]: Whether the sort should be case sensitive.

**set_layout**
	XXX

**focus_group**
	XXX

**move_to_group**
	XXX

**select_by_index**
	XXX

**next_bookmark**
	Select the next bookmarked region.

**prev_bookmark**
	Select the previous bookmarked region.

**toggle_bookmark**
	Sets or unsets a bookmark for the active region(s). (Bookmarks can be
	accessed via the regions API using ``"bookmarks"`` as the key.)

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
	Capitalizes the selection's first character and turns the rest into lower case.

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

**yank**
	XXX

**show_at_center**
	XXX

**increase_font_size**
	Increases the font size.

**decrease_font_size**
	Decreases the font size.

**fold**
	XXX

**unfold**
	XXX

**fold_by_level**
	XXX

**context_menu**
	Shows the context menu.

.. Some regex-related and search-related commands missing. they don's seem to
.. be too useful.
