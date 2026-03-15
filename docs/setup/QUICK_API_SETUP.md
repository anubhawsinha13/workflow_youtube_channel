# Quick API Keys Setup

## Fast Setup (5 minutes)

### Step 1: Create .env file
```bash
cp .env.example .env
```

### Step 2: Get API Keys

#### 1. OpenAI (Required for scripts & images)
- **Go to**: https://platform.openai.com/api-keys
- **Click**: Create new secret key
- **Copy** the key (starts with `sk-proj-`)
- **Set billing limit**: $50-100/month

**OR use Gemini (often cheaper/faster)**:
- **Go to**: https://makersuite.google.com/app/apikey
- **Click**: Create API Key
- **Copy** the key (starts with `AIzaSy`)
- **Set**: `USE_GEMINI=true` in `.env`

#### 2. Perplexity (Required for research)
- **Go to**: https://www.perplexity.ai → Settings → API Keys
- **Click**: Create API Key
- **Copy** the key (starts with `pplx-`)

#### 3. ElevenLabs (Required for voiceover)
- **Go to**: https://elevenlabs.io → Profile Settings → API Keys
- **Click**: Generate API Key
- **Copy** the key

#### 4. Creatomate (Required for video assembly)
- **Go to**: https://creatomate.com → Project Settings → API Keys
- **Click**: Create API Key
- **Copy** the key
- **Get Template ID**: Templates → Select template → Copy ID

#### 5. YouTube API (Required for publishing)
- **Go to**: https://console.cloud.google.com
- **Enable**: YouTube Data API v3
- **Create**: OAuth 2.0 Desktop App credentials
- **Download**: Save as `credentials/client_secrets.json`

### Step 3: Edit .env file
```bash
nano .env  # or use your preferred editor
```

Replace the placeholder values with your actual keys:
```env
OPENAI_API_KEY=sk-proj-your-actual-key-here
GEMINI_API_KEY=AIzaSy-your-actual-key-here  # Optional: alternative
USE_GEMINI=false  # Set to 'true' to use Gemini
PERPLEXITY_API_KEY=pplx-your-actual-key-here
ELEVENLABS_API_KEY=your-actual-key-here
CREATOMATE_API_KEY=your-actual-key-here
CREATOMATE_TEMPLATE_ID=your-template-id-here
```

### Step 4: Test Setup
```bash
source venv/bin/activate
python execution/research_topic.py "Test topic" 4
```

If you see research results, you're all set! ✅

---

## Cost Overview

**Per Video**: ~$0.35 - $0.90 (optimized)
**Per Month** (10 videos/day): ~$105 - $270

---

## Need Help?

See `API_KEYS_SETUP.md` for detailed instructions and troubleshooting.
