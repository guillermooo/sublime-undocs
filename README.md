# Sublime Text Unofficial Documentation


We started this project to fill the gaps in the Sublime Text
[official documentation][off-docs]. You can visit this guide at
<http://docs.sublimetext.info/>. It is hosted via [ReadTheDocs][] and built
using [Sphinx][].

Following our [fundraiser on BountySource][fundraiser] during July-August 2014,
we've started revising all topics and adding new ones. You can follow our
progress on our public [Trello board][trello].

Huge thanks to [all our backers](./BACKERS.md)!


## Support Us

You can support our writing by treating us to a beer or sending a donation:

*PayPal/Gittip/Pledgie be here*


## Contributing

We accept error reports and requests for new content via our [issue tracker](https://github.com/guillermooo/sublime-undocs/issues)
and encourage you to send pull requests (but we cannot guarantee they will
always be merged).

**Please follow our style guidelines as described in
[CONTRIBUTING.md](./CONTRIBUTING.md).**

This repository includes a `.sublime-project` with predefined settings and a
build system that builds the HTML docs using [Sphinx][].


### Building (HTML Preview)

In order to build and preview the docs you'll need Sphinx, which in turn
requires **Python 2.7**. **Python 3+ will not work.**

    pip install sphinx

When previewing the docs, a standard Sphinx theme will be used by default, but
you can install and use the ReadTheDocs theme if you prefer that:

    pip install sphinx_rtd_theme

If the theme is available, the build system will pick it up.


[off-docs]: http://sublimetext.com/docs/3
[trello]: https://trello.com/b/ArLlY4X7/sublime-text-unofficial-documentation
[fundraiser]: https://www.bountysource.com/teams/st-undocs/fundraiser

[issues]: https://github.com/guillermooo/sublime-undocs/issues
[Sphinx]: http://sphinx-doc.org/
[ReadTheDocs]: https://readthedocs.org/
