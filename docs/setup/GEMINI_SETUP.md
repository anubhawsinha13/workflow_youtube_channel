# Gemini API Setup Guide

This guide explains how to use Google Gemini API as an alternative to OpenAI for script writing and image generation.

## Why Use Gemini?

### Advantages
- ✅ **Cost-Effective**: Often cheaper than GPT-4
- ✅ **Fast**: Quick response times
- ✅ **Native JSON**: Built-in JSON output support
- ✅ **High Quality**: Excellent results for script generation
- ✅ **Free Tier**: Generous free tier available

### When to Use
- Script writing (especially for cost optimization)
- Image generation (via Imagen 3)
- When OpenAI rate limits are hit
- For testing and development

## Setup

### Step 1: Get Gemini API Key

1. Go to https://makersuite.google.com/app/apikey
2. Sign in with your Google account
3. Click **Create API Key**
4. Select or create a Google Cloud project
5. Copy the API key (starts with `AIzaSy`)

### Step 2: Add to .env

```env
GEMINI_API_KEY=AIzaSy-your-actual-key-here
USE_GEMINI=false  # Set to 'true' to enable Gemini
```

### Step 3: Enable Gemini

**Option A: Environment Variable** (Recommended)
```env
USE_GEMINI=true
```

**Option B: Command Line**
```bash
# For script generation
python execution/generate_script.py research.json "Topic" "Niche" true

# For image generation
python execution/generate_visuals.py script.json true
```

**Option C: Auto-Fallback**
If OpenAI fails, scripts will automatically try Gemini (if API key is set).

## Script Generation with Gemini

### Features
- Uses `gemini-1.5-pro` model
- Native JSON output mode
- Fast response times
- Cost-effective

### Example
```bash
# Using Gemini
python execution/generate_script.py research.json "Blackberry History" "History & Biographies" true

# Using OpenAI (default)
python execution/generate_script.py research.json "Blackberry History" "History & Biographies" false
```

## Image Generation

**Note**: Gemini doesn't have direct image generation like DALL-E. Options:

### Option 1: Use Vertex AI Imagen 3
1. Enable Vertex AI API in Google Cloud Console
2. Enable Imagen API
3. Use Imagen 3 for image generation
4. More cost-effective than DALL-E

### Option 2: Use OpenAI DALL-E (Current)
- Scripts support fallback to DALL-E if Gemini unavailable
- Set `USE_GEMINI=false` for images

### Option 3: Prompt Enhancement
- Use Gemini to enhance visual prompts
- Then generate with DALL-E or Imagen

## Cost Comparison

| Task | OpenAI | Gemini | Savings |
|------|--------|--------|---------|
| Script (1500 words) | $0.10-$0.15 | $0.03-$0.08 | ~50% |
| Metadata | $0.01-$0.03 | $0.01-$0.02 | ~33% |
| Images (4 scenes) | $0.20-$0.40 | $0.15-$0.30 | ~25% |

**Total per video**: 
- OpenAI: ~$0.46-$1.30
- Gemini: ~$0.35-$0.90
- **Savings: ~25-30%**

## Mixed Usage

You can use both APIs for different tasks:

```env
# Use Gemini for scripts (cheaper)
USE_GEMINI=true

# Use OpenAI for images (better quality)
# Set USE_GEMINI=false in image generation script
```

## Troubleshooting

### "Gemini API key not found"
- Check `.env` file has `GEMINI_API_KEY` set
- Ensure no quotes around the key value
- Verify key is valid at https://makersuite.google.com/app/apikey

### "Permission denied"
- Ensure API is enabled in Google Cloud Console
- Check project permissions
- Verify billing is enabled (for paid usage)

### "Rate limit exceeded"
- Free tier has rate limits
- Consider upgrading to paid tier
- Use fallback to OpenAI

### Image generation not working
- Gemini doesn't have direct image generation
- Use Vertex AI Imagen 3 or OpenAI DALL-E
- Check Vertex AI API is enabled

## Best Practices

1. **Start with Free Tier**: Test with Gemini free tier first
2. **Monitor Usage**: Track costs in Google Cloud Console
3. **Use Fallbacks**: Always have OpenAI as backup
4. **Test Quality**: Compare outputs between APIs
5. **Optimize Costs**: Use Gemini for scripts, DALL-E for images

## API Limits

- **Free Tier**: 60 requests/minute
- **Paid Tier**: Higher limits (check current pricing)
- **Rate Limits**: May vary by project tier

## Next Steps

1. Get your Gemini API key
2. Add to `.env` file
3. Test script generation
4. Compare quality with OpenAI
5. Choose based on your needs

For detailed API documentation:
- https://ai.google.dev/docs
- https://cloud.google.com/vertex-ai/docs
