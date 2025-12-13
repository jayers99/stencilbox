# Discovery Process (Work Context)

> **Inherits from:** `home/code/discovery/PROCESS.md`  
> **Base process:** See [home/code/discovery/PROCESS.md](../../home/code/discovery/PROCESS.md) for the full discovery workflow

This guide adapts the base discovery process for work constraints and compliance requirements.

## Work-Specific Considerations

When running discovery in a work context, additionally address:

- **Problem Statement:** Capture business need and constraints, including regulatory requirements
- **Stakeholders:** List approvers and domain contacts (architecture, security, compliance)
- **Risks & Compliance:** Enumerate regulatory or data restrictions (SOX, PCI, data classification)
- **Validation Plan:** Define safe experiments aligned with policies (no production data in dev)
- **MVP Scope:** Balance value with compliance and supportability requirements

## Additional Steps for Work Context

### Before Step 1: Check Approvals
- [ ] Is this effort approved via change management?
- [ ] Do we have architecture sign-off to proceed?
- [ ] Is there budget allocated for this work?

### During Step 2: Enhanced Problem Statement
Include in problem statement:
- Compliance requirements (which regulations apply?)
- Data classification (what data sensitivity levels?)
- Approval chain (who must sign off?)

### During Step 3: Risk Assessment
Additional validation questions for work:
- What are the security implications?
- What data will this touch and what's its classification?
- What are the compliance requirements?
- What's the change management process?
- What's the rollback plan?

### During Step 4: MVP Scoping with Constraints
Consider work constraints when scoping MVP:
- Can we use approved tools only?
- Does this require new approvals or waivers?
- What's the minimum security/compliance requirements?
- What testing/validation is required before production?

## Outputs

Same as base process, but with additional work-specific content in each artifact.
