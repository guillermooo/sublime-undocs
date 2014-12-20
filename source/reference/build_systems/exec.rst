==========================
``exec`` Command Arguments
==========================

All the options that follow
are related to the ``exec`` command
(see also :ref:`Exec Command Reference <cmd-exec>`).
If you change the ``target`` command,
these options can no longer be relied on
(see :ref:`build-arbitrary-options` for details).

``cmd``
    Required if ``shell_cmd`` is empty.

    Overriden by ``shell_cmd``.

    Array containing the command to run
    and its desired arguments.
    If you don't specify an absolute path,
    the external program
    will be searched in your :const:`PATH`.
    Ultimately, ``subprocess.Popen(cmd)`` is called.

    On Windows, GUIs are supressed.

``shell_cmd``
    Required if ``cmd`` is empty.

    Overrides ``cmd`` if used.

    A string that specifies
    the command to be run
    and its arguments.
    Ultimately, ``subprocess.Popen(shell_cmd, shell=True)`` is called.

    It should help in getting right
    invocations involving complex uses
    of quotation marks.

``working_dir``
    Optional.

    Directory to change
    the current directory to
    before running ``cmd``.
    The original current directory
    is restored afterwards.

``encoding``
    Optional.

    Output encoding of ``cmd``.
    Must be a valid Python encoding.
    Defaults to ``UTF-8``.

``env``
    Optional.

    Dictionary of environment variables
    to be merged with the current process'
    before passing them to ``cmd``.

    Use this option, for example,
    to add or modify environment variables
    without modifying your system's settings.

    Environmental variables
    will be expanded.

``shell``
    Optional.

    If *true*, ``cmd``
    will be run through the shell
    (``cmd.exe``, ``bash``...).

    If ``shell_cmd`` is used,
    this option has no effect.

``path``
    Optional.

    :const:`PATH` used
    by the ``cmd`` subprocess.

    Use this option
    to add directories to :const:`PATH`
    without having to modify
    your system's settings.

    Environmental variables
    will be expandend.

``file_regex``
    Optional.

    Sets the ``result_file_regex``
    for the results view.

    See :ref:`build-capture-error-output`
    for details.

``line_regex``
    Optional.

    Sets the ``result_line_regex``
    for the results view.

    See :ref:`build-capture-error-output`
    for details.

``syntax``
    Optional.

    If provided,
    it will be used to colorize
    the build system's output.

