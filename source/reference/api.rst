Python API
==========

.. seealso::

    `Official Documentation for Sublime Text 2 <http://www.sublimetext.com/docs/2/api_reference.html>`_
        API documentation.

    `Official Documentation for Sublime Text 3 <http://www.sublimetext.com/docs/3/api_reference.html>`_
        API documentation.


Missing in the official docs
----------------------------

There are quite a few things that are not (yet) documented in the official docs,
this section tries to solve this.

.. py:module:: sublime

.. py:class:: Window

    .. py:method:: set_layout(layout)

        Expects a dictionatry like this::

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

        :param layout: dictionary with layout options, see below
        :returns: None


Exploring the API
-----------------

A quick way to see the API in action:

#. Add ``Packages\Default`` (**Preferences | Browse Packages…**) to your project.
#. ``CTRL + SHIFT + F``
#. Enter ``*.py`` in the **In Files:** field
#. Check ``Use Buffer`` option
#. Search API name
#. ``F4``
#. Study relevant source code