![Stencilbox banner](shared/assets/StencilBoxBanner.jpg)

Templates, prompts, and workflows for AI-assisted creation - code, images, and writing.

## Structure

```
stencilbox/
├── shared/             # TRUNK - universal foundations
│   ├── agreements/         # Base human-AI team agreement
│   ├── conventions/        # File naming, commit messages
│   ├── frameworks/         # Tone guide, interview questions
│   ├── personas/           # AI personalities
│   ├── assets/             # Images, banners
│   └── code/
│       └── templates/      # Base document templates
├── home/               # BRANCH - personal/creative work
│   ├── code/               # Software development templates
│   ├── images/             # Image generation prompts
│   ├── writing/            # Fiction, nonfiction, copywriting
│   └── learning/           # Programming skill development
├── work/               # BRANCH - regulated environment
│   ├── code/               # Work-adapted engineering docs
│   └── project-planning/   # SOD workflow and prompts
└── CHANGELOG.md
```

## Quick Start

### Code Projects (Home)

```
Read code/discovery/PROCESS.md and help me brainstorm a new project.
Read code/bootstrap/PROCESS.md and create a Python CLI project.
Read code/coding-human-ai-team-agreement.md and help me get started.
```

See [home/code/README.md](home/code/README.md) for full development workflow.

### Work (Regulated Environment)

Start with:
- `work/code/README.md` for overview and constraints
- `work/code/work-environment.md` to document approvals and policies
- `work/project-planning/README.md` for the AI-assisted SOD and story workflow

Quick commands:
- Add notes: use `work/project-planning/snippets/sod.code-snippets` (`sodnotes`)
- View/lock SOD: `showsod` / `locksod`
- Generate stories: `sodstories`

### Image Generation

| Tool | Location |
|------|----------|
| DALL-E / ChatGPT | `home/images/prompts/dalle/` |
| Midjourney | `home/images/prompts/midjourney/` |
| Gemini / Nano Banana | `home/images/prompts/gemini/` |
| Style references | `home/images/styles/` |
| Multi-step workflows | `home/images/workflows/` |

### Writing

| Type | Location |
|------|----------|
| Fiction | `home/writing/fiction/` |
| Nonfiction | `home/writing/nonfiction/` |
| Prompts | `home/writing/prompts/` |

### Learning

Track programming skill development:

| Folder | Purpose |
|--------|---------|
| `home/learning/problem-solving/` | Algorithms, debugging, thinking frameworks |
| `home/learning/fundamentals/` | CS concepts, design patterns |
| `home/learning/journal/` | Progress tracking, reflections |

## Active Projects

| Project | Description |
|---------|-------------|
| [bowerbird](https://github.com/jayers99/bowerbird) | Photo collection to illustration generator |
| [pebble](https://github.com/jayers99/pebble) | Scrum standup helper |
| Work planning | See `work/project-planning/` for SOD and story workflow |

## Shared Resources (Trunk)

| Resource | Location | Purpose |
|----------|----------|---------|
| Base Agreement | `shared/agreements/human-ai-team-agreement.md` | Universal collaboration principles |
| Code Templates | `shared/code/templates/docs/` | Base document templates (ADR, design, requirements, backlog) |
| Tone Guide | `shared/frameworks/tone-guide.md` | Writing tones for AI-seeded content |
| Interview Questions | `shared/frameworks/interview-questions.md` | Techniques for gathering material |
| File Naming | `shared/conventions/file-naming.md` | Naming standards |
| Personas | `shared/personas/` | AI personalities for different tasks |

## Inheritance Model

Domain-specific agreements extend the base:

```
shared/agreements/human-ai-team-agreement.md (BASE)
    ├── home/code/coding-human-ai-team-agreement.md
    ├── home/writing/writing-human-ai-team-agreement.md
    ├── home/images/image-human-ai-team-agreement.md
    ├── home/learning/learning-human-ai-team-agreement.md
    └── work/code/coding-human-ai-team-agreement.md
```

Document templates also follow inheritance:

```
shared/code/templates/docs/ (BASE TEMPLATES)
    ├── home/code/docs/templates/ (home-specific guidance)
    └── work/code/docs/templates/ (work-specific requirements)
```

Process guides in work/code extend their home/code counterparts with compliance requirements.

## Philosophy

Stencils, not scaffolds. These are patterns to trace, not structures to fill. Use them as starting points, adapt freely, discard what doesn't fit.
