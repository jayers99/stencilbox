## Logo with Transparent Background

**Tool:** Gemini (Imagen)
**Purpose:** Company logo that works on any background
**Date:** 2025-12-12

**Prompt:**
```
I need a professional logo design for a tech startup. 
Create a minimalist geometric logo featuring overlapping circles 
forming an abstract letter "T", modern clean lines, gradient from 
teal to blue, transparent background with alpha channel, vector style, 
no shadow, optimized for web and print use. This needs to work on 
both light and dark backgrounds.
```

**Verification steps:**
1. Download generated image
2. Check file extension is PNG (not JPG)
3. Open in Preview/image editor
4. Verify Properties show "Alpha Channel" or "RGBA"
5. Test on black background in image editor
6. Test on white background
7. Check for any checkerboard pattern baked into image
8. If checkerboard exists, it's fake transparency - regenerate

**Post-processing (if needed):**
1. If Gemini produced fake transparency (checkerboard):
   - Regenerate with "solid white background" instead
   - Use remove.bg or Photoshop to remove background manually
2. If edges have color fringe:
   - In Photoshop: Layer > Matting > Defringe (1-2px)
   - Or: Layer > Matting > Remove White Matte
3. Export as PNG-24 with transparency

**Result:** Logo with true alpha channel transparency

**Notes:**
- Explaining the use case ("works on both light and dark backgrounds") helped Gemini understand requirements
- "Transparent background with alpha channel" was more explicit than just "transparent"
- "Vector style" helped create clean, sharp edges
- "No shadow" prevented unwanted background artifacts
- Always verify the alpha channel - Gemini sometimes produces fake transparency
- First generation had true transparency, no post-processing needed

**Variations tried:**
- First attempt: just "transparent background" - got checkerboard pattern baked in
- Second attempt: added "with alpha channel" - got true transparency
- Third attempt: explained full use case - best results

**When to use this:**
- Company logos
- App icons
- Brand marks
- Any design needing background flexibility
- Designs for both web and print

**Testing checklist:**
- [ ] File is PNG format
- [ ] Alpha channel exists in file properties
- [ ] Looks correct on black background
- [ ] Looks correct on white background
- [ ] Edges are clean with no fringing
- [ ] No checkerboard pattern baked in

**Export specifications:**
- Web: PNG, 72-144 DPI, optimized file size
- Print: PNG, 300 DPI minimum, uncompressed
- Both: Include SVG version if possible for scaling
