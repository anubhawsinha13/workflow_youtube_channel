# Project Testing Guide

**Date**: January 2026  
**Purpose**: Step-by-step guide to test the complete workflow

---

## Prerequisites Checklist

### ✅ 1. Environment Setup
- [x] Python 3.8+ installed
- [x] Virtual environment created and activated
- [x] Dependencies installed (`pip install -r requirements.txt`)

### ⚠️ 2. API Keys Required
Make sure you have all API keys in your `.env` file:

- [ ] **Perplexity API Key** - Required for research
  - Get from: https://www.perplexity.ai → Settings → API Keys
  - Add to `.env`: `PERPLEXITY_API_KEY=pplx-...`

- [ ] **Gemini API Key** - Required for script generation
  - Get from: https://aistudio.google.com/apikey
  - Add to `.env`: `GEMINI_API_KEY=...`

- [ ] **OpenAI API Key** - Required for script generation (fallback)
  - Get from: https://platform.openai.com/api-keys
  - Add to `.env`: `OPENAI_API_KEY=...`

- [ ] **ElevenLabs API Key** - Required for voiceover generation
  - Get from: https://elevenlabs.io → Profile → API Keys
  - Add to `.env`: `ELEVENLABS_API_KEY=...`

- [ ] **Creatomate API Key** - Required for video assembly
  - Get from: https://creatomate.com → Project Settings → API Keys
  - Add to `.env`: `CREATOMATE_API_KEY=...`

- [ ] **Creatomate Template ID** - Required for video assembly
  - Create template in Creatomate dashboard
  - Get Template ID from template settings
  - Add to `.env`: `CREATOMATE_TEMPLATE_ID=...`

### ⚠️ 3. Creatomate Template Setup
- [ ] Template created in Creatomate dashboard
- [ ] Dynamic elements configured:
  - Voiceover elements: `Voiceover-1`, `Voiceover-2`, etc.
  - Image elements: `Image-1`, `Image-2`, etc.
  - Text elements (optional): `Text-1`, `Text-2`, etc.
- [ ] Element naming convention documented

---

## Testing Steps

### Phase 1: Research ✅

**Test Research Generation**:

```bash
cd workflow_youtube_channel
source venv/bin/activate
python execution/research_topic.py "The rise and fall of Blackberry" 4 "blackberry_test"
```

**What to expect**:
- ✅ Research facts generated
- ✅ Sources extracted
- ✅ File saved to: `projects/blackberry_test/research/research_{timestamp}.json`

**Manual Review**:

```bash
python execution/review_research.py projects/blackberry_test/research/research_*.json
```

**Options**:
- Approve → Continue to script generation
- Edit → Modify the research file
- Regenerate → Run research again
- Reject → Exit

**Expected Output**:
```
projects/blackberry_test/
└── research/
    └── research_20260120_214340.json
```

---

### Phase 2: Script Generation ✅

**Test Script Generation**:

```bash
python execution/generate_script.py projects/blackberry_test/research/research_*.json "The rise and fall of Blackberry"
```

**What to expect**:
- ✅ Script generated with Gemini or OpenAI
- ✅ Multiple scenes with dialogue and visual descriptions
- ✅ Description and dialogue limited to 1000 characters
- ✅ File saved to: `projects/blackberry_test/script_{timestamp}.json`

**Manual Review**:

```bash
python execution/review_script.py projects/blackberry_test/script_*.json
```

**Options**:
- Approve → Continue to voiceover generation
- Edit → Modify the script file
- Regenerate → Generate new script
- Reject → Exit

**Expected Output**:
```
projects/blackberry_test/
├── research/
│   └── research_20260120_214340.json
└── script_20260120_211046.json
```

---

### Phase 3: Voiceover Generation ⚠️

**Test Voiceover Generation**:

```bash
python execution/generate_voiceover.py projects/blackberry_test/script_*.json
```

**With Turbo model (optional, 30-40% cheaper)**:

```bash
python execution/generate_voiceover.py projects/blackberry_test/script_*.json None true blackberry_test
```

**What to expect**:
- ✅ Audio files generated for each scene
- ✅ Files saved to: `projects/blackberry_test/voiceover/scene_{num}.mp3`
- ✅ Model used: `eleven_multilingual_v2` (default) or `eleven_turbo_v2_5` (if turbo)
- ⚠️ Requires ElevenLabs credits

**Expected Output**:
```
projects/blackberry_test/
├── research/
├── script_*.json
└── voiceover/
    ├── scene_1.mp3
    ├── scene_2.mp3
    └── ...
```

**Note**: If you get a quota error, add credits to your ElevenLabs account.

---

### Phase 4: Visual Generation ⚠️

**Test Visual Generation**:

```bash
python execution/generate_visuals.py projects/blackberry_test/script_*.json
```

**What to expect**:
- ✅ Checks `character/` folder first for existing images
- ✅ If no character images found, generates with Gemini or DALL-E
- ✅ Images saved to: `.tmp/images/scene_{num}.png`

**Optional: Add Character Images**:
1. Place images in `character/` folder
2. Name them: `character_1.png`, `character_2.png`, etc. or generic names
3. These will be used automatically instead of generating new images

**Expected Output**:
```
.tmp/images/
├── scene_1.png
├── scene_2.png
└── ...
```

---

### Phase 5: Video Assembly ⚠️

**Prepare Audio and Image Files**:

First, create JSON files listing the generated files:

**audio_files.json**:
```json
{
  "voiceover_files": [
    "projects/blackberry_test/voiceover/scene_1.mp3",
    "projects/blackberry_test/voiceover/scene_2.mp3"
  ]
}
```

**image_files.json**:
```json
{
  "image_files": [
    ".tmp/images/scene_1.png",
    ".tmp/images/scene_2.png"
  ]
}
```

**Test Video Assembly**:

```bash
python execution/assemble_video.py projects/blackberry_test/script_*.json audio_files.json image_files.json
```

**What to expect**:
- ✅ Assets uploaded to Creatomate
- ✅ Video render initiated
- ✅ Render status polling (may take 2-5 minutes)
- ✅ Video downloaded and saved to: `projects/blackberry_test/video/video_{render_id}_{timestamp}.mp4`

**Expected Output**:
```
projects/blackberry_test/
├── research/
├── script_*.json
├── voiceover/
│   ├── scene_1.mp3
│   └── ...
└── video/
    └── video_render123_20260120_123456.mp4
```

---

## Quick Test (All Phases)

### Complete End-to-End Test:

```bash
# 1. Research
python execution/research_topic.py "The rise and fall of Blackberry" 4 "blackberry_test"
python execution/review_research.py projects/blackberry_test/research/research_*.json
# (Approve the research)

# 2. Script Generation
python execution/generate_script.py projects/blackberry_test/research/research_*.json "The rise and fall of Blackberry"
python execution/review_script.py projects/blackberry_test/script_*.json
# (Approve the script)

# 3. Voiceover Generation
python execution/generate_voiceover.py projects/blackberry_test/script_*.json

# 4. Visual Generation
python execution/generate_visuals.py projects/blackberry_test/script_*.json

# 5. Video Assembly
# (Create audio_files.json and image_files.json first)
python execution/assemble_video.py projects/blackberry_test/script_*.json audio_files.json image_files.json
```

---

## Testing Individual Components

### Test Perplexity API:

```bash
python execution/research_topic.py "Test topic" 4 "test_project"
```

### Test Gemini API:

```bash
python test_gemini_api.py
```

### Test ElevenLabs API:

```bash
python test_elevenlabs_api.py
```

### Test Script Generation:

Use an existing research file:
```bash
python execution/generate_script.py projects/blackberry_test/research/research_*.json "Test topic"
```

---

## Troubleshooting

### Common Issues:

1. **API Key Not Found**:
   - Check `.env` file exists
   - Verify API key format
   - Ensure keys are in correct format (no quotes, no spaces)

2. **Perplexity Error - Model Not Found**:
   - ✅ Fixed - Using `sonar` model

3. **Gemini Error - Model Not Found**:
   - ✅ Fixed - Using fallback chain: `gemini-1.5-pro` → `gemini-2.5-pro` → `gemini-pro-latest`

4. **ElevenLabs Quota Exceeded**:
   - Add credits to ElevenLabs account
   - Integration is working, just needs credits

5. **Creatomate Template Error**:
   - Verify template ID is correct
   - Check element names match template
   - Ensure template is active in Creatomate dashboard

6. **File Not Found Errors**:
   - Check file paths are correct
   - Ensure previous phases completed successfully
   - Verify project folder exists

---

## Expected Project Structure After Testing

```
projects/
└── blackberry_test/
    ├── research/
    │   └── research_20260120_214340.json
    ├── script_20260120_211046.json
    ├── voiceover/
    │   ├── scene_1.mp3
    │   ├── scene_2.mp3
    │   └── ...
    └── video/
        └── video_render123_20260120_123456.mp4
```

---

## Testing Checklist

### Pre-Testing:
- [ ] All API keys in `.env`
- [ ] Creatomate template configured
- [ ] Virtual environment activated
- [ ] Dependencies installed

### Phase-by-Phase:
- [ ] Phase 1: Research ✅ (Tested and working)
- [ ] Phase 2: Script Generation ✅ (Tested and working)
- [ ] Phase 3: Voiceover Generation ⚠️ (Ready, needs credits)
- [ ] Phase 4: Visual Generation ⚠️ (Ready, needs testing)
- [ ] Phase 5: Video Assembly ⚠️ (Ready, needs testing)

### End-to-End:
- [ ] Complete workflow tested
- [ ] All files saved to project folders
- [ ] Video generated successfully

---

## Cost Estimates

### Per Video (Approximate):
- **Research (Perplexity)**: ~$0.05-$0.15
- **Script (Gemini/OpenAI)**: ~$0.10-$0.30
- **Voiceover (ElevenLabs)**: ~$0.12-$0.30 (or ~$0.08-$0.18 with Turbo)
- **Visuals (Gemini/DALL-E)**: ~$0.10-$0.40
- **Video Assembly (Creatomate)**: Varies by plan

**Total**: ~$0.37-$1.15 per video (or ~$0.33-$1.03 with Turbo)

---

## Next Steps After Testing

1. **Review Outputs**:
   - Check research accuracy
   - Review script quality
   - Listen to voiceover samples
   - Preview generated visuals
   - Watch final video

2. **Optimize Settings**:
   - Adjust voice settings (stability, similarity, style)
   - Tune character limits
   - Optimize prompts
   - Enable Turbo for cost savings

3. **Production Ready**:
   - Once all phases work correctly
   - Consider implementing LangGraph orchestration
   - Add YouTube publishing automation
   - Set up scheduled runs

---

## Support & Documentation

- **API Setup**: See `API_KEYS_SETUP.md`
- **Workflow Details**: See `END_TO_END_TESTING_READINESS.md`
- **Project Status**: See `PROJECT_STATUS.md`
- **Architecture**: See `AGENT_BASED_ARCHITECTURE.md`

---

## Summary

✅ **Ready for Testing**: Core workflow (Phases 1-5) is implemented and ready

**Quick Start**:
1. Ensure all API keys in `.env`
2. Set up Creatomate template
3. Run phases sequentially
4. Review outputs in project folders

**Status**: ✅ **Ready for Manual Testing**
