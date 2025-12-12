# DALL-E Transparent Background Quick Reference

## Key Points

- DALL-E 3 has **limited native transparency support**
- Best approach: Generate with solid background → Remove background externally
- Request "isolated" or "cutout" style for cleaner results

## Essential Prompt Phrases

✅ **Use these:**
- "isolated on white background"
- "isolated on transparent background" (sometimes works)
- "flat design, no background"
- "cutout style"
- "product photography on white backdrop"

❌ **Avoid these:**
- "realistic shadows"
- "environmental lighting"
- "scene with background"

## Template Prompts

### For Logos/Icons
```
[design description], flat design style, vector art, isolated on transparent background, clean edges
```

### For Characters/Mascots
```
[character description], cartoon style, isolated on white background, no shadow, centered composition
```

### For Product Images
```
[product description], product photography, studio lighting, pure white background, professional, clean
```

### For Sticker Designs
```
[sticker design], bold outlines, vibrant colors, isolated, no background, sticker style
```

## Post-Processing Workflow

1. **Generate** with white background
2. **Download** the image
3. **Use** remove.bg or Photoshop Quick Select
4. **Export** as PNG with alpha channel
5. **Verify** on different backgrounds

## Example: Web Banner Mascot

**Prompt:**
```
A friendly robot mascot waving hello, cute character design, 
simple geometric shapes, isolated on white background, 
flat design style, clean edges, no shadow
```

**After generation:**
1. Upload to remove.bg
2. Download transparent PNG
3. Test on light and dark backgrounds
4. Adjust if needed using image editor

## Tips

- **Simpler = Better:** Flat designs work better for transparency
- **Lighting matters:** Request "flat lighting" or "studio lighting"
- **Edge quality:** Add "clean edges" or "sharp edges" to prompt
- **Composition:** Use "centered" or "isolated" for better cutouts

## Common Issues

| Issue | Solution |
|-------|----------|
| Background has gradient | Request "solid white background" |
| Edges are fuzzy | Add "clean edges, sharp" to prompt |
| Shadow baked in | Add "no shadow, flat lighting" |
| Subject blends with background | Use "high contrast" or darker subject |

## Date: 2025-12-12
