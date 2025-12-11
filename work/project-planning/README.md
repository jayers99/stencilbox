# AI-Assisted Project Definition & Backlog System  
**Version: v0.1.0**

A structured workflow for turning raw ideas into a finalized Solution Overview Document (SOD) and then into Jira stories, using AI agent behaviors and two supporting spike tickets.

This system supports DevSecOps, cloud engineering, and enterprise-grade software delivery in a conservative banking/regulated environment.

---

## Table of Contents
1. Overview  
2. Workflow Summary  
3. Behavior Model  
   - Spike #1  
   - SOD (Brain Dump → Structured Document)  
   - Spike #2  
   - Story Generation  
4. Master Unified Prompt  
5. Speed Mode Commands  
6. VS Code / Copilot Snippets  
7. Sample SOD  
8. License (optional)

---

# 1. Overview

This repository defines a reusable method for:

1. Capturing a **brain dump** of raw ideas.  
2. Converting those raw ideas into a structured **Solution Overview Document (SOD)** through iterative Q&A with an AI agent.  
3. Using **Spike #2** to review the SOD and determine all required epics and stories.  
4. Generating Jira-ready stories using a strict template and Speed Mode.

This system creates a **clean, PMO-compliant content pipeline** for any technical project.

---

# 2. Workflow Summary

```
                 ┌────────────────────────────┐
                 │      Business Need         │
                 └─────────────┬──────────────┘
                               │
                               ▼
                  ┌──────────────────────────┐
                  │      SPIKE #1            │
                  │ Investigate & Gather     │
                  │   Raw Inputs / Notes     │
                  └─────────────┬────────────┘
                                │
                  New notes →→→ │
                  Clarifying Qs │
                                ▼
                 ┌────────────────────────────┐
                 │   Brain Dump → SOD Mode    │
                 │  Build Solution Overview   │
                 │ Document (iteratively)     │
                 └─────────────┬──────────────┘
                               │
                      “Lock the SOD”
                               │
                               ▼
               ┌────────────────────────────────┐
               │           SPIKE #2             │
               │ Analyze SOD → Create plan for  │
               │ epics, stories, dependencies   │
               └───────────────┬────────────────┘
                               │
                               ▼
                ┌──────────────────────────────┐
                │     Story Generation         │
                │  (Using strict Jira template │
                │         + Speed Mode)        │
                └──────────────────────────────┘
```

---

# 3. Behavior Model

## Behavior 1 — Spike #1: Investigate for SOD Creation
Purpose: Explore the problem space, collect raw notes, uncertainties, assumptions, and constraints before formalizing the SOD.

### Trigger
```
Generate Spike 1
```

---

## Behavior 2 — Brain Dump → SOD
Purpose: Convert raw notes into a structured Solution Overview Document via iterative Q&A.

### How it works
- You provide raw input:  
  ```
  New notes: <your idea>
  ```
- The AI incorporates it into the SOD and asks 1–2 clarifying questions.
- You can repeat this all day as ideas arise.
- When ready:
  ```
  Show SOD
  ```
- When the document is finalized:
  ```
  Lock the SOD
  ```

### SOD Structure
```
Solution Overview Document (SOD)
- Problem Statement
- Business Context / Drivers
- Goals
- Non-Goals
- Functional Overview
- High-Level Architecture / Workflow
- Assumptions
- Constraints (Technical, Security, Compliance, Operational)
- Dependencies
- Phases / Components
- Risks & Mitigations
- Open Questions
- Glossary / Definitions
```

---

## Behavior 3 — Spike #2: SOD → Work Breakdown
Purpose: Analyze the locked SOD and plan the backlog structure (epics, stories, sequencing).

### Trigger
```
Generate Spike 2
```

---

## Behavior 4 — Story Generation (Jira Template)
Once the SOD is locked:

### Trigger
```
Convert SOD to stories
```

The system uses your strict Jira story template and Speed Mode to generate high-quality, ready-to-paste stories.

---

# 4. Master Unified Prompt

*(Stored separately for cleanliness. Recommended to save in `/prompts/master.md`.)*

---

# 5. Speed Mode Commands

### Add new ideas
```
Speed Mode: Integrate these notes into the SOD and ask the next clarifying question.

Notes:
<your note>
```

### View the SOD
```
Speed Mode: Show SOD.
```

### Finalize the SOD
```
Speed Mode: Lock the SOD.
```

### Generate stories
```
Speed Mode: Convert SOD to stories.
```

---

# 6. VS Code / Copilot Snippets

### Add New Notes
```
"sodnotes": {
  "prefix": "sodnotes",
  "body": ["New notes: $1"],
  "description": "Add new brain dump notes to SOD"
}
```

### Show SOD
```
"showsod": {
  "prefix": "showsod",
  "body": ["Show SOD"]
}
```

### Lock SOD
```
"locksod": {
  "prefix": "locksod",
  "body": ["Lock the SOD"]
}
```

### Spike 1
```
"spike1": {
  "prefix": "spike1",
  "body": ["Generate Spike 1"]
}
```

### Spike 2
```
"spike2": {
  "prefix": "spike2",
  "body": ["Generate Spike 2"]
}
```

### Convert SOD to Stories
```
"sodstories": {
  "prefix": "sodstories",
  "body": ["Convert SOD to stories"]
}
```

---

# 7. Sample SOD

See `/samples/sample_sod_aws_vault_replication.md` for a complete example.

---

# 8. License
Choose a license appropriate for public or internal distribution.

---
