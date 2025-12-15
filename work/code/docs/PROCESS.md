# Delivery Process (Work-Safe)

> **Inherits from:** `home/code/docs/PROCESS.md`  
> **Base process:** See [home/code/docs/PROCESS.md](../../../home/code/docs/PROCESS.md) for the full documentation workflow

This guide adapts the base documentation and delivery process for work context with JPMC policies and compliance requirements.

## Work-Specific Documentation Requirements

### Requirements Documentation
- Use `docs/templates/requirements.md` adapted for compliance
- Include security requirements (SEC-XXX)
- Include compliance requirements (COMP-XXX)
- Document audit and logging requirements
- Link to change management tickets

### Design Documentation
- Capture decisions in `docs/templates/adr.md`
- Include security architecture section
- Document data classification and handling
- Specify audit logging requirements
- Include approval chain and sign-offs

### Backlog Management
- Maintain in approved tracker (Jira, ServiceNow, etc.)
- Mirror high-level items in repository `docs/templates/backlog.md`
- Include change ticket references for each story
- Document compliance gates and approvals

### Reviews
- Enforce required sign-offs:
  - Technical lead approval
  - Security review for security-sensitive changes
  - Architecture review for architectural changes
  - Compliance sign-off for regulated components
- Run automated checks:
  - Security scanning
  - License compliance
  - Code quality gates
  - Dependency vulnerability scans

### Release Process
- Document change tickets and approvals
- Create rollout plans with rollback procedures
- Schedule deployments in approved windows
- Complete required compliance documentation
- Update audit logs and documentation

## Additional Work Requirements

All documentation must be:
- Reviewed and approved through proper channels
- Versioned and change-controlled
- Accessible to audit and compliance teams
- Updated as part of change management process
