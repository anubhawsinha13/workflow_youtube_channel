# Next Steps for Gemini Veo Video Generation 🚀

## Current Status

Based on the setup check, here's what needs to be done:

### ✅ Completed
- ✅ Gemini Veo integration code created
- ✅ Audio overlay module created
- ✅ Documentation created

### ⚠️ Required Setup Steps

---

## Step 1: Install Dependencies (5 minutes)

### 1.1 Install Python Packages

```bash
cd workflow_youtube_channel
source venv/bin/activate
pip install google-cloud-aiplatform>=1.38.0
pip install google-generativeai>=0.3.0
```

**Or use the setup script:**
```bash
./setup_gemini_veo.sh
```

### 1.2 Install FFmpeg (for Audio Overlay)

**macOS:**
```bash
brew install ffmpeg
```

**Linux:**
```bash
sudo apt-get install ffmpeg
```

**Verify:**
```bash
ffmpeg -version
```

---

## Step 2: Google Cloud Project Setup (10 minutes)

### 2.1 Create Google Cloud Project

1. **Go to**: https://console.cloud.google.com
2. **Create Project**:
   - Click "Select a project" → "New Project"
   - Name: `youtube-workflow-veo` (or your choice)
   - **Note your Project ID** (e.g., `youtube-workflow-485004`)

### 2.2 Enable APIs

Enable these APIs in your project:

1. **Vertex AI API**:
   - Go to: APIs & Services → Library
   - Search: "Vertex AI API"
   - Click "Enable"

2. **Generative Language API**:
   - Search: "Generative Language API"
   - Click "Enable"

### 2.3 Set Up Authentication

**Option A: Application Default Credentials (Easiest)**

```bash
# Install Google Cloud SDK (if not installed)
# macOS: brew install google-cloud-sdk
# Or download: https://cloud.google.com/sdk/docs/install

# Authenticate
gcloud auth login
gcloud auth application-default login

# Set your project
gcloud config set project YOUR_PROJECT_ID
```

**Option B: Service Account (For Production)**

1. Go to: IAM & Admin → Service Accounts
2. Create service account: `veo-video-generator`
3. Grant roles:
   - `Vertex AI User`
   - `Storage Object Viewer` (if using GCS)
4. Create JSON key and save to `credentials/vertex-ai-service-account.json`
5. Set environment variable:
   ```bash
   export GOOGLE_APPLICATION_CREDENTIALS="credentials/vertex-ai-service-account.json"
   ```

---

## Step 3: Configure Environment Variables (2 minutes)

Edit `.env` file and add:

```env
# Gemini API (for image uploads)
GEMINI_API_KEY=your-gemini-api-key-here

# Gemini Veo Video Generation
USE_GEMINI_VIDEO=true  # Set to true to use Veo instead of Creatomate

# Vertex AI Configuration (REQUIRED for Veo)
GOOGLE_CLOUD_PROJECT=your-project-id-here
GOOGLE_CLOUD_LOCATION=us-central1  # or us-east1, europe-west1, etc.
```

**Get Gemini API Key:**
1. Go to: https://makersuite.google.com/app/apikey
2. Sign in with Google account
3. Click "Create API Key"
4. Copy key (starts with `AIzaSy`)

---

## Step 4: Test Setup (5 minutes)

### 4.1 Test Gemini API

```bash
cd workflow_youtube_channel
source venv/bin/activate
python test_gemini_api.py
```

**Expected:** ✅ Connected to Gemini API

### 4.2 Test Vertex AI Connection

```bash
python -c "
from google.cloud import aiplatform
import os
from dotenv import load_dotenv
load_dotenv()

project = os.getenv('GOOGLE_CLOUD_PROJECT')
location = os.getenv('GOOGLE_CLOUD_LOCATION', 'us-central1')

if project:
    try:
        aiplatform.init(project=project, location=location)
        print(f'✅ Vertex AI initialized: {project} in {location}')
    except Exception as e:
        print(f'❌ Vertex AI initialization failed: {e}')
else:
    print('❌ GOOGLE_CLOUD_PROJECT not set in .env')
"
```

**Expected:** ✅ Vertex AI initialized

### 4.3 Test FFmpeg

```bash
ffmpeg -version
```

**Expected:** FFmpeg version information

---

## Step 5: Test Video Generation (10 minutes)

### 5.1 Prepare Test Files

Make sure you have test files ready:
- Script JSON: `projects/supply__demand_in_economics_for_school/script_20260120_225130.json`
- Audio files: `test_audio_files.json`
- Image files: `test_image_files.json`

### 5.2 Run Test

```bash
cd workflow_youtube_channel
source venv/bin/activate

python execution/assemble_video.py \
    projects/supply__demand_in_economics_for_school/script_20260120_225130.json \
    test_audio_files.json \
    test_image_files.json \
    supply__demand_in_economics_for_school \
    --use-gemini-video
```

**Expected Workflow:**
1. ✅ Upload images to Gemini Files API
2. ✅ Generate video with Veo model
3. ✅ Poll for completion (may take 5-10 minutes)
4. ✅ Download video
5. ✅ Add audio overlay with FFmpeg
6. ✅ Save to project folder

---

## Quick Setup Checklist

Run this to check your setup:

```bash
cd workflow_youtube_channel
./setup_gemini_veo.sh
```

Or manually check:

- [ ] `google-cloud-aiplatform` installed
- [ ] `google-generativeai` installed
- [ ] FFmpeg installed
- [ ] Google Cloud project created
- [ ] Vertex AI API enabled
- [ ] Authentication configured (`gcloud auth`)
- [ ] `.env` file configured
- [ ] `GOOGLE_CLOUD_PROJECT` set
- [ ] `GEMINI_API_KEY` set
- [ ] Test connection successful

---

## Troubleshooting

### Error: "Vertex AI not configured"

**Fix:**
```bash
# Check .env file
cat .env | grep GOOGLE_CLOUD_PROJECT

# Set if missing
export GOOGLE_CLOUD_PROJECT=your-project-id
export GOOGLE_CLOUD_LOCATION=us-central1
```

### Error: "Authentication failed"

**Fix:**
```bash
# Re-authenticate
gcloud auth application-default login

# Or use service account
export GOOGLE_APPLICATION_CREDENTIALS="credentials/vertex-ai-service-account.json"
```

### Error: "Veo model not available"

**Possible causes:**
- Veo may require allowlist/access request
- Not available in all regions
- Check Vertex AI documentation

**Fix:**
- Try different region: `GOOGLE_CLOUD_LOCATION=us-east1`
- Check Vertex AI docs for Veo availability
- Contact Google Cloud support

### Error: "FFmpeg not found"

**Fix:**
```bash
# macOS
brew install ffmpeg

# Verify
ffmpeg -version
```

**Note:** Video generation will work, but audio overlay may be slower without FFmpeg.

---

## Expected Results

### Successful Video Generation

After running the test, you should see:

```
🎬 Using Gemini Veo API for video generation...
📤 Uploading 6 images to Gemini Files API...
   Image 1: Uploading scene_1.png...
   ✅ Uploaded: files/abc123...
🎬 Generating video with Veo model...
   Prompt: Create a video about: Supply & Demand...
   Images: 6
✅ Video generation started: operations/123456789
⏳ Polling for video generation completion...
   Status: running, Waiting...
   Status: succeeded, Progress: 100%
✅ Render complete! Video URL: https://...
📥 Downloading video to project folder...
✅ Video saved to project folder: projects/.../video/video_veo_20260121_120000.mp4
🎵 Adding audio overlay to Gemini Veo video...
✅ Audio overlay added: projects/.../video/video_with_audio_20260121_120100.mp4
```

### Output Files

- Video without audio: `projects/{project_name}/video/video_veo_{timestamp}.mp4`
- Video with audio: `projects/{project_name}/video/video_with_audio_{timestamp}.mp4`

---

## Next Steps After Success

1. **Compare Results**:
   - Test Creatomate vs Gemini Veo
   - Compare video quality and style
   - Measure generation time

2. **Optimize Prompts**:
   - Refine visual descriptions in script
   - Adjust Veo prompts for better results
   - Test different image combinations

3. **Production Use**:
   - Set `USE_GEMINI_VIDEO=true` in `.env` for default
   - Monitor costs in Google Cloud Console
   - Set up error handling and retries

---

## Cost Considerations

### Gemini Veo Pricing
- Check: https://cloud.google.com/vertex-ai/pricing
- Veo may have different pricing
- Monitor usage in Google Cloud Console

### Cost Optimization
- Use Creatomate for simple videos (cheaper)
- Use Veo for creative/unique videos
- Cache generated videos when possible

---

## Support

- **Setup Guide**: `GEMINI_VEO_SETUP_STEPS.md`
- **Audio Overlay**: `AUDIO_OVERLAY_GUIDE.md`
- **Integration Docs**: `GEMINI_VEO_INTEGRATION.md`
- **Vertex AI Docs**: https://cloud.google.com/vertex-ai/docs
- **Gemini API Docs**: https://ai.google.dev/docs

---

## Ready to Start! 🎬

Run the setup script:
```bash
cd workflow_youtube_channel
./setup_gemini_veo.sh
```

Then test video generation:
```bash
python execution/assemble_video.py script.json audio.json image.json project_name --use-gemini-video
```

Good luck! 🚀
