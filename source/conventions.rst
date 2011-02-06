About This Documentation
========================

This is the unofficial documentation for the Sublime Text editor, maintained by
volunteers. We hope it's useful!

Sublime Text 1 vs Sublime Text 2
********************************

This documentation was initially written for Sublime Text 1. The second version
of the editor has brought about a few notable changes that render part of the
information in these pages inexact. For example, the settings format is now
JSON_, and the naming conventions for almost everything are based on PEP8_, which
means that ``namesLikeThis`` look like ``names_like_this`` in Sublime Text 2.

.. _JSON: http://www.json.org/
.. _PEP8: http://www.python.org/dev/peps/pep-0008/

In the following weeks, we hope to bring the documentation in line with Sublime
Text 2. Until then, watch out for the differences between the two versions!

Conventions in This Guide
*************************

* This guide is written from the perspective of a Windows user. Most
  instructions should require trivial changes to work on other platforms.

* Relative paths (e. g. ``Packages\User``) are rooted at the parent of
  ``sublime.packages_path()`` unless otherwise stated.

* We assume default key bindings when indicating keyboard shortcuts unless
  otherwise noted. Due to the way Sublime Text maps keys to commands, **some
  key bindings won't match your locale's keyboard layout**.

* This guide is in the process of being rewritten to target Sublime Text 2.
  Nevertheless, *mutatis mutandis*, most new information should be useful for
  Sublime Text users too. Hey, that was Latin back there!

Before you continue reading the material contained in this guide, we recommend
you to take a look at the :doc:`basic_concepts` section.

Happy learning!