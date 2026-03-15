# Video Assembly Directive

## Goal
Combine voiceover, images, and script into final video using Creatomate API.

## Inputs
- `script` (dict): Final script
- `voiceover_files` (list): Audio files from voiceover_generation
- `image_files` (list): Image files from visual_generation
- `template_id` (str): Creatomate template ID

## Execution
Run `execution/assemble_video.py` with all assets.

## Outputs
- `video_url` (str): URL to final rendered video
- `video_file` (str, optional): Local path if video downloaded
- `render_id` (str): Creatomate render ID for tracking

## Tools
- Creatomate API (`requests` package)
- Template with dynamic elements (Text-1, Image-1, Voiceover-1, etc.)

## Edge Cases
- Missing assets: Wait or use placeholders
- Template mismatch: Validate element names before render
- Render timeout: Poll status and handle long renders
- Render failures: Retry with simplified template

## Quality Requirements
- Audio and visuals properly synced
- Smooth transitions between scenes
- Professional video quality
- Appropriate video length for content

## Error Handling
- Poll render status every 10 seconds
- Timeout after 5 minutes of waiting
- Retry failed renders
- Log all render errors

## Cost Optimization
- Use appropriate video quality settings
- Batch multiple videos when possible
- Monitor render costs per video

## Notes
- Video assembly is final step before publishing
- Ensure all assets are accessible to Creatomate
- Test template with sample data first
- Download video file for YouTube upload
