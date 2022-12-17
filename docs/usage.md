# Usage

You can configure autotag in your `mkdocs.yml`:

```yaml
plugins:
- autotag:
    globs:
      "*": Documentation
      "test/**": Test page
      "index.md": "Index page"
      "**/index.md": "Index page"
```

## globs

In the `globs` setting, you can pass the patterns as key and the tag to apply as a value.
I have implemented custom glob logic, which should match the general implementation of globs:

- `**` should match any string, including one containging path separators (`/`).
    Use this when you want to specify that a file may be nested deeply in a folder.
- `*` should maych any string except path separators.
    You can use it to specify the pattern of a single file/folder name without it including subfolders.
- `?` should match any single character (except path separators).
