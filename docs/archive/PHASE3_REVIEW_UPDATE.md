# Phase 3: Script Generation with Manual Review - Complete ✅

## Summary

Updated the script generation step (Phase 3) to include:
1. ✅ Manual review step
2. ✅ Project folder organization
3. ✅ Script update capability after review

## What Was Added

### 1. Project Folder Structure

**Location**: `projects/{project_name}/`

**Auto-created** when generating scripts:
```
projects/
└── {project_name}/              # Auto-created from topic
    └── script_{timestamp}.json  # Generated script with metadata
```

**Example**:
```
projects/the_rise_and_fall_of_blackberry/
└── script_20260120_211046.json
```

### 2. Updated Script Generation

**File**: `execution/generate_script.py`

**New Features**:
- ✅ Automatically saves scripts to project folders
- ✅ Creates project folder from topic name
- ✅ Adds metadata (project_name, topic, timestamp, status)
- ✅ Sets review_status to "pending"
- ✅ Provides path to saved script file

**Usage**:
```bash
python execution/generate_script.py research.json "Topic" "Niche" true "project_name"
```

### 3. Manual Review Script

**File**: `execution/review_script.py`

**Features**:
- ✅ Interactive review interface
- ✅ Displays script contents (title, scenes, tags)
- ✅ Review options:
  - Approve and continue
  - Edit script manually
  - Regenerate script
  - Reject and stop
- ✅ Creates review checkpoint files

**Usage**:
```bash
python execution/review_script.py projects/{project_name}/script_{timestamp}.json
```

### 4. Update Script Tool

**File**: `execution/update_script.py`

**Features**:
- ✅ Update existing script after review
- ✅ Automatic backup creation
- ✅ Approve updated scripts
- ✅ Track update history

**Usage**:
```bash
# Update script
python execution/update_script.py projects/{project_name}/script_{timestamp}.json

# Approve script
python execution/update_script.py projects/{project_name}/script_{timestamp}.json --approve
```

### 5. Documentation

**Files Created**:
- ✅ `MANUAL_REVIEW_WORKFLOW.md` - Complete workflow guide
- ✅ Updated `directives/script_generation.md` - Updated directive
- ✅ Updated `execution/generate_script.py` - Save to project folders

## Complete Workflow

### Step 1: Generate Script
```bash
python execution/generate_script.py .tmp/test_research.json \
  "The rise and fall of Blackberry" \
  "History & Biographies" \
  true \
  "blackberry_history"
```

**Output**:
- Script saved to: `projects/blackberry_history/script_20260120_211046.json`
- Status: `review_status: "pending"`

### Step 2: Review Script
```bash
python execution/review_script.py projects/blackberry_history/script_20260120_211046.json
```

**Options**:
1. ✅ Approve → Continue to fact-check/compliance
2. ✏️ Edit → Manually edit JSON file, then review again
3. 🔄 Regenerate → Request new script generation
4. ❌ Reject → Stop workflow

### Step 3: Update Script (if edited)
```bash
# Option A: Edit JSON file directly, then:
python execution/review_script.py projects/blackberry_history/script_20260120_211046.json

# Option B: Use update script
python execution/update_script.py projects/blackberry_history/script_20260120_211046.json
# Edit file when prompted, then save
```

### Step 4: Approve Script
```bash
python execution/update_script.py projects/blackberry_history/script_20260120_211046.json --approve
```

**Result**: `review_status: "approved"` → Ready for next phase

## Script File Structure

```json
{
  "project_name": "blackberry_history",
  "topic": "The rise and fall of Blackberry",
  "generated_at": "2024-01-20T21:10:46",
  "status": "generated",
  "review_status": "pending",
  "success": true,
  "script": {
    "scenes": [
      {
        "scene_number": 1,
        "text": "...",
        "visual_prompt": "...",
        "duration_estimate": 20
      }
    ],
    "title": "...",
    "description": "...",
    "tags": [...]
  },
  "provider": "gemini"
}
```

**After Review**:
```json
{
  ...
  "status": "approved",
  "review_status": "approved",
  "approved_at": "2024-01-20T21:15:30",
  "updated_at": "2024-01-20T21:13:45"  // If edited
}
```

## Benefits

1. **Organization**: All scripts organized by project/use case
2. **Version Control**: Easy to track script versions
3. **Review Process**: Built-in quality gate before expensive operations
4. **Flexibility**: Edit and update scripts easily
5. **Backup**: Automatic backups on updates
6. **Traceability**: Full history of script generation and reviews

## Next Steps

After script is approved:
- ✅ Proceed to fact-check phase
- ✅ Continue to compliance check
- ✅ Generate voiceover
- ✅ Generate visuals
- ✅ Assemble video

See `MANUAL_REVIEW_WORKFLOW.md` for detailed documentation.
