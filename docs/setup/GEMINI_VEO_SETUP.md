# Gemini Veo Video Generation Setup

This guide explains how to switch from Creatomate API to Gemini Veo API for video generation.

## Overview

Gemini Veo is Google's video generation model that creates videos from images and text prompts. Unlike Creatomate (which assembles videos from templates), Veo uses AI to generate video content.

## Key Differences

### Creatomate API
- **Method**: Template-based video assembly
- **Input**: Images, audio files, text overlays
- **Output**: Assembled video with precise timing
- **Control**: Full control over timing, transitions, effects

### Gemini Veo API
- **Method**: AI-generated video from images + prompt
- **Input**: Reference images + text prompt
- **Output**: AI-generated video sequence
- **Control**: Prompt-based, less precise timing control

## Setup

### Step 1: Install Dependencies

```bash
pip install google-cloud-aiplatform>=1.38.0
```

### Step 2: Configure Google Cloud Project

Gemini Veo requires Vertex AI, which needs a Google Cloud project:

1. **Create/Select Google Cloud Project**
   - Go to https://console.cloud.google.com
   - Create a new project or select existing one
   - Note your Project ID

2. **Enable Vertex AI API**
   - Go to APIs & Services > Library
   - Search for "Vertex AI API"
   - Click "Enable"

3. **Enable Veo API** (if available)
   - Check Vertex AI documentation for Veo availability
   - Enable required APIs

4. **Set Up Authentication**
   ```bash
   # Option 1: Application Default Credentials (recommended)
   gcloud auth application-default login
   
   # Option 2: Service Account (for production)
   # Create service account and download JSON key
   export GOOGLE_APPLICATION_CREDENTIALS="path/to/service-account-key.json"
   ```

### Step 3: Configure Environment Variables

Add to `.env`:

```env
# Gemini Veo Configuration
GEMINI_API_KEY=your-gemini-api-key-here
USE_GEMINI_VIDEO=true  # Set to true to use Veo instead of Creatomate

# Vertex AI Configuration (required for Veo)
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_LOCATION=us-central1  # or your preferred region
```

### Step 4: Test Configuration

```bash
# Test Gemini Veo video generation
python execution/generate_video_gemini.py script.json image_files.json project_name
```

## Usage

### Option 1: Environment Variable (Recommended)

Set `USE_GEMINI_VIDEO=true` in `.env`:

```env
USE_GEMINI_VIDEO=true
```

All video generation will use Gemini Veo automatically.

### Option 2: Command Line

```bash
# Use Gemini Veo
python execution/assemble_video.py script.json audio.json image.json project_name --use-gemini-video

# Use Creatomate (default)
python execution/assemble_video.py script.json audio.json image.json project_name
```

### Option 3: Programmatic

```python
from execution.assemble_video import assemble_video

result = assemble_video(
    script=script_data,
    audio_files=audio_files,
    image_files=image_files,
    project_name="project_name",
    use_gemini_video=True  # Use Gemini Veo
)
```

## How It Works

### 1. Image Upload
- Images are uploaded to Gemini Files API
- Each image gets a file URI for reference

### 2. Prompt Generation
- Script scenes are converted to a comprehensive prompt
- Includes visual descriptions and dialogue context

### 3. Video Generation
- Veo model generates video from images + prompt
- Asynchronous operation (polling required)

### 4. Video Download
- Generated video is downloaded to project folder
- Saved as `video_{operation_id}_{timestamp}.mp4`

## Limitations & Considerations

### Current Limitations

1. **Audio Not Included**: Gemini Veo generates video only (no audio)
   - **Solution**: Audio needs to be added separately using ffmpeg or similar
   - Future enhancement: Add audio overlay step

2. **Timing Control**: Less precise than Creatomate
   - Veo uses prompts, not exact timing
   - Duration may vary

3. **Vertex AI Required**: Veo requires Vertex AI setup
   - More complex than Creatomate API key setup
   - Requires Google Cloud project

### When to Use Gemini Veo

✅ **Use Veo when:**
- You want AI-generated video content
- You have reference images and descriptive prompts
- You don't need precise timing control
- You want to explore AI video generation

✅ **Use Creatomate when:**
- You need precise timing and transitions
- You have audio files to sync
- You need template-based assembly
- You want full control over video structure

## Troubleshooting

### Error: "Vertex AI not configured"
- **Solution**: Set `GOOGLE_CLOUD_PROJECT` and `GOOGLE_CLOUD_LOCATION` in `.env`
- Verify: `gcloud config get-value project`

### Error: "Veo model not available"
- **Solution**: Check if Veo is available in your region
- Check Vertex AI documentation for availability

### Error: "Authentication failed"
- **Solution**: Run `gcloud auth application-default login`
- Or set `GOOGLE_APPLICATION_CREDENTIALS` environment variable

### Error: "Operation timeout"
- **Solution**: Video generation can take 5-10 minutes
- Increase `MAX_POLL_TIME` in `generate_video_gemini.py` if needed

## Next Steps

1. **Add Audio Overlay**: Implement ffmpeg-based audio overlay for Veo videos
2. **Multi-Scene Support**: Generate separate videos per scene and combine
3. **Prompt Optimization**: Refine prompts for better Veo results
4. **Cost Monitoring**: Track Vertex AI usage and costs

## Resources

- [Gemini API Documentation](https://ai.google.dev/docs)
- [Vertex AI Documentation](https://cloud.google.com/vertex-ai/docs)
- [Veo Model Documentation](https://cloud.google.com/vertex-ai/docs/generative-ai/video/veo-overview)
