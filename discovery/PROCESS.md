# Discovery Process

> **AI Instructions:** The Human has pointed you to this template file from their project directory. Follow this process to guide them through discovery. Create all output files in the Human's **current working directory** (not in this templates folder). For example, if working in `~/code/my-new-app/`, create `~/code/my-new-app/discovery/brainstorm.md`.

---

## Step 1: Brain Dump

**Goal:** Get everything out of the Human's head without filtering.

**AI Actions:**
1. Ask: *"What's the idea? Tell me everything—features, concerns, constraints, half-baked thoughts. No filter."*
2. Listen and capture. Don't critique yet.
3. Ask follow-up questions to pull out more: *"What else? What are you worried about? What would make this a success?"*

**Output:** Save raw notes to `discovery/brainstorm.md`

---

## Step 2: Problem Statement

**Goal:** Distill the brain dump into a clear problem definition.

**AI Actions:**
1. Review `brainstorm.md`
2. Draft a problem statement using this template:

```markdown
## Problem Statement

**Problem:** [What pain point or need exists?]

**Who has it:** [Who experiences this problem?]

**Current state:** [How is it handled today?]

**Desired state:** [What does success look like?]

**Constraints:** [Time, budget, tech limitations, must-haves]
```

3. Ask the Human to validate and refine

**Output:** Save to `discovery/problem_statement.md`

---

## Step 3: Validate the Idea

**Goal:** Stress-test the idea before investing more time.

**AI Actions:**
1. Ask the 5 Whys to get to root motivation
2. Play devil's advocate: *"What are the reasons this might fail?"*
3. Run a pre-mortem: *"Imagine this failed. What went wrong?"*
4. Ask: *"Is this problem worth solving? Are you the right person? Is now the right time?"*

**Output:** Document concerns and mitigations in `discovery/validation.md`

---

## Step 4: Scope the MVP

**Goal:** Define the smallest thing that solves the core problem.

**AI Actions:**
1. Ask: *"What's the simplest thing that could possibly work?"*
2. Help distinguish must-haves from nice-to-haves
3. Identify what can be deferred to v2

**Output:** Save to `discovery/mvp_scope.md`

---

## Step 5: Exit Criteria

**Goal:** Know when discovery is complete and we're ready for design.

**Checklist:**
- [ ] Problem statement is clear and validated
- [ ] Human can explain the idea in one sentence
- [ ] MVP scope is defined
- [ ] Major risks are identified
- [ ] Human says "let's build this"

---

## Files to Create in Your Project

Create a `discovery/` folder in your project directory and save these files there:

| File | Purpose |
|------|---------|
| `brainstorm.md` | Raw brain dump (created during Step 1) |
| `problem_statement.md` | Refined problem definition (created during Step 2) |
| `validation.md` | Risk analysis and validation notes (created during Step 3) |
| `mvp_scope.md` | MVP feature list and boundaries (created during Step 4) |

---

## Tips

- Keep discovery conversational—don't rush to solutions
- It's okay to abandon an idea here. That's a success, not a failure.
