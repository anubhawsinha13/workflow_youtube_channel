# Gemini Veo Setup Steps - Complete Guide

## Current Status Check

Let's verify your setup step by step:

### Step 1: Check Dependencies ✅

**Required:**
- ✅ `google-cloud-aiplatform` - For Vertex AI Veo API
- ✅ `google-generativeai` - For Gemini API
- ✅ `ffmpeg` - For audio overlay (optional but recommended)

**Check installation:**
```bash
pip install google-cloud-aiplatform>=1.38.0
pip install google-generativeai>=0.3.0
```

**Check FFmpeg:**
```bash
brew install ffmpeg  # macOS
ffmpeg -version      # Verify installation
```

---

### Step 2: Google Cloud Project Setup

#### 2.1 Create/Select Google Cloud Project

1. **Go to Google Cloud Console**: https://console.cloud.google.com
2. **Create New Project** (or select existing):
   - Click "Select a project" → "New Project"
   - Name: `youtube-workflow-veo` (or your preferred name)
   - Note your **Project ID** (e.g., `youtube-workflow-485004`)

#### 2.2 Enable Required APIs

Enable these APIs in your project:

1. **Vertex AI API**:
   - Go to: APIs & Services → Library
   - Search: "Vertex AI API"
   - Click "Enable"

2. **Generative Language API** (for Gemini):
   - Search: "Generative Language API"
   - Click "Enable"

3. **Veo API** (if available):
   - Check Vertex AI documentation for Veo availability
   - May require allowlist/access request

#### 2.3 Set Up Authentication

**Option A: Application Default Credentials (Recommended for Development)**

```bash
# Install Google Cloud SDK if not installed
# macOS: brew install google-cloud-sdk
# Or download from: https://cloud.google.com/sdk/docs/install

# Authenticate
gcloud auth login
gcloud auth application-default login

# Set project
gcloud config set project YOUR_PROJECT_ID
```

**Option B: Service Account (Recommended for Production)**

1. **Create Service Account**:
   - Go to: IAM & Admin → Service Accounts
   - Click "Create Service Account"
   - Name: `veo-video-generator`
   - Grant roles:
     - `Vertex AI User`
     - `Storage Object Viewer` (if using GCS)

2. **Create Key**:
   - Click on service account → Keys → Add Key → JSON
   - Download JSON key file
   - Save to: `credentials/vertex-ai-service-account.json`

3. **Set Environment Variable**:
   ```bash
   export GOOGLE_APPLICATION_CREDENTIALS="credentials/vertex-ai-service-account.json"
   ```

---

### Step 3: Configure Environment Variables

Add to `.env` file:

```env
# Gemini API (for image uploads)
GEMINI_API_KEY=your-gemini-api-key-here

# Gemini Veo Video Generation
USE_GEMINI_VIDEO=true  # Set to true to use Veo instead of Creatomate

# Vertex AI Configuration (REQUIRED for Veo)
GOOGLE_CLOUD_PROJECT=your-project-id-here
GOOGLE_CLOUD_LOCATION=us-central1  # or us-east1, europe-west1, etc.

# Optional: Service Account (if using service account auth)
# GOOGLE_APPLICATION_CREDENTIALS=credentials/vertex-ai-service-account.json
```

**Get Gemini API Key:**
1. Go to: https://makersuite.google.com/app/apikey
2. Sign in with Google account
3. Click "Create API Key"
4. Copy key (starts with `AIzaSy`)

---

### Step 4: Test Setup

#### 4.1 Test Gemini API Connection

```bash
cd workflow_youtube_channel
source venv/bin/activate
python test_gemini_api.py
```

Expected output:
```
✅ Gemini API key found
✅ Connected to Gemini API
✅ Model available: gemini-1.5-pro
```

#### 4.2 Test Vertex AI Connection

```bash
python -c "
from google.cloud import aiplatform
import os
project = os.getenv('GOOGLE_CLOUD_PROJECT')
location = os.getenv('GOOGLE_CLOUD_LOCATION', 'us-central1')
if project:
    aiplatform.init(project=project, location=location)
    print(f'✅ Vertex AI initialized: {project} in {location}')
else:
    print('❌ GOOGLE_CLOUD_PROJECT not set')
"
```

#### 4.3 Test FFmpeg (for Audio Overlay)

```bash
ffmpeg -version
```

Expected output:
```
ffmpeg version 6.x.x
```

---

### Step 5: Test Video Generation

#### 5.1 Prepare Test Files

Make sure you have:
- ✅ Script JSON file
- ✅ Image files (PNG/JPG)
- ✅ Audio files (MP3) - optional but recommended

#### 5.2 Test with Gemini Veo

```bash
# Test video generation with Veo
python execution/assemble_video.py \
    projects/supply__demand_in_economics_for_school/script_20260120_225130.json \
    test_audio_files.json \
    test_image_files.json \
    supply__demand_in_economics_for_school \
    --use-gemini-video
```

**Expected workflow:**
1. ✅ Upload images to Gemini Files API
2. ✅ Generate video with Veo model
3. ✅ Poll for completion
4. ✅ Download video
5. ✅ Add audio overlay (if FFmpeg available)
6. ✅ Save to project folder

---

## Troubleshooting

### Error: "Vertex AI not configured"

**Solution:**
```bash
# Check environment variables
echo $GOOGLE_CLOUD_PROJECT
echo $GOOGLE_CLOUD_LOCATION

# Set if missing
export GOOGLE_CLOUD_PROJECT=your-project-id
export GOOGLE_CLOUD_LOCATION=us-central1
```

### Error: "Authentication failed"

**Solution:**
```bash
# Re-authenticate
gcloud auth application-default login

# Or set service account
export GOOGLE_APPLICATION_CREDENTIALS="credentials/vertex-ai-service-account.json"
```

### Error: "Veo model not available"

**Possible causes:**
1. Veo may require allowlist/access request
2. Check Vertex AI documentation for availability
3. May not be available in all regions

**Solution:**
- Check Vertex AI documentation
- Try different region (us-central1, us-east1)
- Contact Google Cloud support for Veo access

### Error: "FFmpeg not found" (for audio overlay)

**Solution:**
```bash
# macOS
brew install ffmpeg

# Linux
sudo apt-get install ffmpeg

# Verify
ffmpeg -version
```

**Note:** Audio overlay will still work, but may use slower methods (Creatomate/Cloudinary)

---

## Next Steps After Setup

### 1. Test End-to-End Workflow

```bash
# Full workflow with Gemini Veo
python execution/research_topic.py "Supply & Demand" "Economics" supply_demand_test
python execution/generate_script.py research.json "Supply & Demand" "Economics" true supply_demand_test
python execution/generate_voiceover.py script.json supply_demand_test
python execution/generate_visuals.py script.json true supply_demand_test
python execution/assemble_video.py script.json audio.json image.json supply_demand_test --use-gemini-video
```

### 2. Compare Results

- **Creatomate**: Template-based, precise timing
- **Gemini Veo**: AI-generated, creative variations

### 3. Optimize Prompts

- Refine visual descriptions in script
- Adjust Veo prompts for better results
- Test different image combinations

---

## Cost Considerations

### Gemini Veo Pricing
- Check Vertex AI pricing: https://cloud.google.com/vertex-ai/pricing
- Veo may have different pricing than standard Vertex AI
- Monitor usage in Google Cloud Console

### Cost Optimization
- Use Creatomate for simple videos (cheaper)
- Use Veo for creative/unique videos
- Cache generated videos when possible

---

## Summary Checklist

- [ ] Google Cloud project created
- [ ] Vertex AI API enabled
- [ ] Authentication configured (gcloud auth)
- [ ] Environment variables set (.env)
- [ ] Dependencies installed (google-cloud-aiplatform)
- [ ] FFmpeg installed (for audio overlay)
- [ ] Test connection successful
- [ ] Test video generation successful

---

## Support Resources

- **Vertex AI Docs**: https://cloud.google.com/vertex-ai/docs
- **Gemini API Docs**: https://ai.google.dev/docs
- **Veo Documentation**: Check Vertex AI docs for latest Veo info
- **Google Cloud Support**: https://cloud.google.com/support

---

## Ready to Test!

Once all steps are complete, run:

```bash
python execution/assemble_video.py script.json audio.json image.json project_name --use-gemini-video
```

Good luck! 🚀
