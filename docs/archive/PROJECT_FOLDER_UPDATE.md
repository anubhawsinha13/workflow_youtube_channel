# Project Folder Organization Update ✅

## Summary

Updated voiceover and video generation to save outputs in project folder structure, matching the pattern used for research and scripts.

## Changes Made

### 1. Voiceover Generation - Project Folder Support

**Updated**: `execution/generate_voiceover.py`

**New Features**:
- ✅ Save voiceover files to `projects/{project_name}/voiceover/`
- ✅ Accept `project_name` parameter
- ✅ Auto-detect `project_name` from script JSON
- ✅ Copy files to project folder after generation
- ✅ Maintain backward compatibility (still works without project_name)

**Project Structure**:
```
projects/
└── {project_name}/
    ├── research/
    │   └── research_{timestamp}.json
    ├── script/
    │   └── script_{timestamp}.json
    └── voiceover/                    # ← NEW
        ├── scene_1.mp3
        ├── scene_2.mp3
        └── ...
```

### 2. Video Generation - Project Folder Support

**Updated**: `execution/assemble_video.py`

**New Features**:
- ✅ Download final video from Creatomate URL
- ✅ Save video to `projects/{project_name}/video/`
- ✅ Accept `project_name` parameter
- ✅ Auto-detect `project_name` from script JSON
- ✅ Automatic video download after render completes

**Project Structure**:
```
projects/
└── {project_name}/
    ├── research/
    ├── script/
    ├── voiceover/
    └── video/                         # ← NEW
        └── video_{render_id}_{timestamp}.mp4
```

## Updated Functions

### `generate_voiceovers()`
- Added `project_name` parameter
- Automatically saves to project folder if `project_name` provided
- Returns project folder information in result

### `save_voiceovers_to_project()`
- New function to copy voiceover files to project folder
- Returns project directory paths

### `assemble_video()`
- Added `project_name` parameter
- Automatically downloads and saves video if `project_name` provided

### `save_video_to_project()`
- New function to download and save video to project folder
- Creates timestamped filename with render_id

### `wait_for_render()`
- Updated to accept `project_name` parameter
- Automatically downloads video after render completes

### `download_video()`
- New function to download video from URL to local file
- Handles streaming download with chunked writing

## Usage Examples

### Generate Voiceover with Project Folder
```bash
python execution/generate_voiceover.py script.json [voice_id] [use_turbo] [project_name]
```

**Example**:
```bash
python execution/generate_voiceover.py projects/blackberry/script_*.json None false blackberry
```

**Result**:
- Voiceover files saved to: `projects/blackberry/voiceover/scene_*.mp3`
- Returns: `{"voiceover_dir": "projects/blackberry/voiceover", ...}`

### Assemble Video with Project Folder
```bash
python execution/assemble_video.py script.json audio.json image.json [template_id] [element_prefix] [project_name]
```

**Example**:
```bash
python execution/assemble_video.py script.json audio.json image.json template_id None blackberry
```

**Result**:
- Video downloaded and saved to: `projects/blackberry/video/video_{render_id}_{timestamp}.mp4`
- Returns: `{"video_path": "projects/blackberry/video/video_...mp4", ...}`

## Project Folder Structure

**Complete Structure**:
```
projects/
└── {project_name}/
    ├── research/
    │   └── research_{timestamp}.json
    ├── script/
    │   └── script_{timestamp}.json
    ├── voiceover/
    │   ├── scene_1.mp3
    │   ├── scene_2.mp3
    │   └── ...
    └── video/
        └── video_{render_id}_{timestamp}.mp4
```

## Auto-Detection

Both functions automatically detect `project_name` from script JSON if not provided:

```python
# Script JSON contains:
{
  "project_name": "blackberry_history",
  "script": {...}
}

# Functions automatically use this project_name
```

## Backward Compatibility

- ✅ Still works without `project_name` (saves to `.tmp/` folders)
- ✅ Voiceover files saved to temp first, then copied to project
- ✅ Video URL still returned even if download fails

## Output Structure

### Voiceover Result
```json
{
  "success": true,
  "voiceover_files": [
    "projects/blackberry/voiceover/scene_1.mp3",
    "projects/blackberry/voiceover/scene_2.mp3"
  ],
  "project_dir": "projects/blackberry",
  "voiceover_dir": "projects/blackberry/voiceover",
  "total_duration": 120.5
}
```

### Video Result
```json
{
  "success": true,
  "video_url": "https://creatomate.com/video/...",
  "video_path": "projects/blackberry/video/video_render123_20260120_123456.mp4",
  "project_dir": "projects/blackberry",
  "video_dir": "projects/blackberry/video",
  "render_id": "render123",
  "status": "succeeded"
}
```

## Benefits

1. **Organization**: All project assets in one place
2. **Traceability**: Easy to find voiceovers and videos for each project
3. **Backup**: Project folders can be easily backed up
4. **Consistency**: Matches existing project folder pattern
5. **Archival**: Easy to archive complete projects

## Updated Files

1. ✅ `execution/generate_voiceover.py` - Added project folder support
2. ✅ `execution/assemble_video.py` - Added video download and project folder support
3. ✅ `PROJECT_FOLDER_UPDATE.md` - This documentation

## Notes

- Voiceover files are still generated in temp folder first, then copied to project
- Video files are downloaded after render completes (may take time)
- Project folders are auto-created if they don't exist
- Video filenames include render_id for easy tracking
