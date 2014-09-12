Python API
==========

.. seealso::

    `Official Documentation <http://www.sublimetext.com/docs/3/api_reference.html>`_
        API documentation.


Missing in the official docs
----------------------------

There are quite a few things that are not (yet) documented in the official docs,
this section tries to solve this.

.. py:module:: sublime

.. py:class:: Window

    .. py:method:: set_layout(layout)

        Changes the tile-based panel layout of view groups.

        :param dict layout: specifies the new layout, see below
        :returns: None

        Expects a dictionary like this::

            {"cols": [float], "rows": [float], "cells": [[int]]}

        where :samp:`[type]` represents a list of *type*.

        **cols**
            A list of the column separators (floating point numbers), should
            start with ``0`` (left) and end with ``1`` (right).

        **rows**
            A list of the row separators (floating point numbers), should start
            with ``0`` (top) and end with ``1`` (bottom).

        **cells**
            A list of cell lists which describe a cell's boundaries each. Cells
            can be imagines as rectangles with the rows and cols specified along
            in this dictionary. Think like this::

                [x1, y1, x2, y2]

            where all values are integers respectively and map to the *cols* and
            *rows* indicies. Thus, a cell with ``[0, 0, 1, 2]`` translates to a
            cell from the top left to the first column and the second row
            separator (in a 2x2 grid this would be bottom center).

        .. note::

            **rows** and **cols** are not tested for boundaries and they are not
            adjusted either. Thus, it is possible to specify values lower than
            ``0`` or higher than ``1`` and Sublime Text will in fact treat them
            accordingly. That means you can crop views or create borders. It is
            not known whether the "background color" of these empty spaces can
            be modified, the default is black. Use at your own risk!

            The order of column or row separators is not checked either. If you,
            for example, use a reversed column list like ``[1, 0.5, 0]`` you
            get to see two black panels. Sublime Text is unusable in this state.

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

            # A 2-column layout with the separator in the middle and the right
            # column being split in half
            window.set_layout({
                "cols": [0, 0.5, 1],
                "rows": [0, 0.5, 1],
                "cells": [[0, 0, 1, 2], [1, 0, 2, 1],
                                        [1, 1, 2, 2]]
            })


Exploring the API
*****************

A quick way to see the API in action:

#. Add ``Packages\Default`` (**Preferences | Browse Packages...**) to your project.
#. ``CTRL + SHIFT + F``
#. Enter ``*.py`` in the **In Files:** field
#. Check ``Use Buffer`` option
#. Search API name
#. ``F4``
#. Study relevant source code
