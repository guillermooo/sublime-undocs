Python API
==========

.. _api-official-docs:

.. seealso::

    `Official Documentation for Sublime Text 2 <http://www.sublimetext.com/docs/2/api_reference.html>`_
        API documentation.

    `Official Documentation for Sublime Text 3 <http://www.sublimetext.com/docs/3/api_reference.html>`_
        API documentation.


Missing in the official docs
****************************

This section tries to address missing topics in the official documentation.


Index
-----

.. XXX It would be very nice if this could've been automatically generated but I
.. couldn't find a way and nobody was able to help me out. I AM DISAPPOINT! - FF

.. py:currentmodule:: sublime

module :py:mod:`sublime`
    - class :py:class:`Window`
        * :py:meth:`~Window.set_layout`
    - class :py:class:`View`
        * :py:meth:`~View.match_selector`

.. py:currentmodule:: sublime_plugin

module :py:mod:`sublime_plugin`
    - class :py:class:`EventListener`
        * :py:meth:`~EventListener.on_query_completions`


.. #############################################################################
.. # sublime docs
.. #############################################################################

.. py:module:: sublime

``sublime`` module
------------------

.. py:class:: Window

    This class represents windows in Sublime Text and provides an interface of
    methods to interact with them. For all available methods, see the
    `official documentation <http://www.sublimetext.com/docs/2/api_reference.html#sublime.Window>`__.

    .. py:method:: set_layout(layout)

        Changes the group layout of the current window.

        Expects a dictionary like this::

            {"cols": [float], "rows": [float], "cells": [[int]]}

        where :samp:`[type]` represents a list of *type*.

        **cols**
            A list of the column seperators (*float*), should start with ``0``
            (left) and end with ``1`` (right).

        **rows**
            A list of the row seperators (*float*), should start with ``0``
            (top) and end with ``1`` (bottom).

        **cells**
            A list of cell lists which describe a cell's boundaries each. Cells
            can be imagines as rectangles with the rows and cols specified along
            in this dictionary. Think like this::

                [x1, y1, x2, y2]

            where all values are integers respectively and map to the *cols* and
            *rows* indices. Thus, a cell with ``[0, 0, 1, 2]`` translates to a
            cell from the top left to the first column and the second row
            separator (in a 2x2 grid this would be bottom center).

        .. note::

            *rows* and *cols* are not tested for boundaries. Thus, even though
            it makes zero sense to have a values lower than ``0`` or higher than
            ``1`` it is possible to specify them and Sublime Text will in fact
            treat them accordingly. Furthermore, it is possible to have the
            first value not be ``0`` and the last not be ``1``, the remaining
            space will simply be black in this case. Don't try this at home!

        **Examples**::

            # A 2-column layout with a separator in the middle
            window.set_layout({
                "cols": [0, 0.5, 1],
                "rows": [0, 1],
                "cells": [[0, 0, 1, 1], [1, 0, 2, 1]]
            })

        ::

            # A 2x2 grid layout with all separators in the middle
            window.set_layout({
                "cols": [0, 0.5, 1],
                "rows": [0, 0.5, 1],
                "cells": [[0, 0, 1, 1], [1, 0, 2, 1],
                          [0, 1, 1, 2], [1, 1, 2, 2]]
            })

        ::

            # A 2-column layout with the seperator in the middle and the right
            # column being split in half
            window.set_layout({
                "cols": [0, 0.5, 1],
                "rows": [0, 0.5, 1],
                "cells": [[0, 0, 1, 2], [1, 0, 2, 1],
                                        [1, 1, 2, 2]]
            })


.. py:class:: View

    Similar to :py:class:`Window`, this class represents views in Sublime Text
    and provides an interface of methods to interact with them. For all
    available methods, see the
    `official documentation <http://www.sublimetext.com/docs/2/api_reference.html#sublime.View>`__.

    .. py:method:: match_selector(point, selector)

        Matches the scope at ``point`` against the specified ``selector``.

        Equivalent to::

            view.score_selector(point, selector) != 0

        or::

            sublime.score_selector(view.scope_name(point), selector) != 0


.. #############################################################################
.. # sublime_plugin docs
.. #############################################################################

.. py:module:: sublime_plugin

``sublime_plugin`` module
-------------------------

.. py:class:: EventListener

    A wrapper class for events. Subclass and define the methods you want to
    receive events on and you are done, no registering necessary.

    .. py:method:: on_query_completions(view, prefix, locations)

        Called whenever the completion list is requested.

        This accounts for all views and all windows, so in order to provide
        syntax-specific completions you should test the current scope of
        ``locations`` with :py:meth:`~sublime.View.match_selector`.

        **view**
            A :py:class:`~sublime.View` instance for which the completions should
            be made.

        **prefix**
            The text entered so far. This is only until the next word separator.

        **locations**
            Array of points in ``view`` where the completion should be
            inserted. This can be interpreted as the current selection.

            If you want to handle completions that depend on word separator
            characters you need to test each location individually. See
            :ref:`completions-multi-cursor` on how Sublime Text handles
            completions with multiple cursors.

        *Return value*
            Expects two (three) formats for return values:

            1.  :samp:`[[{trigger}, {contents}], ...]`

                A **list** of completions similar to
                :ref:`completions-trigger-based` but without mapping keys.
                *trigger* may use the ``\\t`` description syntax.

                **Note:** In Sublime Text 3, completions may also consist of
                plain strings instead of the trigger-contents-list.

            2.  :samp:`([[{trigger}, {contents}], ...], {flags})`

                Basically the same as above but wrapped in a 2-sized **tuple**.
                The second element, the *flags*, may be a bitwise OR combination
                of these flags:

                ``sublime.INHIBIT_WORD_COMPLETIONS``
                    Prevents Sublime Text from adding its word completions to
                    the completion list after all plugins have been processed.

                ``sublime.INHIBIT_EXPLICIT_COMPLETIONS``
                    XXX What does this do?

                Flags are shared among all completions, once set by one
                plugin you can not revert them.

            3.  Anything else (e.g. ``None``)

                No effect.

        **Example**:
            See :ref:`plugins-completions-example` for an example on how to use
            this event.


Exploring the API
-----------------

A quick way to see the API in action:

#. Add :file:`Packages/Default` (**Preferences | Browse Packages…**) to your project.
#. :kbd:`Ctrl + Shift + F`
#. Enter ``*.py`` in the **In Files:** field
#. Check ``Use Buffer`` option
#. Search API name
#. :kbd:`F4`
#. Study relevant source code
