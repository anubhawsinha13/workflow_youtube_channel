# Voiceover Generation Directive

## Goal
Convert script text into high-quality audio narration using ElevenLabs.

## Inputs
- `script` (dict): Verified script from fact_check directive
- `voice_id` (str, optional): ElevenLabs voice ID (default: "Deep Narration")

## Execution
Run `execution/generate_voiceover.py` with script scenes.

## Outputs
- `voiceover_files` (list): List of audio file paths
  - Each scene generates one audio file: `scene_1.mp3`, `scene_2.mp3`, etc.
- `total_duration` (float): Total audio duration in seconds

## Tools
- ElevenLabs API (`elevenlabs` package)
- Voice: "Deep Narration" or custom cloned voice

## Edge Cases
- Text too long for single API call: Split into chunks
- API rate limits: Implement queue and retry
- Audio quality issues: Use higher quality settings
- Missing voice_id: Use default voice

## Quality Requirements
- Audio should be clear and natural
- Appropriate pacing (not too fast/slow)
- Consistent voice throughout all scenes
- No audio glitches or artifacts

## Error Handling
- Retry failed audio generations
- Save partial voiceovers if some scenes fail
- Log all generation errors
- Validate audio files exist and are playable

## Cost Optimization
- Use Turbo models when available (faster, cheaper)
- Cache voiceover if script unchanged (idempotency)
- Batch process scenes when possible

## Notes
- Voiceover quality is critical for viewer retention
- Test voice before bulk generation
- Consider voice cloning for channel consistency
- Store audio files in `.tmp/` during processing
