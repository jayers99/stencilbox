# SOD System - File Guide

Quick reference for all files in the SOD system and how they work together.

---

## For New Users (Start Here! 👇)

1. **[QUICKSTART.md](./QUICKSTART.md)** - 3-minute guide to get started
   - Copy seed prompt
   - Paste into AI
   - Start conversation

2. **[prompts/sod-wizard-seed.md](./prompts/sod-wizard-seed.md)** - The seed prompt itself
   - Complete, ready-to-use prompt
   - Copy entire code block
   - Use with any AI assistant

---

## Reference Files

3. **[SOD.md](./SOD.md)** - SOD template structure
   - Lists all required sections
   - Use as a checklist
   - Quick reference

4. **[samples/sample_sod_aws_vault_replication.md](./samples/sample_sod_aws_vault_replication.md)** - Example SOD
   - See what a complete SOD looks like
   - Real-world example
   - Reference for your own SOD

5. **[commands.md](./commands.md)** - Quick command reference
   - Speed Mode commands
   - Copy-paste ready
   - Cheat sheet

6. **[snippets/sod.code-snippets](./snippets/sod.code-snippets)** - VS Code snippets
   - Install in VS Code
   - Type prefixes to auto-complete
   - Optional productivity boost

---

## Learning & Best Practices

7. **[RESOURCES.md](./RESOURCES.md)** - SOD learning resources ⭐ NEW
   - Dave Farley's technical design guidance
   - ThoughtWorks & Martin Fowler architecture resources
   - Books, videos, and courses
   - Practical tools and templates

---

## Advanced/Full Workflow

8. **[README.md](./README.md)** - Complete system documentation
   - Full workflow (Spike #1 → SOD → Spike #2 → Stories)
   - Behavior model
   - Table of contents for everything

9. **[prompts/master.md](./prompts/master.md)** - Master unified prompt
   - All four behaviors in one prompt
   - For experienced users
   - Full lifecycle support

---

## Testing & Validation

10. **[TEST_SCENARIO.md](./TEST_SCENARIO.md)** - Test case for the wizard
   - Example conversation flow
   - Manual testing instructions
   - Verification checklist

---

## File Relationship Diagram

```
┌─────────────────────────────────────────────────────────┐
│                    NEW USER PATH                         │
└─────────────────────────────────────────────────────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │  QUICKSTART.md   │ ← Start here!
                  └────────┬─────────┘
                           │
                           ▼
           ┌───────────────────────────────┐
           │ prompts/sod-wizard-seed.md    │ ← Copy this prompt
           └───────────┬───────────────────┘
                       │
                       ▼
           ┌─────────────────────────┐
           │   Paste into AI Chat    │
           │  (Claude, ChatGPT, etc) │
           └──────────┬──────────────┘
                      │
                      ▼
              ┌───────────────┐
              │ Have Convo    │
              │ Build your SOD│
              └───────┬───────┘
                      │
                      ▼
              ┌───────────────┐
              │  Lock SOD     │
              │  Save to file │
              └───────────────┘

┌─────────────────────────────────────────────────────────┐
│                  REFERENCE FILES                         │
└─────────────────────────────────────────────────────────┘

       ┌──────────────┐         ┌──────────────────┐
       │   SOD.md     │         │   samples/       │
       │  (structure) │         │sample_sod_*.md   │
       └──────────────┘         └──────────────────┘
              │                          │
              └──────────┬───────────────┘
                         │
                         ▼
                 What to include?
                 What does it look like?

       ┌──────────────┐         ┌──────────────────┐
       │ commands.md  │         │  snippets/       │
       │ (shortcuts)  │         │*.code-snippets   │
       └──────────────┘         └──────────────────┘
              │                          │
              └──────────┬───────────────┘
                         │
                         ▼
                 Speed up workflow

       ┌──────────────────────────────────┐
       │      RESOURCES.md                │
       │  (Learning & Best Practices)     │
       └──────────────────────────────────┘
                         │
                         ▼
         Dave Farley, ThoughtWorks,
         Books, Videos, Courses


┌─────────────────────────────────────────────────────────┐
│                   ADVANCED PATH                          │
└─────────────────────────────────────────────────────────┘

                  ┌──────────────────┐
                  │   README.md      │ ← Full documentation
                  └────────┬─────────┘
                           │
                           ▼
           ┌────────────────────────────────┐
           │  prompts/master.md             │ ← All behaviors
           │  (Spike #1 → SOD → Spike #2    │   in one prompt
           │   → Story Generation)          │
           └────────────────────────────────┘
```

---

## Typical User Journey

### First Time User
1. Read `QUICKSTART.md` (3 min)
2. Copy prompt from `prompts/sod-wizard-seed.md`
3. Paste into AI and start conversation
4. Reference `samples/sample_sod_*.md` if stuck
5. Save completed SOD to your project

### Regular User
1. Copy prompt from `prompts/sod-wizard-seed.md`
2. Type `New notes: ...` to add ideas
3. Type `Show SOD` to check progress
4. Type `Lock the SOD` when done
5. Use `commands.md` for quick reference

### Power User
1. Use `prompts/master.md` for full workflow
2. Install `snippets/*.code-snippets` in VS Code
3. Use Speed Mode commands for rapid iteration
4. Generate Spike #1, SOD, Spike #2, and Stories all in one session

---

## File Sizes

| File | Lines | Purpose |
|------|-------|---------|
| `RESOURCES.md` | 185 | Learning resources & best practices ⭐ |
| `FILE_GUIDE.md` | 195 | Navigation guide |
| `QUICKSTART.md` | 131 | Getting started guide |
| `prompts/sod-wizard-seed.md` | 127 | The seed prompt to copy |
| `prompts/master.md` | 159 | Full unified prompt |
| `TEST_SCENARIO.md` | 155 | Test case and validation |
| `README.md` | 278 | Complete documentation |
| `SOD.md` | 15 | Template structure |
| `commands.md` | 26 | Command reference |
| `samples/sample_sod_*.md` | varies | Example SOD |
| `snippets/*.code-snippets` | varies | VS Code integration |

---

## Next Steps After Creating Your SOD

1. **Save it**: Copy final SOD to your project as `SOD.md`
2. **Share it**: Review with stakeholders
3. **Spike #2**: Use `Generate Spike 2` to break down into stories
4. **Story Generation**: Use `Convert SOD to stories` for Jira tickets
5. **Execute**: Start building! 🚀

---
