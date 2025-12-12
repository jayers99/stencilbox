# Transparent Background Resources - Quick Start

If you need images with transparent backgrounds for web banners, stickers, logos, or any design that needs to work on multiple backgrounds, start here.

## The Problem

AI image generators often produce:
- **Fake transparency**: Checkerboard patterns baked into the image (not real alpha channel)
- **Solid backgrounds**: That need to be removed manually
- **Background artifacts**: Shadows, gradients, or environmental elements

## The Solution

This directory contains **prompt guardrails** - specific keywords, phrases, and workflows to get true transparent backgrounds from DALL-E, Midjourney, and Gemini.

## Quick Navigation

### Choose Your Tool

**DALL-E (ChatGPT):**
- 📖 [Quick Reference](dalle/transparent-background-quick-ref.md)
- 📝 [Example: Web Banner](dalle/example-web-banner-transparent.md)
- ⚡ **Quick tip:** Request "isolated on white background" + post-process

**Midjourney:**
- 📖 [Quick Reference](midjourney/transparent-background-quick-ref.md)
- 📝 [Example: Die-Cut Sticker](midjourney/example-sticker-transparent.md)
- ⚡ **Quick tip:** Use `--no shadow, background` + post-process required

**Gemini / Nano Banana Pro:**
- 📖 [Quick Reference](gemini/transparent-background-quick-ref.md)
- 📝 [Example: Logo Design](gemini/example-logo-transparent.md)
- ⚡ **Quick tip:** Request "transparent background with alpha channel" + verify

### Learn More

- 📚 [Comprehensive Guide](transparent-background.md) - Deep dive into all three tools
- 🤝 [Team Agreement](../Image_Human_AI_Team_Agreement.md) - Full image generation workflow

## Common Use Cases

### Web Banners (Light/Dark Mode)
→ Use [DALL-E guide](dalle/transparent-background-quick-ref.md) or [example](dalle/example-web-banner-transparent.md)

**Key phrases:**
- "isolated on white background"
- "flat design, no shadow"
- "clean edges"

**Post-process:** remove.bg or Photoshop Quick Select

### Die-Cut Stickers
→ Use [Midjourney guide](midjourney/transparent-background-quick-ref.md) or [example](midjourney/example-sticker-transparent.md)

**Key phrases:**
- "pure white background"
- "bold outlines, no shadow"
- "--no shadow, background"

**Post-process:** Required - use Photoshop or GIMP

### Logos / Icons
→ Use [Gemini guide](gemini/transparent-background-quick-ref.md) or [example](gemini/example-logo-transparent.md)

**Key phrases:**
- "transparent background with alpha channel"
- "vector style, clean edges"
- "no shadow, optimized for web"

**Verify:** Always check for real alpha channel vs fake checkerboard

## Essential Keywords Across All Tools

✅ **Use these:**
- "isolated"
- "transparent background"
- "clean edges"
- "no shadow"
- "flat design"
- "cutout style"

❌ **Avoid these:**
- "realistic shadows"
- "environmental"
- "atmospheric"
- "scene"

## Verification Checklist

After generating any image that needs transparency:

- [ ] File is PNG (not JPG)
- [ ] Alpha channel exists (check file properties)
- [ ] No checkerboard pattern baked in
- [ ] Edges are clean (no white/colored fringe)
- [ ] Works on black background
- [ ] Works on white background
- [ ] Works on colored backgrounds

## Post-Processing Tools

| Tool | Best For | Cost |
|------|----------|------|
| [remove.bg](https://remove.bg) | Fast automatic removal | Free tier |
| Photoshop | Professional refinement | Subscription |
| GIMP | Free alternative | Free |
| Figma | Design integration | Free tier |

## Need Help?

1. **Quick fix:** Check the quick reference for your tool
2. **Detailed workflow:** See the comprehensive guide
3. **Real example:** Look at the example prompts
4. **Best practices:** Review the Team Agreement

## Contributing

Found a prompt that works great? Document it using the format from the [Team Agreement](../Image_Human_AI_Team_Agreement.md#8-prompt-documentation-format) and add it to the appropriate tool directory.

---

**Last updated:** 2025-12-12
**Issue reference:** Feature request for transparent background prompt behavior
