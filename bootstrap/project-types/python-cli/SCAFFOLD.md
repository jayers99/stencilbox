# Python CLI Project Scaffold

> **AI Instructions:** Use this scaffold when bootstrapping a Python command-line project.

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
├── .gitignore
├── .claude/
│   └── settings.json        # AI permissions
├── Pipfile                  # Dependencies (pipenv)
├── pyproject.toml           # Package config
├── README.md
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

### Modern Software Engineering (Dave Farley)

- Optimize for fast, frequent, low-risk changes
- Always keep the codebase releasable (trunk-based)
- Prefer clear, simple, composable design
- Automate everything repeatable

### Test-Driven Development (TDD)

- Tests come first, then minimal implementation, then refactor
- Use pytest
- Keep tests fast and deterministic
- Mirror src layout in tests/

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
2. **.python-version** - Python version (recommend 3.11+)
3. **.gitignore** - Python-specific ignores
4. **Pipfile** - Initial dependencies
5. **pyproject.toml** - Package configuration
6. **src/<name>/__init__.py** - Package init
7. **src/<name>/cli.py** - Entry point with argparse
8. **src/<name>/domain/__init__.py** - Domain layer
9. **src/<name>/application/__init__.py** - Application layer
10. **src/<name>/infrastructure/__init__.py** - Infrastructure layer
11. **tests/unit/test_version.py** - First test (TDD)
12. **.claude/settings.json** - AI permissions

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
      "git log"
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

- Use **Plan Mode** to review the scaffold before generating
- Ask Claude to explain any architectural decisions
- Request tests before implementation (TDD)
- Have Claude verify setup instructions work
