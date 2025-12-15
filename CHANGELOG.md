# Changelog

All notable changes to this project will be documented in this file.

## v0.2.0 — 2025-12-11

- Restructure repository to introduce work-specific area:
  - Added `work/` top-level directory.
  - Moved former `code_work` into `work/code`.
  - Created `work/project-planning` with planning workflow and artifacts.
- Scaffolded planning system supporting SOD and story generation:
  - `work/project-planning/README.md` outlining AI-assisted workflow.
  - `work/project-planning/SOD.md` template for Solution Overview Document.
  - `work/project-planning/prompts/master.md` placeholder for unified prompt.
  - `work/project-planning/snippets/sod.code-snippets` VS Code snippets.
  - `work/project-planning/commands.md` Speed Mode commands reference.
  - `work/project-planning/samples/sample_sod_aws_vault_replication.md` example.
- Established `work/code` docs aligned to regulated environment constraints:
  - `README.md` purpose and structure.
  - `WORK_ENVIRONMENT.md` constraints checklist.
  - Process docs under `bootstrap/`, `discovery/`, `docs/`, and `prompts/`.
