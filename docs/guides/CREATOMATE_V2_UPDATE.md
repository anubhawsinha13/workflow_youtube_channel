# Creatomate v2 API Integration Update ✅

## Summary

Updated Creatomate integration to use v2 API format based on sample payload from `elevlabs.txt`.

## Key Changes

### 1. API Endpoint Updated
- **Old**: `https://api.creatomate.com/v1/renders`
- **New**: `https://api.creatomate.com/v2/renders` ✅

### 2. Payload Structure - Dot Notation Format

**Old Format (v1):**
```json
{
  "template_id": "template_id",
  "modifications": {
    "Voiceover-1": {
      "source": "audio_url",
      "trim": 0,
      "volume": 100
    },
    "Image-1": {
      "source": "image_url"
    },
    "Text-1": {
      "text": "dialogue"
    }
  }
}
```

**New Format (v2) - Dot Notation:**
```json
{
  "template_id": "template_id",
  "modifications": {
    "Voiceover-1.source": "audio_url",
    "Voiceover-1.trim": 0,
    "Voiceover-1.volume": 100,
    "Image-1.source": "image_url",
    "Text-1.text": "dialogue"
  }
}
```

### 3. Element Naming Patterns

Based on sample payload, Creatomate uses various element naming patterns:

**Text Elements:**
- `IT-Text.text` - Intro text
- `ID-Date.text` - Date text
- `ID-Name.text` - Name text
- `1PC-Caption.text` - Caption text
- `FM-Text.text` - Final/memorial text
- `FT-Name.text` - Final name text

**Image/Photo Elements:**
- `1PC-Photo.source` - Single photo
- `MPP-Photo-{num}.source` - Multi-photo layout
- `SPB-Photo.source` - Single photo background
- `3P-Photo-{num}.source` - Three photo layout
- `2P-Photo-{num}.source` - Two photo layout
- `1PF-Photo.source` - Single photo final
- `1PA-Photo.source` - Single photo alternative

**Audio Elements:**
- `Voiceover-{num}.source` - Voiceover audio
- Audio uses `.source` suffix like images

### 4. Updated Functions

**`build_creatomate_payload()`:**
- ✅ Now uses dot notation for element names
- ✅ Supports element prefix (e.g., `1PC-`, `MPP-`)
- ✅ Text elements use `.text` suffix
- ✅ Image/audio elements use `.source` suffix
- ✅ Flexible element naming

**`render_video()`:**
- ✅ Updated to use v2 API endpoint
- ✅ Proper error handling

**`upload_asset_to_creatomate()`:**
- ✅ Updated to try v2 upload endpoint first
- ✅ Fallback to v1 if v2 fails

### 5. Element Prefix Support

The updated function now supports element prefixes for complex templates:

```python
# Without prefix (default)
modifications = {
    "Voiceover-1.source": "...",
    "Image-1.source": "...",
    "Text-1.text": "..."
}

# With prefix
modifications = {
    "1PC-Voiceover-1.source": "...",
    "1PC-Photo-1.source": "...",
    "1PC-Caption.text": "..."
}
```

## Usage Examples

### Basic Usage (Default Element Names)
```bash
python execution/assemble_video.py script.json audio.json image.json
```

**Result:**
```json
{
  "template_id": "...",
  "modifications": {
    "Voiceover-1.source": "https://...",
    "Image-1.source": "https://...",
    "Text-1.text": "Dialogue text..."
  }
}
```

### With Element Prefix
```bash
python execution/assemble_video.py script.json audio.json image.json template_id "1PC-"
```

**Result:**
```json
{
  "template_id": "...",
  "modifications": {
    "1PC-Voiceover-1.source": "https://...",
    "1PC-Photo-1.source": "https://...",
    "1PC-Caption.text": "Dialogue text..."
  }
}
```

## Sample Payload Reference

From `elevlabs.txt`:
```json
{
  "template_id": "ffe9e01b-1c66-4e12-b597-1b87f5feff7b",
  "modifications": {
    "IT-Text.text": "in loving memory of",
    "ID-Date.text": "12.2.2002 ~ 12.3.2024",
    "ID-Name.text": "Buddy Barker",
    "1PC-Caption.text": "A faithful companion...",
    "1PC-Photo.source": "https://creatomate.com/files/assets/...",
    "MPP-Photo-1.source": "https://creatomate.com/files/assets/...",
    "FM-Text.text": "As we look to the stars...",
    "FT-Name.text": "Buddy"
  }
}
```

## Implementation Details

### Element Mapping
- **Text/Dialogue**: `{element_name}.text`
- **Images/Photos**: `{element_name}.source`
- **Audio/Voiceover**: `{element_name}.source`

### Default Element Names
- Audio: `Voiceover-{scene_num}`
- Images: `Image-{scene_num}`
- Text: `Text-{scene_num}`

### Custom Element Names
Pass `element_prefix` parameter to customize:
- `1PC-` for single photo layouts
- `MPP-` for multi-photo layouts
- `ID-` for intro/date elements
- `FM-`, `FT-` for final elements
- Or any custom prefix

## API Endpoints

### Render (v2)
```
POST https://api.creatomate.com/v2/renders
```

### Upload (v2 with v1 fallback)
```
POST https://api.creatomate.com/v2/uploads  (tried first)
POST https://api.creatomate.com/v1/uploads  (fallback)
```

### Status (v2)
```
GET https://api.creatomate.com/v2/renders/{render_id}
```

## Backward Compatibility

- ✅ Still works with v1 API if v2 fails
- ✅ Supports both nested and dot notation formats
- ✅ Handles various element naming patterns

## Updated Files

1. ✅ `execution/assemble_video.py` - Updated to v2 API format
2. ✅ `CREATOMATE_V2_UPDATE.md` - This documentation

## Notes

- The sample payload shows Creatomate uses UUID format for template IDs
- Asset URLs use `https://creatomate.com/files/assets/{uuid}` format
- Element names are case-sensitive
- Dot notation is required for v2 API

## Next Steps

1. ✅ API endpoint updated to v2
2. ✅ Payload format updated to dot notation
3. ✅ Element prefix support added
4. ⚠️ Test with actual Creatomate template to verify element names
5. ⚠️ Update template documentation with actual element names
