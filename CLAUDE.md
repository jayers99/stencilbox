# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with this repository.

Last verified: 2025-12-13

## Repository Purpose

**Stencilbox** is a template repository for AI-assisted creation across multiple domains: code, images, writing, and learning. It contains process guides, document templates, prompts, and scaffolds—not code to execute.

## How This Repository Is Used

Users point Claude Code to files in this repo from their actual project:

```
"Read ~/icloud/stencilbox/home/code/discovery/PROCESS.md and help me brainstorm"
"Read ~/icloud/stencilbox/home/code/bootstrap/PROCESS.md and create a Python CLI project"
```

**Important:** Output files (brainstorm.md, requirements.md, etc.) should be created in the user's working directory, NOT in this templates folder.

## Structure (Inheritance Model)

```
stencilbox/
├── shared/                 # TRUNK - universal foundations
│   ├── agreements/             # Base human-AI team agreement
│   ├── conventions/            # File naming, commit messages
│   ├── frameworks/             # Tone guide, interview questions
│   ├── personas/               # AI personalities
│   ├── assets/                 # Images, banners
│   └── code/                   # Shared code templates
│       └── templates/
│           └── docs/           # Base doc templates (ADR, design, etc.)
├── home/                   # BRANCH - personal/creative work
│   ├── code/                   # Software development templates
│   ├── images/                 # Image generation prompts
│   ├── writing/                # Fiction, nonfiction, copywriting
│   └── learning/               # Programming skill development
└── work/                   # BRANCH - regulated environment
    ├── code/                   # Work-adapted engineering docs
    └── project-planning/       # SOD workflow and prompts
```

## Key Files

### Shared (Trunk)

| File | Purpose |
|------|---------|
| `shared/agreements/human-ai-team-agreement.md` | Base collaboration agreement - all domains inherit from this |
| `shared/conventions/file-naming.md` | Naming standards (kebab-case for docs, snake_case for Python) |
| `shared/frameworks/tone-guide.md` | Writing tones for AI-seeded content |
| `shared/frameworks/interview-questions.md` | Techniques for gathering material |
| `shared/code/templates/docs/` | Base document templates (ADR, design, requirements, backlog) |

### Home (Personal)

| File | Purpose |
|------|---------|
| `home/code/coding-human-ai-team-agreement.md` | Code workflow (TDD, git, PRs) - extends base |
| `home/code/discovery/PROCESS.md` | Brainstorming and idea validation |
| `home/code/discovery/examples/` | Example discovery outputs (reference only) |
| `home/code/bootstrap/PROCESS.md` | Project setup guide |
| `home/code/docs/templates/` | Document templates with home-specific guidance |
| `home/writing/writing-human-ai-team-agreement.md` | Writing workflow - extends base |
| `home/images/image-human-ai-team-agreement.md` | Image generation workflow - extends base |
| `home/learning/learning-human-ai-team-agreement.md` | Learning workflow - extends base |

### Work (Regulated Environment)

| File | Purpose |
|------|---------|
| `work/code/work-environment.md` | JPMC constraints and approved tools |
| `work/code/discovery/PROCESS.md` | Discovery process with work constraints - extends home version |
| `work/code/bootstrap/PROCESS.md` | Bootstrap process with compliance requirements - extends home version |
| `work/code/docs/PROCESS.md` | Documentation process with compliance - extends home version |
| `work/code/docs/templates/` | Document templates with work-specific requirements |
| `work/project-planning/QUICKSTART.md` | SOD workflow quick start |

## Inheritance Model

Domain-specific agreements extend the base:

```
shared/agreements/human-ai-team-agreement.md (BASE)
    ├── home/code/coding-human-ai-team-agreement.md
    ├── home/writing/writing-human-ai-team-agreement.md
    ├── home/images/image-human-ai-team-agreement.md
    └── home/learning/learning-human-ai-team-agreement.md
```

**Each domain file includes:** "Inherits from: [base]" header. Read the base first, then the domain-specific additions.

### Template Inheritance

Document templates also follow an inheritance model:

```
shared/code/templates/docs/ (BASE TEMPLATES)
    ├── adr.md, backlog.md, design.md, requirements.md
    ├── home/code/docs/templates/ (home-specific guidance)
    │   └── Reference shared templates with personal project adaptations
    └── work/code/docs/templates/ (work-specific requirements)
        └── Reference shared templates with compliance additions
```

Process guides (PROCESS.md) in work/code reference their home/code counterparts and add work-specific constraints.

## Code Development Conventions

For projects created from `home/code/` templates:

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

## Common Tasks

```
# Start a new project idea
"Read ~/icloud/stencilbox/home/code/discovery/PROCESS.md and help me brainstorm"

# Bootstrap a Python CLI project
"Read ~/icloud/stencilbox/home/code/bootstrap/PROCESS.md and create a Python CLI project"

# Create requirements for a project
"Read ~/icloud/stencilbox/home/code/docs/PROCESS.md and help me create requirements"

# Get back up to speed on the workflow
"Read ~/icloud/stencilbox/shared/agreements/human-ai-team-agreement.md first,
 then ~/icloud/stencilbox/home/code/coding-human-ai-team-agreement.md"
```

## Working on Stencilbox Itself

When modifying this repository (not using it as a template):

- Update this CLAUDE.md if you change directory structure
- Verify file paths in tables are accurate
- Follow the inheritance model: generic → shared → domain
- Update "Last verified" date after review
