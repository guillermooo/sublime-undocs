Plugins
=======

.. seealso::

   :doc:`API Reference <../reference/api>`
        More information on the Python API.

   :doc:`Plugins Reference <../reference/plugins>`
        More information about plugins.

This section is intended for users with programming skills.


Sublime Text can be extended through Python plugins. Plugins build features by
reusing existing commands or creating new ones. Plugins are a logical entity,
rather than a physical one.


Prerequisites
*************

In order to write plugins, you must be able to program in Python_.
At the time of this writing, Sublime Text used Python 3.

.. _Python: http://www.python.org


Where to Store Plugins
**********************

Sublime Text will look for plugins only in these places:

* ``Installed Packages`` (only *.sublime-package* files)
* ``Packages``
* ``Packages/<pkg_name>/``

As a consequence, any plugin nested deeper in ``Packages`` won't be loaded.

Keeping plugins directly under ``Packages`` is discouraged. Sublime Text sorts
packages in a predefined way before loading them, so if you save plugin files
directly under ``Packages`` you might get confusing results.


Your First Plugin
*****************

Let's write a "Hello, World!" plugin for Sublime Text:

#. Select **Tools | New Plugin...** in the menu.
#. Save to ``Packages/User/hello_world.py``.

You've just written your first plugin! Let's put it to use:

#. Create a new buffer (``Ctrl+n``).
#. Open the Python console (``Ctrl+```).
#. Type: ``view.run_command("example")`` and press enter.

You should see the text "Hello, World!" in the newly created buffer.


Analyzing Your First Plugin
***************************

The plugin created in the previous section should look roughly like this::

    import sublime, sublime_plugin

    class ExampleCommand(sublime_plugin.TextCommand):
        def run(self, edit):
            self.view.insert(edit, 0, "Hello, World!")


Both the ``sublime`` and ``sublime_plugin`` modules are provided by
Sublime Text; they are not part of the Python standard library.

As we mentioned earlier, plugins reuse or create *commands*. Commands are an
essential building block in Sublime Text. They are simply Python classes
that can be called in similar ways from different Sublime Text facilities,
like the plugin API, menu files, macros, etc.

Sublime Text Commands derive from the ``*Command`` classes defined in
``sublime_plugin`` (more on this later).

The rest of the code in our example is concerned with particulars of
``TextCommand`` or with the API. We'll discuss those topics in later sections.

Before moving on, though, we'll look at how we invoked the new command: first
we opened the Python console and then we issued a call to
``view.run_command()``. This is a rather inconvenient way of calling commands,
but it's often useful when you're in the development phase of a plugin. For
now, keep in mind that your commands can be accessed through key bindings
and by other means, just like other commands.

Conventions for Command Names
-----------------------------

You may have noticed that our command is named ``ExampleCommand``, but we
passed the string ``example`` to the API call instead. This is necessary
because Sublime Text standardizes command names by stripping the ``Command``
suffix and separating ``PhrasesLikeThis`` with underscores, like so:
``phrases_like_this``.

New commands should follow the same naming pattern.


Types of Commands
*****************

You can create the following types of commands:

* Window commands (``sublime_plugin.WindowCommand``)
* Text commands (``sublime_plugin.TextCommand``)

When writing plugins, consider your goal and choose the appropriate type of
commands.


Shared Traits of Commands
-------------------------

All commands need to implement a ``.run()`` method in order to work. Additionally,
they can receive an arbitrarily long number of keyword parameters.

**Note:** Parameters to commands must be valid JSON values due to how ST
serializes them internally.

Window Commands
---------------

Window commands operate at the window level. This doesn't mean that you can't
manipulate views from window commands, but rather that you don't need views in
order for window commands to be available. For instance, the built-in command
``new_file`` is defined as a ``WindowCommand`` so it works even when no view
is open. Requiring a view to exist in that case wouldn't make sense.

Window command instances have a ``.window`` attribute to point to the window
instance that created them.

The ``.run()`` method of a window command doesn't require any positional
parameter.

Window commands are able to route text commands to their window's active view.

Text Commands
-------------

Text commands operate at the view level, so they require a view to exist
in order to be available.

Text command instances have a ``.view`` attribute pointing to the view instance
that created them.

The ``.run()`` method of text commands requires an ``edit`` instance as
its first positional argument.

Text Commands and the ``edit`` Object
-------------------------------------

The edit object groups modifications to the view so that undo and macros work
sensibly.

**Note:** Contrary to older versions, Sublime Text 3 doesn't allow programmatic
control over edit objects. The API is in charge of managing their life cycle.
Plugin creators must ensure that all modifying operations occur inside the
``.run`` method of new text commands. To call existing commands, you can use
``view.run_command(<cmd_name>, <args>)`` or similar API calls.

Responding to Events
--------------------

Any command deriving from ``EventListener`` will be able to respond to events.


Another Plugin Example: Feeding the Completions List
----------------------------------------------------

Let's create a plugin that fetches data from Google's Autocomplete service and
then feeds it to the Sublime Text completions list. Please note that, as ideas
for plugins go, this a very bad one.

::

	import sublime, sublime_plugin

	from xml.etree import ElementTree as ET
	from urllib import urlopen

	GOOGLE_AC = r"http://google.com/complete/search?output=toolbar&q=%s"

	class GoogleAutocomplete(sublime_plugin.EventListener):
	    def on_query_completions(self, view, prefix, locations):
	        elements = ET.parse(
	                        urlopen(GOOGLE_AC % prefix)
	                    ).getroot().findall("./CompleteSuggestion/suggestion")

	        sugs = [(x.attrib["data"],) * 2 for x in elements]

	        return sugs

.. note::
	Make sure you don't keep this plugin around after trying it or it will
	interfere with Sublime Text's autocompletion.


Learning the API
****************

In order to create plugins, you need to get acquainted with the Sublime Text
API and the available commands. Documentation on both is scarce at the time of
this writing, but you can read existing code and learn from it.

In particular, the ``$PATH_TO_SUBLIME/Packages/Default.sublime-package``
contains many examples of undocumented commands and API calls. Note that you
will first have to extract its content to a folder if you want to take a look at
the code within. As an exercise, you can try creating a build system to do that
on demand, and a project file to be able to peek at the sample code easily.
