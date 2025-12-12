# Midjourney Transparent Background Quick Reference

## Key Points

- Midjourney **does NOT support native transparency**
- Always requires post-processing for transparent backgrounds
- Strategy: Generate with clean, simple background → Remove externally

## Essential Parameters & Keywords

✅ **Use these parameters:**
```
--v 6                    # Latest version
--ar 1:1                 # Square format (best for stickers/logos)
--ar 16:9                # Wide format (banners)
--no background          # Reduces background complexity
--no shadow              # Prevents shadow artifacts
--style raw              # Less stylized (easier removal)
```

✅ **Use these keywords:**
- "pure white background"
- "solid black background"
- "isolated"
- "product photography"
- "studio lighting"
- "clean white backdrop"
- "simple background"

❌ **Avoid these:**
- "environmental"
- "atmospheric"
- "realistic scene"
- "complex background"

## Template Prompts

### For Sticker Designs
```
[subject], vibrant colors, bold outlines, pure white background, 
centered, isolated --no shadow, background details --v 6 --ar 1:1
```

### For Logo/Icon Designs
```
[design], minimalist, geometric, clean white background, 
professional --v 6 --ar 1:1 --style raw
```

### For Character Art
```
[character], cartoon style, solid white background, 
full body, centered composition, no shadow --v 6 --ar 1:1
```

### For Web Banners
```
[banner elements], modern design, pure white background, 
clean layout --no shadow --v 6 --ar 16:9
```

## Post-Processing Workflow

1. **Generate** in Midjourney with solid background
2. **Upscale** the best result (U1, U2, U3, or U4)
3. **Download** the upscaled image
4. **Remove background:**
   - Option A: remove.bg (fast, automatic)
   - Option B: Photoshop Magic Wand + Refine Edge
   - Option C: GIMP layer mask
5. **Export** as PNG with alpha channel
6. **Test** on different backgrounds

## Parameter Guide for Transparency Prep

| Parameter | Value | Purpose |
|-----------|-------|---------|
| `--ar` | `1:1` | Square (stickers, icons) |
| `--ar` | `16:9` | Wide (banners) |
| `--ar` | `4:5` | Portrait (social media) |
| `--no` | `shadow` | Cleaner edges |
| `--no` | `background` | Simpler to remove |
| `--style` | `raw` | Less MJ aesthetic |
| `--v` | `6` | Latest features |

## Example: Die-Cut Sticker

**Prompt:**
```
Cute kawaii avocado character with happy face, bold black outline, 
vibrant green color, sticker art style, pure white background, 
centered --no shadow, gradients --v 6 --ar 1:1
```

**After Midjourney:**
1. Upscale best variant
2. Download PNG
3. Open in Photoshop
4. Magic Wand → Select white background
5. Delete → Add layer mask for refinement
6. Export as PNG-24 with transparency
7. Verify clean edges

## Tips

- **White vs Black background:** Use white for light subjects, black for light/glow effects
- **Negative prompts:** `--no` parameter removes unwanted elements
- **Composition:** "centered" keeps subject away from edges
- **Test variations:** Generate 4 options, pick cleanest background

## Background Removal Best Practices

### In Photoshop
1. Magic Wand (W) → Click background
2. Select → Modify → Expand (2px)
3. Select → Modify → Feather (1px)
4. Layer → Layer Mask → Hide Selection
5. Layer → Matting → Defringe (2px)

### In GIMP
1. Select → By Color → Click background
2. Select → Grow (2px)
3. Select → Feather (1px)
4. Layer → Transparency → Add Alpha Channel
5. Edit → Clear

## Common Issues

| Issue | Solution |
|-------|----------|
| Background too complex | Use `--no background, scenery, environment` |
| Subject has shadow | Add `--no shadow` parameter |
| Edges blend with BG | Request higher contrast subject |
| Can't select background cleanly | Generate with pure white/black BG |

## Remix Mode Tip

If first generation has complex background:

```
/settings → Enable Remix Mode
Click 🔄 (Vary button)
Add to prompt: ", pure white background --no shadow"
```

## Date: 2025-12-12
