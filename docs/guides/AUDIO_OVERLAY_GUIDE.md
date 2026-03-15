# Audio Overlay Guide - Video Generation with Audio

This guide explains how to generate videos with audio overlay via API, covering multiple methods and use cases.

## Overview

There are several ways to add audio overlay to videos:

1. **Creatomate API** - Native audio support in RenderScript
2. **FFmpeg** - Local processing (fastest, free)
3. **Cloudinary API** - Cloud-based processing
4. **Gemini Veo + Audio Overlay** - Post-processing step

---

## Method 1: Creatomate API (Native Audio Support) ✅

Creatomate supports audio overlay natively in RenderScript. This is already implemented in your workflow.

### How It Works

Creatomate RenderScript includes `audio` elements that can overlay on video:

```json
{
  "output_format": "mp4",
  "elements": [
    {
      "type": "video",
      "source": "https://example.com/video.mp4"
    },
    {
      "type": "audio",
      "source": "https://example.com/voiceover.mp3",
      "volume": "100%",
      "time": 0.0,
      "duration": "media"
    }
  ]
}
```

### Current Implementation

Your `execution/assemble_video.py` already handles this:

```python
# Audio is added via modifications in template_id mode
modifications[f"Voiceover-1.source"] = audio_urls[0]
modifications[f"Voiceover-1.volume"] = 100
modifications[f"Voiceover-1.time"] = cumulative_time
```

### Usage

```bash
# Audio overlay is automatic when using Creatomate
python execution/assemble_video.py script.json audio.json image.json project_name
```

**Advantages:**
- ✅ Native support - no post-processing needed
- ✅ Precise timing control
- ✅ Multiple audio tracks supported
- ✅ Automatic synchronization

---

## Method 2: FFmpeg (Local Processing) ✅

FFmpeg is the most flexible and fastest option for local audio overlay.

### Setup

**macOS:**
```bash
brew install ffmpeg
```

**Linux:**
```bash
sudo apt-get install ffmpeg
```

**Windows:**
Download from https://ffmpeg.org/download.html

### Usage

**Command Line:**
```bash
python execution/add_audio_overlay.py video.mp4 audio.mp3 --output output.mp4 --method ffmpeg
```

**Programmatic:**
```python
from execution.add_audio_overlay import add_audio_overlay_to_video

result = add_audio_overlay_to_video(
    video_path="video.mp4",
    audio_paths=["audio.mp3"],
    output_path="output.mp4",
    method="ffmpeg",
    replace_audio=True  # Replace existing audio
)
```

### Features

- ✅ **Replace Audio**: `replace_audio=True` replaces existing audio track
- ✅ **Mix Audio**: `replace_audio=False` mixes with existing audio
- ✅ **Volume Control**: Adjust audio volume (0.0 to 1.0)
- ✅ **Start Time**: Set when audio starts (seconds)
- ✅ **Multiple Tracks**: Can handle multiple audio files

**Advantages:**
- ✅ Fast local processing
- ✅ No API costs
- ✅ Full control over audio mixing
- ✅ Works offline

**Disadvantages:**
- ❌ Requires FFmpeg installation
- ❌ Local processing (uses your machine resources)

---

## Method 3: Cloudinary API (Cloud Processing)

Cloudinary provides cloud-based video processing with audio overlay.

### Setup

1. **Sign up**: https://cloudinary.com
2. **Get credentials**: Cloud name, API key, API secret
3. **Add to `.env`**:
```env
CLOUDINARY_CLOUD_NAME=your-cloud-name
CLOUDINARY_API_KEY=your-api-key
CLOUDINARY_API_SECRET=your-api-secret
```

4. **Install SDK**:
```bash
pip install cloudinary
```

### Usage

```python
from execution.add_audio_overlay import add_audio_overlay_to_video

result = add_audio_overlay_to_video(
    video_path="https://example.com/video.mp4",  # Must be URL
    audio_paths=["https://example.com/audio.mp3"],  # Must be URL
    method="cloudinary"
)
```

**Advantages:**
- ✅ No local installation needed
- ✅ Scalable cloud processing
- ✅ Handles large files

**Disadvantages:**
- ❌ Requires public URLs (upload files first)
- ❌ API costs
- ❌ Less control than FFmpeg

---

## Method 4: Gemini Veo + Audio Overlay ✅

Gemini Veo generates video without audio. Add audio overlay as a post-processing step.

### Current Implementation

Your `execution/generate_video_gemini.py` automatically adds audio overlay:

```python
# After Veo video generation
if audio_files and video_path:
    audio_result = add_audio_overlay_to_video(
        video_path=video_path,
        audio_paths=audio_files,
        method="auto",  # Auto-detect (prefers FFmpeg)
        replace_audio=True
    )
```

### Usage

```bash
# Audio overlay is automatic when using Gemini Veo
python execution/assemble_video.py script.json audio.json image.json project_name --use-gemini-video
```

**Workflow:**
1. Generate video with Veo (no audio)
2. Automatically add audio overlay using FFmpeg (or fallback method)
3. Save final video with audio

**Advantages:**
- ✅ Automatic audio overlay
- ✅ Works with Gemini Veo videos
- ✅ Uses best available method (FFmpeg preferred)

---

## Comparison Table

| Method | Setup Complexity | Cost | Speed | Audio Control | Best For |
|--------|-----------------|------|-------|---------------|----------|
| **Creatomate** | Easy (API key) | Pay per render | Fast | High | Template-based videos |
| **FFmpeg** | Medium (install) | Free | Very Fast | Very High | Local processing |
| **Cloudinary** | Easy (API key) | Pay per process | Medium | Medium | Cloud processing |
| **Veo + Overlay** | Medium (Veo + FFmpeg) | Veo cost + Free | Slow | High | AI-generated videos |

---

## Recommended Approach

### For Creatomate Videos
✅ **Use Creatomate's native audio support** (already implemented)
- No post-processing needed
- Precise timing control
- Automatic synchronization

### For Gemini Veo Videos
✅ **Use FFmpeg for audio overlay** (automatically used)
- Fast local processing
- Full control
- No additional API costs

### For Custom Workflows
✅ **Use FFmpeg** if available, otherwise **Creatomate** or **Cloudinary**

---

## Examples

### Example 1: Add Single Audio Track

```python
from execution.add_audio_overlay import add_audio_overlay_to_video

result = add_audio_overlay_to_video(
    video_path="video.mp4",
    audio_paths=["voiceover.mp3"],
    output_path="video_with_audio.mp4",
    method="ffmpeg",
    replace_audio=True
)
```

### Example 2: Add Multiple Audio Tracks (Sequential)

```python
# For multiple scenes, concatenate audio first or use Creatomate
result = add_audio_overlay_to_video(
    video_path="video.mp4",
    audio_paths=["scene1.mp3", "scene2.mp3", "scene3.mp3"],
    method="ffmpeg",
    replace_audio=True
)
```

### Example 3: Mix Audio (Background Music + Voiceover)

```python
# First add voiceover
result1 = add_audio_overlay_to_video(
    video_path="video.mp4",
    audio_paths=["voiceover.mp3"],
    method="ffmpeg",
    replace_audio=True
)

# Then mix background music
result2 = add_audio_overlay_to_video(
    video_path=result1["output_path"],
    audio_paths=["background_music.mp3"],
    method="ffmpeg",
    replace_audio=False,  # Mix, don't replace
    audio_volumes=[0.3]  # Lower volume for background
)
```

---

## Troubleshooting

### FFmpeg Not Found
```bash
# macOS
brew install ffmpeg

# Linux
sudo apt-get install ffmpeg

# Verify installation
ffmpeg -version
```

### Audio Out of Sync
- Check audio file format (MP3, AAC recommended)
- Verify video and audio durations match
- Use `audio_start_time` parameter to adjust timing

### Audio Too Loud/Quiet
- Adjust `audio_volume` parameter (0.0 to 1.0)
- For background music, use lower volume (0.2-0.5)

### Multiple Audio Tracks
- Use Creatomate for precise multi-track control
- Or concatenate audio files first, then overlay

---

## Next Steps

1. **Install FFmpeg** (recommended for Gemini Veo):
   ```bash
   brew install ffmpeg  # macOS
   ```

2. **Test Audio Overlay**:
   ```bash
   python execution/add_audio_overlay.py video.mp4 audio.mp3 --output test.mp4
   ```

3. **Use in Workflow**:
   - Creatomate: Audio overlay is automatic ✅
   - Gemini Veo: Audio overlay is automatic ✅

---

## Summary

✅ **Creatomate**: Native audio support - use for template-based videos  
✅ **FFmpeg**: Best for local processing - use for Gemini Veo videos  
✅ **Cloudinary**: Cloud alternative - use if FFmpeg unavailable  
✅ **Automatic**: Both Creatomate and Gemini Veo workflows include audio overlay automatically
