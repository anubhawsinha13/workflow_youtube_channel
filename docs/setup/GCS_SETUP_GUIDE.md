# Google Cloud Storage (GCS) Setup Guide

## Overview

This guide will help you set up Google Cloud Storage to host files publicly for Creatomate. GCS allows you to upload audio and image files and get public URLs that Creatomate can access.

---

## Step 1: Create Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Click **"Select a project"** → **"New Project"**
3. Enter project name (e.g., `youtube-workflow`)
4. Click **"Create"**
5. Wait for project creation (may take a minute)

---

## Step 2: Enable Cloud Storage API

1. In Google Cloud Console, go to **"APIs & Services"** → **"Library"**
2. Search for **"Cloud Storage API"**
3. Click on it and click **"Enable"**

---

## Step 3: Create Storage Bucket

1. Go to **"Cloud Storage"** → **"Buckets"**
2. Click **"Create Bucket"**
3. Configure bucket:
   - **Name**: `your-bucket-name` (must be globally unique, e.g., `youtube-workflow-assets-12345`)
   - **Location type**: `Region` (choose closest to you)
   - **Storage class**: `Standard`
   - **Access control**: `Uniform` (recommended)
   - **Public access**: Check **"Enforce public access prevention"** → **Uncheck it** (we need public access)
   - Click **"Create"**

---

## Step 4: Make Bucket Public

1. Go to your bucket → **"Permissions"** tab
2. Click **"Grant Access"**
3. Add:
   - **Principal**: `allUsers`
   - **Role**: `Storage Object Viewer`
   - Click **"Save"**
4. Confirm the warning about public access

**Alternative (via gsutil):**
```bash
gsutil iam ch allUsers:objectViewer gs://your-bucket-name
```

---

## Step 5: Create Service Account (For API Access)

1. Go to **"IAM & Admin"** → **"Service Accounts"**
2. Click **"Create Service Account"**
3. Fill in:
   - **Name**: `youtube-workflow-uploader`
   - **Description**: `Service account for uploading files to GCS`
   - Click **"Create and Continue"**
4. Grant role: **"Storage Object Admin"** (or **"Storage Admin"** for full access)
5. Click **"Continue"** → **"Done"**

---

## Step 6: Create and Download Service Account Key

1. Click on the service account you just created
2. Go to **"Keys"** tab
3. Click **"Add Key"** → **"Create new key"**
4. Choose **JSON** format
5. Click **"Create"**
6. **Save the JSON file** to your project:
   - Location: `workflow_youtube_channel/credentials/gcs-service-account.json`
   - **⚠️ IMPORTANT**: Add this file to `.gitignore` (already done)

---

## Step 7: Install Google Cloud Storage Library

```bash
cd workflow_youtube_channel
source venv/bin/activate
pip install google-cloud-storage
```

Or add to `requirements.txt`:
```
google-cloud-storage>=2.10.0
```

---

## Step 8: Set Environment Variables

Add to your `.env` file:

```bash
# Google Cloud Storage
GCS_BUCKET_NAME=your-bucket-name
GCS_SERVICE_ACCOUNT_PATH=credentials/gcs-service-account.json
GCS_PUBLIC_URL_PREFIX=https://storage.googleapis.com/your-bucket-name
```

**Note**: Replace `your-bucket-name` with your actual bucket name.

---

## Step 9: Test Upload

Run the test script:

```bash
python execution/upload_to_gcs.py --test
```

Or upload a file manually:

```bash
python execution/upload_to_gcs.py \
  projects/supply__demand_in_economics_for_school/voiceover/scene_1.mp3 \
  voiceovers/scene_1.mp3
```

---

## Usage in Code

### Basic Upload

```python
from execution.upload_to_gcs import upload_file_to_gcs

# Upload file and get public URL
result = upload_file_to_gcs(
    local_path="projects/project/voiceover/scene_1.mp3",
    gcs_path="voiceovers/scene_1.mp3"  # Path in bucket
)

if result["success"]:
    public_url = result["public_url"]
    print(f"Public URL: {public_url}")
else:
    print(f"Error: {result['error']}")
```

### Upload Multiple Files

```python
from execution.upload_to_gcs import upload_files_to_gcs

files = [
    ("local/path/scene_1.mp3", "voiceovers/scene_1.mp3"),
    ("local/path/scene_2.mp3", "voiceovers/scene_2.mp3"),
    ("local/path/image_1.png", "images/image_1.png"),
]

results = upload_files_to_gcs(files)
for result in results:
    if result["success"]:
        print(f"✅ {result['public_url']}")
    else:
        print(f"❌ {result['error']}")
```

---

## Public URL Format

After uploading, files will be accessible at:
```
https://storage.googleapis.com/{bucket-name}/{file-path}
```

Example:
```
https://storage.googleapis.com/youtube-workflow-assets-12345/voiceovers/scene_1.mp3
```

---

## Cost Considerations

- **Free Tier**: 5 GB storage, 1 GB egress/month
- **Storage**: ~$0.020 per GB/month
- **Egress**: ~$0.12 per GB (after free tier)
- **Operations**: Minimal cost (thousands of operations per dollar)

**For this project**: Very low cost (few MB of files, minimal egress)

---

## Security Best Practices

1. ✅ **Service Account**: Use service account (not your personal account)
2. ✅ **Least Privilege**: Grant only `Storage Object Admin` role
3. ✅ **Credentials**: Never commit service account JSON to git
4. ✅ **Bucket Policy**: Consider restricting public access to specific paths
5. ✅ **Monitoring**: Enable Cloud Storage audit logs

---

## Troubleshooting

### Error: "Could not automatically determine credentials"

**Solution**: Set environment variable:
```bash
export GOOGLE_APPLICATION_CREDENTIALS="credentials/gcs-service-account.json"
```

Or in `.env`:
```bash
GOOGLE_APPLICATION_CREDENTIALS=credentials/gcs-service-account.json
```

### Error: "Access Denied" or "Permission Denied"

**Solutions**:
1. Check service account has `Storage Object Admin` role
2. Verify bucket name is correct
3. Ensure bucket allows public access (if needed)

### Error: "Bucket not found"

**Solutions**:
1. Verify bucket name in `.env` matches actual bucket
2. Check bucket exists in Google Cloud Console
3. Ensure you're using the correct project

### Files not publicly accessible

**Solutions**:
1. Check bucket permissions (should have `allUsers:objectViewer`)
2. Verify file was uploaded successfully
3. Check file path in URL matches GCS path

---

## Next Steps

1. ✅ Complete GCS setup
2. ✅ Test upload script
3. ✅ Update `assemble_video.py` to use GCS
4. ✅ Test end-to-end workflow

---

## References

- [Google Cloud Storage Documentation](https://cloud.google.com/storage/docs)
- [Python Client Library](https://googleapis.dev/python/storage/latest/index.html)
- [Public Access Setup](https://cloud.google.com/storage/docs/access-control/making-data-public)
