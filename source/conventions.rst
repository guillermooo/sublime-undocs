About This Documentation
========================

This is the unofficial documentation for the Sublime Text editor, maintained by
volunteers. We hope it's useful!

Sublime Text 1 vs Sublime Text 2
********************************

This documentation was initially written for v1 of Sublime Text. v2 has brought
about a few notable changes that render part of the information in these pages
inexact. In particular, the settings format of choice is now JSON, and the
naming conventions for almost anything is based on PEP8. Basically, this
means that whatever was named ``someCommandName`` in v1 is now called
``some_command_name`` in v2.

In the following weeks, we hope to bring the documentation into line with
Sublime Text 2. Until then, though, watch out for the differences between
versions!

Conventions
***********

* This guide is written from the perspective of a Windows user, but most
  instructions should require trivial changes to work on other platforms.

* Relative paths (e. g. ``Packages\User``) are rooted at the parent of
  ``sublime.packages_path()`` unless otherwise stated.

* We assume default key bindings when indicating keyboard shortcuts unless
  otherwise noted. This means **some key bindings won't match your locale's
  keyboard layout!**

* This guide is in the process of being rewritten to target Sublime Text 2
  specifically. Nevertheless, *mutatis mutandis*, most new information should
  be useful for Sublime Text users too. Hey, we've just used Latin back there!

The Sublime Text Python Console
*******************************

You'll come across frequent references to the python console in these help
files. In order to open it, press ``CTRL + ~``.
