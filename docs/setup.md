# Setup

Install the plugin using pip:

```bash
pip install mkdocs-auto-tag-plugin
```

Then, add the plugin to your `mkdocs.yml`:

```yaml
plugins:
  - search
  - autotag
```

> If you have no `plugins` entry in your config file yet, you'll likely also want to add the `search` plugin. MkDocs enables it by default if there is no `plugins` entry set.

More information about plugins in the [MkDocs documentation](http://www.mkdocs.org/user-guide/plugins/).
