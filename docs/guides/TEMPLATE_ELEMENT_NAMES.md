# Creatomate Template Element Names Configuration

## Problem

The video was generated but may not match expectations because:

1. **Character Images**: All scenes used the same character image (only one image in `character/` folder)
2. **Template Element Names**: Code uses default names (`Image-{num}`, `Voiceover-{num}`) but template may expect different names

## Current Element Names

The code generates these element names by default:
- `Image-1.source`, `Image-2.source`, etc. (for images)
- `Voiceover-1.source`, `Voiceover-2.source`, etc. (for audio)
- `Text-1.text`, `Text-2.text`, etc. (for dialogue)

## Your Template (from creatomate.txt)

Your template uses these patterns:
- `1PC-Photo.source` - Single photo
- `MPP-Photo-{num}.source` - Multi-photo layout
- `IT-Text.text` - Intro text
- `ID-Date.text` - Date text
- `FM-Text.text` - Final text

## Solution Options

### Option 1: Use Element Prefix

Pass an element prefix when running the script:

```bash
python execution/assemble_video.py \
  script.json \
  audio_files.json \
  image_files.json \
  your_template_id \
  "1PC-"  # Element prefix
```

This generates:
- `1PC-Photo-1.source`
- `1PC-Voiceover-1.source`
- `1PC-Text-1.text`

### Option 2: Update Your Creatomate Template

Rename elements in your Creatomate template to match:
- `Image-1`, `Image-2`, etc. (for images)
- `Voiceover-1`, `Voiceover-2`, etc. (for audio)
- `Text-1`, `Text-2`, etc. (for dialogue)

### Option 3: Custom Element Mapping

Update the code to match your specific template element names.

## Character Folder Fix

**Issue**: Only one character image exists, so all scenes use the same image.

**Solutions**:
1. Add scene-specific images to `character/`:
   - `character_1.png`, `character_2.png`, etc.
   - OR `scene_1.png`, `scene_2.png`, etc.

2. Remove the single character image to force scene-specific generation

3. The code now skips using a single generic character image for all scenes

## Next Steps

1. Check your Creatomate template element names
2. Either:
   - Update template to use `Image-{num}`, `Voiceover-{num}`
   - OR pass element prefix when running script
   - OR customize element names in code
3. Add scene-specific character images OR regenerate visuals
