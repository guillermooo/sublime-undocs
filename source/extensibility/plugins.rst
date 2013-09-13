=======
Plugins
=======

.. seealso::

   :doc:`API Reference <../reference/api>`
        More information on the Python API.

   :doc:`Plugins Reference <../reference/plugins>`
        More information about plugins.


Sublime Text 2 is programmable with Python scripts. Plugins reuse existing
commands or create new ones to build a feature. Plugins are a logical entity,
rather than a physical one.


Prerequisites
*************

In order to write plugins, you must be able to program in Python_.

.. _Python: http://www.python.org


Where to Store Plugins
**********************

Sublime Text 2 will only look for plugins in these places:

* ``Packages``
* ``Packages/<pkg_name>/``

Consequently, any plugin nested deeper in ``Packages`` won't be loaded.

Keeping plugins just under ``Packages`` is discouraged, because Sublime Text
sorts packages in a predefined way before loading them. So, you might get
confusing results if your plugins live outside a package.


Your First Plugin
*****************

Let's write a "Hello, World!" plugin for Sublime Text 2:

#. Select **Tools | New Plugin…** in the menu.
#. Save to ``Packages/User/hello_world.py``.

You've just written your first plugin. Let's put it to use:

#. Create a new buffer (``Ctrl+n``).
#. Open the python console (``Ctrl+```).
#. Type: ``view.run_command("example")`` and press enter.

You should see the text "Hello, World!" in your new buffer.


Analyzing Your First Plugin
***************************

The plugin created in the previous section should look roughly like this::

    import sublime, sublime_plugin

    class ExampleCommand(sublime_plugin.TextCommand):
        def run(self, edit):
            self.view.insert(edit, 0, "Hello, World!")


Both the ``sublime`` and ``sublime_plugin`` modules are provided by
Sublime Text 2.

All new commands derive from the ``*Command`` classes defined in ``sublime_plugin``
(more on this later).

The rest of the code is concerned with the particulars of ``TextCommand`` or with
the API. We'll discuss those topics in later sections.

Before moving on, though, we'll look at how we invoked the new command. First we
opened the python console, and then we issued a call to ``view.run_command()``. This
is rather an inconvenient way of using plugins, but it's often useful when
you're in the development phase of a plugin. For now, keep in mind that your commands
can be accessed both through key bindings and by other means, just like other commands.

Conventions for Command Names
-----------------------------

You might have noticed that our command is defined with the name ``ExampleCommand``,
but we pass the string ``example`` to the API call instead. This is necessary because
Sublime Text 2 normalizes command names, stripping the ``Command`` suffix and
separating ``CamelCasedPhrases`` with underscores, like this: ``snake_cased_phrases``.

New commands should follow the CamelCase pattern for class names.


Types of Commands
*****************

You can create the following types of commands:

* Application commands (``ApplicationCommand``)
* Window commands (``WindowCommand``)
* Text commands (``TextCommand``)

When writing plugins, consider your goal and choose the appropriate type of
commands for your plugin.


Shared Traits of Commands
-------------------------

All commands need to implement a ``.run()`` method in order to work. Additionally,
they can receive an arbitrarily long number of keyword parameters.


Application Commands
--------------------

Application commands derive from ``sublime_plugin.ApplicationCommand`` and
can be executed with ``sublime.run_command()``.

Window Commands
---------------

Window commands operate at the window level. This doesn't mean you can't
manipulate views from window commands, but rather that you don't need views
in order for window commands to be available. For instance, the built-in
command ``new_file`` is defined as a ``WindowCommand`` so it works, even when no
view is open. Requiring a view to exist in that case wouldn't make sense.

Window command instances have a ``.window`` attribute to point to the window
instance that created them.

The ``.run()`` method of a window command does not take any required
arguments.

Text Commands
-------------

Text commands operate at the buffer level, so they require a buffer to exist
in order to be available.

View command instances have a ``.view`` attribute pointing to the view instance
that created them.

The ``.run()`` method of a text command needs to accept an ``edit`` instance as
the first positional argument.

Text Commands and the ``edit`` Object
-------------------------------------

The edit object groups any modifications to the view so as to enable undo and
macros to work sensibly.

You are responsible for creating and closing edit objects. To do
so, you can call ``view.begin_edit()`` and ``edit.end_edit()``.
For convenience, the currently open ``edit`` object gets passed to text
commands' ``run`` method automatically.
Additionally, many ``View`` methods require an edit object.


Responding to Events
--------------------

Any command deriving from ``EventListener`` will be able to respond to events.


.. _plugins-completions-example:

Another Plugin Example: Feeding the Completions List
----------------------------------------------------

Let's create a plugin that fetches data from Google's Autocomplete service and then
feeds it to the Sublime Text 2 completions list. Please note that, as ideas for
plugins go, this a very bad one.

.. sourcecode:: py

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
    interfere with the autocompletion system.

.. seealso::

    .. py:currentmodule:: sublime_plugin

    :py:meth:`EventListener.on_query_completions`
        Documentation on the API event used in this example.


Learning the API
****************

In order to create plugins, you need to get acquainted with the Sublime Text
API and the available commands. Documentation on both is scarce at the time of
this writing, but you can read existing code and learn from it too. In
particular, the :file:`Packages/Default` folder contains many examples of
undocumented commands and API calls.

