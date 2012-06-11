Commands
********

Overview
========

This list of commands is a work in progress.


Gotchas
=======


Some commands taking paths as parameters support snippet-like syntax, while
others don't. The first kind of command would take a parameter like
``{$packages}/SomeDir/SomeFile.Ext`` whereas the second kind of command would
take a parameter like ``Packages/SomeDir/SomeFile.Ext``.


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

	- **by** [Enum]: Values: characters, words, word_ends, subwords, subword_ends, lines, pages.
	- **forward** [Bool]: Whether to advance or reverse in the buffer.

**move_to**
	Advances the caret to predefined locations.

	- **to** [Enum]: Values: bol, eol, bof, eof, brackets.
	- **extend**: Whether to extend the selection. Default to ``false``.
