# Sublime Text Unofficial Documentation


This project was started because the [official documentation][off-docs] of
Sublime Text is lacking. You can visit it online on
<http://docs.sublimetext.info/>, hosted via [ReadTheDocs][] and built using
[Sphinx][].

Following our [fundraiser on BountySource][fundraiser] during July-August 2014
we are currently in the process of revising all topics and adding more topics
in general. You can follow our progress on our public [Trello board][trello].

Huge thanks to [all our supporters](./BACKERS.md)


## Supporting

You can support us by treating us to a beer or alternatively sending a
donation:

*PayPal/Gittip/Pledgie be here*


## Contributing

You are free to submit any form of issue on our [issues][] page and we are very
open to pull requests. Your PR will be reviewed and might not be accepted.
**Please follow our (style) guidelines in
[CONTRIBUTING.md](./CONTRIBUTING.md).**

A `.sublime-project` file is included in this repository with a few general
settings and a build system that builds the HTML docs using [Sphinx][].


### Building (HTML Preview)

In order to build and preview the docs you need Sphinx, which in return
requires **Python 2.7**. Python 3+ does not work.

    pip install sphinx

By default, a standard theme will be used, but you can make it use the
ReadTheDocs theme by installing it as well:

    pip install sphinx_rtd_theme

The build script will check for and use it, if the theme is available.


[off-docs]: http://sublimetext.com/docs/3
[trello]: https://trello.com/b/ArLlY4X7/sublime-text-unofficial-documentation
[fundraiser]: https://www.bountysource.com/teams/st-undocs/fundraiser

[issues]: https://github.com/guillermooo/sublime-undocs/issues
[Sphinx]: http://sphinx-doc.org/
[ReadTheDocs]: https://readthedocs.org/
