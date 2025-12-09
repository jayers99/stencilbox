# Bootstrap Process

> **AI Instructions:** When the Human is ready to start a new project (after Discovery phase), read this file first. Help them select a project type and execute the bootstrap.

---

## Prerequisites

Before bootstrapping, confirm:

- [ ] Discovery phase is complete (`discovery/mvp_scope.md` exists and is filled out)
- [ ] Human can describe the project in one sentence
- [ ] Project type is identified

---

## Step 1: Select Project Type

**Available Project Types:**

| Type | Directory | Description |
|------|-----------|-------------|
| Python CLI | `project-types/python-cli/` | Command-line tool with DDD architecture |
| *(more coming)* | | |

**AI Actions:**

1. Ask: *"What type of project is this? CLI tool, web API, frontend app, etc.?"*
2. Match to available project type or identify need for new scaffold
3. Read the project type's `SCAFFOLD.md` for specific instructions

---

## Step 2: Gather Project Details

**AI Actions:**

1. Read the selected project type's `SCAFFOLD.md`
2. Ask Human for required details (name, description, etc.)
3. Validate naming conventions and constraints

**Common Details (all project types):**

- Project name (package-safe, lowercase, underscores)
- Short description (1-2 sentences)
- Repository location

---

## Step 3: Create Repository

**AI Actions:**

1. Create directory structure per project type scaffold
2. Initialize git repository
3. Create initial files from templates
4. Make initial commit

**Checklist:**

- [ ] Repository created
- [ ] .gitignore appropriate for tech stack
- [ ] README.md with project description
- [ ] LICENSE file (if applicable)
- [ ] Initial commit made

---

## Step 4: Configure Environment

**AI Actions:**

1. Set up dependency management per project type
2. Create `.env.example` if secrets are needed
3. Verify setup instructions work

**Checklist:**

- [ ] Dependencies installed
- [ ] Development environment runs
- [ ] Basic smoke test passes

---

## Step 5: Configure AI Permissions

**AI Actions:**

1. Create `.claude/settings.json` with appropriate permissions
2. Review guard rails with Human
3. Confirm allowed/denied commands

---

## Exit Criteria

Bootstrap is complete when:

- [ ] Repository exists with initial structure
- [ ] `git status` shows clean working tree
- [ ] README has setup instructions that work
- [ ] Human can run a basic command/test
- [ ] AI permissions are configured

**Next Phase:** Requirements & Design (Section 3 of Team Agreement)

---

## Files in This Directory

| File | Purpose |
|------|---------|
| `project-types/` | Directory containing scaffolds for each project type |
