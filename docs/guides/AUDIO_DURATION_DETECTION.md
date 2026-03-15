# Audio Duration Detection Fix ✅

## Issue
The video was using `duration_estimate` from the script (20 seconds for scene 1), but the actual audio file is only **17 seconds**. This mismatch causes:
- Image/text elements to display longer than audio plays
- Incorrect total video duration
- Timing misalignment between scenes

## Root Cause
The code was using `duration_estimate` from the script without verifying against actual audio file durations.

## Fix Applied

### ✅ 1. Added Mutagen Library
**Updated**: `requirements.txt`
```python
mutagen>=1.47.0  # For reading audio file metadata (duration)
```

### ✅ 2. Added Audio Duration Detection Function
**Updated**: `execution/assemble_video.py`

```python
def get_audio_duration(audio_path: str) -> float:
    """
    Get actual duration of audio file in seconds.
    
    Args:
        audio_path: Path to audio file (local file path)
        
    Returns:
        Duration in seconds, or None if unable to detect
    """
    if not MUTAGEN_AVAILABLE:
        return None
    
    try:
        audio_file = MutagenFile(audio_path)
        if audio_file is not None:
            return audio_file.info.length
    except Exception as e:
        print(f"⚠️  Could not detect audio duration for {audio_path}: {e}")
    
    return None
```

### ✅ 3. Updated Duration Calculation Logic
**Updated**: `execution/assemble_video.py` → `build_creatomate_payload()`

**Before**:
```python
# Always used duration_estimate from script
audio_duration = scene.get("duration_estimate", 5.0)
```

**After**:
```python
# Try actual audio file duration first
audio_duration = None
if audio_files and scene_idx < len(audio_files):
    actual_duration = get_audio_duration(audio_files[scene_idx])
    if actual_duration:
        audio_duration = actual_duration  # Use actual duration
        
# Fallback to duration_estimate if detection fails
if audio_duration is None:
    audio_duration = scene.get("duration_estimate", 5.0)
```

### ✅ 4. Pass Audio Files to Payload Builder
**Updated**: `execution/assemble_video.py` → `assemble_video()`

```python
payload = build_creatomate_payload(
    script, audio_urls, image_urls,
    renderscript_path=renderscript_path,
    audio_files=audio_files  # Pass local file paths for duration detection
)
```

## How It Works Now

1. **Detect Actual Duration**: Reads audio file metadata using Mutagen
2. **Use Actual Duration**: If detection succeeds, use actual file duration
3. **Fallback to Estimate**: If detection fails, use `duration_estimate` from script
4. **Default Fallback**: If no estimate, use 5 seconds default

## Example

**Scene 1**:
- Script `duration_estimate`: 20 seconds
- **Actual audio file**: 17 seconds ✅
- **Used duration**: 17 seconds (from file)

**Scene 2**:
- Script `duration_estimate`: 25 seconds
- **Actual audio file**: 24.5 seconds ✅
- **Used duration**: 24.5 seconds (from file)

## Benefits

✅ **Accurate Timing**: Image/text elements match actual audio length  
✅ **Correct Duration**: Total video duration matches sum of actual audio durations  
✅ **Proper Alignment**: Scenes start at correct cumulative times  
✅ **Fallback Support**: Still works if duration detection fails  

## Testing

After this fix:
- ✅ Scene 1 uses 17 seconds (actual) instead of 20 seconds (estimate)
- ✅ Image/text elements display for 17 seconds (matching audio)
- ✅ Total video duration calculated from actual audio lengths
- ✅ Scenes properly aligned on timeline

## Summary

✅ **Fixed**: Audio duration detection using Mutagen  
✅ **Fixed**: Use actual file durations instead of estimates  
✅ **Fixed**: Fallback to estimates if detection fails  
✅ **Result**: Videos now use accurate audio durations  

The audio duration mismatch should now be resolved! 🎬
