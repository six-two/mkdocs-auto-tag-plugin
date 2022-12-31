# mkdocs-auto-tag-plugin

I|github|six-two/mkdocs-auto-tag-plugin|
I|pypi|mkdocs-auto-tag-plugin|
L|Documentation|https://mkdocs-auto-tag-plugin.six-two.dev/|

`mkdocs-auto-tag-plugin` is a plugin for [mkdocs](https://www.mkdocs.org/), allows you to tag files based on their path.

## Why I wrote it

This plugin was developed, since I have many pages with similar headlines / contents in different folders, which are for different aspects of a thing.
However it is hard to differentiate them when using `Material for MkDocs`'s search, so I hope that I can make it easier by tagging the pages according to their category.
And since nobody wants to add tags to hundreds of pages by hand, here is an plugin to automate that task. 😉

## Features

- Automatically assign tags based on file names or paths:
    - Match via [globs](/usage/#globs), no need to understand regular expressions.
    - Generate dynamic tags using regular expressions and capture groups.
- Designed to work with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/), but should probably work with other tag plugins too.

## Interested?

Then click `Next` or use the search function (in the top right corner) to learn more.
You can also checkout the source code of the plugin and this site at the [Github repository](https://github.com/six-two/mkdocs-auto-tag-plugin).
