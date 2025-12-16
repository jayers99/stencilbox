# Python CLI Project Scaffold

> **AI Instructions:** Use this scaffold when bootstrapping a Python command-line project.
> **Reference Implementation:** `~/code/shuffle-aws-vaults/`

---

## Defaults (Don't Ask)

These are pre-configured. Don't prompt the Human for these:

- **Platform:** GitHub
- **License:** MIT
- **Python:** 3.12+ (pyenv)
- **Branch protection:** None
- **CI/CD:** None
- **CODEOWNERS:** None
- **.gitignore:** Python
- **Naming:** Python conventions (lowercase, underscores)
- **Testing:** TDD with pytest (always)
- **Code Quality:** black, ruff, mypy (configured in pyproject.toml)
- **PR Reviews:** GitHub Copilot (Claude polls every 30 seconds for completion)
- **Branching:** One branch per story (`feature/STORY-N-desc`) or bugfix (`bugfix/BUG-N-desc`)
- **Releases:** Semver release created after every PR merge

---

## Project Details to Gather

Ask the Human for:

1. **Project name** (package-safe): lowercase, underscores, no hyphens
   - Example: `aws_backup_migrator`
2. **CLI command name** (kebab-case): what users type to run the CLI
   - Example: `aws-backup-migrator`
3. **Short description**: 1-2 sentences
4. **Primary cloud provider(s)**: AWS / GCP / Both / None
5. **High-level tasks/goals**: What will this CLI do?

---

## Architecture: Domain-Driven Design (DDD)

This scaffold follows a three-layer architecture:

```
src/<project_name>/
├── __init__.py
├── cli.py              # Entry point, argparse
├── domain/             # Pure logic, no dependencies
├── application/        # Use cases, orchestration (Protocol-based)
└── infrastructure/     # Cloud SDKs, I/O, config, retry, logging
```

**Why DDD?**

- Domain layer is testable without mocks
- Cloud providers can be swapped via Protocol interfaces
- Clear separation of concerns
- Application layer uses dependency inversion (depends on abstractions)

**Protocol Pattern (Application Layer):**

```python
from typing import Protocol

class BackupRepository(Protocol):
    """Abstract interface for backup operations."""
    def list_vaults(self, region: str) -> list[Vault]: ...
    def get_recovery_points(self, vault_name: str) -> list[RecoveryPoint]: ...

# Infrastructure implements the Protocol
class AWSBackupRepository:
    """Concrete AWS implementation."""
    def list_vaults(self, region: str) -> list[Vault]:
        # boto3 calls here
        ...
```

---

## Directory Structure

```
<project_name>/
├── .python-version          # pyenv version (3.12)
├── .gitignore               # Python gitignore
├── .claude/
│   └── settings.json        # AI permissions
├── LICENSE                  # MIT
├── Pipfile                  # Virtual env management (pipenv)
├── pyproject.toml           # Package config + ALL tool configs
├── README.md
├── BACKLOG.md               # Story tracking
├── CHANGELOG.md             # Release history
├── CONTRIBUTING.md          # Development workflow
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
│           ├── __init__.py
│           ├── config.py        # Configuration management
│           ├── logger.py        # Logging setup
│           └── retry.py         # Retry decorator (if needed)
└── tests/
    ├── conftest.py              # Shared pytest fixtures
    ├── unit/
    │   ├── domain/
    │   └── application/
    └── integration/
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
- Use type hints everywhere (mypy strict mode)
- Use `snake_case` for functions and variables
- Use `PascalCase` for classes
- Use `UPPER_CASE` for constants
- Use modern Python 3.12+ syntax (`list[T]` not `List[T]`, `X | Y` not `Union[X, Y]`)

### File-Level Metadata

Every `.py` file must have:

```python
#!/usr/bin/env python3
"""Module description here."""

__version__ = "0.1.0"
__author__ = "John Ayers"


def file_info() -> dict[str, str]:
    return {
        "name": "module_name",
        "description": "Module description",
        "version": __version__,
        "author": __author__,
        "last_updated": "YYYY-MM-DD",
    }
```

### CLI Design

- Use standard library `argparse`
- Entry point via `[project.scripts]` in pyproject.toml
- Include `--version` and `--help` flags
- Use `--dry-run` for destructive operations
- Use `-v/--verbose` for debug output
- Support `--output text|json` for scriptable output

**Subcommand Pattern:**

```python
def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="CLI description")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable debug output")
    parser.add_argument("--dry-run", action="store_true", help="Preview without changes")
    parser.add_argument("--output", choices=["text", "json"], default="text")

    subparsers = parser.add_subparsers(dest="command", required=True)

    # Add subcommands
    list_parser = subparsers.add_parser("list", help="List items")
    list_parser.add_argument("--filter", help="Filter pattern")

    return parser

def main() -> NoReturn:
    parser = create_parser()
    args = parser.parse_args()

    commands = {
        "list": cmd_list,
        "copy": cmd_copy,
    }

    exit_code = commands[args.command](args)
    sys.exit(exit_code)
```

**Exit Codes:**

| Code | Meaning |
|------|---------|
| 0 | Success |
| 1 | Error (validation, API failure, etc.) |
| 2 | Incomplete (timeout, partial completion) |

### Cloud Operations

- Never hardcode credentials
- Use environment variables or cloud-native auth
- Operations should be idempotent when possible
- Use structured logging with clear levels

---

## pyproject.toml Template

This is the single source of truth for package metadata and all tool configurations:

```toml
[build-system]
requires = ["setuptools>=68.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "<project-name>"  # kebab-case for PyPI
version = "0.1.0"
description = "<description>"
authors = [{name = "John Ayers"}]
readme = "README.md"
requires-python = ">=3.12"
license = {text = "MIT"}
classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.12",
]

dependencies = [
    # Add runtime dependencies here
    # "boto3~=1.35",
]

[project.optional-dependencies]
dev = [
    "pytest~=8.3",
    "pytest-cov~=6.0",
    "pytest-mock~=3.14",
    "black~=24.10",
    "ruff~=0.7",
    "mypy~=1.13",
    # Add type stubs as needed:
    # "boto3-stubs[backup]~=1.35",
]

[project.scripts]
<cli-name> = "<package_name>.cli:main"

[tool.setuptools.packages.find]
where = ["src"]

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = "--cov=src/<package_name> --cov-report=term-missing --cov-report=html"

[tool.black]
line-length = 100
target-version = ["py312"]

[tool.ruff]
line-length = 100
target-version = "py312"

[tool.ruff.lint]
select = ["E", "F", "I", "N", "W", "UP"]
ignore = []

[tool.mypy]
python_version = "3.12"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
```

---

## Infrastructure Utilities (Reference Patterns)

For complex CLIs, copy and adapt these patterns from the reference implementation:

| Utility | File | Purpose |
|---------|------|---------|
| Retry decorator | `shuffle-aws-vaults/infrastructure/retry.py` | Exponential backoff for transient errors |
| Logger setup | `shuffle-aws-vaults/infrastructure/logger.py` | Structured logging with verbose mode |
| Signal handler | `shuffle-aws-vaults/infrastructure/signal_handler.py` | Graceful shutdown on SIGINT/SIGTERM |
| State persistence | `shuffle-aws-vaults/infrastructure/state_repository.py` | JSON-based resume capability |
| Progress tracker | `shuffle-aws-vaults/infrastructure/progress_tracker.py` | Real-time progress with ETA |

**Reference:** `~/code/shuffle-aws-vaults/src/shuffle_aws_vaults/infrastructure/`

---

## Testing Strategy

### pytest Configuration

Already configured in pyproject.toml. Use fixtures in `tests/conftest.py`:

```python
import pytest
from <package_name>.domain.vault import Vault

@pytest.fixture
def sample_vault() -> Vault:
    """Shared fixture for vault domain object."""
    return Vault(name="test-vault", arn="arn:aws:backup:us-east-1:123456789012:vault:test-vault")

@pytest.fixture
def empty_vault() -> Vault:
    """Vault with no recovery points."""
    return Vault(name="empty-vault", arn="arn:aws:backup:us-east-1:123456789012:vault:empty")
```

### Test Organization

```
tests/
├── conftest.py              # Shared fixtures
├── unit/
│   ├── domain/              # Pure domain logic tests (no mocks needed)
│   │   └── test_vault.py
│   ├── application/         # Service tests (mock repositories)
│   │   └── test_list_service.py
│   └── test_cli.py          # Parser tests (not command execution)
└── integration/             # Tests with real infrastructure (mocked AWS)
    └── test_aws_repository.py
```

### CLI Parser Testing

Test the parser separately from command execution:

```python
def test_list_command_accepts_filter():
    parser = create_parser()
    args = parser.parse_args(["list", "--filter", "prod"])
    assert args.command == "list"
    assert args.filter == "prod"

def test_invalid_output_format_rejected():
    parser = create_parser()
    with pytest.raises(SystemExit):
        parser.parse_args(["list", "--output", "invalid"])
```

### Protocol-Based Mocking

Mock at the Protocol boundary, not internal implementations:

```python
def test_list_service_returns_vaults(sample_vault):
    # Mock repository implements Protocol
    mock_repo = Mock()
    mock_repo.list_vaults.return_value = [sample_vault]

    service = ListService(repository=mock_repo)
    result = service.execute(region="us-east-1")

    assert len(result) == 1
    mock_repo.list_vaults.assert_called_once_with("us-east-1")
```

---

## Code Quality Checks

All tools are configured in pyproject.toml. Run before every commit:

```bash
# Format code
pipenv run black .

# Lint (auto-fix)
pipenv run ruff check --fix .

# Type check
pipenv run mypy src/

# Run tests with coverage
pipenv run pytest
```

**Tool Configuration Summary:**

| Tool | Purpose | Key Settings |
|------|---------|--------------|
| black | Formatting | line-length=100, py312 |
| ruff | Linting | E, F, I, N, W, UP rules |
| mypy | Type checking | strict mode, disallow_untyped_defs |
| pytest | Testing | coverage to term + HTML |

---

## Initial Files to Generate

When scaffolding, create these files:

1. **README.md** - Project description, setup, usage
2. **CLAUDE.md** - AI team agreement and project context (from `CLAUDE.md.template`)
3. **LICENSE** - MIT license
4. **.python-version** - `3.12` (or latest)
5. **.gitignore** - Python gitignore (from GitHub template)
6. **Pipfile** - Virtual env with dev dependencies
7. **pyproject.toml** - Package config + all tool configs (see template above)
8. **BACKLOG.md** - Copy from `docs/templates/backlog.md`
9. **CHANGELOG.md** - Empty changelog template
10. **CONTRIBUTING.md** - Development workflow
11. **docs/requirements.md** - Copy from `docs/templates/requirements.md`
12. **src/<name>/__init__.py** - Package init with `__version__`
13. **src/<name>/cli.py** - Entry point with argparse (subcommand pattern)
14. **src/<name>/domain/__init__.py** - Domain layer
15. **src/<name>/application/__init__.py** - Application layer
16. **src/<name>/infrastructure/__init__.py** - Infrastructure layer
17. **src/<name>/infrastructure/logger.py** - Logging setup
18. **tests/conftest.py** - Pytest fixtures
19. **tests/unit/test_cli.py** - Parser tests (TDD)
20. **.claude/settings.json** - AI permissions

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

**Creating a Branch and PR:**

```bash
# Create branch for story
git checkout -b feature/STORY-X-description

# ... make changes, commit ...

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

**Poll for Copilot Review (every 30 seconds):**

```bash
# Wait for Copilot review to complete
PR_NUM=$(gh pr view --json number -q '.number')
echo "Waiting for Copilot review on PR #$PR_NUM..."

while true; do
  REVIEWS=$(gh api repos/:owner/:repo/pulls/$PR_NUM/reviews 2>/dev/null)
  if echo "$REVIEWS" | grep -q "copilot\|github-actions"; then
    echo "Copilot review found!"
    break
  fi
  echo "Still waiting... (checking again in 30 seconds)"
  sleep 30
done

# View the comments
gh pr view --comments
```

**After Copilot Reviews:**

```bash
# View PR and comments
gh pr view --comments

# Or open in browser
gh pr view --web
```

**Claude addresses Copilot comments, then Human approves and merges.**

**After Merge - Create Release:**

```bash
# Pull merged changes
git checkout main && git pull

# Determine version bump (based on commit types)
# fix: → PATCH, feat: → MINOR, breaking → MAJOR

# Create release
gh release create vX.Y.Z --generate-notes
```

---

## Environment Setup

### pipenv Configuration

Set this environment variable to keep the virtual environment inside the project directory (recommended):

```bash
# Add to ~/.zshrc or ~/.bashrc
export PIPENV_VENV_IN_PROJECT=1
```

This creates `.venv/` in the project root instead of `~/.local/share/virtualenvs/`.

### Global CLI Access

To run the CLI like a compiled utility from any directory:

**Option 1: Shell Alias (Recommended for Development)**

```bash
# Add to ~/.zshrc or ~/.bashrc
alias <cli-name>='PIPENV_PIPFILE=~/code/<project_name>/Pipfile pipenv run <cli-name>'
```

This runs the CLI from anywhere without changing directories.

**Option 2: pipx (For Distribution)**

```bash
# Install pipx if needed
brew install pipx
pipx ensurepath

# Install from local source (editable)
pipx install -e /path/to/<project_name>

# Now available globally
<cli-name> --help
```

**Option 3: Activate virtualenv**

```bash
cd <project_name>
pipenv shell
<cli-name> --help
exit  # to deactivate
```

---

## Post-Scaffold Commands

After creating files:

```bash
cd <project_name>

# Install dependencies and package in editable mode
pipenv install --dev
pipenv install -e .

# Verify setup
pipenv run pytest tests/ -v          # Run tests
pipenv run black --check .           # Check formatting
pipenv run ruff check .              # Check linting
pipenv run mypy src/                 # Check types

# Run the CLI
pipenv run <cli-name> --help
pipenv run <cli-name> --version
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
