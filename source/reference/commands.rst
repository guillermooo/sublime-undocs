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

	*variant* [String]: Optional. The name of the variant to be run.

**run_macro_file**
	Runs a *.sublime-macro* file.

	*file* [String]: Path to the macro file.
