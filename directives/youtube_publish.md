# YouTube Publishing Directive

## Goal
Upload final video to YouTube with proper metadata and AI disclosure.

## Inputs
- `video_file` (str): Path to final video file
- `script` (dict): Script with metadata (title, description, tags)
- `privacy_status` (str): "private", "unlisted", or "public" (default: "private")
- `niche` (str): Content niche

## Execution
Run `execution/publish_to_youtube.py` with video file and metadata.

## Outputs
- `youtube_video_id` (str): YouTube video ID
- `youtube_url` (str): Video URL
- `upload_status` (str): "uploaded", "processing", or "failed"

## Tools
- YouTube Data API v3 (`google-api-python-client`)
- OAuth 2.0 authentication

## Critical Requirements
- **MUST** set "Altered Content" flag (required for AI content in 2026)
- Include AI disclosure in description
- Proper metadata (title, description, tags)
- Correct category and privacy settings

## Edge Cases
- Large video files: Use resumable upload
- OAuth token expired: Refresh token automatically
- Upload quota exceeded: Queue for later upload
- Metadata too long: Truncate and validate

## Error Handling
- Retry failed uploads with exponential backoff
- Resume interrupted uploads
- Validate video file exists and is readable
- Handle YouTube API errors gracefully

## Compliance Checklist
- [ ] AI content disclosed
- [ ] "Altered Content" flag set
- [ ] Fair Use guidelines followed
- [ ] Original content value added
- [ ] No copyright violations
- [ ] Appropriate thumbnail uploaded

## Notes
- Publishing is irreversible - verify everything first
- Always start with "private" status for review
- Monitor upload progress for large files
- Keep credentials secure (use OAuth, not API key)
