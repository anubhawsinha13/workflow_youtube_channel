#!/usr/bin/env python3
"""
Simple Gemini API Test
Tests direct connection to Gemini API
"""

import os
import json
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

print("Testing Gemini API Connection...")
print(f"API Key: {'✅ Set' if GEMINI_API_KEY and 'your_gemini_key_here' not in GEMINI_API_KEY else '❌ Not set'}")
print(f"Key starts with: {GEMINI_API_KEY[:15] if GEMINI_API_KEY else 'N/A'}...")
print()

try:
    import google.generativeai as genai
    
    print("✅ google.generativeai imported successfully")
    
    if not GEMINI_API_KEY:
        print("❌ GEMINI_API_KEY not set in .env")
        exit(1)
    
    # Configure Gemini
    genai.configure(api_key=GEMINI_API_KEY)
    print("✅ Gemini configured with API key")
    
    # Try to list models
    print("\n📋 Available models:")
    try:
        models = genai.list_models()
        for model in models:
            if 'generateContent' in model.supported_generation_methods:
                print(f"  - {model.name}")
    except Exception as e:
        print(f"  ⚠️  Could not list models: {e}")
    
    # Test simple generation
    print("\n🧪 Testing content generation...")
    # Try gemini-1.5-pro first, fallback if not available
    model = None
    model_name = None
    model_attempts = [
        'gemini-1.5-pro',
        'models/gemini-1.5-pro',
        'gemini-2.5-pro',
        'models/gemini-2.5-pro',
        'gemini-pro-latest',
        'models/gemini-pro-latest'
    ]
    
    for model_name_attempt in model_attempts:
        try:
            test_model = genai.GenerativeModel(model_name_attempt)
            # Try minimal generation to verify model works
            try:
                test_response = test_model.generate_content("test", generation_config={"max_output_tokens": 1})
                model = test_model
                model_name = model_name_attempt
                print(f"  ✅ Using: {model_name}")
                break
            except Exception as e:
                # Model exists but might have issues, continue to next
                continue
        except Exception:
            continue
    
    if model is None:
        print("  ❌ No available Gemini Pro models found")
        exit(1)
    
    response = model.generate_content("Say 'Hello from Gemini!' in one sentence.")
    print(f"✅ Response received: {response.text}")
    
    # Test JSON mode
    print("\n🧪 Testing JSON mode...")
    generation_config = {
        "temperature": 0.7,
        "response_mime_type": "application/json",
    }
    
    json_response = model.generate_content(
        'Return {"test": "success"} as JSON.',
        generation_config=generation_config
    )
    
    result = json.loads(json_response.text)
    print(f"✅ JSON mode works: {result}")
    
    print("\n✅ All Gemini API tests passed!")
    
except ImportError as e:
    print(f"❌ Failed to import google.generativeai: {e}")
    print("   Run: pip install google-generativeai")
except Exception as e:
    print(f"❌ Error: {e}")
    print(f"   Type: {type(e).__name__}")
    import traceback
    traceback.print_exc()
