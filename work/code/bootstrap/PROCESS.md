# Bootstrap Process (Work-Safe)

> **Inherits from:** `home/code/bootstrap/PROCESS.md`  
> **Base process:** See [home/code/bootstrap/PROCESS.md](../../../home/code/bootstrap/PROCESS.md) for the full bootstrap workflow

This guide adapts the base bootstrap process for work-safe project setup with compliance requirements.

## Work-Specific Requirements

When bootstrapping projects in a work context, follow the base process but with these adaptations:

### 1. Project Setup
- Define project type and compliance needs
- Verify approved language/runtime versions
- Check for approved base templates or scaffolds

### 2. Repository Creation
- Initialize repo with mandatory files:
  - `README.md` with project overview
  - `CODEOWNERS` with approval chain
  - `SECURITY.md` with security contacts and procedures
  - `WORK_ENVIRONMENT.md` documenting constraints and approvals
- Use internal repository hosting (GitHub Enterprise, Bitbucket, etc.)

### 3. Dependency Management
- Configure dependency sources to internal registries/mirrors
- Do not fetch from public registries unless explicitly approved
- Document any approved external dependencies in `WORK_ENVIRONMENT.md`

### 4. CI/CD Setup
- Set up CI with required checks:
  - Security scanning (Snyk, SonarQube, etc.)
  - License compliance checking
  - Dependency vulnerability scanning
  - Code quality gates
- Integrate with approved build systems

### 5. Secrets Management
- Integrate with approved vault mechanisms (HashiCorp Vault, CyberArk, etc.)
- Never commit secrets to repository
- Document secret access patterns in `SECURITY.md`

### 6. Documentation
- Document all deviations from standard process in `WORK_ENVIRONMENT.md`
- Include approval references and waivers
- List constraints and their business justification

## Notes
- Prefer internal templates and generators when available
- Request waivers through proper channels if needed
- Keep security and compliance teams informed throughout setup
