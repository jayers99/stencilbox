# SOD Quick Start Guide

Get started creating your Solution Overview Document in 3 steps.

---

## Step 1: Copy the Seed Prompt

Open `/prompts/sod-wizard-seed.md` and copy the entire seed prompt (the large code block).

**Direct link**: [sod-wizard-seed.md](./prompts/sod-wizard-seed.md)

---

## Step 2: Start Your AI Session

Paste the seed prompt into your preferred AI assistant:
- Claude (claude.ai)
- ChatGPT (chat.openai.com)  
- GitHub Copilot Chat
- Any other LLM interface

The AI will respond and ask: "What project or idea would you like to create an SOD for?"

---

## Step 3: Have a Conversation

Use these simple commands to build your SOD:

### Share your ideas
```
New notes: We need to replicate secrets across AWS regions for disaster recovery
```

### Check progress
```
Show SOD
```

### Finalize
```
Lock the SOD
```

The AI will:
- Organize your notes into the proper SOD sections
- Ask clarifying questions (1-2 at a time)
- Help you fill gaps
- Let you know when the SOD is complete

---

## Example Session

```
You: [Paste seed prompt]

AI: Ready! What project or idea would you like to create an SOD for?

You: New notes: We need cross-region Vault replication for DR purposes

AI: Got it—I've added this to Problem Statement and Functional Overview.
    Questions:
    1. What's driving this—regulatory requirement or proactive planning?
    2. Are there specific RPO/RTO targets?

You: Regulatory requirement. RPO 15 min, RTO 30 min.

AI: Added to Business Context/Drivers and Constraints. 
    Questions:
    1. Which regions are in scope?
    2. Any specific compliance frameworks (PCI, HIPAA, etc.)?

You: Show SOD

AI: [Displays current SOD with all sections]

You: Lock the SOD

AI: Reviewing... Your SOD is comprehensive and ready. Locked!
```

---

## Tips for Success

✅ **Start simple**: Share your initial idea, even if rough  
✅ **Be conversational**: The AI organizes; you just think out loud  
✅ **Iterate freely**: Add notes multiple times over days/weeks  
✅ **Ask for guidance**: "What sections still need work?"  
✅ **Review often**: Use `Show SOD` to see progress  

---

## What's in an SOD?

Your completed SOD will include:

- Problem Statement
- Business Context / Drivers
- Goals
- Non-Goals
- Functional Overview
- High-Level Architecture / Workflow
- Assumptions
- Constraints (Technical, Security, Compliance, Operational)
- Dependencies
- Phases / Components
- Risks & Mitigations
- Open Questions
- Glossary / Definitions

---

## After Your SOD is Complete

1. **Save it**: Copy the final SOD to your project as `SOD.md`
2. **Spike #2**: Analyze the SOD for work breakdown (epics, stories)
3. **Generate Stories**: Convert to Jira-ready tickets

See [README.md](./README.md) for the full workflow.

---

## Need Help?

- **Sample SOD**: See `/samples/sample_sod_aws_vault_replication.md`
- **Full Workflow**: See `/README.md`
- **All Commands**: See `/commands.md`
- **VS Code Snippets**: See `/snippets/sod.code-snippets`

---

## Learn More About SOD Best Practices

📚 **[SOD Resources & Best Practices](./RESOURCES.md)**

Curated learning resources from industry experts:
- Dave Farley's technical design guidance
- Martin Fowler & ThoughtWorks architecture resources
- Books, videos, and courses on solution design
- Practical tools and templates

New to technical design? Start with Dave Farley's [How to Write Better Technical Design Documents](https://www.youtube.com/watch?v=DAlwnyBjmSw)
