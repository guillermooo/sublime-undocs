Plugins
=======

.. seealso::

   :doc:`API Reference <../reference/api>`
        More information on the Python API.

   :doc:`Plugins Reference <../reference/plugins>`
        More information about plugins.        


Sublime Text 2 is programmable with Python scripts. Plugins reuse existing
commands or create new ones to build a feature. Plugins are rather a logical
entity than a physical one.


Prerequisites
*************

In order to write plugins, you must be able to program in Python_.

.. _Python: http://www.python.org


Where to Store Plugins
**********************

Sublime Text 2 will look for plugins in these places:

* ``Packages``
* ``Packages/<pkg_name>/``

Consequently, any plugin nested deeper in ``Packages`` won't be loaded.

Keeping plugins right under ``Packages`` is discouraged, because Sublime Text
sorts packages in a predefined way before loading them. Thus, you might get
confusing results if your plugins live outside of a package.


Your First Plugin
*****************

Let's write a "Hello, World!" plugin for Sublime Text 2:

#. Select **Tools | New Plugin...** in the menu.
#. Make sure there's a colon after ``class ExampleCommand(sublime_plugin.TextCommand)``. This step is required due to a bug in Sublime Text 2 at the time of this writing.
#. Save to ``Packages/User/hello_world.py``.

You've just written your first plugin. Let's put it to use:

#. Create a new buffer (``CTRL + N``).
#. Open the python console (``CTRL + ```).
#. Type: ``view.run_command("example")`` and press enter.

You should see the text "Hello, World!" in your new buffer.


Analyzing Your First Plugin
***************************

The plugin created in the previous section should look roughly like this::

    import sublime, sublime_plugin
    
    class ExampleCommand(sublime_plugin.TextCommand):
        def run(self, edit):
            self.view.insert(edit, 0, "Hello, World!")


The ``sublime`` and ``sublime_plugin`` modules are both provided by
Sublime Text 2.

New commands derive from the ``*Command`` classes defined in ``sublime_plugin``
(more on this later).

The rest of the code is concerned with particulars of the ``TextCommand`` or
the API that we'll discuss in the next sections.

Before moving on, though, we'll look at how we called the new command: We first
opened the python console, and then issued a call to ``view.run_command``. This
is a rather inconvenient way of using plugins, but it's often useful when
you're in the development phase. For now, keep in mind that your commands
can be accessed through key bindings or other means, just as other commands are.

Conventions for Command Names
-----------------------------

You might have noticed that our command is defined with the name ``ExampleCommand``,
but we pass the string ``example`` to the API call instead. This is necessary because
Sublime Text 2 normalizes command names by stripping the ``Command`` suffix and
separating ``CamelCasedPhrases`` with underscores, like this: ``camel_cased_phrases``.

New commands should follow the pattern mentioned above for class names.


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
exist in order for window commands to be available. For instance, the built-in
command ``new_file`` is defined as a ``WindowCommand`` so it works too when no
view is open. Requiring a view to exisit in that case wouln't make sense.


Text Commands
-------------

Text commands operate at the buffer level and they require a buffer to exist
in order to be available.

Text Commands and the ``edit`` Object
-------------------------------------

The edit object groups modifications to the view so undo and macros work in a
sensible way. You are responsible for creating and closing edit objects. To do
so, you can call ``view.begin_edit`` and ``edit.end_edit``. Text commands get
passed an open ``edit`` object in their ``run`` method for convenience.
Additionally, many ``View`` methods require an edit object.


Responding to Events
--------------------

Any command deriving from ``EventListener`` will be able to respond to events.


Another Plugin Example: Feeding the Completions List
----------------------------------------------------

Let's create a plugin that fetches data from Google Autocomplete service and
feeds it to Sublime Text 2 completions list. Please note that as ideas for
plugins go, this a very bad one.

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
	Please make sure you don't keep this plugin around after trying it. It will
	interefere with the autocompletions look-up chain.


Learning the API
****************

In order to create plugins, you need to get acquainted with the Python API
Sublime Text 2 exposes, and the available commands. Documentation on both is
scarce at the time of this writing, but you can read existing code and learn
from it too. In particular, the ``Packages/Default`` folder contains many
examples of undocumented commands and API calls.

