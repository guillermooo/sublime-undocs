==============================
Build Systems -- Configuration
==============================

.. warning::

   Build system selection is currently
   undergoing a rework in the dev channel.
   The following information may be outdated.

   See `this forum thread <http://www.sublimetext.com/forum/viewtopic.php?f=2&t=17471&sid=81fd17a6c886e151a3f69c0eaa87272d>`_ for details.


Overview
========

The build system framework in Sublime Text
tries to be flexible enough to accommodate
a large number of build scenarios.

Should the default configuration options
fall short for your needs,
you can implement your own build system
mechanism in two main ways:

- as a custom ``target`` command
  (still using the default build system framework)
- as an entirely new plugin
  (skipping the build system framework)


Meta Options in Build Systems
=============================

This is a list of standard options
that all build systems understand.
These options are used internally
by Sublime Text.
The ``target`` command does not
receive any of these options.

.. _bs-target-option:

``target`` *(optional)*
    A Sublime Text ``WindowCommand``.
    Defaults to ``exec`` (:file:`Packages/Default/exec.py`).
    This command receives
    all the :ref:`target command arguments <build-arbitrary-options>` specified
    in the ``.sublime-build`` file (as ``**kwargs``).

    Used to override the default build system command.
    Note that
    if you choose
    to override the default command
    for build systems,
    you can add any number of extra options
    to the ``.sublime-build`` file.

``selector`` *(optional)*
    Used when **Tools | Build System | Automatic**
    is set to ``true``.
    Sublime Text uses this scope selector
    to find the appropriate build system
    for the active view.

``windows``, ``osx`` and ``linux`` *(optional)*
    Used to selectively apply options by OS.
    OS-specific values override defaults.
    Each of the listed items
    accepts a dictionary of options.

    See `Platform-specific Options`_.

``variants`` *(optional)*
    A list of dictionaries of options.
    Variant names will appear in the Command Palette
    for easy access if the build system's selector
    matches for the active file.

    Using variants it's possible
    to specify multiple build system tasks
    in the same ``.sublime-build`` file.

    See Variants_.

``name`` *(optional)*
    **Only valid inside a variant**.

    Identifies a build system task.
    If the ``name`` is 'Run',
    the variant will show up
    under **Tools | Build System**.
    Sublime Text will automatically
    bind the 'Run' task to :kbd:`Ctrl+Shift+B`.

    See Variants_.


.. _build-arbitrary-options:

Target Command Arguments
************************

Thanks to the ``target`` setting,
which overrides the default ``exec`` command
with any other command of your choice,
a build system may contain
any number of custom arguments
that the new ``target`` command accepts.

See the :ref:`target<bs-target-option>` option.


Platform-specific Options
*************************

The ``windows``, ``osx`` and ``linux`` elements
let you provide platform-specific data
in the build system.
Here's an example:

.. sourcecode:: javascript

    {
        "cmd": ["ant"],
        "file_regex": "^ *\\[javac\\] (.+):([0-9]+):() (.*)$",
        "working_dir": "${project_path:${folder}}",
        "selector": "source.java",

        "windows": {
            "cmd": ["ant.bat"]
        }
    }

In this case, ``ant`` will be executed
for every platform except Windows,
where ``ant.bat`` will be used instead.


Variants
********

Here's a contrived example
of a build system with variants:

.. sourcecode:: javascript

    {
        "selector": "source.python",
        "cmd": ["date"],

        "variants": [

            { "name": "List Python Files",
              "cmd": ["ls -l *.py"],
              "shell": true
            },

            { "name": "Word Count (current file)",
              "cmd": ["wc", "$file"]
            },

            { "name": "Run",
              "cmd": ["python", "-u", "$file"]
            }
        ]
    }


Given these settings,
:kbd:`Ctrl+B` would run the *date* command,
:kbd:`Crtl+Shift+B` would run the Python interpreter
and the remaining variants would appear
in the :ref:`Command Palette <ext-command-palette-overview>`
as :samp:`Build: {name}` whenever the build system was active.


.. _build-capture-error-output:

Capturing Build System Results
==============================

When build systems output text
to a results view,
it's possible to capture
*results data* in order to enable
result navigation.

.. note::

    *Results* can also mean *errors*.
    Often, build systems produce
    error data.

Set the following **view settings**
in a results view
if you want to enable results navigation:

``result_file_regex``
    A Perl-style regular expression
    to capture up to four fields of error information
    from a results view, namely:
    *filename*, *line number*, *column number* and *error message*.
    Use groups in the pattern
    to capture this information.
    The *filename* field and
    the *line number* field are required.

``result_line_regex``
    If ``result_file_regex`` doesn't match
    but ``result_line_regex`` exists
    and does match on the current line,
    walk backwards through the buffer
    until a line matching ``result_file_regex`` is found,
    and use the two matches
    to determine the file and line to go to.

``result_base_dir``
    Used to find files where results occur.

When result data is captured,
you can navigate to results
in your project's files with :kbd:`F4` and :kbd:`Shift+F4`.
If available, the captured *error message*
will be displayed in the status bar.


.. _build-system-variables:

Build System Variables
======================

Build systems expand the following variables
in ``.sublime-build`` files:

======================  ===========================================================
``$file_path``          The directory of the current file,
                        e.g., *C:\\Files*.
``$file``               The full path to the current file,
                        e.g., *C:\\Files\\Chapter1.txt*.
``$file_name``          The name portion of the current file,
                        e.g., *Chapter1.txt*.
``$file_extension``     The extension portion of the current file,
                        e.g., *txt*.
``$file_base_name``     The name-only portion of the current file,
                        e.g., *Document*.
``$folder``             The path to the first folder opened in the current project.
``$project``            The full path to the current project file.
``$project_path``       The directory of the current project file.
``$project_name``       The name portion of the current project file.
``$project_extension``  The extension portion of the current project file.
``$project_base_name``  The name-only portion of the current project file.
``$packages``           The full path to the *Packages* folder.
======================  ===========================================================


.. note::

    Expansion is currently applied only
    to the following keys in the :file:`.sublime-build` file:
    ``cmd``, ``shell_cmd``, and ``working_dir``.


Placeholders for Variables
**************************

Features found in snippets
can be used with these variables.
For example::

    ${project_name:Default}

This will emit the name of the current project
if there is one, otherwise ``Default``.

::

    ${file/\.php/\.txt/}

This will emit
the full path of the current file,
replacing *.php* with *.txt*.

.. seealso::

    :doc:`/extensibility/snippets`
        Documentation on snippet variables.


Running Build Systems
=====================

Select the desired build system
from **Tools | Build System**,
and then select **Tools | Build**.
Alternatively, you can use
the command palette or
the following key bindings:


===================  =========================
:kbd:`Ctrl+B`        Run default build task
:kbd:`F7`            Run default build task
:kbd:`Ctrl+Shift+B`  Run 'Run' build task
:kbd:`Ctrl+Break`    Cancel running build task
===================  =========================

See `Variants`_.
