Build Systems
=============

.. warning::

    This topic is a draft.

**The specifics of this topic target Sublime Text X.**

Build systems run external programs to process your project's files.

File Format
***********

Build systems use JSON. Here's an example:

.. sourcecode:: python

    {
        "cmd": ["python", "-u", "$file"],
        "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
        "selector": "source.python"
    }

Options
*******

=============== ================================================================================
``cmd``         Array containing the command to run and its desired arguments.
``file_regex``  Regular expression to capture error output.
``selector``    Scope where the build system will be active.
``working_dir`` Directory to change to before running ``cmd``.
=============== ================================================================================

Capturing Error Output with ``file_regex``
------------------------------------------

The ``file_regex`` option uses a Perl-style regular expression to capture up  to
four fields of error information from the build program's standard streams, namely:
**file name**, **line number**, **column number** and **error message**.

When error information is captured, you can cycle through error instances in your
project's files with ``F4`` and ``SHIFT + F4``


Variables
*********

================= =====================================================================================
``$file``         The full path to the current file, e.g., ``C:\\Files\\Chapter1.txt``
``$file_dir``     The directory of the current file, e.g., ``C:\\Files``
``$file_name``    The name portion of the current file, e.g., ``Chapter1.txt``
``$file_ext``     The extension portion of the current file, e.g., ``txt``
``$base_name``    The name only portion of the current file, e.g., ``Document``
``$project_dir``  The directory of the current project , e.g., ``C:\\Files``
``$project_name`` The name portion of the current project, e.g., ``Book`` for ``C:\\Files\\Book.sublime-project``
================= =====================================================================================

Variable Place Holders
----------------------

Snippet style formatting can be used with these variables, for example::

    ${project_name:Default}

This will emit the name of the current project if there is one, otherwise *Default*.

::

    ${File/\.php/\.txt/}

This will emit the name of the current file, replacing *.php* with *.txt*.

Like snippets.

Running Build Systems
*********************

Check under **Tools** in the Sublime Text X menu or press ``F7``.

Troubleshooting
***************

External programs used in build systems need to be in your ``PATH``. As a quick test, you
can try to run them from the command line first and see whether they work. However,
note that your shell's ``PATH`` variable might differ to that seen by Sublime Text X due
to your shell's profile.
