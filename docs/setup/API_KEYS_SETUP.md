# API Keys Setup Guide

This guide will help you obtain and configure all required API keys for the YouTube workflow automation system.

## Quick Start

1. **Copy the example file**:
   ```bash
   cp .env.example .env
   ```

2. **Edit `.env` file** with your API keys (see sections below)

3. **Verify your setup** by testing the research script

## Required API Keys

### 1. OpenAI API Key

**Purpose**: Script writing, fact-checking, compliance checking, image generation (DALL-E)

**Where to get it**:
1. Go to https://platform.openai.com
2. Sign up or log in
3. Click on your profile → **API Keys**
4. Click **Create new secret key**
5. Copy the key immediately (you won't see it again!)
6. **Set billing limits** (recommended: $50-100/month initially)
   - Go to **Settings** → **Billing** → **Usage limits**

**Add to `.env`**:
```env
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

**Cost**: ~$0.10-$0.30 per video (with optimization)
- GPT-4o for script writing
- GPT-4o-mini for parsing/metadata (cost optimization)
- DALL-E for image generation

**Security**: Keep this key secret! Never commit it to Git.

---

### 1.5. Google Gemini API Key (Optional Alternative)

**Purpose**: Script writing and image generation (alternative to OpenAI)

**Where to get it**:
1. Go to https://makersuite.google.com/app/apikey
2. Sign in with your Google account
3. Click **Create API Key**
4. Select or create a Google Cloud project
5. Copy the API key
6. (Optional) Enable Vertex AI Imagen 3 for image generation
   - Go to https://console.cloud.google.com
   - Enable Vertex AI API
   - Enable Imagen API

**Add to `.env`**:
```env
GEMINI_API_KEY=AIzaSyxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
USE_GEMINI=false  # Set to 'true' to use Gemini instead of OpenAI
```

**Cost**: 
- **Gemini Pro**: Often more cost-effective than GPT-4
- **Imagen 3**: Competitive with DALL-E pricing
- Free tier available with generous limits

**Benefits**:
- ✅ Often faster response times
- ✅ Better cost efficiency for script generation
- ✅ Native JSON output support
- ✅ Good quality results

**To use Gemini**:
Set `USE_GEMINI=true` in `.env` or pass `use_gemini=True` to scripts

**Security**: Keep this key secret! Never commit it to Git.

---

### 2. Perplexity API Key

**Purpose**: Research and fact-gathering for video topics

**Where to get it**:
1. Go to https://www.perplexity.ai
2. Sign up or log in
3. Navigate to **Settings** → **API Keys**
4. Click **Create API Key**
5. Copy the key

**Add to `.env`**:
```env
PERPLEXITY_API_KEY=pplx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

**Cost**: ~$0.05-$0.15 per video
- Free tier has rate limits
- Paid tier recommended for production

**Security**: Keep this key secret! Never commit it to Git.

---

### 3. ElevenLabs API Key

**Purpose**: Voiceover generation (text-to-speech)

**Where to get it**:
1. Go to https://elevenlabs.io
2. Sign up or log in
3. Go to **Profile Settings** → **API Keys**
4. Click **Generate API Key**
5. Copy the key

**Add to `.env`**:
```env
ELEVENLABS_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

**Cost**: ~$0.12-$0.30 per video
- Turbo models available (30-40% cheaper)
- Consider voice cloning for consistency

**Security**: Keep this key secret! Never commit it to Git.

---

### 4. Creatomate API Key & Template ID

**Purpose**: Video assembly (combining audio, images, and script)

**Where to get it**:

**Step 1: Get API Key**
1. Go to https://creatomate.com
2. Sign up or log in
3. Go to **Project Settings** → **API Keys**
4. Click **Create API Key**
5. Copy the API key

**Step 2: Get Template ID**
1. Go to **Templates** in your Creatomate dashboard
2. Create a new template or select an existing one
3. Note the template ID (visible in template settings)
4. Configure dynamic elements:
   - `Voiceover-1`, `Voiceover-2`, etc. (for audio)
   - `Image-1`, `Image-2`, etc. (for visuals)
   - `Text-1`, `Text-2`, etc. (for subtitles, optional)

**Add to `.env`**:
```env
CREATOMATE_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
CREATOMATE_TEMPLATE_ID=your_template_id_here
```

**Cost**: ~$0.10-$0.30 per video

**Security**: Keep this key secret! Never commit it to Git.

---

### 5. YouTube Data API v3 (OAuth 2.0)

**Purpose**: Uploading videos to YouTube

**Where to get it**:

**Step 1: Enable YouTube Data API**
1. Go to https://console.cloud.google.com
2. Create a new project or select existing project
3. Enable **YouTube Data API v3**:
   - Go to **APIs & Services** → **Library**
   - Search for "YouTube Data API v3"
   - Click **Enable**

**Step 2: Create OAuth 2.0 Credentials**
1. Go to **APIs & Services** → **Credentials**
2. Click **Create Credentials** → **OAuth client ID**
3. Configure OAuth consent screen (if not done):
   - User type: **External** (for personal use)
   - App name: Your YouTube channel name
   - Scopes: Add `https://www.googleapis.com/auth/youtube.upload`
   - Test users: Add your Google account email
4. Select **Application type**: **Desktop app**
5. Name: "YouTube Uploader" (or any name)
6. Click **Create**
7. Download the JSON file (save as `credentials/client_secrets.json`)

**Step 3: Authenticate (One-time setup)**
1. Run the authentication script (will be created):
   ```bash
   python execution/authenticate_youtube.py
   ```
2. Follow the browser prompts to authorize
3. This creates `credentials/youtube_credentials.json` (refresh token)

**Add to `.env`**:
```env
YOUTUBE_CLIENT_SECRETS_FILE=credentials/client_secrets.json
YOUTUBE_CREDENTIALS_FILE=credentials/youtube_credentials.json
```

**Cost**: Free (within quota limits)

**Security**: 
- Keep `client_secrets.json` secure
- Keep `youtube_credentials.json` secure (contains refresh token)
- Both files are in `.gitignore`

---

## Complete .env File Example

```env
# API Keys - Get these from respective service dashboards
OPENAI_API_KEY=sk-proj-your-actual-key-here
GEMINI_API_KEY=AIzaSy-your-actual-key-here  # Optional: alternative to OpenAI
USE_GEMINI=false  # Set to 'true' to use Gemini for scripts/images
PERPLEXITY_API_KEY=pplx-your-actual-key-here
ELEVENLABS_API_KEY=your-actual-key-here
CREATOMATE_API_KEY=your-actual-key-here
CREATOMATE_TEMPLATE_ID=your-template-id-here

# Google Cloud Storage (optional - for Creatomate assets)
GCS_BUCKET_NAME=your-bucket-name
GCS_SERVICE_ACCOUNT_PATH=credentials/gcs-service-account.json
GCS_PUBLIC_URL_PREFIX=https://storage.googleapis.com/your-bucket-name

# YouTube OAuth - Path to credential files
YOUTUBE_CLIENT_SECRETS_FILE=credentials/client_secrets.json
YOUTUBE_CREDENTIALS_FILE=credentials/youtube_credentials.json

# Configuration
DEFAULT_NICHE=History & Biographies
DEFAULT_VIDEO_LENGTH=1500
LOG_LEVEL=INFO
```

---

## Step-by-Step Setup

### Step 1: Create .env File

```bash
# Navigate to project directory
cd workflow_youtube_channel

# Copy example file
cp .env.example .env

# Edit the file (use your preferred editor)
nano .env
# or
code .env
# or
vim .env
```

### Step 2: Add Each API Key

For each service above:
1. Get the API key from the service dashboard
2. Copy it (without quotes or spaces)
3. Paste it into `.env` after the `=` sign
4. Save the file

### Step 3: Verify .env File

Make sure your `.env` file:
- ✅ Has all required keys
- ✅ No quotes around values (unless specified)
- ✅ No extra spaces
- ✅ Each key is on its own line

**Correct**:
```env
OPENAI_API_KEY=sk-proj-abc123
```

**Incorrect**:
```env
OPENAI_API_KEY="sk-proj-abc123"  # No quotes needed
OPENAI_API_KEY = sk-proj-abc123  # No spaces around =
```

### Step 4: Verify Setup

Test that your API keys work:

```bash
# Activate virtual environment
source venv/bin/activate

# Test OpenAI (will print usage info)
python -c "from openai import OpenAI; import os; from dotenv import load_dotenv; load_dotenv(); client = OpenAI(); print('✅ OpenAI API key is valid')"

# Test Perplexity (research script)
python execution/research_topic.py "The rise and fall of Blackberry" 4

# If successful, you'll see research results
```

---

## Security Best Practices

1. **Never commit .env to Git**
   - Already in `.gitignore` ✅
   - Double-check before committing

2. **Use different keys for different environments**
   - Development keys (with lower limits)
   - Production keys (with higher limits)

3. **Rotate keys regularly**
   - Change API keys every 3-6 months
   - Delete old keys when rotating

4. **Set billing limits**
   - OpenAI: $50-100/month initially
   - Monitor usage in dashboards

5. **Use secrets management for production**
   - Environment variables in deployment
   - AWS Secrets Manager, Google Secret Manager, etc.

6. **Keep credentials folder secure**
   - `credentials/` is in `.gitignore` ✅
   - Never share OAuth credentials

---

## Troubleshooting

### "API key not found" error
- Check that `.env` file exists in project root
- Verify key name matches exactly (no typos)
- Ensure no quotes or spaces around the value

### "Invalid API key" error
- Verify you copied the entire key
- Check if key has expired or been revoked
- Ensure you're using the right key type (some services have multiple key types)

### "Permission denied" error
- Verify API key has correct permissions/scopes
- Check if billing is set up (for paid APIs)
- Ensure API is enabled in service dashboard

### YouTube OAuth issues
- Ensure OAuth consent screen is configured
- Add your email as a test user
- Verify scopes include `youtube.upload`
- Check that credentials file paths are correct

---

## Cost Estimation

Approximate cost per video:
- **Base**: $0.46 - $1.30 per video
- **Optimized**: $0.35 - $0.90 per video (with GPT-4o-mini and Turbo models)

**Monthly estimates** (10 videos/day):
- Base: $138 - $390/month
- Optimized: $105 - $270/month

**Tips to reduce costs**:
- Use GPT-4o-mini for parsing/metadata
- Use ElevenLabs Turbo models
- Implement asset caching (idempotency)
- Monitor and optimize usage

---

## Next Steps

Once all API keys are configured:

1. **Test the research script**:
   ```bash
   source venv/bin/activate
   python execution/research_topic.py "Test topic" 4
   ```

2. **Proceed to Phase 2**: Building execution scripts

3. **Set up YouTube OAuth** (for Phase 9):
   - Run authentication script when ready
   - This requires browser access

---

## Quick Reference

| Service | Where to Get | Cost per Video |
|---------|-------------|----------------|
| OpenAI | platform.openai.com | $0.10-$0.30 |
| Gemini (alt) | makersuite.google.com/app/apikey | $0.05-$0.15 (scripts) |
| Perplexity | perplexity.ai → Settings → API | $0.05-$0.15 |
| ElevenLabs | elevenlabs.io → Profile → API Keys | $0.12-$0.30 |
| Creatomate | creatomate.com → Project → API Keys | $0.10-$0.30 |
| YouTube | console.cloud.google.com | Free (within quota) |

---

## Support

If you encounter issues:
1. Check the troubleshooting section above
2. Verify API keys are correct
3. Check service status pages
4. Review service documentation

---

**Remember**: Never share your API keys publicly or commit them to version control!
