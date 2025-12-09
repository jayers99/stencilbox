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

> **First Principle:** Clear communication prevents wasted effort. Both Human and AI should signal early when something isn't right.

### Human to AI Signals

**Stop / Abort:**

- Type `stop` or `wait` - AI should halt current action
- Press `Ctrl+C` - Interrupts Claude Code execution
- Close the terminal - Hard stop (loses context)

**Pause / Hold:**

- *"Pause - I need to think about this"*
- *"Hold on, let me review what you've done so far"*
- *"Don't proceed until I say so"*

**Change Direction:**

- *"Actually, let's try a different approach"*
- *"Scratch that - here's what I really want"*
- *"This isn't working. Let's step back."*

**Clarify Scope:**

- *"Just do X, nothing else"*
- *"Only modify file Y"*
- *"Don't refactor, just fix the bug"*

**Request Confirmation:**

- *"Before you do anything, tell me your plan"*
- *"What files will this change?"*
- *"Walk me through what you're about to do"*

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

**Methodology: Red-Green-Refactor**

1. **Red** - Write a failing test first
2. **Green** - Write minimal code to pass the test
3. **Refactor** - Clean up while keeping tests green

**Why TDD?**

- Forces you to think about interface before implementation
- Tests serve as documentation
- Catches regressions immediately
- Keeps code focused and minimal

**Claude Tips:**

- Tell Claude: *"Write the test first, then the implementation"*
- Enforce TDD: *"Don't write implementation until we have a failing test"*
- Ask for test cases: *"What test cases do we need for this feature?"*

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

**Trunk-Based Development (Solo):**

For solo work, keep it simple:

- `main` - Always releasable
- `feature/<name>` - Short-lived feature branches
- `bugfix/<name>` - Bug fix branches

**Branch Naming:**

```
feature/add-user-login
feature/issue-42-export-csv
bugfix/fix-null-pointer
bugfix/issue-15-crash-on-empty
```

**Rules:**

- Branch from `main`
- Keep branches short-lived (ideally < 1 day)
- Delete branch after merge
- Never commit directly to `main`

**Claude Tips:**

- Ask Claude to create branch: *"Create a feature branch for this story"*
- Check branch status: *"Are we on the right branch? Is it up to date with main?"*

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
