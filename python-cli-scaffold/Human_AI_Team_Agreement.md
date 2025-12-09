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

- Create repository
- Define allowed commands
- Set up initial project structure

### Environment Setup

- TODO: Local dev environment requirements
- TODO: Dependencies management
- TODO: Secrets management

---

## 3. Requirements & Design

### Requirements Documentation

- Store requirements in **markdown format**
- Include **semver versioning** in the document (keep filename consistent)
- AI assistant should read requirements doc before starting work

### Design Process

- Iterate on the design doc first
- AI assistant should pull description and context from the design doc
- Create roadmap after design is finalized

### Tech Stack Decisions

- TODO: Where to document architectural choices?

### Definition of Done (Global)

- TODO: Define criteria that apply to all work (e.g., tests pass, docs updated, no lint errors)

### Project Completion Criteria

- TODO: Define MVP criteria
- TODO: When is v1.0 ready?

---

## 4. Story & Ticket Creation

### Story Sizing

- Each story should be **3-5 story points**
- Stories must be completable with unit tests, integration tests, and UAT in a single cycle
- Stories should have **concrete acceptance criteria**

### Ticket Requirements

- All tickets/stories must include:
  - Clear acceptance requirements
  - Unit test criteria
  - Integration test criteria
  - UAT test criteria
- Use **spike tickets** for research/investigation work

### Acceptance Criteria

- Spend adequate time defining stories—get acceptance criteria right before development begins
- Break down requirements into well-defined tickets with testable outcomes

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
