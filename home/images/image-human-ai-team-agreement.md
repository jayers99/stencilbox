# Image Generation Human-AI Team Agreement

> **Inherits from:** [shared/agreements/human-ai-team-agreement.md](../../shared/agreements/human-ai-team-agreement.md)
>
> Read the base agreement first. This document adds image-generation-specific workflow.

A workflow for creating images with AI assistance across DALL-E, Midjourney, and Gemini/Nano Banana Pro.

## 1. Collaboration Model

**Human responsibilities:**
- Provide creative direction and intent
- Curate reference images and style guides
- Make final selections from variations
- Maintain consistency across a project

**AI responsibilities:**
- Translate intent into tool-specific prompts
- Suggest style keywords and modifiers
- Iterate based on feedback
- Document successful prompts for reuse

## 2. Tool-Specific Conventions

### DALL-E (ChatGPT)

| Aspect | Convention |
|--------|------------|
| Strengths | Natural language, photorealism, text in images |
| Prompt style | Conversational, detailed descriptions |
| Iteration | "Make it more...", "Keep X but change Y" |
| Limitations | Less stylistic control than MJ |
| Transparency | Limited support - use white BG + post-process ([guide](prompts/dalle/transparent-background-quick-ref.md)) |

### Midjourney

| Aspect | Convention |
|--------|------------|
| Strengths | Artistic styles, aesthetics, composition |
| Prompt style | Keywords, parameters (--ar, --v, --style) |
| Iteration | Use variations, remix mode, /describe |
| Parameters | Always specify aspect ratio and version |
| Transparency | No native support - requires post-processing ([guide](prompts/midjourney/transparent-background-quick-ref.md)) |

Common Midjourney parameters:
```
--ar 16:9    # Aspect ratio
--v 6        # Version
--style raw  # Less Midjourney aesthetic
--no [item]  # Negative prompt
--q 2        # Quality
--s 250      # Stylize (0-1000)
```

### Gemini / Nano Banana Pro

| Aspect | Convention |
|--------|------------|
| Strengths | Speed, integration with Google ecosystem |
| Prompt style | Clear, specific descriptions |
| Iteration | Refine through conversation |
| Transparency | Limited - verify alpha channel, may need post-process ([guide](prompts/gemini/transparent-background-quick-ref.md)) |

## 3. Workflow Phases

### Phase 1: Concept
1. Human describes the vision (mood, subject, purpose)
2. AI asks clarifying questions
3. AI suggests style references and keywords
4. Human approves direction

### Phase 2: Exploration
1. AI generates initial prompts for chosen tool
2. Human runs prompts, shares results
3. Identify what's working and what isn't
4. AI refines prompts based on feedback

### Phase 3: Refinement
1. Narrow down to best candidates
2. Iterate on details (lighting, composition, color)
3. Generate variations of winners
4. Human makes final selection

### Phase 4: Documentation
1. Save successful prompts to appropriate folder
2. Note what worked and why
3. Tag with style/subject for future reference

## 4. Quality Standards

**A good image generation session produces:**
- [ ] Images that match the stated intent
- [ ] Documented prompts for reproduction
- [ ] Style notes for consistency
- [ ] Learnings captured for future use
- [ ] Proper transparency if required (see [transparent background guide](prompts/transparent-background.md))

**Red flags to watch for:**
- Prompt drift (losing original intent)
- Over-iteration (diminishing returns)
- Style inconsistency within a project
- Fake transparency (checkerboard patterns instead of alpha channel)

## 5. Project Consistency

When working on a series (like bowerbird illustrations):

1. **Establish a style guide** before generating
   - Color palette
   - Art style keywords
   - Consistent parameters
   - Example reference images

2. **Use prompt templates**
   ```
   [subject] in the style of [style guide], [lighting], [composition], [mood]
   ```

3. **Document the "hero prompt"** that captures your look

## 6. Iteration Protocol

**Feedback format:**
- "More X, less Y"
- "Keep [specific element], change [specific element]"
- "Try a different [aspect]"
- "This is close, but [specific issue]"

**When to stop:**
- You have what you need
- 3 rounds without meaningful improvement
- You're changing direction, not refining

## 7. File Organization

```
images/
├── prompts/
│   ├── dalle/          # DALL-E specific prompts
│   ├── midjourney/     # MJ prompts with parameters
│   ├── gemini/         # Gemini/Nano Banana prompts
│   └── transparent-background.md  # Comprehensive transparency guide
├── styles/             # Style guides and references
└── workflows/          # Multi-step generation processes
```

**Transparency Resources:**
- [Comprehensive transparency guide](prompts/transparent-background.md) - Full guide for all tools
- [DALL-E quick reference](prompts/dalle/transparent-background-quick-ref.md)
- [Midjourney quick reference](prompts/midjourney/transparent-background-quick-ref.md)
- [Gemini quick reference](prompts/gemini/transparent-background-quick-ref.md)

## 8. Prompt Documentation Format

```markdown
## [Descriptive Name]

**Tool:** Midjourney v6
**Purpose:** [What this is for]
**Date:** [When it worked]

**Prompt:**
[Full prompt text with parameters]

**Result:** [Link or description]

**Notes:**
- What worked well
- Variations tried
- When to use this
```

## 9. Communication Shortcuts

| Say | Means |
|-----|-------|
| "Warmer" | More orange/yellow tones, cozier feel |
| "Cooler" | More blue tones, calmer feel |
| "Punch it up" | More contrast, saturation, drama |
| "Softer" | Less contrast, more diffused |
| "More breathing room" | More negative space |
| "Tighter" | Closer crop, less background |
| "Make it transparent" | Remove background, save with alpha channel |
| "Isolated" | Subject only, no background elements |
| "Clean edges" | Sharp alpha channel, no fringing |
