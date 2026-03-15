#!/bin/bash
# Gemini Veo Setup Script
# This script helps set up Gemini Veo video generation

set -e

echo "🚀 Gemini Veo Setup Script"
echo "=========================="
echo ""

# Check if we're in the right directory
if [ ! -f "requirements.txt" ]; then
    echo "❌ Error: Please run this script from the workflow_youtube_channel directory"
    exit 1
fi

# Step 1: Install Python dependencies
echo "📦 Step 1: Installing Python dependencies..."
if [ -d "venv" ]; then
    source venv/bin/activate
else
    echo "⚠️  Virtual environment not found. Creating one..."
    python3 -m venv venv
    source venv/bin/activate
fi

pip install -q --upgrade pip
pip install -q google-cloud-aiplatform>=1.38.0
pip install -q google-generativeai>=0.3.0

echo "✅ Python dependencies installed"
echo ""

# Step 2: Check FFmpeg
echo "🎬 Step 2: Checking FFmpeg installation..."
if command -v ffmpeg &> /dev/null; then
    echo "✅ FFmpeg is installed: $(ffmpeg -version | head -1)"
else
    echo "⚠️  FFmpeg not found"
    echo "   Install with: brew install ffmpeg (macOS)"
    echo "   Or: sudo apt-get install ffmpeg (Linux)"
fi
echo ""

# Step 3: Check Google Cloud SDK
echo "☁️  Step 3: Checking Google Cloud SDK..."
if command -v gcloud &> /dev/null; then
    echo "✅ Google Cloud SDK is installed"
    gcloud --version | head -1
else
    echo "⚠️  Google Cloud SDK not found (optional)"
    echo "   Install from: https://cloud.google.com/sdk/docs/install"
    echo "   Or use service account authentication instead"
fi
echo ""

# Step 4: Check environment variables
echo "🔐 Step 4: Checking environment variables..."
if [ -f ".env" ]; then
    source .env 2>/dev/null || true
    
    if [ -z "$GEMINI_API_KEY" ]; then
        echo "❌ GEMINI_API_KEY not set in .env"
    else
        echo "✅ GEMINI_API_KEY is set"
    fi
    
    if [ -z "$GOOGLE_CLOUD_PROJECT" ]; then
        echo "❌ GOOGLE_CLOUD_PROJECT not set in .env"
    else
        echo "✅ GOOGLE_CLOUD_PROJECT is set: $GOOGLE_CLOUD_PROJECT"
    fi
    
    if [ -z "$GOOGLE_CLOUD_LOCATION" ]; then
        echo "⚠️  GOOGLE_CLOUD_LOCATION not set (default: us-central1)"
    else
        echo "✅ GOOGLE_CLOUD_LOCATION is set: $GOOGLE_CLOUD_LOCATION"
    fi
    
    if [ "$USE_GEMINI_VIDEO" = "true" ]; then
        echo "✅ USE_GEMINI_VIDEO is enabled"
    else
        echo "⚠️  USE_GEMINI_VIDEO is not enabled (set to 'true' in .env)"
    fi
else
    echo "❌ .env file not found"
    echo "   Create .env file with required variables"
fi
echo ""

# Step 5: Test imports
echo "🧪 Step 5: Testing Python imports..."
python3 -c "
try:
    import google.cloud.aiplatform
    print('✅ google-cloud-aiplatform imported successfully')
except ImportError as e:
    print(f'❌ google-cloud-aiplatform import failed: {e}')

try:
    import google.generativeai
    print('✅ google-generativeai imported successfully')
except ImportError as e:
    print(f'❌ google-generativeai import failed: {e}')
"
echo ""

# Step 6: Summary and next steps
echo "📋 Setup Summary"
echo "================"
echo ""
echo "Next steps:"
echo ""
echo "1. Set up Google Cloud Project:"
echo "   - Go to: https://console.cloud.google.com"
echo "   - Create/select a project"
echo "   - Enable Vertex AI API"
echo ""
echo "2. Configure authentication:"
echo "   - Run: gcloud auth application-default login"
echo "   - Or set up service account (see GEMINI_VEO_SETUP_STEPS.md)"
echo ""
echo "3. Update .env file:"
echo "   - Add GOOGLE_CLOUD_PROJECT=your-project-id"
echo "   - Add GOOGLE_CLOUD_LOCATION=us-central1"
echo "   - Set USE_GEMINI_VIDEO=true (optional)"
echo ""
echo "4. Test video generation:"
echo "   python execution/assemble_video.py script.json audio.json image.json project_name --use-gemini-video"
echo ""
echo "📖 For detailed instructions, see: GEMINI_VEO_SETUP_STEPS.md"
echo ""
