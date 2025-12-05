# Python CLI Project Scaffolding - Guard Rails Prompt

Use this prompt with Claude Code to scaffold a new Python CLI project following Modern Software Engineering, TDD, and DDD principles.

---

You are my AI pair programmer and scaffolding assistant.

I am creating a new Python command-line project. Follow these guard rails:

1) Modern Software Engineering (Dave Farley)
- Optimize for fast, frequent, low-risk changes.
- Always keep the codebase releasable (trunk-based).
- Prefer clear, simple, composable design; avoid premature abstractions.
- Automate everything repeatable: tests, linting, formatting, packaging, release steps.

2) Test-Driven Development (TDD)
- Tests come first, then minimal implementation, then refactor.
- Use pytest.
- Keep tests fast and deterministic; use fakes instead of real cloud calls.
- Mirror the src layout inside tests/.

3) Lightweight Domain-Driven Design (DDD)
- Organize the system into three layers:
  - Domain: pure logic, deterministic, no SDK dependencies.
  - Application: orchestrates use cases and workflows.
  - Infrastructure: AWS/GCP calls, configuration, logging, I/O.
- Domain objects should be small, explicit dataclasses with behavior.
- Use interfaces/protocols for cloud operations to keep the domain independent.
- Cloud adapters are replaceable; domain tests use fakes/mocks.
- Keep the Ubiquitous Language small, consistent, and evolving.

4) Runtime & dependency management
- Python version managed via pyenv (provide a recommended version and .python-version).
- Virtualenv and packages managed via pipenv (provide an initial Pipfile).
- Keep dependencies minimal and justified.

5) Project layout & CLI-first design
- Proposed structure:
  /README.md
  /.python-version
  /Pipfile
  /src/<project_name>/__init__.py
  /src/<project_name>/cli.py
  /src/<project_name>/domain/
  /src/<project_name>/application/
  /src/<project_name>/infrastructure/
  /tests/unit/...
  /tests/integration/...
  /scripts/
- CLI must use standard library argparse unless there is a strong reason otherwise.
- Modules must:
  - Work as importable modules AND standalone executables.
  - Start with "#!/usr/bin/env python3"
  - Include a main() function and an if __name__ == "__main__": main() block.

6) File-level metadata (every .py file)
- A short module docstring describing the file's responsibility.
- __version__ = "0.1.0"  (semver)
- A file_info() function returning:
  - name
  - description
  - version
  - author (default "John Ayers")
  - last_updated (placeholder string)

7) Trunk-based solo development
- Assume I work alone.
- Work in tiny vertical slices that always leave trunk releasable.
- Keep PR-sized increments: tests + implementation + refactor + doc update.
- Avoid speculative features.

8) Cloud-focused tooling (AWS/GCP)
- Prefer official SDKs: boto3/botocore and google-cloud-*.
- Operations must be:
  - Idempotent when possible
  - Safe by default (use --dry-run options)
  - Logged with clear levels and human-readable messages
- Never hardcode credentials.
- Use environment variables or cloud-native auth (IMDS, GCP metadata server).
- Separate cloud logic into infrastructure layer.

When I describe the specific project, respond with:

A) A clear restatement of the project and key workflows (CLI commands/subcommands).
B) A proposed repo structure based on these guard rails.
C) Concrete file scaffolding:
   - README.md (first draft)
   - .python-version
   - Pipfile (initial)
   - cli.py with argparse, version flag, and a placeholder command
   - One domain module with metadata template
   - One application module
   - One infrastructure placeholder module
D) Initial unit tests using TDD (version command + domain placeholder).
E) A first set of trunk-based development slices.

Project details to use:

Project name (package-safe): <PROJECT_NAME>
Short description: <ONE_OR_TWO_SENTENCES>
Primary cloud provider(s): <AWS / GCP / BOTH>
High-level tasks / goals: <LIST>

---

## Usage Instructions

1. Copy this prompt into Claude Code
2. Fill in the project details at the bottom:
   - PROJECT_NAME (e.g., `my_cli_tool`)
   - Short description
   - Cloud provider(s)
   - High-level tasks/goals
3. Claude will scaffold the entire project with:
   - Complete DDD architecture
   - Comprehensive tests (TDD)
   - All configuration files
   - Development roadmap in slices

## What You Get

- ✅ Full project structure following DDD
- ✅ pytest test suite with 40+ tests
- ✅ CLI with argparse
- ✅ pyproject.toml for package installation
- ✅ All dependencies configured (pipenv)
- ✅ README with usage examples
- ✅ Trunk-based development roadmap

## Example Project Details

```
Project name (package-safe): aws_backup_migrator
Short description: CLI tool to migrate AWS Backup recovery points between accounts
Primary cloud provider(s): AWS
High-level tasks / goals:
- List backup vaults and recovery points across regions
- Copy recovery points to destination account
- Verify successful migration
- Track progress for large batches
```

## Follow-up Commands

After scaffolding:
1. `pipenv install --dev` - Install dependencies
2. `pipenv install -e .` - Install package in editable mode
3. `pipenv run pytest tests/ -v` - Run tests
4. Follow the development slices for feature implementation

---

Last used: 2025-12-04
Template version: 1.0
