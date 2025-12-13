# Shared Code Templates

Base templates for code documentation across all domains (home and work).

## Purpose

These templates provide the foundational structure for code project documentation. Domain-specific directories (home/code, work/code) extend these base templates with their own constraints and additions.

## Templates

| Template | Purpose |
|----------|---------|
| `docs/adr.md` | Architectural Decision Record - documents significant technical decisions |
| `docs/backlog.md` | Backlog structure - tracks stories, tasks, and work in progress |
| `docs/design.md` | Design document - describes feature architecture and approach |
| `docs/requirements.md` | Requirements specification - defines what needs to be built |

## Usage

These templates are referenced by:
- `home/code/docs/templates/` - Personal project variants with lightweight processes
- `work/code/docs/templates/` - Work-safe variants with compliance requirements

Domain-specific templates include:
1. Reference to this shared base template
2. Domain-specific notes and requirements
3. Additional sections required for that context

## Inheritance Model

```
shared/code/templates/docs/[template].md (BASE)
    ├── home/code/docs/templates/[template].md (home-specific additions)
    └── work/code/docs/templates/[template].md (work-specific additions)
```

## Editing Guidelines

When modifying these base templates:
1. Keep them domain-neutral and broadly applicable
2. Focus on structure and core content areas
3. Avoid domain-specific terminology or constraints
4. Update both home and work variants if structure changes significantly
5. Document the change in CHANGELOG.md
