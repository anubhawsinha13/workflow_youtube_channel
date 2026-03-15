# Creatomate RenderScript API Template - Complete Solution ✅

## Summary

✅ **Created a programmatic template solution** using Creatomate's RenderScript API  
✅ **No dashboard template needed** - everything is done via API  
✅ **Exact element names** matching your workflow: `Image-{num}`, `Voiceover-{num}`, `Text-{num}`  
✅ **Integrated with existing workflow** - `assemble_video.py` now supports RenderScript  

## What Was Created

### 1. RenderScript Template Generator
**File**: `execution/create_creatomate_template.py`

Generates a Creatomate RenderScript JSON structure with:
- Exact element names: `Image-1`, `Image-2`, ..., `Voiceover-1`, `Voiceover-2`, ..., `Text-1`, `Text-2`, ...
- Full video structure: composition, timing, layout
- Configurable: scenes, resolution, duration

**Usage:**
```bash
python execution/create_creatomate_template.py --scenes 6 --output creatomate_renderscript_template.json
```

### 2. Generated Template File
**File**: `creatomate_renderscript_template.json`

A complete RenderScript JSON with:
- 6 scenes (configurable)
- 1920x1080 resolution
- 5 seconds per scene
- All elements properly named

### 3. Updated Video Assembly Script
**File**: `execution/assemble_video.py`

Now supports two modes:
1. **RenderScript mode** (preferred): Uses JSON template, no dashboard needed
2. **Template ID mode**: Uses dashboard template (existing functionality)

**New features:**
- `renderscript_path` parameter
- `CREATOMATE_RENDERSCRIPT_PATH` environment variable support
- CLI flag: `--renderscript path/to/template.json`

## How to Use

### Option 1: Set Environment Variable (Recommended)

Add to `.env`:
```env
CREATOMATE_RENDERSCRIPT_PATH=creatomate_renderscript_template.json
```

Then use `assemble_video.py` as normal - it will automatically use RenderScript!

### Option 2: Use CLI Flag

```bash
python execution/assemble_video.py \
  script.json \
  audio_files.json \
  image_files.json \
  --renderscript creatomate_renderscript_template.json \
  project_name
```

### Option 3: Direct API Usage

```python
import requests
import json

# Load RenderScript
with open("creatomate_renderscript_template.json") as f:
    renderscript = json.load(f)

# Prepare modifications
modifications = {
    "Image-1.source": "https://your-image-1.jpg",
    "Voiceover-1.source": "https://your-audio-1.mp3",
    "Text-1.text": "Scene 1 dialogue",
    # ... continue for all scenes
}

# Create video
payload = {
    "source": renderscript,
    "modifications": modifications
}

response = requests.post(
    "https://api.creatomate.com/v2/renders",
    json=payload,
    headers={"Authorization": f"Bearer {API_KEY}"}
)
```

## Element Names

The RenderScript template uses these exact names (matching your workflow):

| Element Type | Naming Pattern | Example |
|-------------|----------------|---------|
| Images | `Image-{num}` | `Image-1`, `Image-2`, `Image-3` |
| Audio | `Voiceover-{num}` | `Voiceover-1`, `Voiceover-2`, `Voiceover-3` |
| Text | `Text-{num}` | `Text-1`, `Text-2`, `Text-3` |

**Usage in modifications:**
- `Image-1.source` = image URL
- `Voiceover-1.source` = audio URL
- `Text-1.text` = dialogue text

## Advantages

✅ **No Dashboard Required**: Create templates programmatically  
✅ **Version Control**: Template structure in JSON (can be versioned)  
✅ **Exact Element Names**: Full control over naming convention  
✅ **Dynamic Templates**: Generate different templates for different use cases  
✅ **Automation**: Perfect for CI/CD pipelines  
✅ **Matches Workflow**: Element names match your code exactly  

## Template Structure

The RenderScript includes:

- **Composition**: 1920x1080, 30fps
- **Image Elements**: Full-screen images, one per scene
- **Audio Elements**: Voiceover tracks, one per scene  
- **Text Elements**: Subtitles/captions, positioned at bottom center
- **Timing**: Sequential scenes, 5 seconds each (configurable)

## Customization

Generate custom templates:

```bash
# 10 scenes, 1280x720, 3 seconds per scene
python execution/create_creatomate_template.py \
  --scenes 10 \
  --width 1280 \
  --height 720 \
  --duration 3.0 \
  --output custom_template.json
```

## Integration Status

✅ RenderScript template generator created  
✅ Template file generated (`creatomate_renderscript_template.json`)  
✅ `assemble_video.py` updated to support RenderScript  
✅ Environment variable support added  
✅ CLI flag support added  
✅ Documentation created  

## Next Steps

1. ✅ **Template created** - `creatomate_renderscript_template.json`
2. ✅ **Code updated** - `assemble_video.py` supports RenderScript
3. ⚠️ **Test workflow** - Run end-to-end test with RenderScript
4. ⚠️ **Optional**: Add `CREATOMATE_RENDERSCRIPT_PATH` to `.env`

## Example: Complete Workflow

```bash
# 1. Generate template (if needed)
python execution/create_creatomate_template.py --scenes 6

# 2. Add to .env (optional)
echo "CREATOMATE_RENDERSCRIPT_PATH=creatomate_renderscript_template.json" >> .env

# 3. Use in workflow
python execution/assemble_video.py \
  projects/my_project/script.json \
  projects/my_project/audio_files.json \
  projects/my_project/image_files.json \
  project_name
```

The script will automatically use RenderScript if `CREATOMATE_RENDERSCRIPT_PATH` is set!

## Summary

🎉 **You now have a programmatic Creatomate template solution!**

- ✅ No dashboard template needed
- ✅ Exact element names matching your workflow
- ✅ Fully automated via API
- ✅ Integrated with existing code

The template is ready to use - just set `CREATOMATE_RENDERSCRIPT_PATH` in `.env` or use the `--renderscript` flag!
