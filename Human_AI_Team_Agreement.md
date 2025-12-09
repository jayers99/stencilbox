# Human-AI Team Agreement

> A working agreement between the AI programming assistant and the Human (acting as Product Owner, UAT Tester, and End User).

---

## 1. Discovery & Brainstorming

> **First Principle:** Understand the problem deeply before proposing solutions. Time spent here saves exponentially more time later.

### Idea Capture

**Methodologies:**

- **Brain Dump** - Write everything down without filtering. Quantity over quality at this stage.
- **Mind Mapping** - Start with the core idea and branch out to related concepts, constraints, and questions.
- **5 Whys** - Ask "why" repeatedly to get to the root need behind the surface request.

**Process:**

- Capture raw ideas in a `brainstorm.md` file (throwaway, not version controlled)
- No idea is too small or too "obvious" to write down
- Include constraints, concerns, and unknowns alongside features

**Claude Tips:**

- Start a conversation with Claude to explore your idea before any code exists
- Use open-ended prompts: *"I'm thinking about building X. What questions should I be asking myself?"*
- Ask Claude to play devil's advocate: *"What are the reasons this might fail or be harder than I expect?"*
- Use **Plan Mode** (`Shift+Tab` to toggle, or `claude --permission-mode plan`) for exploratory conversations where you don't want any files created yet

### Problem Statement

**Template:**

> **Problem:** [What pain point or need exists?]
> **Who has it:** [Who experiences this problem?]
> **Current state:** [How is it handled today, if at all?]
> **Desired state:** [What does success look like?]
> **Constraints:** [Time, budget, technical limitations, must-haves]

**Validation Questions:**

- Is this problem worth solving?
- Am I the right person to solve it?
- Is now the right time?
- What's the simplest thing that could possibly work?

**Claude Tips:**

- Share your problem statement with Claude and ask: *"What am I missing? What assumptions am I making?"*
- Ask Claude to restate the problem in different ways to test your understanding
- Request a *"pre-mortem"*: *"Imagine this project failed. What went wrong?"*

---

## 2. Project Bootstrap

> **First Principle:** A consistent, reproducible project structure reduces cognitive load and lets you focus on the problem, not the plumbing.

### Repository Setup

**Checklist:**

- [ ] Create repository (GitHub/GitLab/Bitbucket)
- [ ] Initialize with README, .gitignore, LICENSE
- [ ] Set up branch protection rules on main
- [ ] Configure CI/CD pipeline (even if minimal)
- [ ] Add CODEOWNERS if applicable

**Naming Convention:**

- Use lowercase with hyphens: `my-project-name`
- Be descriptive but concise
- Include language/framework prefix if you have many repos: `py-my-tool`, `ts-my-app`

**Claude Tips:**

- Ask Claude to generate a `.gitignore` for your tech stack: *"Generate a .gitignore for a Python CLI project using Poetry"*
- Have Claude create initial CI workflow: *"Create a GitHub Actions workflow for Python that runs pytest and mypy"*

### Project Structure

**Principle:** Follow conventions for your language/framework. Don't invent new patterns unless you have a good reason.

**Process:**

1. AI reads `bootstrap/PROCESS.md`
2. Human selects project type from `bootstrap/project-types/`
3. AI reads the selected `SCAFFOLD.md` and generates structure

**Available Project Types:**

| Type | Location | Description |
|------|----------|-------------|
| Python CLI | `bootstrap/project-types/python-cli/` | CLI tool with DDD, TDD, pytest |
| *(add more as needed)* | | |

**Claude Tips:**

- Tell Claude: *"Read bootstrap/PROCESS.md and help me start a new project"*
- Or be specific: *"Read bootstrap/project-types/python-cli/SCAFFOLD.md and create a project called X"*
- If unsure about conventions: *"What's the standard project structure for [framework]?"*

### Environment Setup

**Local Development:**

- Document exact steps to get from clone to running in README
- Use version managers (pyenv, nvm, etc.) to pin language versions
- Include a `Makefile` or `justfile` for common commands

**Dependencies:**

- Pin dependencies with lock files (poetry.lock, package-lock.json)
- Separate dev dependencies from production
- Document why non-obvious dependencies exist

**Secrets Management:**

- **Never commit secrets** - use `.env` files (gitignored) or environment variables
- Provide a `.env.example` with dummy values
- Document which secrets are needed and where to get them

**Claude Tips:**

- Ask Claude to create a Makefile: *"Create a Makefile with targets for install, test, lint, and run"*
- For secrets: *"What environment variables does this project need? Create a .env.example"*
- Use Claude to write setup instructions: *"Write README setup instructions assuming a fresh Mac with Homebrew"*

### Define Allowed Commands

**Principle:** Limit what the AI can execute to reduce risk of unintended side effects.

**Consider restricting:**

- Destructive git commands (force push, hard reset)
- Package publishing
- Production deployments
- Commands that modify system state outside the project

**Claude Code Configuration:**

You can configure allowed/denied commands in `.claude/settings.json`:

```json
{
  "permissions": {
    "allow": ["npm test", "npm run build"],
    "deny": ["rm -rf", "git push --force"]
  }
}
```

**Claude Tips:**

- Start restrictive, loosen as you build trust
- Review Claude's proposed commands before approving
- Use Plan Mode when you want analysis without execution

---

## 3. Requirements & Design

> **First Principle:** Requirements are a conversation, not a specification. Write them to communicate intent, not to cover every edge case. Design emerges through iteration.

### Requirements Documentation

**Methodology: Living Documents**

- Requirements evolve—treat them as living documents, not contracts
- Write for clarity, not completeness
- Focus on *what* and *why*, not *how*

**Format:**

- Store in `docs/requirements.md` (or `docs/requirements/` for larger projects)
- Use markdown with clear headings
- Include **semver version** at the top (e.g., `v0.1.0`)
- Keep filename consistent; update version inside the doc

**Structure Template:**

```markdown
# Requirements: [Project Name]
Version: 0.1.0

## Overview
[1-2 paragraph summary]

## User Stories
- As a [user], I want [goal] so that [reason]

## Functional Requirements
### FR-001: [Name]
- Description: ...
- Acceptance Criteria: ...

## Non-Functional Requirements
- Performance: ...
- Security: ...

## Out of Scope
- [Explicitly list what this version does NOT include]
```

**Claude Tips:**

- Tell Claude: *"Read docs/requirements.md before we start any work"*
- Ask Claude to identify gaps: *"What's unclear or missing from these requirements?"*
- Have Claude generate user stories: *"Convert these requirements into user stories"*

### Design Process

**Methodology: Design Docs**

A design doc answers: *"How will we build this?"*

**When to Write a Design Doc:**

- New features with multiple components
- Changes affecting multiple files/modules
- Decisions with long-term implications
- Anything you'd want to discuss before coding

**Design Doc Template:**

```markdown
# Design: [Feature Name]
Version: 0.1.0
Status: Draft | Review | Approved

## Context
[Why are we doing this? Link to requirements.]

## Goals
- [What must this achieve?]

## Non-Goals
- [What are we explicitly NOT solving?]

## Proposed Solution
[Describe the approach]

## Alternatives Considered
[What else did we consider? Why not?]

## Technical Details
[Architecture, data flow, APIs, etc.]

## Open Questions
- [Things still to decide]
```

**Process:**

1. Write draft design doc
2. Review with Claude (or team)
3. Iterate until approved
4. Create roadmap/stories from approved design

**Claude Tips:**

- Use **Plan Mode** when iterating on design: *"Let's design feature X. Don't write any code yet."*
- Ask for alternatives: *"What are other ways to approach this?"*
- Request critique: *"What are the weaknesses of this design?"*
- Have Claude fill in technical details: *"Expand the technical details section"*

### Tech Stack Decisions

**Document in:** `docs/architecture.md` or `docs/adr/` (Architecture Decision Records)

**ADR Template (lightweight):**

```markdown
# ADR-001: [Decision Title]
Date: YYYY-MM-DD
Status: Proposed | Accepted | Deprecated

## Context
[What situation prompted this decision?]

## Decision
[What did we decide?]

## Consequences
[What are the implications—good and bad?]
```

**Claude Tips:**

- Ask Claude to help evaluate options: *"Compare Redux vs Context for state management in this project"*
- Document the decision even if it seems obvious—future you will thank you

### Definition of Done (Global)

**All work must meet these criteria before being considered complete:**

- [ ] Code compiles/runs without errors
- [ ] All tests pass (unit + integration)
- [ ] No linter errors or warnings
- [ ] Code reviewed (by Copilot + Claude or Human)
- [ ] Documentation updated (if user-facing changes)
- [ ] Commit message follows convention
- [ ] PR includes UAT instructions

**Claude Tips:**

- Before marking work complete, ask: *"Does this meet our Definition of Done?"*
- Have Claude run the checklist: *"Review this PR against our DoD"*

### Project Completion Criteria

**MVP Criteria (from Discovery phase):**

- Defined in `discovery/mvp_scope.md`
- All must-haves implemented and tested
- Success criteria measurable and met

**v1.0 Readiness Checklist:**

- [ ] All MVP features complete
- [ ] No critical or high-severity bugs
- [ ] Documentation complete (README, user docs)
- [ ] Setup instructions tested on clean environment
- [ ] Release notes written
- [ ] Version tagged in git

**Claude Tips:**

- Ask Claude: *"Are we ready for v1.0? What's missing?"*
- Have Claude draft release notes: *"Write release notes for v1.0 based on our commits"*

---

## 4. Story & Ticket Creation

> **First Principle:** A good story is small enough to complete in one cycle, clear enough that anyone can understand it, and testable enough that you know when it's done.

### Story Sizing

**Methodology: Story Points**

Story points measure *complexity*, not time. Use a simple scale:

| Points | Complexity | Guideline |
|--------|------------|-----------|
| 1 | Trivial | Config change, typo fix |
| 2 | Small | Single function, simple test |
| 3 | Medium | Feature with tests, touches 2-3 files |
| 5 | Large | Multiple components, integration needed |
| 8+ | Too big | Break it down |

**Target:** Each story should be **3-5 points**

**Rules:**

- Stories must be completable with unit tests, integration tests, and UAT in a single cycle
- If a story feels bigger than 5 points, split it
- If you can't estimate it, it's a spike (research ticket)

**Claude Tips:**

- Ask Claude to estimate: *"How many story points is this? What's the complexity?"*
- Have Claude split large stories: *"This feels too big. How would you break it down?"*

### Ticket Types

**Story** - Delivers user value

```markdown
## [STORY] As a [user], I want [feature]

**Description:**
[What and why]

**Acceptance Criteria:**
- [ ] Given [context], when [action], then [result]
- [ ] ...

**Technical Notes:**
[Implementation hints, if any]

**Test Criteria:**
- Unit: [what to test]
- Integration: [what to test]
- UAT: [how to verify manually]
```

**Bug** - Fixes broken behavior

```markdown
## [BUG] [Short description]

**Current Behavior:**
[What happens now]

**Expected Behavior:**
[What should happen]

**Steps to Reproduce:**
1. ...

**Environment:**
[Version, OS, etc.]
```

**Spike** - Research/investigation (timeboxed)

```markdown
## [SPIKE] Investigate [topic]

**Question to Answer:**
[What are we trying to learn?]

**Timebox:**
[Max time to spend, e.g., 2 hours]

**Output:**
- [ ] Document findings in [location]
- [ ] Recommend next steps
```

**Chore** - Maintenance, no user-visible change

```markdown
## [CHORE] [Short description]

**Description:**
[What needs to be done]

**Why:**
[Why is this necessary?]
```

### Acceptance Criteria

**Methodology: Given-When-Then (Gherkin-style)**

Write acceptance criteria that are:
- **Specific** - No ambiguity
- **Testable** - You can verify pass/fail
- **Independent** - Each criterion stands alone

**Format:**

```
Given [precondition/context]
When [action is taken]
Then [expected result]
```

**Examples:**

```
Given a user is logged in
When they click the logout button
Then they are redirected to the login page
And their session is invalidated

Given an invalid email format
When the user submits the form
Then an error message "Invalid email" is displayed
And the form is not submitted
```

**Claude Tips:**

- Ask Claude to write acceptance criteria: *"Write Given-When-Then acceptance criteria for this feature"*
- Have Claude review: *"Are these acceptance criteria complete and testable?"*
- Generate test cases: *"Convert these acceptance criteria into pytest test cases"*

### Workflow: From Design to Stories

1. **Start with approved design doc**
2. **Identify deliverables** - What are the shippable increments?
3. **Create stories** - One per deliverable, 3-5 points each
4. **Order by dependency** - What must be built first?
5. **Add acceptance criteria** - Given-When-Then for each
6. **Review with Claude** - Gaps? Missing tests? Too big?

**Claude Tips:**

- Tell Claude: *"Read the design doc and break it into stories"*
- Ask for ordering: *"What order should these stories be implemented?"*
- Validate completeness: *"Do these stories cover all the requirements?"*

### Tracking (Lightweight)

For solo work, a simple markdown file works:

```markdown
# Backlog

## In Progress
- [ ] [STORY] Feature X (3 pts) - PR #12

## Ready
- [ ] [STORY] Feature Y (5 pts)
- [ ] [BUG] Fix Z (2 pts)

## Done
- [x] [STORY] Feature A (3 pts) - PR #10
```

Or use GitHub Issues/Projects if you prefer a UI.

**Claude Tips:**

- Ask Claude to update the backlog: *"Mark story X as done and move Y to in progress"*
- Request status: *"What's our current backlog status?"*

---

## 5. Communication Protocols

### Human to AI Signals

- TODO: How does Human signal "stop", "pause", "change direction"?

### AI to Human Signals

- TODO: How does AI signal it's blocked or confused?

### Context Handoff

- TODO: What happens when starting a new session?
- TODO: What context files should AI read first?

---

## 6. Development

### Pre-Development

- **Do not start building immediately**—plan first
- Use Claude Code's **plan mode** for complex tasks
- AI assistant reads and understands requirements before coding

### During Development

- Make **frequent commits**
- Limit work-in-progress (WIP) per Agile principles
- Wait for integration testing to pass before starting the next story

### Branch Naming Convention

Follow Jira/Bitbucket patterns:

- `feature/<description>` for new features
- `bugfix/<description>` for bug fixes

### Error Handling Conventions

- TODO: Logging standards
- TODO: Error message formats

---

## 7. Testing

### Test Coverage

- Every story must include:
  - **Unit tests**
  - **Integration tests**
  - **UAT test instructions**

### Integration Testing

- AI assistant should write integration tests
- AI assistant should provide instructions to run tests
- Complete integration testing before moving to next story

### UAT Testing

- Each PR must include UAT testing instructions
- UAT is the final step before merge approval

### Test Data Management

- TODO: How to handle fixtures, mocks, test databases?

### Performance Testing

- TODO: Load testing requirements (if applicable)

---

## 8. Code Review & PR Process

### PR Review Flow

1. Developer creates PR
2. **GitHub Copilot agent** reviews all PRs
3. **Claude Code** reviews Copilot's comments and either:
   - Fixes the issue, OR
   - Ignores with inline comment explaining the decision

### PR Approval

- Configure GitHub to allow appropriate PR approvals
- Limit prompts to PR approval after story is finished

### Merge Strategy

- TODO: Squash? Rebase? Merge commits?

### Rollback Plan

- TODO: What happens if a merged PR breaks something?

### Notifications

- Sound a beep notification when ready for PR review
- Explore detection of merged commits for workflow automation

---

## 9. Release & Deployment

### Versioning

- TODO: Versioning strategy (semver?)

### Changelog

- TODO: How to maintain changelog?

### Deployment Process

- TODO: Deployment steps and environments

---

## 10. Documentation Updates

- Update user documentation as development progresses

---

## 11. Maintenance & Future Work

- Establish patterns for returning to completed projects
- Define process for bug fixes and feature additions post-release

---

## 12. Open Questions & Improvements

- [ ] How to ask Claude Code where it is in the current plan?
- [ ] How to get Claude Code to reply to Copilot PR change comments?
- [ ] Can we interact via CLI and have it add notes to PRs?
- [ ] Can we detect when commits are merged?

---

Last updated: 2025-12-08
