Plugins
=======

Sublime Text 2 is extensible with Python plugins. Plugins add functionality by
reusing existing commands or creating new ones. A plugin can consist of a new
command or a collection of commands working together to build a feature.
Therefore, plugins are rather a logical entity than a physical one.


Prerequisites
*************

In order to write plugins, you must be able to program in Python_.

.. _Python: http://www.python.org


Where to Store Plugins
**********************

Often, plugins come bundled in packages, but you can keep your own collection
of plugins under ``Packages/User`` too.

Sublime Text 2 will look for plugins in these places:

* ``Packages``
* ``Packages/<pkg_name>/``

Therefore, any plugin nested more than one level deep from ``Packages`` won't
be picked up by Sublime Text 2. You shouldn't keep plugins lying around right under
``Packages`` for organizational reasons.

.. don't patronize; explain order matters

Your First Plugin
*****************

Let's write a "Hello, World!" plugin for Sublime Text 2:

#. Select **Tools | New Plugin...** in the menu.
#. Make sure there's a colon after ``class ExampleCommand(sublime_plugin.TextCommand)``. This step is required due to a bug in Sublime Text 2 at the time of this writing.
#. Save to ``Packages/User/hello_world.py``.

You've just written your first plugin. Let's put it to use:

#. Create a new, empty buffer (``CTRL + N``).
#. Open the python console (``CTRL + ```).
#. Type: ``view.run_command("example")``.

You should see the text "Hello, World!" in your new buffer.


Analyzing Your First Plugin
***************************

The plugin created in the previous section should rogughly look like this::

    import sublime, sublime_plugin
    
    class ExampleCommand(sublime_plugin.TextCommand):
        def run(self, edit):
            self.view.insert(edit, 0, "Hello, World!")


``sublime`` and ``sublime_plugin`` are both provided by Sublime Text 2 and will often be
required when you write new plugins.

New commands derive the ``ApplicationCommand``, ``WindowCommand`` and ``TextCommand``
classes defined in ``sublime_plugin``.

The rest of the code is concerned with particulars of the ``TextCommand`` or the
API that will discuss in the next sections.

However, before moving on, we'll look at how we called the new command. First,
we opened the python console, and then we issued a call to ``view.run_command``.
This is a rather inconvenient way of using plugins, but it's often useful when
you're in the development phase. For now, keep in mind that plugin commands
can be accessed through key bindings or other means, just as normal commands are.

You might have noticed that our command is defined with the name ``ExampleCommand``,
but we pass instead the string ``example`` to the API call. This is necessary bevause
Sublime Text 2 normalizes command names by stripping the ``Command`` suffix and
separating ``CamelCasedPhrases`` with underscores, like this: ``camel_cased_phrases``.


Types of Commands
*****************

You can create the following types of commands:

* Application commands (``ApplicationCommand``)
* Window commands (``WindowCommand``)
* Text commands (``TextCommand``)

When you're writing your plugins, you need to consider the purpose of your
plugin and choose the appropriate type of commands for it.


Commonalities between Types of Commands
---------------------------------------

All commands need to implement a ``run`` method in order to work. Additionally,
they can receive and arbitrarily long number of keyword parameters.


Application Commands
--------------------

Application commands derive from ``sublime_plugin.ApplicationCommand``. Due to
the status of the API at the time of this writing, we won't discuss application
commands any further at the moment.


Window Commands
---------------

Window commands operate at the window level. This doesn't mean that you cannot
manipulate views from window commands, but rather that you don't need views to
exist in order for window commands to be available. For isntance, it wouln't
make sense for the built-in command ``new_window`` to need a pre-existent view
to be available. You want to be able to create new views regardless of there is
any open.


Text Commands
-------------

Text commands operate at the buffer level and they require a buffer to exist
in order to be available. When writing text commands, it is important to keep
in mind the edit object. The edit object groups modifications to the bufffer
atomically so undo and macros work in a sensible way. You are responsible of
creating and closing edit objects. To do so, you can call ``view.begin_edit``
and ``edit.end_edit``. Text commands get passed an ``edit`` object in their
``run`` method for convenience.


Responding to Events
--------------------

Any command deriving from ``EventListener`` will be able to respond to events.


Another Plugin Example: Feeding the Completions List
----------------------------------------------------

Let's create a plugin that fetches data from Google Autocomplete service and
feeds it to Sublime Text 2 completions list.

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
	                    
	        sugs = [(x.attrib["data"], x.attrib["data"]) for x in elements]
	
	        return sugs
