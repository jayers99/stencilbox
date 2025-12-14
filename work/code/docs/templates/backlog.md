# Backlog (Work)

> **Note:** This extends the base template from `shared/code/templates/docs/backlog.md`
> 
> See [shared/code/templates/docs/backlog.md](../../../../shared/code/templates/docs/backlog.md) for the full template.

## Work-Specific Requirements

For work projects, backlog items must include:
- **Change ticket references** - Link to approved change requests
- **Security classification** - Data sensitivity level
- **Compliance gates** - Required reviews before deployment
- **Approvals** - Who must sign off before work begins
- **Risk assessment** - Impact and rollback procedures

## Story Template (Work)

```markdown
- [ ] **STORY-N** [Short description] (X pts)
  - Requirement: FR-XXX
  - Change Ticket: CHG-XXXXX
  - Security: [Public/Internal/Confidential/Restricted]
  - Approvals Required: [Architecture/Security/Change Board]
  - Risk Level: [Low/Medium/High]
  - Rollback Plan: [Description]
  
  **Acceptance Criteria:**
  - [ ] Functional: Given X, when Y, then Z
  - [ ] Security: [Security requirements validated]
  - [ ] Compliance: [Required approvals obtained]
```
