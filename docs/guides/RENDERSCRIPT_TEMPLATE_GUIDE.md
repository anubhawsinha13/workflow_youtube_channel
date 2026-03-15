# Creatomate RenderScript Template Guide

## Overview

Instead of creating a template in the Creatomate dashboard, you can use **RenderScript** - a JSON-based format that defines your entire video structure programmatically. This allows you to create templates with exact element names via API.

## What is RenderScript?

RenderScript is Creatomate's programmatic way to define video structure:
- ✅ No dashboard template needed
- ✅ Exact element names (Image-1, Voiceover-1, Text-1, etc.)
- ✅ Full control over layout, timing, and animations
- ✅ Perfect for automated workflows

## Generated Template

A RenderScript template has been generated: `creatomate_renderscript_template.json`

### Element Names

The template includes these exact element names (matching your workflow):

**For 6 scenes:**
- `Image-1`, `Image-2`, `Image-3`, `Image-4`, `Image-5`, `Image-6`
- `Voiceover-1`, `Voiceover-2`, `Voiceover-3`, `Voiceover-4`, `Voiceover-5`, `Voiceover-6`
- `Text-1`, `Text-2`, `Text-3`, `Text-4`, `Text-5`, `Text-6`

## Usage Methods

### Method 1: Direct API Usage

Use the RenderScript JSON directly with Creatomate API:

```python
import requests
import json

# Load RenderScript
with open("creatomate_renderscript_template.json", "r") as f:
    renderscript = json.load(f)

# Create video
payload = {
    "source": renderscript,
    "modifications": {
        "Image-1.source": "https://your-image-url-1.jpg",
        "Voiceover-1.source": "https://your-audio-url-1.mp3",
        "Text-1.text": "Scene 1 dialogue text",
        "Image-2.source": "https://your-image-url-2.jpg",
        "Voiceover-2.source": "https://your-audio-url-2.mp3",
        "Text-2.text": "Scene 2 dialogue text",
        # ... continue for all scenes
    }
}

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {CREATOMATE_API_KEY}"
}

response = requests.post(
    "https://api.creatomate.com/v2/renders",
    json=payload,
    headers=headers
)
```

### Method 2: Use with assemble_video.py

The `assemble_video.py` script can be updated to support RenderScript. Instead of using `template_id`, it can use the RenderScript JSON.

**Current workflow (with template_id):**
```bash
python execution/assemble_video.py script.json audio.json image.json template_id
```

**Future workflow (with RenderScript):**
```bash
python execution/assemble_video.py script.json audio.json image.json --renderscript creatomate_renderscript_template.json
```

## Advantages of RenderScript

1. **No Dashboard Required**: Create templates programmatically
2. **Exact Element Names**: Full control over naming convention
3. **Version Control**: Template structure in JSON (can be versioned)
4. **Dynamic Templates**: Generate different templates for different use cases
5. **Automation**: Perfect for CI/CD pipelines

## Template Structure

The RenderScript template includes:

- **Composition**: 1920x1080, 30fps, total duration based on scenes
- **Image Elements**: Full-screen images, one per scene
- **Audio Elements**: Voiceover tracks, one per scene
- **Text Elements**: Subtitles/captions, positioned at bottom center

### Scene Timing

- Each scene: 5 seconds (configurable)
- Scenes play sequentially
- Total duration: `num_scenes × scene_duration`

## Customization

### Generate Custom Template

```bash
python execution/create_creatomate_template.py \
  --scenes 10 \
  --width 1280 \
  --height 720 \
  --duration 3.0 \
  --output custom_template.json
```

### Parameters

- `--scenes`: Number of scenes (default: 6)
- `--width`: Video width in pixels (default: 1920)
- `--height`: Video height in pixels (default: 1080)
- `--duration`: Duration per scene in seconds (default: 5.0)
- `--output`: Output JSON file path

## Element Properties

### Image Elements
- **Name**: `Image-{num}`
- **Property**: `source` (URL to image)
- **Usage**: `Image-1.source = "https://image-url.jpg"`

### Audio Elements
- **Name**: `Voiceover-{num}`
- **Property**: `source` (URL to audio)
- **Usage**: `Voiceover-1.source = "https://audio-url.mp3"`

### Text Elements
- **Name**: `Text-{num}`
- **Property**: `text` (dialogue text)
- **Usage**: `Text-1.text = "Scene 1 dialogue"`

## Integration with Workflow

The RenderScript template matches your workflow's element naming convention:

1. **Script Generation**: Generates scenes with `dialogue` and `visual_description`
2. **Voiceover Generation**: Creates audio files for each scene
3. **Visual Generation**: Creates images for each scene
4. **Video Assembly**: Uses RenderScript with exact element names

## Next Steps

1. ✅ RenderScript template generated
2. ⚠️ Update `assemble_video.py` to support RenderScript (optional)
3. ✅ Use RenderScript directly via API
4. ✅ Element names match workflow exactly

## Example: Complete Workflow

```python
# 1. Load RenderScript
with open("creatomate_renderscript_template.json") as f:
    renderscript = json.load(f)

# 2. Load script with scenes
with open("script.json") as f:
    script = json.load(f)

# 3. Prepare modifications
modifications = {}
for i, scene in enumerate(script["scenes"], 1):
    modifications[f"Image-{i}.source"] = scene["image_url"]
    modifications[f"Voiceover-{i}.source"] = scene["audio_url"]
    modifications[f"Text-{i}.text"] = scene["dialogue"]

# 4. Create video
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

## Summary

✅ **RenderScript template created** with exact element names  
✅ **No dashboard template needed** - use RenderScript directly  
✅ **Element names match workflow**: Image-{num}, Voiceover-{num}, Text-{num}  
✅ **Fully automated** - create videos programmatically  

The template is ready to use with your workflow!
