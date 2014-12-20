=======================
Writing a Simple Plugin
=======================


Overview
========

In this tutorial
we'll write a simple plugin
that inserts the string
``Hello World!`` into the active buffer.



Writing the Plugin
==================

1. Create a new buffer (:kbd:`Ctrl+N`)
2. Type in the following:

::

   import sublime
   import sublime_plugin

   class InsertHelloWorldCommand(sublime_plugin.TextCommand):
       def __init__(self, *args, **kwargs):
           super().__init__(*args, **kwargs)

       def run(self, edit):
           self.view.insert(edit, 0, 'Hello world!')


3. Save to ``Packages/User/hello_world.py``.

Now our plugin has been saved
to a location where Sublime Text
can find it.
Let's use it.

#. Create a new buffer (:kbd:`Ctrl+N`)
#. Open the Python console (:kbd:`Ctrl+``)
#. Type: ``view.run_command("insert_hello_world")`` and press :kbd:`Return`.

You should see the text "Hello, World!" in the newly created buffer.

