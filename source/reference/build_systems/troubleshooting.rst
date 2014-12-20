.. _troubleshooting-build-systems:

Troubleshooting Build Systems
*****************************

Build systems will look for executables
in your :const:`PATH`.
Therefore, your :const:`PATH`
variable must be correctly set.

On some operating systems,
the value of :const:`PATH`
may vary between terminal windows
and graphical applications.
Thus, depending on
how you start Sublime Text,
the build system may or may not work.

To solve this issue,
make sure you set the :const:`PATH`
so that graphical applications such as Sublime Text
can find it.
See the links below
for more information.

Alternatively, you can use the ``path`` option
in a ``.sublime-build`` file
to override the :const:`PATH` used to locate
the executable specified in ``cmd``.

.. seealso::

    `Managing Environment Variables in Windows <http://goo.gl/F77EM>`_
        Search Microsoft knowledge base for this topic.

    `Setting Environment Variables in OSX <http://stackoverflow.com/q/135688/1670>`_
        StackOverflow topic.
