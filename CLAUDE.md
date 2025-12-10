# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a **template repository** for AI-assisted solo development workflows. It contains process guides, document templates, and scaffolds—not code to execute. When users reference files here, they're typically working in a different project directory and using these as external templates.

## How This Repository Is Used

Users point Claude Code to files in this repo from their actual project:
- `"Read discovery/PROCESS.md and help me brainstorm"` - Start a new project idea
- `"Read bootstrap/PROCESS.md and create a Python CLI project"` - Scaffold a new project
- `"Read docs/PROCESS.md and help me create requirements"` - Create documentation

**Important:** Output files (brainstorm.md, requirements.md, etc.) should be created in the user's working directory, not in this templates folder.

## Key Files

| File | Purpose |
|------|---------|
| `Human_AI_Team_Agreement.md` | Core workflow document covering all development phases |
| `discovery/PROCESS.md` | Guide for brainstorming and validating ideas |
| `bootstrap/PROCESS.md` | Guide for setting up new projects |
| `docs/PROCESS.md` | Guide for creating requirements and design docs |
| `bootstrap/project-types/python-cli/SCAFFOLD.md` | Python CLI project template |

## Workflow Phases

1. **Discovery** (`discovery/`) - Brainstorm, problem statement, validation, MVP scoping
2. **Bootstrap** (`bootstrap/`) - Project setup, repo creation, environment config
3. **Documentation** (`docs/templates/`) - Requirements, design docs, ADRs, backlog

## Development Conventions (for projects created from these templates)

- **TDD always**: Red-Green-Refactor cycle, never write implementation without tests
- **Trunk-based development**: Short-lived feature branches, squash merge to main
- **Commit format**: `<type>: <description>` where type is feat/fix/test/refactor/docs/chore
- **Branch naming**: `feature/STORY-N-description` or `bugfix/BUG-N-description`
- **One story in progress** at a time (WIP limit of 1)

## Python CLI Projects (from SCAFFOLD.md)

Architecture follows DDD with three layers:
- `domain/` - Pure business logic, no external dependencies
- `application/` - Use cases and orchestration
- `infrastructure/` - Cloud SDKs, I/O, configuration

Every Python file should include docstring and `file_info()` function with version metadata.

## PR Process

1. Claude creates branch for story (`feature/STORY-N-desc`) or bugfix (`bugfix/BUG-N-desc`)
2. Claude Code creates PR with UAT instructions
3. GitHub Copilot auto-reviews
4. Claude polls GitHub every 30 seconds until Copilot review completes
5. Claude addresses Copilot comments
6. Human runs UAT and approves
7. Squash merge, delete branch
8. Claude creates semver release (PATCH for fixes, MINOR for features, MAJOR for breaking changes)
