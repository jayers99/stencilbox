# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with this repository.

Last verified: 2025-12-10

## Repository Purpose

**Stencilbox** is a template repository for AI-assisted creation across multiple domains: code, images, writing, and learning. It contains process guides, document templates, prompts, and scaffolds—not code to execute.

## How This Repository Is Used

Users point Claude Code to files in this repo from their actual project:

```
"Read ~/code/stencilbox/code/discovery/PROCESS.md and help me brainstorm"
"Read ~/code/stencilbox/code/bootstrap/PROCESS.md and create a Python CLI project"
```

**Important:** Output files (brainstorm.md, requirements.md, etc.) should be created in the user's working directory, NOT in this templates folder.

## Structure

```
stencilbox/
├── code/           # Software development templates
├── images/         # Image generation prompts & workflows
├── writing/        # Fiction, nonfiction, copywriting
├── learning/       # Programming skill development
├── projects/       # Active project-specific stencils
└── shared/         # Cross-domain personas & workflows
```

## Key Files by Domain

### Code (`code/`)

| File | Purpose |
|------|---------|
| `code/Coding_Human_AI_Team_Agreement.md` | Core workflow for AI-assisted development |
| `code/discovery/PROCESS.md` | Brainstorming and idea validation |
| `code/bootstrap/PROCESS.md` | Project setup guide |
| `code/bootstrap/project-types/python-cli/SCAFFOLD.md` | Python CLI project template |
| `code/bootstrap/project-types/python-cli/CLAUDE.md.template` | CLAUDE.md template for new projects |
| `code/docs/PROCESS.md` | Requirements and design docs |
| `code/docs/templates/` | Templates for requirements, design, ADR, backlog |

### Images (`images/`)

| File | Purpose |
|------|---------|
| `images/Image_Human_AI_Team_Agreement.md` | Workflow for image generation |

### Writing (`writing/`)

| File | Purpose |
|------|---------|
| `writing/Writing_Human_AI_Team_Agreement.md` | Workflow for writing projects |

### Learning (`learning/`)

| File | Purpose |
|------|---------|
| `learning/Learning_Human_AI_Team_Agreement.md` | Workflow for skill development |

## Code Development Conventions

For projects created from `code/` templates:

- **TDD always**: Red-Green-Refactor cycle
- **Trunk-based development**: Short-lived feature branches, squash merge to main
- **Commit format**: `<type>: <description>` (feat/fix/test/refactor/docs/chore)
- **Branch naming**: `feature/STORY-N-description` or `bugfix/BUG-N-description`
- **WIP limit**: One story in progress at a time

## PR Process (Code Projects)

1. Claude creates branch (`feature/STORY-N-desc` or `bugfix/BUG-N-desc`)
2. Claude creates PR with UAT instructions
3. GitHub Copilot auto-reviews
4. Claude polls GitHub every 30 seconds until review completes
5. Claude addresses Copilot comments
6. Human runs UAT and approves
7. Squash merge, delete branch
8. Claude creates semver release

## Working on Stencilbox Itself

When modifying this repository (not using it as a template):

- Update this CLAUDE.md if you change directory structure
- Verify file paths in tables are accurate
- Update "Last verified" date after review
