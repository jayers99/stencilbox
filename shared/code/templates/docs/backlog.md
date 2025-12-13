# Backlog

> **AI Instructions:** Read this file to understand current work status. Pick up the next item from "Ready" when asked. Update status as work progresses.

---

## In Progress

<!-- Only ONE item here at a time (WIP limit) -->

- [ ] **STORY-X** [Description] (X pts)
  - Requirement: FR-XXX
  - Depends on: —
  - Branch: `feature/STORY-X-description`
  - PR: —

---

## Ready

<!-- Ordered by priority. Top item is next. Only items with no unmet dependencies. -->

- [ ] **STORY-X** [Description] (X pts) - FR-XXX
- [ ] **STORY-X** [Description] (X pts) - FR-XXX

---

## Up Next

<!-- Needs refinement, blocked, or has unmet dependencies. -->

- [ ] **STORY-X** [Description] (X pts) - FR-XXX - *needs design*
- [ ] **STORY-X** [Description] (X pts) - FR-XXX - ⛔ depends on STORY-Y
- [ ] **BUG-X** [Description] (X pts) - *needs reproduction steps*

---

## Done (Current Release)

<!-- Completed in this release cycle. Move to CHANGELOG on release. -->

- [x] **STORY-X** [Description] (X pts) - FR-XXX → PR #X ✓
- [x] **STORY-X** [Description] (X pts) - FR-XXX → PR #X ✓

---

## Icebox

<!-- Deferred. Not planned for current version. -->

- [ ] **STORY-X** [Description] (X pts) - FR-XXX - *v2*

---

## Story Template

When creating a new story:

```markdown
- [ ] **STORY-N** [Short description] (X pts)
  - Requirement: FR-XXX
  - Depends on: STORY-X (or — if none)
  - Branch: `feature/STORY-N-short-description`
  - PR: —

  **Acceptance Criteria:**
  - [ ] Given X, when Y, then Z
  - [ ] Given A, when B, then C
```

**Dependency Rules:**

- Stories with unmet dependencies stay in "Up Next" with ⛔ marker
- When a dependency completes, move the unblocked story to "Ready"
- AI should check dependencies before picking up a story

---

## Branch Naming

| Type | Format | Example |
|------|--------|---------|
| Feature | `feature/STORY-N-description` | `feature/STORY-5-user-login` |
| Bug fix | `bugfix/BUG-N-description` | `bugfix/BUG-3-null-crash` |
| Chore | `chore/CHORE-N-description` | `chore/CHORE-1-update-deps` |

---

## Claude Commands

| Action | Prompt |
|--------|--------|
| Start next story | *"Read BACKLOG.md and pick up the next ready story"* |
| Check status | *"What's currently in progress?"* |
| Mark done | *"Mark STORY-X as done with PR #Y and unblock any dependent stories"* |
| Add story | *"Add a new story for [feature] linked to FR-XXX"* |
| Check dependencies | *"What stories are blocked? What do they depend on?"* |
