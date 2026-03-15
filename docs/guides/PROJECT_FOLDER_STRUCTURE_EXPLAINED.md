# Project Folder Structure Explained

## Why Research Folder is Separate

The research folder (`projects/{project_name}/research/`) is separate because the workflow follows a **step-by-step process** where each phase has its own folder for organization and tracking.

## Complete Project Structure

```
projects/
└── {project_name}/
    ├── research/              # Phase 2: Research output
    │   └── research_{timestamp}.json
    ├── script/                # Phase 3: Script generation
    │   └── script_{timestamp}.json
    ├── voiceover/             # Phase 4: Voiceover generation
    │   ├── scene_1.mp3
    │   ├── scene_2.mp3
    │   └── ...
    └── video/                 # Phase 5: Final video
        └── video_{render_id}_{timestamp}.mp4
```

## Reasons for Separate Folders

### 1. **Workflow Phases**
Each folder represents a distinct phase in the video creation workflow:
- **Research** → Gather facts and information
- **Script** → Write video script based on research
- **Voiceover** → Generate audio from script
- **Video** → Assemble final video

### 2. **Manual Review Process**
Research and scripts go through **manual review**:
- Research files are saved with `review_status: "pending"`
- After review, status changes to `"approved"` or `"rejected"`
- Separate folders make it easy to find files for review

### 3. **File Organization**
- **Research**: JSON files with facts and sources
- **Script**: JSON files with scenes and dialogue
- **Voiceover**: MP3 audio files
- **Video**: MP4 video files

Different file types are easier to manage in separate folders.

### 4. **Version Control**
Each step can have multiple versions:
- `research_20260120_214340.json`
- `research_20260120_220000.json` (regenerated)
- `script_20260120_225130.json`

Separate folders prevent file name conflicts.

### 5. **Workflow Tracking**
You can see workflow progress by checking folders:
```
projects/my_project/
├── research/     ✅ Research complete
├── script/        ✅ Script complete
├── voiceover/     ✅ Voiceover complete
└── video/         ✅ Video complete
```

## Current Structure Examples

### Example 1: `supply_demand_economics`
```
projects/supply_demand_economics/
└── research/
    └── research_20260120_225050.json
```
**Status**: Research phase complete, script not yet generated

### Example 2: `supply__demand_in_economics_for_school`
```
projects/supply__demand_in_economics_for_school/
├── script_20260120_225130.json  # ⚠️ Should be in script/ folder
├── voiceover/
│   ├── scene_1.mp3
│   └── ...
└── video/
    └── video_*.mp4
```
**Status**: Workflow complete, but script file is in root (inconsistency)

## Inconsistency Found

**Issue**: Some projects have scripts in root folder instead of `script/` folder.

**Expected Structure**:
```
projects/{project_name}/
├── research/
├── script/          # ← Scripts should be here
├── voiceover/
└── video/
```

**Current Structure** (inconsistent):
```
projects/{project_name}/
├── script_*.json    # ← Scripts are here (wrong location)
├── voiceover/
└── video/
```

## Why This Matters

1. **Consistency**: All projects should follow the same structure
2. **Organization**: Easier to find files when organized by phase
3. **Review Process**: Script review expects files in `script/` folder
4. **Workflow Tracking**: Clear folder structure shows progress

## Recommendation

**Option 1: Move Scripts to `script/` Folder** (Recommended)
- Update `generate_script.py` to save to `projects/{project_name}/script/`
- Move existing scripts to correct folders
- Maintains consistency with research folder structure

**Option 2: Keep Current Structure**
- Accept scripts in root folder
- Update documentation to reflect this
- Less organized but simpler

## Summary

The research folder is separate because:
- ✅ **Workflow organization** - Each phase has its own folder
- ✅ **Manual review** - Easy to find files for review
- ✅ **File types** - Different file types (JSON, MP3, MP4) organized separately
- ✅ **Version control** - Multiple versions per phase
- ✅ **Progress tracking** - Clear workflow status

**Note**: There's an inconsistency where scripts are saved to root folder instead of `script/` folder. Consider standardizing the structure.
