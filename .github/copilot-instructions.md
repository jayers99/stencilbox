# GitHub Copilot Instructions

## Overview
- Treat this repository as a knowledge base of templates, prompts, and workflows rather than an executable project; all output files (requirements, ADRs, code) must land in the user's current working directory, not inside `stencilbox` (see `CLAUDE.md`).
- The structure follows a trunk-with-branches model: `shared/` holds the universal agreements, conventions, and templates; `home/` is the creative/personal branch; `work/` layers compliance and JPMC-specific constraints on top of the home templates (see both `README.md` and `CLAUDE.md` for the diagram and explanations).

## Home Code Flow (Personal Projects)
- Start every new idea by reading `home/code/discovery/PROCESS.md`; it walks through idea capture, problem statements, validation (brainstorm.md, problem_statement.md, validation.md, MVP scoping) before touching code.
- Once a direction exists, run through `home/code/bootstrap/PROCESS.md` and the relevant `bootstrap/project-types/*/SCAFFOLD.md` (Python CLI is currently the canonical option) to generate the repo structure, dependency strategy, and tooling (README, Makefile/justfile, env setup).
- Close the loop with `home/code/docs/PROCESS.md` plus the templates under `home/code/docs/templates/` for requirements, design docs, and ADRs; include semver versions and keep the living requirements doc updated (the Human-AI Team Agreement lays out the Definition of Done checklist).
- Refer to `home/code/README.md` for the full workflow and the agile rhythm (brainstorm → bootstrap → docs → stories/tests). Use `Plan Mode` (Shift+Tab or `claude --permission-mode plan`) during early conversations.

## Work Flow (Regulated Projects)
- For any regulated work, read `work/code/README.md` first so you know which work-approved tooling and package sources are allowed, then document the specific constraints in `work/code/work-environment.md` (this file is the living capture of approved OS, networks, registries, secrets, CI, and allowed AI commands).
- Follow the `work/code/bootstrap/PROCESS.md`, `work/code/discovery/PROCESS.md`, and `work/code/docs/PROCESS.md` in that order; all of them reference their `home/code` counterparts and append compliance requirements (read `work/code/coding-human-ai-team-agreement.md` after the home agreement to understand the workflow expectations).
- Use the Solution Overview Document workflow in `work/project-planning/QUICKSTART.md`: copy `/prompts/sod-wizard-seed.md`, paste it into your chosen model, then issue the `New notes`, `Show SOD`, `Lock the SOD`, and `sodstories`/`sodnotes` commands to manage the living plan; the AI organizes drivers, architecture, risks, and deliverables into an SOD.md you can copy into a real project.

## Conventions & Quality
- Always read `shared/agreements/human-ai-team-agreement.md` before diving into any domain extension (`home/code/coding-human-ai-team-agreement.md`, `home/writing/...`, `work/code/...`) because the base doc defines the collaboration signals (Stop/Pause/Clarify) and quality rules that every domain inherits.
- Code work follows TDD, trunk-based development, and `feat/fix/test/refactor/docs/chore` commit messages; feature branches use `feature/STORY-N-description` or `bugfix/BUG-N-description`. Each story should aim for 3-5 points, include unit/integration/UAT tests, and satisfy the Definition of Done list in the agreement.
- File naming is intentional: Markdown/docs use `kebab-case`, Python modules use `snake_case`, CLI entry points use dashes, directories use `kebab-case`, and canonical files (`README.md`, `CLAUDE.md`, `CHANGELOG.md`) remain uppercase (see `shared/conventions/file-naming.md`).
- Document templates live in `shared/code/templates/docs/`; home and work `docs/templates/` directories reference those base templates but add domain-specific instructions, so copy with care and update inheritance notes when you extend or adapt them.

## Collaboration & Signals
- Ask clarifying questions whenever anything is ambiguous, and never proceed when confused—use the base agreement's signals and say, “I’m not sure if you meant X or Y.”
- If a task scope balloons, say so and offer to split it; avoid making assumptions about destructive commands and limit execution to clearly approved actions documented in `home/code/coding-human-ai-team-agreement.md` (allow list first, add commands only after confirmation).
- When exploring solutions, keep Plan Mode active until there is consensus on what to build so you don’t create files before the human approves the approach.
- Remember that the human always makes the final decision; your job is to surface options, explain trade-offs, and keep everything documented with referenceable links (e.g., cite `home/code/docs/PROCESS.md` when you follow that process).

## Repository Maintenance Notes
- If you ever change the directory structure, prompts, or workflow order, update both `CLAUDE.md` and this `.github/copilot-instructions.md` plus bump their verification dates so future agents know the guidance is fresh.
- Use `shared/agreements/human-ai-team-agreement.md` as the canonical source for behavioral expectations and link back to it whenever you extend the workflow for a new domain.
- No matter where you work, trace your reasoning back to these documents before changing conventions, commands, or templates so the “stencils, not scaffolds” philosophy stays alive.
