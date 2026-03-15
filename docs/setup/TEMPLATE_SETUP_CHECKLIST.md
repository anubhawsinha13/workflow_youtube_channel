# Creatomate Blank Template Setup Checklist

## Quick Reference

Since your template is blank, here's exactly what to create:

## Required Elements

### For Each Scene (Scene 1, Scene 2, Scene 3, etc.):

1. **Image Element**
   - Name: `Image-1`, `Image-2`, `Image-3`, etc.
   - Type: Image/Photo
   - Position: Full screen or as desired

2. **Audio Element**
   - Name: `Voiceover-1`, `Voiceover-2`, `Voiceover-3`, etc.
   - Type: Audio/Voiceover
   - Position: Timeline (matches scene duration)

3. **Text Element** (Optional - for subtitles)
   - Name: `Text-1`, `Text-2`, `Text-3`, etc.
   - Type: Text
   - Position: Bottom center (or as desired)

## Element Naming Rules

✅ **DO:**
- `Image-1` (with hyphen)
- `Voiceover-1` (with hyphen)
- `Text-1` (with hyphen)
- Start from 1 (not 0)
- Match scene number (Scene 1 → Image-1)

❌ **DON'T:**
- `image-1` (lowercase)
- `Image_1` (underscore)
- `Image1` (no hyphen)
- `Image-0` (start from 0)

## Example: 6-Scene Template

```
Scene 1:
├── Image-1 (image element)
├── Voiceover-1 (audio element)
└── Text-1 (text element, optional)

Scene 2:
├── Image-2
├── Voiceover-2
└── Text-2

Scene 3:
├── Image-3
├── Voiceover-3
└── Text-3

... and so on for all scenes
```

## Setup Steps

1. **Open Creatomate** → Your blank template
2. **Add Image Element** → Name it `Image-1`
3. **Add Audio Element** → Name it `Voiceover-1`
4. **Add Text Element** → Name it `Text-1` (optional)
5. **Repeat for Scene 2**: `Image-2`, `Voiceover-2`, `Text-2`
6. **Repeat for all scenes**
7. **Save template**
8. **Copy Template ID** → Add to `.env`

## Verification

After setup, verify:
- ✅ All elements have correct names (`Image-1`, `Voiceover-1`, etc.)
- ✅ Names match scene numbers (Scene 1 → Image-1)
- ✅ Template ID is in `.env`
- ✅ Timeline is configured correctly

## That's It!

Once elements are named correctly, the code will automatically match them!
