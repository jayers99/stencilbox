# Development Templates

A complete AI-assisted development workflow for solo developers working with Claude Code.

## Quick Start

### Starting a New Project

**Step 1: Discovery (brainstorm your idea)**

```
Read discovery/PROCESS.md and help me brainstorm a new project idea.
```

This guides you through:
- Brain dump and idea capture
- Problem statement definition
- Validation (5 Whys, pre-mortem)
- MVP scoping

**Step 2: Bootstrap (set up the project)**

```
Read bootstrap/PROCESS.md and help me create a new project.
```

This guides you through:
- Selecting a project type
- Creating repository structure
- Setting up environment
- Configuring AI permissions

**Step 3: Requirements & Design**

```
Read docs/PROCESS.md and help me create requirements for this project.
```

Use templates in `docs/templates/` for:
- Requirements documentation
- Design documents
- Architecture Decision Records (ADRs)

### Returning to an Existing Project

```
Read Human_AI_Team_Agreement.md and help me get back up to speed.
Summarize the project status and what we should work on.
```

### Day-to-Day Development

```
Read Human_AI_Team_Agreement.md. Let's work on [feature/bug/task].
```

## Directory Structure

```
templates/
├── Human_AI_Team_Agreement.md   # Core workflow document
├── discovery/                    # Phase 1: Idea exploration
│   ├── PROCESS.md               # AI reads this first
│   ├── brainstorm.md            # Raw ideas
│   ├── problem_statement.md     # Problem definition
│   ├── validation.md            # Risk analysis
│   └── mvp_scope.md             # MVP boundaries
├── bootstrap/                    # Phase 2: Project setup
│   ├── PROCESS.md               # AI reads this first
│   └── project-types/
│       └── python-cli/
│           └── SCAFFOLD.md      # Python CLI project template
├── docs/                         # Phase 3: Documentation
│   ├── PROCESS.md               # AI reads this first
│   └── templates/
│       ├── requirements.md      # Requirements template
│       ├── design.md            # Design doc template
│       └── adr.md               # ADR template
└── README.md                     # This file
```

## The Human-AI Team Agreement

The core of this workflow is [Human_AI_Team_Agreement.md](Human_AI_Team_Agreement.md), which covers:

| Section | Purpose |
|---------|---------|
| 1. Discovery & Brainstorming | How to explore and validate ideas |
| 2. Project Bootstrap | Setting up new projects |
| 3. Requirements & Design | Documentation standards |
| 4. Story & Ticket Creation | Breaking work into stories |
| 5. Communication Protocols | How Human and AI communicate |
| 6. Development | TDD, commits, branches, code style |
| 7. Testing | Unit, integration, UAT |
| 8. Code Review & PR Process | PR creation, review, merge |
| 9. Release & Deployment | Versioning, changelog, releases |
| 10. Documentation Updates | Keeping docs in sync |
| 11. Maintenance & Future Work | Returning to projects, bug fixes |
| 12. Open Questions | Workflow improvements |

## Key Commands

| Action | Prompt |
|--------|--------|
| Enter Plan Mode | `Shift+Tab` or `claude --permission-mode plan` |
| New project | *"Read discovery/PROCESS.md and help me brainstorm"* |
| Bootstrap project | *"Read bootstrap/PROCESS.md and create a Python CLI project"* |
| Start session | *"Read Human_AI_Team_Agreement.md. What should we work on?"* |
| Create PR | *"Create a PR with summary of changes"* |
| Prepare release | *"Prepare release v1.2.0"* |
| Health check | *"Run a health check on this project"* |

## Project Types

Currently available:

| Type | Location | Description |
|------|----------|-------------|
| Python CLI | `bootstrap/project-types/python-cli/` | CLI with DDD, TDD, pytest |

*More coming: TypeScript API, React app, etc.*

## Philosophy

This workflow is built on:

- **First principles** for each phase
- **Popular methodologies** (TDD, trunk-based dev, SemVer)
- **Claude Code tips** for optimal AI collaboration
- **Templates** to reduce boilerplate
- **Checklists** to ensure quality

The goal: Make AI-assisted development predictable, repeatable, and high-quality.

## License

Private repository for personal use.
