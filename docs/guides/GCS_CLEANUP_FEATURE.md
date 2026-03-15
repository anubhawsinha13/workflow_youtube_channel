# GCS Cleanup Feature

## Overview

Files uploaded to Google Cloud Storage (GCS) for Creatomate video rendering are now automatically deleted after the video is successfully generated. This helps reduce storage costs and keeps your bucket clean.

## How It Works

### Automatic Cleanup

When `assemble_video.py` runs:

1. **Upload Phase**: Local files are uploaded to GCS and public URLs are obtained
2. **Render Phase**: Creatomate uses the public URLs to render the video
3. **Cleanup Phase**: After successful video generation, uploaded files are deleted from GCS

### What Gets Cleaned Up

- ✅ Audio files uploaded to GCS (`{project_name}/voiceover/scene_{n}.mp3`)
- ✅ Image files uploaded to GCS (`{project_name}/images/scene_{n}.png`)
- ❌ Files that were already public URLs (not uploaded by us)
- ❌ Files uploaded manually (only auto-uploaded files are tracked)

## Implementation Details

### Tracking Uploaded Files

The system tracks which files were uploaded to GCS:
```python
gcs_paths_to_cleanup = []  # List of GCS paths to delete

# When uploading:
gcs_paths_to_cleanup.append(gcs_path)
```

### Cleanup After Success

Cleanup only happens if:
- ✅ Video generation was successful
- ✅ Files were uploaded to GCS (not base64 or existing URLs)
- ✅ GCS is available and configured

```python
if video_result.get("success") and gcs_paths_to_cleanup and GCS_AVAILABLE:
    delete_files_from_gcs(gcs_paths_to_cleanup)
```

## Manual Cleanup

You can also manually delete files from GCS:

### Delete Single File

```bash
python execution/upload_to_gcs.py --delete "project_name/voiceover/scene_1.mp3"
```

### Delete All Project Files

```bash
python execution/upload_to_gcs.py --delete-project "project_name"
```

This will delete all files under `project_name/` prefix in your GCS bucket.

## Benefits

1. **Cost Savings**: Reduces GCS storage costs by removing temporary files
2. **Clean Bucket**: Keeps your GCS bucket organized
3. **Automatic**: No manual cleanup needed
4. **Safe**: Only deletes files that were uploaded by the system

## Error Handling

If cleanup fails:
- ⚠️ Warning is printed but doesn't fail the video generation
- Files remain in GCS (can be cleaned up manually later)
- Video generation result is still returned successfully

## Configuration

Cleanup is automatic when:
- ✅ `GCS_BUCKET_NAME` is set in `.env`
- ✅ `GCS_SERVICE_ACCOUNT_PATH` points to valid credentials
- ✅ `google-cloud-storage` package is installed

If GCS is not configured, cleanup is skipped (no error).

## Example Workflow

```python
# 1. Upload files to GCS
result = upload_file_to_gcs("local.mp3", "project/voiceover/scene_1.mp3")
# Returns: {"success": True, "public_url": "https://...", "gcs_path": "project/voiceover/scene_1.mp3"}

# 2. Use public URL for Creatomate
creatomate_payload = {
    "modifications": {
        "Voiceover-1.source": result["public_url"]
    }
}

# 3. Render video
video_result = render_video(creatomate_payload)

# 4. Cleanup (automatic)
if video_result["success"]:
    delete_files_from_gcs([result["gcs_path"]])
```

## Files Updated

- ✅ `execution/upload_to_gcs.py` - Added delete functions
- ✅ `execution/assemble_video.py` - Integrated automatic cleanup
- ✅ `GCS_CLEANUP_FEATURE.md` - This documentation

## Summary

**Automatic GCS cleanup** ensures that temporary files uploaded for Creatomate are removed after successful video generation, reducing storage costs and keeping your bucket clean.
