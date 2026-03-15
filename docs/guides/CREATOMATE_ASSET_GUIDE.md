# Creatomate Asset Upload Guide

## Overview

Based on `creatomate.txt`, Creatomate requires **public URLs** for assets (images, audio, video). The API does NOT have a separate upload endpoint.

## Asset URL Format

From `creatomate.txt`, Creatomate uses asset URLs in this format:
```
https://creatomate.com/files/assets/{uuid}
```

These are assets that have been uploaded to Creatomate's system (likely through the dashboard).

## How Creatomate Handles Assets

### ✅ Supported Methods

1. **Public URLs** (Recommended)
   - Any publicly accessible URL (HTTP/HTTPS)
   - Examples: S3, Google Cloud Storage, CDN, GitHub Releases
   ```json
   "modifications": {
     "Image-1.source": "https://your-bucket.s3.amazonaws.com/image.jpg",
     "Voiceover-1.source": "https://your-bucket.s3.amazonaws.com/audio.mp3"
   }
   ```

2. **Creatomate Asset URLs**
   - Assets uploaded through Creatomate dashboard
   - Format: `https://creatomate.com/files/assets/{uuid}`
   ```json
   "modifications": {
     "1PC-Photo.source": "https://creatomate.com/files/assets/979db4e3-47bb-4c64-92d0-ad92711bbe12"
   }
   ```

### ❌ NOT Supported

1. **Local File Paths**
   - Creatomate cannot access files on your local machine
   - Example: `./projects/project/voiceover/scene_1.mp3` ❌

2. **Base64 Data URIs**
   - Too large for API requests
   - Causes 500 Internal Server Error
   - Example: `data:audio/mpeg;base64,{huge_string}` ❌

3. **Separate Upload Endpoint**
   - `/v1/uploads` returns 404
   - `/v2/uploads` doesn't exist
   - No upload API endpoint available ❌

## Solution: Host Files Publicly

### Option 1: AWS S3 (Recommended for Production)

```python
import boto3

s3 = boto3.client('s3')
bucket_name = 'your-public-bucket'

# Upload file
s3.upload_file('local_file.mp3', bucket_name, 'scene_1.mp3')

# Get public URL
public_url = f"https://{bucket_name}.s3.amazonaws.com/scene_1.mp3"
```

### Option 2: Google Cloud Storage

```python
from google.cloud import storage

client = storage.Client()
bucket = client.bucket('your-public-bucket')
blob = bucket.blob('scene_1.mp3')
blob.upload_from_filename('local_file.mp3')
blob.make_public()

public_url = blob.public_url
```

### Option 3: Temporary Public Server (For Testing)

Use tools like:
- **ngrok**: `ngrok http 8000` → exposes local server
- **Python HTTP Server**: Simple server for testing
- **GitHub Releases**: Upload files and use release URLs

### Option 4: Creatomate Dashboard

1. Go to Creatomate dashboard
2. Upload assets manually
3. Copy asset URLs (format: `https://creatomate.com/files/assets/{uuid}`)
4. Use those URLs in your API calls

## Current Implementation

The code in `execution/assemble_video.py`:

1. ✅ **Detects public URLs** - Uses them directly
2. ⚠️ **Falls back to base64** - For local files (may fail with large files)
3. 💡 **Provides guidance** - Shows options when local files detected

## Recommended Workflow

### For Production:
1. Generate voiceover files (ElevenLabs)
2. Generate image files (Gemini/OpenAI)
3. **Upload to S3/GCS** → Get public URLs
4. Pass public URLs to Creatomate API
5. Render video

### For Testing:
1. Use `upload_assets=False`
2. Manually upload files to Creatomate dashboard
3. Get asset URLs from dashboard
4. Use those URLs in your script

## Example Payload (from creatomate.txt)

```python
import requests

url = "https://api.creatomate.com/v2/renders"
api_key = "your_api_key"

data = {
  "template_id": "ffe9e01b-1c66-4e12-b597-1b87f5feff7b",
  "modifications": {
    "IT-Text.text": "in loving memory of",
    "1PC-Photo.source": "https://creatomate.com/files/assets/979db4e3-47bb-4c64-92d0-ad92711bbe12",
    # ... more modifications
  }
}

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

response = requests.post(url, json=data, headers=headers)
```

## Next Steps

1. ✅ Code updated to handle public URLs properly
2. ⚠️ Need to implement file hosting (S3/GCS) for production
3. 💡 For now, use Creatomate dashboard or provide public URLs manually

## Summary

**Creatomate requires public URLs for assets.**
- ✅ Use public URLs (S3, GCS, CDN)
- ✅ Use Creatomate dashboard asset URLs
- ❌ Don't use local file paths
- ❌ Don't use base64 data URIs (too large)
