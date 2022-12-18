# Usage

You can configure autotag in your `mkdocs.yml`.
For example it may look like this:

```yaml
plugins:
- autotag:
    globs:
        "*": Documentation
        "test/**": 
        - Test page
        - Another tag
        "index.md": "Index page"
        "**/index.md": "Index page"
    regex:
        ".*\.md": "Markdown"
        "([^/]+)/([^/]+)/.*":
        - "main folder: {0}"
        - "sub folder: {1}"
        - "{0}/{1}/"
```

You can also look at the [repo's mkdocs.yml](https://github.com/six-two/mkdocs-auto-tag-plugin/blob/main/mkdocs.yml) file.

## globs

In the `globs` setting, you can pass the patterns as key and the tag(s) to apply as a value.
I have implemented custom glob logic, which should match the general implementation of globs:

- `**` should match any string, including one containging path separators (`/`).
    Use this when you want to specify that a file may be nested deeply in a folder.
- `*` should maych any string except path separators.
    You can use it to specify the pattern of a single file/folder name without it including subfolders.
- `?` should match any single character (except path separators).

### Multiple tags

|Version required|0.1.1+|

You can assign multiple tags to a single glob / regex value by specifying them as a list.
Example:

```yaml
plugins:
- autotag:
    globs:
        "*.md": 
            - Page
            - Markdown
        "*.txt": ["Plain text", "Page"]
```

## regex

|Version required|0.1.1+|

Regex (regular expression) rules give you more control about the search pattern.
They also allow you to use capture groups, which you can use in the tag.
Use `{0}` for the first capture group, `{1}` for the second capture group, and so on.

Please do not use more formating values than capture groups exist, or other placeholders such as `{something}`, since they will likely cause the plugin to crash.
