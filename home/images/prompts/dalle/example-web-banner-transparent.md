## Web Banner with Transparent Background

**Tool:** DALL-E 3 (ChatGPT)
**Purpose:** Website header banner that works on light and dark backgrounds
**Date:** 2025-12-12

**Prompt:**
```
Modern tech banner design featuring abstract geometric shapes with gradient colors from blue to purple, 
minimalist style, wide format composition, isolated on white background, clean edges, no shadow, 
flat design optimized for web use
```

**Post-processing:**
1. Download generated image
2. Open in Photoshop or use remove.bg
3. Select white background with Magic Wand (tolerance 32)
4. Delete background and add layer mask
5. Refine edges: Select > Modify > Contract (1px) then Feather (1px)
6. Export as PNG-24 with transparency
7. Test on black and white backgrounds

**Result:** Clean banner with transparent background that scales well on any background color

**Notes:**
- "Isolated on white background" worked better than "transparent background" 
- "Clean edges" helped reduce fringing
- "No shadow" prevented unwanted background artifacts
- "Flat design" kept lighting simple for easier background removal
- Testing on both light/dark backgrounds revealed need for slight edge feathering

**Variations tried:**
- First attempt without "clean edges" had noticeable fringing
- Tried "transparent background" directly but got checkered pattern baked in
- White background + post-process gave best results

**When to use this:**
- Web banners that need to adapt to theme changes
- Headers that overlay on photos
- UI elements requiring flexibility
- Any design that needs to work on multiple background colors
