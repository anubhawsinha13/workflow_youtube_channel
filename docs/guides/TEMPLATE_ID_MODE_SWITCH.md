# Switch to Template ID Mode ✅

## Change Summary

Switched from RenderScript mode to **Template ID mode** to match the Creatomate API format shown in the user's example.

## What Changed

### ✅ 1. Prioritize Template ID Mode
**Updated**: `execution/assemble_video.py` → `build_creatomate_payload()`

**Before**:
```python
# RenderScript mode (preferred - no dashboard template needed)
if renderscript_path:
    # Use RenderScript
else:
    # Use template_id
```

**After**:
```python
# Template ID mode (preferred - requires dashboard template)
template_id = template_id or CREATOMATE_TEMPLATE_ID

if template_id:
    # Use template_id mode
elif renderscript_path:
    # RenderScript mode (fallback only)
```

### ✅ 2. Updated Payload Structure
**Format**: Matches user's example exactly

```python
payload = {
    "template_id": "template_id",
    "modifications": {
        "Image-1.source": "https://...",
        "Voiceover-1.source": "https://...",
        "Text-1.text": "dialogue",
        # ... timing and duration modifications
    }
}
```

### ✅ 3. Added Duration Support
- Uses actual audio file durations (via Mutagen)
- Sets timing and duration for images and text elements
- Calculates cumulative timing for sequential scenes

### ✅ 4. Request Format
**Matches user's example**:
```python
response = requests.post(
    "https://api.creatomate.com/v2/renders",
    json=payload,  # Using json= parameter
    headers=headers
)
```

## Requirements

### 1. Create Template in Creatomate Dashboard
1. Go to Creatomate dashboard
2. Create a new template
3. Add elements with names matching your workflow:
   - `Image-1`, `Image-2`, ..., `Image-6`
   - `Voiceover-1`, `Voiceover-2`, ..., `Voiceover-6`
   - `Text-1`, `Text-2`, ..., `Text-6`
4. Copy the template ID

### 2. Set Environment Variable
Add to `.env`:
```env
CREATOMATE_TEMPLATE_ID=your-template-id-here
```

## Element Names

The template must have these exact element names:
- **Images**: `Image-1`, `Image-2`, `Image-3`, `Image-4`, `Image-5`, `Image-6`
- **Audio**: `Voiceover-1`, `Voiceover-2`, `Voiceover-3`, `Voiceover-4`, `Voiceover-5`, `Voiceover-6`
- **Text**: `Text-1`, `Text-2`, `Text-3`, `Text-4`, `Text-5`, `Text-6`
- **Optional**: `Title`, `Description`

## Modifications Format

The code now sends modifications in this format:
```python
{
    "Image-1.source": "https://...",
    "Image-1.time": 0.0,
    "Image-1.duration": 17.97,
    "Voiceover-1.source": "https://...",
    "Voiceover-1.time": 0.0,
    "Voiceover-1.volume": 100,
    "Text-1.text": "dialogue",
    "Text-1.time": 0.0,
    "Text-1.duration": 17.97,
    # ... for all scenes
}
```

## Benefits

✅ **Matches API Format**: Uses exact format from Creatomate documentation  
✅ **Simpler Structure**: No RenderScript complexity  
✅ **Dashboard Control**: Template can be edited in dashboard  
✅ **Duration Support**: Uses actual audio durations  
✅ **Timing Support**: Sets correct timing for all elements  

## Next Steps

1. **Create Template**: Create template in Creatomate dashboard with correct element names
2. **Set Template ID**: Add `CREATOMATE_TEMPLATE_ID` to `.env`
3. **Test**: Run workflow - should now use template_id mode

## Summary

✅ **Switched**: From RenderScript mode to Template ID mode  
✅ **Format**: Matches user's example exactly  
✅ **Duration**: Uses actual audio file durations  
✅ **Timing**: Sets correct timing for all elements  

The workflow now uses Template ID mode! 🎬
