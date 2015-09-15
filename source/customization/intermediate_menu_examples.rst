============================
 Intermediate Menu Examples
============================

``Main.sublime-menu`` file for packages that have user-settings.

.. code-block:: json

   [
       {
           "id": "preferences",
           "children":
           [
               {
                   // Include this information in case it is the only package using that menu
                   "caption": "Package Settings",
                   "mnemonic": "P",
                   "id": "package-settings",
                   "children":
                   [
                       {
                           "caption": "InsertDate",
                           "id": "insertdate",
                           "children":
                           [
                               // README
                               {
                                   "caption": "README.md",
                                   "command": "open_file",
                                   "args": {"file": "${packages}/InsertDate/README.md"}
                               },
                               { "caption": "-"},
                               // Settings - Default
                               {
                                   "caption": "Settings – Default",
                                   "command": "open_file",
                                   "args": {"file": "${packages}/InsertDate/insert_date.sublime-settings"}
                               },
                               // Settings - User
                               {
                                   "caption": "Settings – User",
                                   "command": "open_file",
                                   "args": {"file": "${packages}/User/insert_date.sublime-settings", "contents": "{\n\t$0\n}"}
                               }
                           ]
                       }
                   ]
               }
           ]
       }
   ]
