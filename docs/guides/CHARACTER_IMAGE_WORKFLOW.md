# Character Image Workflow - Phase 5 Update ✅

## Summary

Updated Phase 5 (Image Generation) to:
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

**Step 1: Check Character Folder**
```python
# For each scene:
1. Check for character files matching scene number
2. If found, copy to output directory (.tmp/images/scene_{num}.{ext})
3. Use character image and skip API generation
```

**Step 2: Fallback to Gemini** (if no character found)
```python
# If no character found:
1. Generate image with Gemini API
2. If Gemini not available, fallback to OpenAI DALL-E
3. Save generated image to .tmp/images/scene_{num}.png
```

### 3. Updated Functions

**File**: `execution/generate_visuals.py`

**New Functions**:
- ✅ `check_character_folder(scene_num)` - Checks character folder for scene-specific or generic images
- ✅ Updated `generate_image_with_gemini()` - Improved with OpenAI fallback
- ✅ Updated `generate_visuals()` - Integrated character folder check first

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

**Naming Rules**:
- Scene-specific: `character_{scene_num}.{ext}` or `scene_{scene_num}.{ext}`
- Generic: Any image file (used as fallback)
- Wildcard: `*{scene_num}*` pattern matching

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

## Character Folder Examples

### Example 1: Scene-Specific Characters
```
character/
├── character_1.png      # Used for scene 1
├── character_2.png      # Used for scene 2
├── character_3.png      # Used for scene 3
└── character_4.png      # Used for scene 4
```

### Example 2: Mixed Naming
```
character/
├── scene_1.png          # Used for scene 1
├── character_2.png      # Used for scene 2
├── main_hero_3.png      # Wildcard match for scene 3
└── generic.png          # Fallback for other scenes
```

### Example 3: Generic Character
```
character/
└── main_character.png   # Used for all scenes if no scene-specific found
```

## Integration with Existing Workflow

### Phase 5: Visual Generation

**Before**:
1. Generate all images with API (DALL-E or Gemini)

**After**:
1. Check `character/` folder for each scene
2. Use character if found
3. Generate with Gemini if no character found
4. Fallback to OpenAI if Gemini fails

**Benefits**:
- ✅ Faster processing (no API calls for character images)
- ✅ Cost savings (reuse existing character images)
- ✅ Consistent character appearance across scenes
- ✅ Flexibility (mix character images with generated images)

## Output Structure

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

## Error Handling

1. **Character Folder Missing**: Skips character check, proceeds to API generation
2. **No Character Found**: Generates with Gemini API
3. **Gemini Not Available**: Falls back to OpenAI DALL-E
4. **All APIs Fail**: Returns error with details

## Best Practices

1. **Organize Character Images**: Use consistent naming (`character_{scene_num}.png`)
2. **Scene-Specific First**: Create scene-specific character images for better control
3. **Generic Fallback**: Include generic character images for scenes without specific images
4. **Format Consistency**: Use same image format (PNG recommended)
5. **Image Quality**: Ensure character images match required resolution (1024x1024+)

## Notes

- Character folder is optional - workflow works without it
- Character images are copied, not moved (original files preserved)
- Multiple scenes can use same character image
- Wildcard matching allows flexible naming conventions
- Generic characters used only when scene-specific not found

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

See `directives/visual_generation.md` for detailed documentation.
