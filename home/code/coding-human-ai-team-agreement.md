# Coding Human-AI Team Agreement

> **Inherits from:** [shared/agreements/human-ai-team-agreement.md](../../shared/agreements/human-ai-team-agreement.md)
>
> Read the base agreement first. This document adds code-specific workflow: TDD, git, PRs, testing, releases.

A working agreement between the AI programming assistant and the Human (acting as Product Owner, UAT Tester, and End User).

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

### Defaults (Pre-Configured)

See `~/.claude/CLAUDE.md` for standard defaults. Don't ask about GitHub, MIT license, Python, or TDD—they're assumed.

### Repository Setup

**Checklist:**

- [ ] Create repository on GitHub
- [ ] Initialize with README, .gitignore (Python), LICENSE (MIT)
- [ ] Push initial commit

**Naming Convention:**

- Use lowercase with underscores: `my_project_name` (Python package-safe)
- Be descriptive but concise

**Commands:**

```bash
# Create repo and push
gh repo create <project_name> --private --source=. --remote=origin
git add -A
git commit -m "feat: initial project scaffold"
git push -u origin main
```

**Claude Tips:**

- Tell Claude: *"Create a GitHub repo for this project using gh"*

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

### Tracking (Markdown-Based)

Use `BACKLOG.md` in project root. See template at `docs/templates/backlog.md`.

**Traceability Chain:**

```
Requirement (FR-001) → Story (STORY-3) → Branch → PR → Done ✓
```

**Files:**

| File | Purpose |
|------|---------|
| `docs/requirements.md` | WHAT we're building (with completion status) |
| `BACKLOG.md` | Stories/tasks to do (ordered work queue) |
| `CHANGELOG.md` | What's been released |

**BACKLOG.md Structure:**

```markdown
## In Progress
- [ ] **STORY-5** Add user login (3 pts)
  - Requirement: FR-001
  - Branch: `feature/STORY-5-user-login`
  - PR: #12

## Ready
- [ ] **STORY-6** Add logout button (2 pts) - FR-001

## Done (Current Release)
- [x] **STORY-3** Project setup (2 pts) - FR-001 → PR #8 ✓
```

**Requirements Summary (in requirements.md):**

```markdown
| ID | Name | Priority | Status | Stories | PRs |
|----|------|----------|--------|---------|-----|
| FR-001 | User Auth | Must Have | 🟡 | STORY-3, STORY-5 | #8, #12 |
| FR-002 | Data Export | Should Have | 🔲 | — | — |
```

**Branch Naming:** See `~/.claude/CLAUDE.md` for conventions (`feature/STORY-N-desc`, `bugfix/BUG-N-desc`).

**Claude Tips:**

- Start work: *"Read BACKLOG.md and pick up the next ready story"*
- Update status: *"Mark STORY-5 as done with PR #12 and update requirements.md"*
- Check status: *"What's currently in progress? What requirement is it for?"*
- Add story: *"Add a new story for [feature] linked to FR-002"*

---

## 5. Communication Protocols

> **First Principle:** Clear communication prevents wasted effort. Both Human and AI should signal early when something isn't right.

### Human to AI Signals

Standard signals ("Stop", "Pause", "Clarify") are defined in `~/.claude/CLAUDE.md`.

Additional context commands:
- *"Just do X, nothing else"* — limit scope
- *"Before you do anything, tell me your plan"* — request confirmation

### AI to Human Signals

**AI should proactively signal when:**

| Situation | Signal |
|-----------|--------|
| Confused about requirements | *"I'm not sure I understand. Do you mean X or Y?"* |
| Multiple valid approaches | *"There are several ways to do this. Would you prefer A or B?"* |
| Blocked by missing info | *"I need to know X before I can proceed"* |
| About to do something risky | *"This will delete/modify X. Should I proceed?"* |
| Task is larger than expected | *"This is bigger than a single story. Should I break it down?"* |
| Found a problem | *"I noticed an issue: X. Should I fix it now or create a ticket?"* |
| Uncertain about a decision | *"I'm assuming X. Is that correct?"* |

**AI should NOT:**

- Proceed when confused (ask instead)
- Make assumptions about destructive actions
- Change scope without asking
- Skip tests to save time

### Context Handoff

**Starting a New Session:**

When beginning work (new conversation or returning to a project), AI should:

1. **Read context files in this order:**
   ```
   1. Human_AI_Team_Agreement.md (this file - how we work)
   2. docs/requirements.md (what we're building)
   3. docs/design/*.md (how we're building it)
   4. BACKLOG.md or current story (what we're working on now)
   5. Recent git log (what's been done)
   ```

2. **Confirm understanding:**
   - *"I've read the context. We're working on [project] and the current task is [X]. Is that right?"*

3. **Ask what to focus on:**
   - *"What would you like to work on today?"*

**Human should provide:**

- Quick summary if context has changed
- Current priority or focus area
- Any blockers or concerns

**Session Startup Prompt:**

```
Read Human_AI_Team_Agreement.md, then docs/requirements.md,
then check git log for recent changes.
Summarize where we are and ask what to work on.
```

### Working Agreements

**AI Commitments:**

- Read context files before starting work
- Ask before making assumptions
- Signal when blocked or confused
- Propose plans before executing
- Make frequent, small commits
- Write tests before implementation

**Human Commitments:**

- Provide clear requirements and acceptance criteria
- Respond to AI questions promptly
- Review proposed plans before approving
- Test UAT criteria before merging
- Signal direction changes early

### Escalation

**When to escalate (AI to Human):**

- Contradictory requirements
- Security concerns
- Changes that affect production
- Unfamiliar territory (new tech, patterns)
- Time-sensitive decisions

**How to escalate:**

- State the issue clearly
- Provide options if possible
- Wait for Human decision
- Don't proceed until resolved

---

## 6. Development

> **First Principle:** Working software over comprehensive documentation. But working means tested, readable, and maintainable—not just "runs once."

### Pre-Development Checklist

Before writing any code:

- [ ] Story/ticket exists with acceptance criteria
- [ ] Requirements are understood (ask if unclear)
- [ ] Design approach is clear (write design doc if complex)
- [ ] Tests are planned (what will you test?)
- [ ] Branch is created from main

**Claude Tips:**

- Use **Plan Mode** for complex tasks: `Shift+Tab` or `claude --permission-mode plan`
- Ask Claude to summarize the task: *"What are we building and how will we know it's done?"*
- Request a plan: *"Before coding, outline the steps and files you'll change"*

### TDD Workflow

**Methodology: Red-Green-Refactor** (always—see `~/.claude/CLAUDE.md`)

1. **Red** - Write a failing test first
2. **Green** - Write minimal code to pass the test
3. **Refactor** - Clean up while keeping tests green

### Commit Practices

**Commit Early, Commit Often:**

- Commit after each meaningful change
- Each commit should leave the codebase working
- Don't bundle unrelated changes

**Commit Message Format:**

```
<type>: <short description>

[optional body - what and why]

[optional footer - references, breaking changes]
```

**Types:**

| Type | Use For |
|------|---------|
| `feat` | New feature |
| `fix` | Bug fix |
| `test` | Adding/updating tests |
| `refactor` | Code change that doesn't add feature or fix bug |
| `docs` | Documentation only |
| `chore` | Maintenance, dependencies |

**Examples:**

```
feat: add user login endpoint

fix: prevent crash when email is empty

test: add unit tests for validation module

refactor: extract email validation to separate function
```

**Claude Tips:**

- Ask Claude to commit: *"Commit this change with an appropriate message"*
- Review before committing: *"What changed? Write a commit message."*

### Branch Strategy

**Trunk-Based Development (Solo):** Branch naming conventions are in `~/.claude/CLAUDE.md`.

**Rules:**
- Branch from `main`
- Keep branches short-lived (ideally < 1 day)
- Delete branch after merge
- Never commit directly to `main`

### Code Style

**Principle:** Follow the conventions of your language/framework. Consistency matters more than personal preference.

**For Python:**

- Follow PEP 8
- Use type hints
- Run `black` for formatting
- Run `mypy` for type checking
- Run `ruff` or `flake8` for linting

**Before Committing:**

```bash
# Format
black .

# Lint
ruff check .

# Type check
mypy src/

# Test
pytest
```

**Claude Tips:**

- Ask Claude to format: *"Run the linter and fix any issues"*
- Enforce style: *"Make sure this follows PEP 8"*

### Error Handling

**Logging Levels:**

| Level | Use For |
|-------|---------|
| `DEBUG` | Detailed diagnostic info (dev only) |
| `INFO` | General operational events |
| `WARNING` | Something unexpected but handled |
| `ERROR` | Something failed but app continues |
| `CRITICAL` | App cannot continue |

**Error Message Format:**

```python
# Bad
raise Exception("Error")

# Good
raise ValueError(f"Invalid email format: {email}")

# Better (with context)
logger.error(f"Failed to send email to {email}: {error}", exc_info=True)
raise EmailDeliveryError(f"Could not deliver to {email}") from error
```

**Principles:**

- Fail fast, fail loud
- Include context in error messages
- Log at appropriate level
- Don't swallow exceptions silently
- Use custom exception types for domain errors

**Claude Tips:**

- Ask for error handling: *"Add appropriate error handling and logging"*
- Review error messages: *"Are these error messages helpful for debugging?"*

### Work in Progress (WIP) Limits

**Rule:** Only one story in progress at a time.

**Why:**

- Context switching is expensive
- Unfinished work blocks others (even future you)
- Easier to track progress
- Forces completion before starting new work

**Process:**

1. Pick one story from backlog
2. Complete it (code + tests + PR + merge)
3. Then pick the next story

**Claude Tips:**

- Ask Claude: *"What's currently in progress? Should we finish it first?"*
- Enforce WIP: *"Don't start a new feature until we merge the current PR"*

---

## 7. Testing

> **First Principle:** Tests are not overhead—they're the safety net that lets you move fast. If you're afraid to change the code, you don't have enough tests.

### Test Pyramid

**Structure your tests as a pyramid:**

```
        /\
       /  \      E2E / UAT (few)
      /----\
     /      \    Integration (some)
    /--------\
   /          \  Unit (many)
  --------------
```

| Type | Quantity | Speed | Scope |
|------|----------|-------|-------|
| Unit | Many | Fast (ms) | Single function/class |
| Integration | Some | Medium (s) | Multiple components |
| E2E/UAT | Few | Slow (s-min) | Full system |

### Unit Tests

**What to Test:**

- Pure functions (given input → expected output)
- Edge cases (empty, null, boundary values)
- Error conditions (invalid input, exceptions)
- Business logic in domain layer

**Characteristics:**

- Fast (< 100ms each)
- Isolated (no external dependencies)
- Deterministic (same result every time)
- Independent (can run in any order)

**Naming Convention:**

```python
def test_<function>_<scenario>_<expected_result>():
    # Example:
    def test_validate_email_with_invalid_format_returns_false():
        assert validate_email("not-an-email") is False
```

**Structure (Arrange-Act-Assert):**

```python
def test_calculate_total_with_discount():
    # Arrange
    items = [Item(price=100), Item(price=50)]
    discount = 0.1

    # Act
    result = calculate_total(items, discount)

    # Assert
    assert result == 135.0
```

**Claude Tips:**

- Ask Claude: *"Write unit tests for this function covering happy path and edge cases"*
- Request coverage: *"What test cases are we missing?"*
- Generate test data: *"Create test fixtures for this scenario"*

### Integration Tests

**What to Test:**

- Components working together
- Database operations
- API endpoints
- External service interactions (with mocks)

**Characteristics:**

- Slower than unit tests (acceptable)
- May use test databases or containers
- Test real interactions, not mocks (where practical)

**When to Write:**

- After unit tests pass
- When testing component boundaries
- For critical paths through the system

**Example:**

```python
def test_user_registration_flow():
    # Test the full registration: API → Service → Database
    response = client.post("/register", json={
        "email": "test@example.com",
        "password": "secure123"
    })

    assert response.status_code == 201
    assert User.query.filter_by(email="test@example.com").first() is not None
```

**Claude Tips:**

- Tell Claude: *"Write an integration test for the user registration flow"*
- Ask for setup: *"What test fixtures do we need for integration tests?"*

### UAT (User Acceptance Testing)

**Purpose:** Verify the feature works from the user's perspective.

**Every PR must include UAT instructions:**

```markdown
## UAT Instructions

### Prerequisites
- [ ] Application running locally
- [ ] Test user account created

### Steps
1. Navigate to /login
2. Enter credentials: test@example.com / password123
3. Click "Login"

### Expected Results
- [ ] User is redirected to dashboard
- [ ] Welcome message shows username
- [ ] Session persists on page refresh

### Edge Cases to Verify
- [ ] Invalid password shows error
- [ ] Empty fields are validated
```

**Who Runs UAT:**

- Human (acting as end user)
- Before approving PR
- After all automated tests pass

**Claude Tips:**

- Ask Claude: *"Write UAT instructions for this feature"*
- Request checklist: *"What should I manually test before merging?"*

### Test Data Management

**Fixtures:**

- Store in `tests/fixtures/` or `tests/conftest.py` (pytest)
- Use factories for complex objects (e.g., `factory_boy`)
- Keep fixtures minimal and focused

**Example (pytest fixtures):**

```python
# conftest.py
import pytest

@pytest.fixture
def sample_user():
    return User(email="test@example.com", name="Test User")

@pytest.fixture
def sample_order(sample_user):
    return Order(user=sample_user, total=100.00)
```

**Mocks:**

- Mock external services (APIs, databases in unit tests)
- Use `unittest.mock` or `pytest-mock`
- Don't mock what you own—test it

**Test Databases:**

- Use SQLite in-memory for fast unit tests
- Use Docker containers for integration tests
- Never test against production data

**Claude Tips:**

- Ask Claude: *"Create pytest fixtures for these test scenarios"*
- Request mocks: *"Mock the external API calls in these tests"*

### Running Tests

**Commands:**

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/unit/test_user.py

# Run tests matching pattern
pytest -k "test_login"

# Run with verbose output
pytest -v

# Stop on first failure
pytest -x
```

**Before Committing:**

```bash
# Full test suite must pass
pytest

# Check coverage (aim for >80%)
pytest --cov=src --cov-fail-under=80
```

**Claude Tips:**

- Ask Claude: *"Run the tests and fix any failures"*
- Request coverage: *"What's our test coverage? What's missing?"*

### Performance Testing

**When Needed:**

- API endpoints with expected high load
- Data processing with large datasets
- Operations with SLA requirements

**Simple Approach (for solo projects):**

```python
import time

def test_bulk_import_performance():
    start = time.time()
    result = bulk_import(large_dataset)
    elapsed = time.time() - start

    assert elapsed < 5.0  # Must complete in under 5 seconds
    assert result.success_count == len(large_dataset)
```

**Tools (when needed):**

- `pytest-benchmark` for micro-benchmarks
- `locust` for load testing
- `cProfile` for profiling

**Claude Tips:**

- Ask Claude: *"Add a performance test for the bulk import function"*
- Request profiling: *"This is slow. Can you profile it and suggest optimizations?"*

---

## 8. Code Review & PR Process

> **First Principle:** Code review catches bugs, improves code quality, and spreads knowledge. Even solo developers benefit from AI-assisted review.

### PR Creation

**Before Creating a PR:**

- [ ] All tests pass locally
- [ ] Code is formatted and linted
- [ ] Self-review completed (read your own diff)
- [ ] Commit history is clean
- [ ] Branch is up to date with main

**PR Template:**

```markdown
## Summary
[Brief description of what this PR does]

## Changes
- [List of changes]

## Testing
- [ ] Unit tests added/updated
- [ ] Integration tests added/updated
- [ ] Manual testing completed

## UAT Instructions
[Steps for Human to verify]

## Screenshots (if UI changes)
[Before/after if applicable]

## Related
- Closes #[issue number]
- Related to #[PR or issue]
```

**Claude Tips:**

- Ask Claude: *"Create a PR with a summary of changes"*
- Request PR description: *"Write a PR description for these changes"*

### PR Review Flow

**Two-Stage AI Review:**

```
1. Claude creates branch for story (feature/STORY-N-desc)
        ↓
2. Claude Code creates PR
        ↓
3. GitHub Copilot reviews (automated)
        ↓
4. Claude polls for Copilot review (every 30 seconds)
        ↓
5. Claude Code addresses Copilot comments
        ↓
6. Human reviews and runs UAT
        ↓
7. Human approves and merges
        ↓
8. Claude creates semver release
```

**Stage 1: Branch and PR Creation**

- Every story gets a branch: `feature/STORY-N-description`
- Every bugfix gets a branch: `bugfix/BUG-N-description`
- Push branch and create PR immediately

**Stage 2: Copilot Review**

- Enable GitHub Copilot code review on the repo
- Copilot automatically reviews all PRs
- Comments appear as review suggestions

**Stage 3: Poll for Copilot Review Completion**

Claude should poll GitHub every 30 seconds to check if Copilot has finished reviewing:

```bash
# Check PR review status
gh pr checks <pr-number> --watch --interval 30

# Or poll manually
while true; do
  gh pr view <pr-number> --json reviews -q '.reviews[] | select(.author.login == "github-actions[bot]" or .author.login == "copilot")'
  sleep 30
done
```

**Claude Tips:**
- Tell Claude: *"Wait for the Copilot review to complete, polling every 30 seconds"*
- Or: *"Check if Copilot has finished reviewing PR #X"*

**Stage 4: Claude Addresses Comments**

For each Copilot comment, Claude should:

1. **Fix** - If the suggestion is valid, implement it
2. **Ignore with explanation** - If not applicable, comment why

```markdown
<!-- Example response to Copilot comment -->
@copilot Thanks for the suggestion. Not applicable here because [reason].
Leaving as-is.
```

**Stage 5: Human Review**

Human reviews:
- Overall approach (does this solve the right problem?)
- Edge cases Copilot might miss
- UAT verification
- Final approval

**Claude Tips:**

- Tell Claude: *"Review the Copilot comments on this PR and address each one"*
- Ask for summary: *"Summarize what Copilot found and what you fixed"*

### PR Commands (Quick Reference)

```bash
# Create PR (Copilot auto-reviews)
gh pr create --title "STORY-X: Description" --body "## Summary
- What this PR does

## Testing
- [x] Tests pass

Closes STORY-X"

# View PR with Copilot comments
gh pr view --comments

# Check PR status
gh pr status

# Merge when ready (squash)
gh pr merge --squash --delete-branch
```

### PR Approval

**Who Approves:** Human (no branch protection configured)

**Approval Checklist:**

- [ ] Code changes look correct
- [ ] Tests are adequate
- [ ] UAT passes
- [ ] No security concerns
- [ ] Documentation updated (if needed)

**Claude Tips:**

- Ask Claude: *"Is this PR ready for my review?"*
- Request checklist: *"Run through the approval checklist for this PR"*

### Merge Strategy

**Recommended: Squash and Merge**

- Keeps main history clean
- One commit per feature/fix
- Easier to revert if needed

**When to Use Each:**

| Strategy | Use When |
|----------|----------|
| Squash | Default for features and fixes |
| Rebase | Clean, logical commit history matters |
| Merge commit | Preserving full branch history matters |

**Process:**

```bash
# Squash merge and delete branch
gh pr merge --squash --delete-branch

# Pull latest locally
git checkout main && git pull
```

**Claude Tips:**

- Ask Claude: *"Merge this PR"*

### Automatic Release After Merge

**Default:** Every merged PR creates a semver release.

**Process:**

1. After PR is merged, Claude determines version bump:
   - `fix:` commits → PATCH bump (1.0.0 → 1.0.1)
   - `feat:` commits → MINOR bump (1.0.0 → 1.1.0)
   - Breaking changes → MAJOR bump (1.0.0 → 2.0.0)

2. Claude creates the release:

```bash
# Get current version
CURRENT=$(git describe --tags --abbrev=0 2>/dev/null || echo "v0.0.0")

# Determine new version based on commits since last tag
# (Claude analyzes commit messages to decide)

# Update version in files (pyproject.toml, __init__.py, etc.)
# Update CHANGELOG.md - move [Unreleased] to new version

# Commit, tag, and push
git add -A
git commit -m "chore: release vX.Y.Z"
git tag -a vX.Y.Z -m "Release vX.Y.Z"
git push origin main --tags

# Create GitHub release
gh release create vX.Y.Z --generate-notes
```

**Claude Tips:**

- Tell Claude: *"Merge this PR and create a release"*
- Or after merge: *"Create a release for the changes just merged"*
- Specify version: *"Create a minor release"* or *"This is a breaking change, create a major release"*

### Rollback Plan

**If a Merged PR Breaks Something:**

**Immediate (< 5 min since merge):**

```bash
# Revert the merge commit
git revert -m 1 <merge-commit-sha>
git push
```

**Recent (same day):**

1. Create a revert PR
2. Fast-track review (Human approves quickly)
3. Merge revert
4. Investigate root cause
5. Fix and re-submit

**Older:**

1. Create a bug ticket
2. Fix forward (don't revert)
3. Follow normal PR process

**Prevention:**

- Run full test suite before merge
- Use feature flags for risky changes
- Deploy to staging first (if applicable)

**Claude Tips:**

- Ask Claude: *"This PR broke something. Help me revert it."*
- Request investigation: *"What went wrong with this change?"*

### Notifications

**PR Ready for Review:**

Claude should signal when PR is ready:

```
🔔 PR #123 is ready for your review.

Summary: [brief description]
UAT: [link to instructions]
Tests: ✅ All passing

Please review when ready.
```

**Optional: System Notification**

```bash
# macOS - play sound when ready
osascript -e 'display notification "PR ready for review" with title "Claude Code"'
# Or use terminal bell
echo -e '\a'
```

**Claude Tips:**

- Tell Claude: *"Notify me when the PR is ready"*
- Configure in settings if supported

---

## 9. Release & Deployment

> **First Principle:** A release should be boring. If you're nervous about releasing, your process isn't automated enough.

### Versioning

**Methodology: Semantic Versioning (SemVer)**

Format: `MAJOR.MINOR.PATCH` (e.g., `1.2.3`)

| Component | When to Increment |
|-----------|-------------------|
| MAJOR | Breaking changes (incompatible API changes) |
| MINOR | New features (backwards compatible) |
| PATCH | Bug fixes (backwards compatible) |

**Pre-release Versions:**

- `1.0.0-alpha.1` - Early development, unstable
- `1.0.0-beta.1` - Feature complete, testing
- `1.0.0-rc.1` - Release candidate, final testing

**Rules:**

- Start at `0.1.0` during initial development
- `0.x.x` means API is not stable
- First stable release is `1.0.0`
- Never reuse version numbers

**Where to Update Version:**

- `pyproject.toml` or `setup.py` (Python)
- `package.json` (Node.js)
- Source code `__version__` if applicable
- Git tag

**Claude Tips:**

- Ask Claude: *"What version should this release be based on the changes?"*
- Request bump: *"Bump the version to 1.2.0 and update all version references"*

### Changelog

**File:** `CHANGELOG.md` in project root

**Format (Keep a Changelog):**

```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added
- New feature X

### Changed
- Updated behavior of Y

### Fixed
- Bug in Z

## [1.0.0] - 2025-01-15

### Added
- Initial release
- Feature A
- Feature B
```

**Categories:**

- `Added` - New features
- `Changed` - Changes to existing functionality
- `Deprecated` - Features to be removed
- `Removed` - Removed features
- `Fixed` - Bug fixes
- `Security` - Security fixes

**Process:**

1. Update `[Unreleased]` section as you merge PRs
2. On release, move `[Unreleased]` content to new version section
3. Add release date
4. Create git tag

**Claude Tips:**

- Ask Claude: *"Update the changelog with this PR's changes"*
- Request release: *"Move unreleased changes to version 1.2.0"*
- Generate from commits: *"Generate changelog entries from recent commits"*

### Release Process

**Pre-Release Checklist:**

- [ ] All tests pass
- [ ] Changelog updated
- [ ] Version bumped
- [ ] Documentation updated
- [ ] No uncommitted changes

**Release Steps:**

```bash
# 1. Ensure clean state
git status  # Should be clean
git pull origin main

# 2. Run full test suite
pytest

# 3. Update version (example for Python)
# Edit pyproject.toml, __version__, etc.

# 4. Update changelog
# Move [Unreleased] to [X.Y.Z] - YYYY-MM-DD

# 5. Commit version bump
git add -A
git commit -m "chore: release v1.2.0"

# 6. Tag the release
git tag -a v1.2.0 -m "Release v1.2.0"

# 7. Push
git push origin main --tags
```

**Claude Tips:**

- Ask Claude: *"Prepare release 1.2.0"*
- Request checklist: *"Run through the pre-release checklist"*

### Deployment

**For CLI Tools (PyPI):**

```bash
# Build
python -m build

# Test upload (TestPyPI)
twine upload --repository testpypi dist/*

# Production upload
twine upload dist/*
```

**For Applications:**

Document environment-specific deployment:

```markdown
## Deployment

### Staging
1. Merge to `staging` branch
2. CI/CD deploys automatically
3. Verify at staging.example.com

### Production
1. Create release tag
2. CI/CD deploys automatically
3. Verify at example.com
4. Monitor for errors
```

**Environments:**

| Environment | Purpose | Deploy Trigger |
|-------------|---------|----------------|
| Local | Development | Manual |
| Staging | Testing | Push to staging branch |
| Production | Live users | Release tag |

**Claude Tips:**

- Ask Claude: *"Deploy this release to staging"*
- Request verification: *"What should I check after deploying?"*

### Rollback

**If Release Has Issues:**

```bash
# Option 1: Deploy previous version
git checkout v1.1.0
# Re-deploy

# Option 2: Revert and release
git revert <bad-commit>
# Bump patch version
# Release v1.2.1
```

**Post-Mortem:**

After any rollback:
1. Document what went wrong
2. Add test to catch it next time
3. Update process if needed

---

## 10. Documentation Updates

> **First Principle:** Documentation is a product feature. If users can't figure out how to use it, it doesn't matter how good the code is.

### Documentation Types

| Type | Audience | Location | Update When |
|------|----------|----------|-------------|
| README | New users, contributors | `README.md` | Setup changes, major features |
| API docs | Developers integrating | `docs/api/` | API changes |
| User guide | End users | `docs/user-guide/` | Feature changes |
| Architecture | Future maintainers | `docs/architecture.md` | Design changes |
| Changelog | Everyone | `CHANGELOG.md` | Every release |

### README Structure

**Every project needs a README with:**

```markdown
# Project Name

Brief description (1-2 sentences)

## Features
- Key feature 1
- Key feature 2

## Quick Start
[Minimal steps to get running]

## Installation
[Detailed installation instructions]

## Usage
[Common use cases with examples]

## Configuration
[Environment variables, config files]

## Development
[Setup for contributors]

## Testing
[How to run tests]

## License
[License type]
```

**Claude Tips:**

- Ask Claude: *"Update the README with the new feature"*
- Request review: *"Is the README accurate and complete?"*
- Generate examples: *"Add usage examples to the README"*

### When to Update Documentation

**Update Immediately (same PR):**

- New features → User guide + README
- API changes → API docs
- Config changes → README + config section
- Breaking changes → Migration guide

**Update on Release:**

- Changelog
- Version numbers in docs
- "What's New" section

**Periodic Review:**

- Screenshots (do they match current UI?)
- Links (are they still valid?)
- Examples (do they still work?)

### Documentation as Code

**Treat docs like code:**

- Store in repo (version controlled)
- Review in PRs
- Test examples (doctest, runnable snippets)
- Lint for style (markdownlint)

**Docstrings (Python):**

```python
def calculate_total(items: list[Item], discount: float = 0.0) -> float:
    """
    Calculate the total price of items with optional discount.

    Args:
        items: List of Item objects with price attribute.
        discount: Discount as decimal (0.1 = 10%). Default 0.

    Returns:
        Total price after discount.

    Raises:
        ValueError: If discount is negative or > 1.

    Example:
        >>> items = [Item(price=100), Item(price=50)]
        >>> calculate_total(items, discount=0.1)
        135.0
    """
```

**Claude Tips:**

- Ask Claude: *"Add docstrings to this module"*
- Generate docs: *"Create API documentation from docstrings"*
- Test examples: *"Verify the docstring examples work"*

### User-Facing Documentation

**Principles:**

- Write for the reader, not yourself
- Show, don't tell (examples > explanations)
- Start with common use cases
- Progressive disclosure (simple → advanced)

**Structure:**

```
docs/
├── getting-started.md    # First-time users
├── user-guide/
│   ├── basic-usage.md
│   ├── advanced-usage.md
│   └── troubleshooting.md
├── api/
│   └── reference.md
└── contributing.md       # For contributors
```

**Claude Tips:**

- Ask Claude: *"Write a getting started guide for new users"*
- Request tutorial: *"Create a step-by-step tutorial for [feature]"*
- Simplify: *"Make this documentation easier to understand"*

### Keeping Docs in Sync

**Definition of Done includes:**

- [ ] Documentation updated for user-facing changes

**PR Checklist:**

- [ ] README updated (if applicable)
- [ ] Docstrings added/updated
- [ ] User guide updated (if applicable)
- [ ] Changelog updated

**Claude Tips:**

- Ask Claude: *"What documentation needs to be updated for this PR?"*
- Request sync: *"Update all documentation to match the current code"*

---

## 11. Maintenance & Future Work

> **First Principle:** Software is never "done." Plan for maintenance from the start, and make it easy to return to a project after time away.

### Returning to a Project

**Context Recovery Checklist:**

When returning to a project after time away:

- [ ] Read `README.md` - Remember what this does
- [ ] Read `CHANGELOG.md` - See recent changes
- [ ] Check `docs/requirements.md` - Recall the goals
- [ ] Run `git log --oneline -20` - See recent commits
- [ ] Check open issues/PRs - Any pending work?
- [ ] Run tests - Does everything still work?
- [ ] Check dependencies - Any security updates?

**Session Startup Prompt:**

```
I'm returning to this project after some time away.
Read the README, CHANGELOG, and recent git history.
Summarize the project status and any pending work.
```

**Claude Tips:**

- Ask Claude: *"Help me get back up to speed on this project"*
- Request summary: *"What's the current state of this project?"*
- Check health: *"Run tests and check for dependency updates"*

### Bug Fix Process

**Triage:**

1. Reproduce the bug
2. Assess severity (Critical / High / Medium / Low)
3. Create bug ticket with reproduction steps

**Severity Guide:**

| Severity | Description | Response |
|----------|-------------|----------|
| Critical | System down, data loss | Fix immediately |
| High | Major feature broken | Fix this sprint |
| Medium | Feature impaired but usable | Schedule fix |
| Low | Minor issue, workaround exists | Backlog |

**Fix Process:**

1. Create `bugfix/<description>` branch
2. Write failing test that reproduces the bug
3. Fix the bug (test should pass)
4. Verify no regressions
5. Update changelog
6. Create PR with root cause analysis

**PR Template for Bug Fixes:**

```markdown
## Bug Fix

**Issue:** #[number] or description

**Root Cause:**
[What caused this bug?]

**Fix:**
[How does this PR fix it?]

**Testing:**
- [ ] Added regression test
- [ ] Verified fix manually
- [ ] Ran full test suite

**Prevention:**
[How do we prevent similar bugs?]
```

**Claude Tips:**

- Ask Claude: *"Help me reproduce and fix this bug"*
- Request analysis: *"What's the root cause of this bug?"*
- Prevent recurrence: *"How can we prevent this type of bug?"*

### Feature Addition Process

**For Existing Projects:**

1. **Evaluate fit** - Does this belong in this project?
2. **Check requirements** - Update `docs/requirements.md`
3. **Design** - Write design doc if non-trivial
4. **Break into stories** - 3-5 points each
5. **Implement** - Follow normal development process

**Considerations:**

- Backwards compatibility
- Migration path for existing users
- Documentation updates
- Changelog entry

**Claude Tips:**

- Ask Claude: *"How would we add [feature] to this project?"*
- Request impact analysis: *"What would this feature change affect?"*

### Dependency Management

**Regular Maintenance:**

```bash
# Check for outdated dependencies (Python)
pip list --outdated

# Check for security vulnerabilities
pip-audit

# Update dependencies
pip install --upgrade <package>
```

**Update Strategy:**

| Type | Frequency | Process |
|------|-----------|---------|
| Security fixes | Immediately | Patch release |
| Minor updates | Monthly | Test and update |
| Major updates | Quarterly | Evaluate breaking changes |

**Claude Tips:**

- Ask Claude: *"Check for dependency updates and security issues"*
- Request upgrade: *"Update [package] to the latest version"*

### Technical Debt

**Tracking:**

- Create `[CHORE]` tickets for tech debt
- Tag with `tech-debt` label
- Include impact and effort estimate

**Prioritization:**

| Priority | Criteria |
|----------|----------|
| High | Blocking features or causing bugs |
| Medium | Slowing development |
| Low | Code smell, no immediate impact |

**Paying Down Debt:**

- Allocate ~20% of sprint capacity to tech debt
- Address high-priority items first
- Refactor incrementally, not all at once

**Claude Tips:**

- Ask Claude: *"What technical debt exists in this codebase?"*
- Request plan: *"How should we address this tech debt?"*

### Project Health Checks

**Periodic Review (monthly/quarterly):**

- [ ] Tests still passing?
- [ ] Dependencies up to date?
- [ ] Security vulnerabilities?
- [ ] Documentation accurate?
- [ ] Any stale branches?
- [ ] Open issues triaged?

**Claude Tips:**

- Ask Claude: *"Run a health check on this project"*
- Request report: *"What maintenance does this project need?"*

---

## 12. Open Questions & Improvements

> This section tracks questions to investigate and potential improvements to this workflow.

### Open Questions

| Question | Status | Notes |
|----------|--------|-------|
| How to ask Claude Code where it is in the current plan? | Open | Try: *"What step are we on?"* |
| How to get Claude Code to reply to Copilot PR comments? | Open | May need `gh` CLI integration |
| Can we interact via CLI and have it add notes to PRs? | Open | Explore `gh pr comment` |
| Can we detect when commits are merged? | Open | Webhook or polling? |
| Can Claude Code run in the background and notify? | Open | Terminal bell works (`echo -e '\a'`) |

### Potential Improvements

**Workflow Automation:**

- [ ] Create slash commands for common tasks (e.g., `/new-story`, `/release`)
- [ ] Automate changelog updates from commit messages
- [ ] Add git hooks for pre-commit checks
- [ ] Create project health check script

**Templates:**

- [ ] Add more project types (TypeScript API, React app, etc.)
- [ ] Create issue/PR templates for GitHub
- [ ] Add CI/CD workflow templates

**Documentation:**

- [ ] Add visual diagrams for workflows
- [ ] Create quick-reference cheat sheet
- [ ] Add troubleshooting guide

### Feedback Log

*Record what's working and what isn't as you use this workflow.*

| Date | Feedback | Action Taken |
|------|----------|--------------|
| 2025-12-08 | Initial version created | - |

### Version History

| Version | Date | Changes |
|---------|------|---------|
| 0.1.0 | 2025-12-08 | Initial draft with all 12 sections |

---

## Quick Reference

### Claude Code Commands

| Action | Command/Prompt |
|--------|----------------|
| Enter Plan Mode | `Shift+Tab` or `claude --permission-mode plan` |
| Start new session | *"Read Human_AI_Team_Agreement.md and help me get started"* |
| Check progress | *"What step are we on? What's next?"* |
| Create PR | *"Create a PR with summary of changes"* |
| Run tests | *"Run tests and fix any failures"* |
| Prepare release | *"Prepare release X.Y.Z"* |

### Key Files

| File | Purpose |
|------|---------|
| `Human_AI_Team_Agreement.md` | This file - how we work together |
| `discovery/PROCESS.md` | Brainstorming and idea validation |
| `bootstrap/PROCESS.md` | Project setup |
| `docs/templates/*.md` | Requirements, design, ADR templates |
| `CHANGELOG.md` | Release history |
| `BACKLOG.md` | Current work items |

---

Last updated: 2025-12-08
