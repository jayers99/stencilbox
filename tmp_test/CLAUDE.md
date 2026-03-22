# CLAUDE.md

This file provides guidance to Claude Code when working with this codebase.

## Project Overview

**Name:** my_test_tool
**CLI:** my-test-tool
**Description:** A test CLI tool

## Commands

```bash
# Install
pipenv install --dev && pipenv install -e .

# Test
pipenv run pytest

# Format & Lint
pipenv run black . && pipenv run ruff check . && pipenv run mypy src/

# Run CLI
pipenv run my-test-tool --help
```

## Architecture

Domain-Driven Design (DDD) with three layers:

```
src/my_test_tool/
├── cli.py              # Entry point (argparse)
├── domain/             # Pure business logic
├── application/        # Use cases (Protocol-based)
└── infrastructure/     # External integrations
```

## Development Practices

- **TDD**: Red-Green-Refactor always
- **Commits**: `<type>: <description>` (feat/fix/test/refactor/docs/chore)
- **Branches**: `feature/STORY-N-desc` or `bugfix/BUG-N-desc`

## Key Files

| File | Purpose |
|------|---------|
| BACKLOG.md | Current stories and tasks |
| CHANGELOG.md | Release history |
