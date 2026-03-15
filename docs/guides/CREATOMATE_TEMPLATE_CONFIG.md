# Creatomate Template Configuration Guide

## Issue Identified

The video assembly is using **default element names** (`Image-{num}`, `Voiceover-{num}`), but your Creatomate template may expect **different element names**.

## Current Element Names Being Used

The code currently generates:
- `Image-1.source`, `Image-2.source`, etc. (for images)
- `Voiceover-1.source`, `Voiceover-2.source`, etc. (for audio)
- `Text-1.text`, `Text-2.text`, etc. (for dialogue)

## Your Template Element Names

Based on `creatomate.txt`, your template uses patterns like:
- `1PC-Photo.source` - Single photo
- `MPP-Photo-{num}.source` - Multi-photo layout
- `IT-Text.text` - Intro text
- `ID-Date.text` - Date text
- `FM-Text.text` - Final text

## Solution: Configure Element Names

You have two options:

### Option 1: Use Element Prefix (Quick Fix)

If your template uses a prefix pattern, pass it when running:

```bash
python execution/assemble_video.py \
  script.json \
  audio_files.json \
  image_files.json \
  your_template_id \
  "1PC-"  # Element prefix
```

This will generate:
- `1PC-Photo-1.source`
- `1PC-Voiceover-1.source`
- `1PC-Text-1.text`

### Option 2: Customize Element Names (Recommended)

Update your Creatomate template to use standard names:
- `Image-1`, `Image-2`, etc. (for images)
- `Voiceover-1`, `Voiceover-2`, etc. (for audio)
- `Text-1`, `Text-2`, etc. (for dialogue)

Or update the code to match your template's element names.

## How to Find Your Template Element Names

1. Go to Creatomate dashboard
2. Open your template
3. Check element names in the template editor
4. Update the code to match those names

## Character Folder Issue

**Problem**: All scenes are using the same character image because:
- Character folder only has ONE image: `Gemini_Generated_Image_5c92b65c92b65c92.png`
- The code copies this same image to all 6 scenes

**Solution**: 
1. Add scene-specific character images to `character/` folder:
   - `character_1.png` or `scene_1.png`
   - `character_2.png` or `scene_2.png`
   - etc.

2. OR: Let the system generate scene-specific images (don't use character folder)

## Next Steps

1. **Check your Creatomate template element names**
2. **Update element names in code OR template to match**
3. **Add scene-specific character images OR disable character folder**
