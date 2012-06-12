Commands
********

Overview
========

This list of commands is a work in progress.


About Paths in Command Arguments
================================

Some commands taking paths as parameters support snippet-like syntax, while
others don't. A command of the first kind would take a parameter like
*${packages}/SomeDir/SomeFile.Ext* whereas a command of the second kind would
take a parameter like *Packages/SomeDir/SomeFile.Ext*.

Generally, newer commands support the snippet-like syntax.

Often, relative paths in arguments to commands are assumed to start at the
``Data`` directory.


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

	- **by** [Enum]: Values: *characters*, *words*, *word_ends*, *subwords*, *subword_ends*, *lines*, *pages*.
	- **forward** [Bool]: Whether to advance or reverse in the buffer.

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

 	- **extensions** [[String]]: Extensions for which switching will be enabled.

 **close**
 	Closes the active view.

 **close_file**
 	Closes the active view and, under certain circumsances, the whole application.

 **toggle_sidebar**
 	Shows or hides the sidebar.

 **toggle_full_screen**
 	Toggles full screen mode on/off.

 **toggle_distraction_free**
 	Toggles distraction free mode on/off.

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
 	Removes the selected text and sends it to the system clipboard.

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
 	Scroll lines in the view.

 	- **amount** [Float]: Positive values scroll lines down and negative values scroll lines up.

 **prev_view**
 	Switch to the previous view.

 **next_view**
 	Switch to the next view.

 **next_view_in_stack**
 	Switch to the view that was active most recently.

 **previous_view_in_stack**
 	Switch to the view that was active before the view that was active most
 	recently. I don't think this is very clear.

 **select_all**
 	Select the whole view contents.

 **split_selection_into_lines**
 	Unsurprisingly, it splits the selection into lines.

 **single_selection**
 	Collapses multiple selections into a single selection.

 **clear_fields**
 	Exhausts snippet fields to prevent further cycling through them.

 **hide_panel**
 	Hides the active panel.

 	- **cancel** [Bool]: XXX

 **hide_overlay**
 	Hides the active overlay.

 **hide_auto_complete**
 	Hides the auto complete list.

 **insert_best_completion**
 	Inserts the best completion that can be inferred from the current context.

 	- **default** [String]: String to insert failing a best completion.

 **replace_completion_with_next_completion**
 	Weird stuff.

 **reindent**
 	Documenting some commands is such a waste of time.

 **indent**
 	Awesome.

 **next_field**
 	Advances the caret to the text snippet field in the current cycle.

 **commit_completion**
 	Inserts the currently selected item in the auto complete list.

 **unindent**
 	Does what it says.

 **prev_field**
 	Moves the caret to the previous snippet field in the current cycle.

 **toggle_overwrite**
 	Toggles overwriting on/off.

 **expand_selection**
 	Extends the selection until predifined limits.

 	- **to** [Enum]: line XXX must be more XXX

 **find_under_expand**
 	Adds a new selection region based on the current selection or the current
 	word.

 **close_tag**
 	Surrounds the current innert text with the appropiate tag.

 **toggle_record_macro**
 	Starts or stops the macro recorder.

 **run_macro**
 	Runs the macro stored in the macro buffer.

 **show_overlay**
 	Shows an overlay.

 	- **overlay** [Enum]: Values: goto, command_palette
 	- **show_files** [Bool]: Optimize overlay display for showing files.

 **show_panel**
 	Shows a panel.

 	- **panel** [Enum]: Values: incremental_find, find, replace, find_in_files, console
 	- **reverse** [Bool]: Whether to search backwards in the buffer.
 	- **toggle** [Bool]: xXX

 **find_next**
 	Find the text occurrence of the current search term.

 **find_prev**
 	Find the previous occurrence of the current search term.

 **find_under**
 	Find the next occurrence of the current selection or the current word.

 **find_under_prev**
 	Find the previous occurrence of the current selection or the current word.

 **find_all_under**
 	Find all occurrences of the current selection or the current word.

 **slurp_find_string**
 	XXX

 **slurp_replace_string**
 	XXX

 **next_result**
 	Find next captured result.

 **prev_result**
 	Find next captured result.

 **toggle_setting**
 	Toggles the value of a boolean setting.

 	- **setting** [String]: The name of the setting to be toggled.

 **next_misspelling**
 	Find the next misspelling

 **prev_misspelling**
 	Find the previous misspelling.

 **swap_line_down**
 	Swaps the current line with the line below it.

 **swap_line_up**
 	Swaps the current line with the line above it.

 **toggle_comment**
 	Comments or uncomments the active regions.

 	- **block** [Bool]: Whether to use a block comment.

 **join_lines**
 	Join the current line with the next one.

 **duplicate_line**
 	Duplicates the current line.

 **auto_complete**
 	Opens the auto comeplete list.

 **replace_completion_with_auto_complete**
 	Sure.

 **show_scope_name**
 	Shows the name for the caret's scope.

 **exec**
 	Runs an external process asynchronously.

 	XXX Document all options.

 **transpose**
 	Make stuff dance.

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
 	XXX

 **prev_bookmark**
 	XXX

 **toggle_bookmark**
 	XXX

 **clear_bookmarks**
 	XXXX

 **select_all_bookmarks**
 	XXX

 **wrap_lines**
 	XXX

 **upper_case**
 	XXX

 **lower_case**
 	XXX

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
 	XXX

 **decrease_font_size**
 	XXX

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









