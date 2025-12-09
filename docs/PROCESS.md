# Documentation Process

> **AI Instructions:** When the Human needs to create or update project documentation, read this file first. Guide them to the appropriate template.

---

## Document Types

| Document | Template | When to Create |
|----------|----------|----------------|
| Requirements | `templates/requirements.md` | After Discovery, before coding |
| Design Doc | `templates/design.md` | Before implementing a feature |
| ADR | `templates/adr.md` | When making architectural decisions |

---

## Step 1: Identify Document Type

**AI Actions:**

1. Ask: *"What are you trying to document—requirements, a design, or an architectural decision?"*
2. Direct to appropriate template
3. Help fill in the template

---

## Step 2: Create Document

**Location in Project:**

```
project/
└── docs/
    ├── requirements.md          # Or requirements/ for larger projects
    ├── design/
    │   └── feature-name.md      # One per feature
    └── adr/
        ├── 001-initial-tech-stack.md
        └── 002-database-choice.md
```

**Naming Conventions:**

- Requirements: `requirements.md` or `requirements-v2.md` for major revisions
- Design docs: `design/<feature-name>.md` (lowercase, hyphens)
- ADRs: `adr/<NNN>-<short-title>.md` (numbered, sequential)

---

## Step 3: Version and Review

**Versioning:**

- Include version number in document header
- Update version when content changes materially
- Use semver: `0.1.0` (draft) → `1.0.0` (approved)

**Review Process:**

1. Draft document
2. AI reviews for gaps and clarity
3. Human approves
4. Update status to "Approved"

---

## Claude Tips

- Use **Plan Mode** when drafting documents
- Ask Claude to review: *"What's missing or unclear in this document?"*
- Have Claude generate content: *"Draft a design doc for feature X"*
- Request alternatives: *"What other approaches should I consider?"*
