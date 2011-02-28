Build Systems
=============

.. warning::

    This topic is a draft.

Build systems run external programs to process your project's files and print
captured output to the output panel.

File Format
***********

Build systems use JSON. Here's an example build system:

.. sourcecode:: python

    {
        "cmd": ["python", "-u", "$file"],
        "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
        "selector": "source.python"
    }

Options
*******

=============== ====================================================================================================
``cmd``         Array containing the command to run and its desired arguments.
``file_regex``  Regular expression to capture error output of ``cmd``.
``selector``    Used when **Tools | Build System | Automatic** is set for automatic discovery based on file's scope.
``working_dir`` Directory to change the current directory to before running ``cmd``.
``encoding``    Output encoding of ``cmd``. Must be a valid python encoding. Defaults to ``utf-8``.
=============== ====================================================================================================

Capturing Error Output with ``file_regex``
------------------------------------------

The ``file_regex`` option uses a Perl-style regular expression to capture up
to four fields of error information from the build program's output, namely:
*file name*, *line number*, *column number* and *error message*. Use
groups in the pattern to capture this information. The *file name* field and
the *line number* field are required fields.

When error information is captured, you can cycle through error instances in
your project's files with ``F4`` and ``SHIFT + F4``. If available, the captured
*error message* will be displayed in the status bar.


Variables
*********

====================== =====================================================================================
``$file``              The full path to the current file, e.g., ``C:\Files\Chapter1.txt``.
``$file_path``         The directory of the current file, e.g., ``C:\Files``.
``$file_name``         The name portion of the current file, e.g., ``Chapter1.txt``.
``$file_extension``    The extension portion of the current file, e.g., ``txt``.
``$file_base_name``    The name only portion of the current file, e.g., ``Document``.
``$project``           The full path to the current project file.
``$project_path``      The directory of the current project file.
``$project_name``      The name portion of the current project file.
``$project_extension`` The extension portion of the current project file.
``$project_base_name`` The name only portion of the current project file.
====================== =====================================================================================

Variable Place Holders
----------------------

Snippet style formatting can be used with these variables, for example::

    ${project_name:Default}

This will emit the name of the current project if there is one, otherwise *Default*.

::

    ${file/\.php/\.txt/}

This will emit the full path of the current file, replacing *.php* with *.txt*.

Running Build Systems
*********************

Select **Tools | Build** in the Sublime Text menu or press ``F7``.

Troubleshooting Build Systems
*****************************

External programs used in build systems need to be in your ``PATH``. As a
quick test, you can try to run them from the command line first and see whether
they work. However, note that your shell's ``PATH`` variable might differ to
that seen by Sublime Text due to your shell's profile.

.. seealso::
	
	`Managing Environmental Variables in Windows <http://goo.gl/F77EM>`_
		Search Microsoft for this topic.
	