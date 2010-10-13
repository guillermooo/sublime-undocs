Macros
======

Macros are a basic automation facility consisting in sequences of commands. Use
them whenever you need to repeat the exact same steps to perform an operation.

Macro files have the extension ``sublime-macro``. Sublime Text ships with a few
macros providing core functionality, such as line and word deletion. You can find
these under **Tools | Macros | Default**.

How to record a macro
*********************

To start recording a macro, press ``CTRL + Q``. After that, carefully execute the
desired steps one by one. When you're done, press ``CTRL + Q`` again to stop
recording. Your new macro won't be saved to a file, but kept in the macro buffer
instead. You can now run the recorded macro by pressing ``CTRL + SHIFT + Q`` or
save it to a file by selecting **Tools | Save macro...**.

The macro buffer will only remember the macro recorded latest.

.. note::
    Recorded macros only capture commands sent to the buffer: window level commands,
    such as creating a new file, will be ignored.

How to edit a macro
*******************

Alternatively to recording a macro, you can edit it by hand. Save a new file with
the extension ``sublime-macro`` under ``\Packages\User`` and add commands to it. You
can only issue one command per line. See the Commands section for more information
on commands.

Macro files can be stored in any package folder, but if you save them to
``\Packages\User``, they will show up under **Tools | Macros | User**.


.. TODO: do we need to escape every kind of quotations marks?
.. note::
    If you're editing a macro by hand, you need to escape quotation marks,
    blank spaces and backslashes by preceding them with ``\``.
