# code_work (JPMC)

Purpose: A work-adapted variant of `code/` tailored for JPMC constraints.

What's different:
- Uses work-approved tooling and package sources
- Assumes restricted internet and internal artifact registries
- Emphasizes security, auditability, and compliant data handling
- Aligns processes with JPMC governance (SDLC, reviews, change mgmt)

Structure:
- `bootstrap/`: work-safe project scaffolding patterns
- `discovery/`: problem framing, validation, and scope
- `docs/`: templates and process docs for delivery
- `prompts/`: AI prompt library adapted for work policies

Start here:
1. Review and complete `WORK_ENVIRONMENT.md`.
2. Use `discovery/PROCESS.md` to kick off efforts.
3. Follow `bootstrap/PROCESS.md` to scaffold projects safely.

Notes:
- This folder mirrors `code/` where possible, with work-specific constraints layered in.
- As constraints evolve, update `WORK_ENVIRONMENT.md` and related guides.
