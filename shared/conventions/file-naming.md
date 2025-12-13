# File Naming Conventions

Standard naming rules for all files in stencilbox and related repositories.

## The Rule

| File Type | Convention | Example |
|-----------|------------|---------|
| **Documentation (`.md`)** | `kebab-case` | `interview-questions-framework.md` |
| **Python modules (`.py`)** | `snake_case` | `my_module.py` |
| **Python packages** | `lowercase` | `mypackage/` |
| **CLI entry points** | `kebab-case` | `my-cli-tool` |
| **Directories** | `kebab-case` | `project-planning/` |

## Why

- **Markdown/docs use dashes:** Shell-friendly, URL-friendly, conventional for documentation
- **Python files use underscores:** Required for valid Python imports (`import my_module`)
- **CLI commands use dashes:** Unix convention, easier to type

## Examples

```
# Good
farewell-communication-framework.md
tone-guide-shortform.md
interview-questions-framework.md
my_python_module.py
utils/string_helpers.py

# Bad
farewell_communication_framework.md  # underscore in markdown
my-python-module.py                  # dash in Python (breaks imports)
```

## Special Cases

| Case | Convention |
|------|------------|
| **README, LICENSE, CHANGELOG** | `UPPERCASE` (convention) |
| **CLAUDE.md** | `UPPERCASE` (tool convention) |
| **Acronyms in kebab-case** | lowercase: `api-guide.md`, not `API-guide.md` |
| **Version numbers** | keep dots: `v1.2.3-release-notes.md` |

## Applying to Existing Files

When renaming files:
1. Update any internal links/references
2. Update imports (for Python)
3. Commit rename separately for clean git history
