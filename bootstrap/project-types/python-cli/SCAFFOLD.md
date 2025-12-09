# Python CLI Project Scaffold

> **AI Instructions:** Use this scaffold when bootstrapping a Python command-line project.

---

## Defaults (Don't Ask)

These are pre-configured. Don't prompt the Human for these:

- **Platform:** GitHub
- **License:** MIT
- **Branch protection:** None
- **CI/CD:** None
- **CODEOWNERS:** None
- **.gitignore:** Python
- **Naming:** Python conventions (lowercase, underscores)
- **Testing:** TDD with pytest (always)
- **PR Reviews:** GitHub Copilot

---

## Project Details to Gather

Ask the Human for:

1. **Project name** (package-safe): lowercase, underscores, no hyphens
   - Example: `aws_backup_migrator`
2. **Short description**: 1-2 sentences
3. **Primary cloud provider(s)**: AWS / GCP / Both / None
4. **High-level tasks/goals**: What will this CLI do?

---

## Architecture: Domain-Driven Design (DDD)

This scaffold follows a three-layer architecture:

```
src/<project_name>/
├── __init__.py
├── cli.py              # Entry point, argparse
├── domain/             # Pure logic, no dependencies
├── application/        # Use cases, orchestration
└── infrastructure/     # Cloud SDKs, I/O, config
```

**Why DDD?**

- Domain layer is testable without mocks
- Cloud providers can be swapped
- Clear separation of concerns

---

## Directory Structure

```
<project_name>/
├── .python-version          # pyenv version
├── .gitignore               # Python gitignore
├── .claude/
│   └── settings.json        # AI permissions
├── LICENSE                  # MIT
├── Pipfile                  # Dependencies (pipenv)
├── pyproject.toml           # Package config
├── README.md
├── BACKLOG.md               # Story tracking
├── CHANGELOG.md             # Release history
├── docs/
│   └── requirements.md      # Requirements
├── src/
│   └── <project_name>/
│       ├── __init__.py
│       ├── cli.py
│       ├── domain/
│       │   └── __init__.py
│       ├── application/
│       │   └── __init__.py
│       └── infrastructure/
│           └── __init__.py
├── tests/
│   ├── conftest.py
│   ├── unit/
│   │   └── ...
│   └── integration/
│       └── ...
└── scripts/
    └── ...
```

---

## Guard Rails

Apply these principles when generating code:

### Test-Driven Development (TDD) - ALWAYS

1. **Red** - Write a failing test first
2. **Green** - Write minimal code to pass
3. **Refactor** - Clean up while tests pass

Never write implementation without a test first.

### Modern Software Engineering (Dave Farley)

- Optimize for fast, frequent, low-risk changes
- Always keep the codebase releasable (trunk-based)
- Prefer clear, simple, composable design
- Automate everything repeatable

### Python Conventions

- Follow PEP 8
- Use type hints everywhere
- Use `snake_case` for functions and variables
- Use `PascalCase` for classes
- Use `UPPER_CASE` for constants

### File-Level Metadata

Every `.py` file must have:

```python
#!/usr/bin/env python3
"""
Module description here.
"""

__version__ = "0.1.0"


def file_info() -> dict:
    return {
        "name": __name__,
        "description": "Module description",
        "version": __version__,
        "author": "John Ayers",
        "last_updated": "YYYY-MM-DD"
    }
```

### CLI Design

- Use standard library `argparse`
- Every module must work as importable AND standalone
- Include `--version` and `--help` flags
- Use `--dry-run` for destructive operations

### Cloud Operations

- Never hardcode credentials
- Use environment variables or cloud-native auth
- Operations should be idempotent when possible
- Log with clear levels and human-readable messages

---

## Initial Files to Generate

When scaffolding, create these files:

1. **README.md** - Project description, setup, usage
2. **LICENSE** - MIT license
3. **.python-version** - Python version (recommend 3.11+)
4. **.gitignore** - Python gitignore (from GitHub template)
5. **Pipfile** - Initial dependencies
6. **pyproject.toml** - Package configuration
7. **BACKLOG.md** - Copy from `docs/templates/backlog.md`
8. **CHANGELOG.md** - Empty changelog template
9. **docs/requirements.md** - Copy from `docs/templates/requirements.md`
10. **src/<name>/__init__.py** - Package init
11. **src/<name>/cli.py** - Entry point with argparse
12. **src/<name>/domain/__init__.py** - Domain layer
13. **src/<name>/application/__init__.py** - Application layer
14. **src/<name>/infrastructure/__init__.py** - Infrastructure layer
15. **tests/conftest.py** - Pytest fixtures
16. **tests/unit/test_version.py** - First test (TDD)
17. **.claude/settings.json** - AI permissions

---

## AI Permissions Template

Create `.claude/settings.json`:

```json
{
  "permissions": {
    "allow": [
      "pipenv install",
      "pipenv run pytest",
      "pipenv run python",
      "git add",
      "git commit",
      "git status",
      "git diff",
      "git log",
      "gh pr create",
      "gh pr view"
    ],
    "deny": [
      "rm -rf",
      "git push --force",
      "git reset --hard",
      "pipenv run python -c"
    ]
  }
}
```

---

## GitHub Repository Setup

After creating files locally:

```bash
# Create GitHub repo
gh repo create <project_name> --private --source=. --remote=origin

# Initial commit and push
git add -A
git commit -m "feat: initial project scaffold"
git push -u origin main
```

---

## PR Workflow with Copilot

**Creating a PR:**

```bash
# Push branch
git push -u origin feature/STORY-X-description

# Create PR (Copilot will auto-review)
gh pr create --title "STORY-X: Description" --body "Implements FR-XXX

## Changes
- Change 1
- Change 2

## Testing
- [x] Unit tests
- [x] Integration tests

## UAT
1. Step 1
2. Step 2
"
```

**After Copilot Reviews:**

```bash
# View PR and comments
gh pr view --comments

# Or open in browser
gh pr view --web
```

**Claude addresses Copilot comments, then Human approves and merges.**

---

## Post-Scaffold Commands

After creating files:

```bash
cd <project_name>
pipenv install --dev
pipenv install -e .
pipenv run pytest tests/ -v
```

---

## Development Slices

After scaffold, work in this order:

1. **Slice 1:** Version command works, tests pass
2. **Slice 2:** First domain object with tests
3. **Slice 3:** First use case in application layer
4. **Slice 4:** Infrastructure adapter (if cloud needed)
5. **Slice 5:** First real CLI command end-to-end

---

## Claude Tips

- **Always TDD** - Write test first, then implementation
- Use **Plan Mode** to review the scaffold before generating
- Ask Claude to explain any architectural decisions
- Have Claude verify setup instructions work
- For PRs: *"Create a PR for this story using gh"*
