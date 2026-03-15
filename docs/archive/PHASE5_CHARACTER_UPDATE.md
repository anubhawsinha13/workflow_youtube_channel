# Phase 5: Visual Generation with Character Folder - Complete ✅

## Summary

Updated Phase 5 (Visual Generation) to:
1. ✅ Check `character/` folder first for character images
2. ✅ Fallback to Gemini API if no character found
3. ✅ Support multiple image formats and naming patterns

## What Was Added

### 1. Character Folder Check

**Location**: `character/` folder in workspace

**Priority**: First check before API generation

**File Naming Patterns** (in order of preference):
- `character_{scene_num}.png` (e.g., `character_1.png`)
- `scene_{scene_num}.png` (e.g., `scene_1.png`)
- `{scene_num}.png` (e.g., `1.png`)
- `*{scene_num}*` (wildcard pattern, e.g., `main_character_1_v2.png`)
- Generic files if scene-specific not found

**Supported Formats**:
- `.png`
- `.jpg` / `.jpeg`
- `.gif`
- `.webp`

### 2. Updated Image Generation Flow

**File**: `execution/generate_visuals.py`

**New Functions**:
- ✅ `check_character_folder(scene_num)` - Checks character folder for scene-specific or generic images
- ✅ Updated `generate_image_with_gemini()` - Improved with OpenAI fallback
- ✅ Updated `generate_visuals()` - Integrated character folder check first

**Workflow**:
1. **Check Character Folder**: For each scene, check for character images first
2. **Use Character**: If found, copy to output directory and skip API generation
3. **Fallback to Gemini**: If no character found, generate with Gemini API
4. **Fallback to OpenAI**: If Gemini fails, fallback to OpenAI DALL-E

### 3. Updated Documentation

**Files Created**:
- ✅ `CHARACTER_IMAGE_WORKFLOW.md` - Complete workflow guide
- ✅ Updated `directives/visual_generation.md` - Updated directive with character folder workflow

## Complete Workflow

### Step 1: Prepare Character Images (Optional)

Place character images in the `character/` folder:

```
character/
├── character_1.png      # For scene 1
├── character_2.png      # For scene 2
├── scene_3.png          # Alternative naming for scene 3
├── main_character.png   # Generic character (used if scene-specific not found)
└── ...
```

### Step 2: Generate Images

```bash
python execution/generate_visuals.py script.json
```

**Process**:
1. ✅ Check `character/` folder for each scene
2. ✅ If character found → Use it (skip API generation)
3. ✅ If no character → Generate with Gemini API
4. ✅ If Gemini fails → Fallback to OpenAI DALL-E
5. ✅ Save all images to `.tmp/images/scene_{num}.{ext}`

### Step 3: Review Generated Images

Images are saved to:
```
.tmp/images/
├── scene_1.png      # From character folder or generated
├── scene_2.png      # From character folder or generated
└── ...
```

## Example Output

```json
{
  "success": true,
  "image_files": [
    ".tmp/images/scene_1.png",    // From character folder
    ".tmp/images/scene_2.png",    // Generated with Gemini
    ".tmp/images/scene_3.png",    // From character folder
    ".tmp/images/scene_4.png"     // Generated with Gemini
  ],
  "provider": "mixed",
  "sources": {
    "scene_1": "character_folder",
    "scene_2": "gemini",
    "scene_3": "character_folder",
    "scene_4": "gemini"
  }
}
```

## Benefits

1. **Cost Savings**: Reuse existing character images (no API calls)
2. **Consistency**: Ensure consistent character appearance across scenes
3. **Flexibility**: Mix character images with generated images
4. **Speed**: Faster processing (skip API generation for character images)
5. **Fallback**: Automatic fallback to Gemini, then OpenAI if needed

## Error Handling

1. **Character Folder Missing**: Skips character check, proceeds to API generation
2. **No Character Found**: Generates with Gemini API
3. **Gemini Not Available**: Falls back to OpenAI DALL-E
4. **All APIs Fail**: Returns error with details

## Usage Examples

### Basic Usage (Character Folder Present)
```bash
# Place character images in character/ folder
# Run image generation
python execution/generate_visuals.py projects/project_name/script/script_*.json
```

### Without Character Folder
```bash
# No character folder - all images generated with Gemini
python execution/generate_visuals.py script.json
```

### Mixed Scenario
```
character/
├── character_1.png      # Scene 1 uses character
└── character_3.png      # Scene 3 uses character
# Scenes 2, 4, 5+ will be generated with Gemini
```

## Notes

- Character folder is optional - workflow works without it
- Character images are copied, not moved (original files preserved)
- Multiple scenes can use same character image
- Wildcard matching allows flexible naming conventions
- Generic characters used only when scene-specific not found

## Test Results

**Status**: ✅ **Working**

**Character Check**: ✅ Function works correctly
**Gemini Fallback**: ✅ Integrated with OpenAI fallback
**Error Handling**: ✅ Proper fallback chain

## Next Steps

After images are generated:
- ✅ Proceed to video assembly
- ✅ Images ready in `.tmp/images/`
- ✅ Mix of character and generated images supported

See `CHARACTER_IMAGE_WORKFLOW.md` for detailed documentation.
