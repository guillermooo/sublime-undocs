Python API
==========

.. warning::
    This topic is a draft and may contain wrong information.
    This reference is unofficial and unsupported by the Sublime Text dev team.
    We hope it will become useful at some point, though.
    Last updated: 20110131

Exploring the API
*****************

A quick way to see the API in action:

#. Add ``Packages\Default`` (**Preferences | Browse Packages...**) to your project.
#. ``CTRL + SHIFT + F``
#. Enter ``*.py`` in the **In Files:** field
#. Check ``Use Buffer`` option
#. Search API name
#. ``F4``
#. Study relevant source code


Module ``sublime``
******************

================================    =====================    ================================================================================
**Method**                          **Return value**         **Description**
================================    =====================    ================================================================================
``active_window()``                 ``Window``               Returns the most recenlty used window.
``error_message(string)``           ``none``                 Displays an error dialog.
``get_clipboard()``                 ``String``               Returns the contents of the clipboard.
``installed_packages_path()``       ``none``                 Returns the path to the ``Installed Packages`` folder.
``load_settings(fname)``            ``Settings``             Loads the settings in the ``.sublime-settings`` file named ``fname``.
``packages_path()``                 ``none``                 Returns the path to the ``Packages`` folder.
``save_settings(fname)``            ``none``                 Save the settings in the ``.sublime-settings`` file named ``fname``.
``set_clipboard(string)``           ``none``                 Sets the contents of the clipboard.
``set_timeout(callback, delay)``    ``none``                 Calls the given ``callback`` after the given ``delay`` (in milliseconds).
                                                             Callbacks with an equal delay will be run in the order they were
                                                             added. It is safe to call ``setTimeout`` from multiple threads.
``status_message(string)``          ``none``                 Sets the status bar text.
``windows()``                       ``[Window]``             Returns a list of the open Sublime Text windows.
================================    =====================    ================================================================================

Class ``sublime.View``
**********************

====================================================    ================    ============================================================================================================
**Method**                                              **Return value**    **Description**
====================================================    ================    ============================================================================================================
add_regions(key, [regions], scope, <flags>)             none                Add a set of regions to the view. If a set of regions already exists with the given key, they'll be overwritten. The scope is used to source a color to draw the regions in, it should be the name of a scope, such as "comment" or "string". If the scope is empty, the regions won't be drawn.

                                                                            The optional flags parameter is a bitwise combination of:
                                                                            
                                                                            sublime.DRAW_EMPTY. Draw empty regions with a vertical bar. By default, they aren't drawn at all.
                                                                            sublime.HIDE_ON_MINIMAP. Don't show the regions on the minimap.
                                                                            sublime.DRAW_EMPTY_AS_OVERWRITE. Draw empty regions with a horizontal bar instead of a vertical one.
                                                                            sublime.DRAW_OUTLINED. Draw regions as an outline, rather than filled in.
                                                                            sublime.PERSISTENT. Save the regions in the session.
begin_edit                                                                  XXXX
buffer_id()                                             int                 Returns a number that uniquely identifies the buffer underlying this view.
end_edit                                                                    XXXX
erase(region)                                           none                Erases the contents of the region from the buffer.
erase_regions(key)                                      none                Removed the named regions
erase_status(key)                                       none                Clears the named status.
extract_completions(prefix, <point>)                    [String]            Returns the completions for the given prefix, based on the contents of the buffer. Completions will be ordered by frequency, and distance from the given point, if supplied.
extract_scope(point)                                    Region              Returns the extents of the syntax name assigned to the character at the given point.
file_name()                                             String              The full name file the file associated with the buffer, or None if it doesn't exist on disk.
find(pattern, fromPosition, <flags>)                    Region              Returns the first Region matching the regex pattern, starting from the given point, or None if it can't be found. The optional flags parameter may be sublime.LITERAL, sublime.IGNORECASE, or the two ORed together.
find_all(pattern, <flags>, <format>, <extractions>)     [Region]            Returns all (non-overlapping) regions matching the regex pattern. The optional flags parameter may be sublime.LITERAL, sublime.IGNORECASE, or the two ORed together. If a format string is given, then all matches will be formatted with the formatted string and placed into the extractions list.
full_line(point)                                        Region              As line(), but the region includes the trailing newline character, if any.
full_line(region)                                       Region              As line(), but the region includes the trailing newline character, if any.
get_regions(key)                                        [regions]           Return the regions associated with the given key, if any
get_status(key)                                         String              Returns the previously assigned value associated with the key, if any.
get_symbols XXX                                                             XXX
has_non_empty_selection_region                                              XXX
id()                                                    int                 Returns a number that uniquely identifies this view.
insert(point, string)                                   int                 Inserts the given string in the buffer at the specified point. Returns the number of characters inserted: this may be different if tabs are being translated into spaces in the current buffer.
is_dirty()                                              bool                Returns true if there are any unsaved modifications to the buffer.
is_loading()                                            bool                Returns true if the buffer is still loading from disk, and not ready for use.
is_read_only()                                          bool                Returns true if the buffer may not be modified.
is_scratch                                                                  XXX
is_scratch()                                            bool                Returns true if the buffer is a scratch buffer. Scratch buffers never report as being dirty.
line(point)                                             Region              Returns the line that contains the point.
line(region)                                            Region              Returns a modified copy of region such that it starts at the beginning of a line, and ends at the end of a line. Note that it may span several lines.
lines(region)                                           [Region]            Returns a list of lines (in sorted order) intersecting the region.
match_selector(point, selector)                         bool                Returns True iff the selector matches the syntax name assigned to the character at the given point.
meta_info XXX                                                               XXX
name()                                                  String              The name assigned to the buffer, if any
replace(region, string)                                 none                Replaces the contents of the region with the given string.
rowcol(point)                                           (int, int)          Calculates the 0 based line and column numbers of the point.
run_command(string, <args>)                             none                Runs the named Text_command with the (optional) given arguments.
sel()                                                   Region_set          Returns a reference to the selection.
set_name(name)                                          none                Assigns a name to the buffer
set_read_only(value)                                    none                Sets the read only property on the buffer.
set_scratch(value)                                      none                Sets the scratch property on the buffer.
set_status(key, value)                                  none                Adds the status key to the view. The value will be displayed in the status bar, in a comma separated list of all status values, ordered by key. Setting the value to the empty string will clear the status.
settings()                                              Options             Returns a reference to the file type options for the view.
show(point, <showSurrounds>)                            none                Scroll the view to show the given point.
show(region, <showSurrounds>)                           none                Scroll the view to show the given region.
show(regionSet, <showSurrounds>)                        none                Scroll the view to show the given regionSet.
size()                                                  int                 Returns the number of character in the file.
split_by_newlines(region)                               [Region]            Splits the region up such that each region returned exists on exactly one line.
substr(point)                                           String              Returns the character to the right of the point.
substr(region)                                          String              Returns the contents of the region as a string.
syntax_name(point)                                      String              Returns the syntax name assigned to the character at the given point.
text_point(row, col)                                    int                 Calculates the character offset of the given, 0 based, row and column. Note that 'col' is interpreted as the number of characters to advance past the beginning of the row.
visible_region()                                        Region              Returns the currently visible area of the view.
window()                                                Window              Returns a reference to the window containing the view.
word(point)                                             Region              Returns the word that contains the point.
word(region)                                            Region              Returns a modified copy of region such that it starts at the beginning of a word, and ends at the end of a word. Note that it may span several words.
====================================================    ================    ============================================================================================================


Class ``sublime.Settings``
**************************

======================    ================    ======================================================================================
**Method**                **Return value**    **Description**
======================    ================    ======================================================================================
``erase(name)``           ``none``            Removes the named setting. Does not remove it from any parent ``Settings``.
``get(name)``             ``value``           Returns the named setting as the appropriate type.
``get(name, default)``    ``value``           Returns the named setting as the appropriate type, or ``default`` if it's not defined.
``has(name)``             ``bool``            Returns true if the named setting exists in this set of Settings or one of its parents.
``set(name, value)``      ``none``            Sets the named setting. Only primitive types are accepted.
======================    ================    ======================================================================================

Class ``sublime.Window``
************************

==========================================================================   ================    ======================================================================================
**Method**                                                                   **Return value**    **Description**
==========================================================================   ================    ======================================================================================
``active_view()``                                                            View                Returns the view being edited currently.
``get_output_panel()``                                                       XXXX                XXXX
``id()``                                                                     int                 Returns a unique identifier for the window.
``new_file()``                                                               View                Creates a new file. The returned view will be empty.
``open_file(filename, <row>, <col>)``                                        View                Opens the named file, and returns the corresponding view.
                                                                                                 Row and col are optional and may be omitted. If the file
                                                                                                 is already opened, it will be brought to the front. Note
                                                                                                 that as file loading is asynchronous, operations on the
                                                                                                 returned view won't be possible until its isLoading method
                                                                                                 returns false.
``run_command(string, <args>)``                                              ``none``            Runs the named ``WindowCommand`` with the (optional) given arguments.
``show_input_panel(caption, initial_text, on_done, on_change, on_cancel)``   ``View``            Shows the input panel, to collect a line of input from the user.
                                                                                                 onDone and onChange, if not None, should both be functions that expect
                                                                                                 a single string argument. onCancel should be a function that expects no
                                                                                                 arguments. The view used for the input widget is returned.
==========================================================================   ================    ======================================================================================

Class ``sublime.RegionSet``
***************************

=======================    ====================    ======================================================================================
**Method**                 **Return value**        **Description**
=======================    ====================    ======================================================================================
``add(region)``            ``none``                Adds the given region. It will be merged with any intersecting regions already contained within the set.
``add_all(region_set)``    ``none``                Adds all regions in the given set.
``clear()``                ``none``                Removes all regions.
``contains(region)``       ``none``                Returns true iff the given region is a subset.
``subtract(region)``       ``none``                Subtracts the region from all regions in the set.
=======================    ====================    ======================================================================================

Class ``sublime.Region``
************************

Represents an area of the buffer. Empty regions, where a == b are valid.

XXX

=======================    ======================================================================================
**Constructors**           **Description**
=======================    ======================================================================================
``Region(a, b)``           Creates a Region with initial values a and b.
=======================    ======================================================================================

XXX

=======================    ====================    ======================================================================================
**Properties**             **Type**                **Description**	
=======================    ====================    ======================================================================================
a                          int                     The first end of the region.
b                          int                     The second end of the region. May be less that a, in which case the region is a reversed one.
=======================    ====================    ======================================================================================

XXX

========================   ================    ======================================================================================
**Method**                 **Return value**    **Description**	
========================   ================    ======================================================================================
``begin()``                int                 Returns the minimum of a and b.
``contains(point)``        bool                Returns True iff begin() <= point <= end().
``contains(region)``       bool                Returns True iff the given region is a subset.
``cover(region)``          int                 Returns a Region spanning both this and the given regions.
``empty()``                int                 Returns true iff begin() == end().
``end()``                  int                 Returns the maximum of a and b.
``intersection(region)``   int                 Returns the set intersection of the two regions.
``intersects(region)``     bool                Returns True iff this == region or both include one or more positions in common.
``meta()``                 int                 XXX
``size()``                 int                 Returns the number of characters spanned by the region. Always >= 0.
========================   ================    ======================================================================================


Class ``sublime.Edit``
**********************

XXX

==============    ================      ===============
**Method**        **Return value**      **Description**
==============    ================      ===============
``append()``
``count()``
``extend()``
``index()``
``insert()``
``pop()``
``remove()``
``reverse()``
``sort()``
==============    ================      ===============

Class sublime_plugin ``EventListener``
**************************************

XXX

=============================================================    ================    ================
**Method**                                                       **Return value**    **Description***
=============================================================    ================    ================
``on_new(view)``
``on_clone(view)``
``on_load (view)``
``on_close(view)``
``on_pre_save (view)``
``on_post_save(view)``
``on_modified(view)``
``on_selection_modified(view)``
``on_activated(view)``
``on_project_load(window)``
``on_project_close (window)``
``on_query_context(view, key, operator, operand, match_all)``
=============================================================    ================    ================

.. XXX
