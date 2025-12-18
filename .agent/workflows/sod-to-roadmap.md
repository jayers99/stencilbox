---
description: Create a Roadmap from a specific Solution Overview Document (SOD)
---

# Workflow: SOD to Roadmap

This workflow analyzes a completed "Solution Overview Document" (SOD) and generates a phased roadmap.

## Prerequisites
- A completed, "locked" SOD file (usually `SOD.md`).

## Steps

1.  **Locate the SOD**
    - Ask the user for the path to their SOD file.
    - Default to `SOD.md` in the current directory if they simply hit enter.
    - *Verify the file exists before proceeding.*

2.  **Analyze the SOD**
    - Read the content of the SOD.
    - Pay special attention to:
        - `Phases / Components`
        - `Dependencies`
        - `Risks & Mitigations`
        - `Constraints`

3.  **Draft the Roadmap**
    - Create a new file named `roadmap.md` using the template at `work/project-planning/templates/roadmap.md` (or creating a similar structure if the template is not accessible).
    - **Phase 1 (MVP)**: Extract the core requirements needed for a functional start.
        - For each Epic, explicitly define the **Goal** (User value), **Scope** (Key features), and **Tech Notes** (Implementation details).
    - **Phase 2+**: Group remaining features into logical subsequent phases.
        - Detailed breakdown (Goal, Scope, Tech Notes) is recommended but optional for later phases.
    - **Dependencies**: List critical path items.
    - **Risks**: Summarize high-impact risks found in the SOD.

4.  **Review**
    - Present the generated `roadmap.md` to the user.
    - Ask: "Does this phasing look correct based on your priorities?"

5.  **Refine**
    - If the user has feedback (e.g., "Move feature X to Phase 1"), edit the `roadmap.md` accordingly.
    - Repeat until approved.
