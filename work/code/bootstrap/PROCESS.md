# Bootstrap Process (Work-Safe)

This process mirrors `code/bootstrap/PROCESS.md` with work-specific adaptations.

1. Define project type and compliance needs.
2. Select approved language/runtime and base template.
3. Initialize repo with mandatory files (README, CODEOWNERS, SECURITY.md).
4. Configure dependency sources to internal registries.
5. Set up CI with required security and license checks.
6. Integrate secrets via approved vault mechanisms.
7. Document deviations and approvals in `WORK_ENVIRONMENT.md`.

Notes
- Prefer internal templates and generators.
- Do not fetch from public registries unless explicitly approved.
