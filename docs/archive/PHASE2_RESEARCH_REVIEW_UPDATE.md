# Phase 2: Research with Manual Review - Complete ✅

## Summary

Updated the research step (Phase 2) to include:
1. ✅ Manual review step
2. ✅ Project folder organization (`projects/{project_name}/research/`)
3. ✅ Research update capability after review

## What Was Added

### 1. Project Folder Structure

**Location**: `projects/{project_name}/research/`

**Auto-created** when generating research:
```
projects/
└── {project_name}/              # Auto-created from topic
    └── research/               # Research step folder
        └── research_{timestamp}.json  # Generated research
```

**Example**:
```
projects/blackberry_test/
└── research/
    └── research_20260120_214340.json
```

### 2. Updated Research Generation

**File**: `execution/research_topic.py`

**New Features**:
- ✅ Automatically saves research to project folder
- ✅ Creates project folder structure: `projects/{project_name}/research/`
- ✅ Adds metadata (project_name, topic, timestamp, status)
- ✅ Sets review_status to "pending"
- ✅ Provides path to saved research file

**Usage**:
```bash
python execution/research_topic.py "Topic" [num_facts] [project_name]
```

**Example**:
```bash
python execution/research_topic.py "The rise and fall of Blackberry" 4 "blackberry_test"
```

### 3. Manual Review Script

**File**: `execution/review_research.py`

**Features**:
- ✅ Interactive review interface
- ✅ Displays research contents (topic, facts, sources, raw response)
- ✅ Review options:
  - **Approve**: Continue to script generation
  - **Edit**: Modify research manually (edit JSON file directly)
  - **Regenerate**: Request new research with same inputs
  - **Reject**: Stop workflow
- ✅ Creates review checkpoint files

**Usage**:
```bash
python execution/review_research.py projects/{project_name}/research/research_{timestamp}.json
```

### 4. Documentation

**Files Created**:
- ✅ `RESEARCH_REVIEW_WORKFLOW.md` - Complete workflow guide
- ✅ Updated `directives/research.md` - Updated directive with manual review step

## Complete Workflow

### Step 1: Generate Research
```bash
python execution/research_topic.py "The rise and fall of Blackberry" 4 "blackberry_test"
```

**Output**:
- Research saved to: `projects/blackberry_test/research/research_20260120_214340.json`
- Status: `review_status: "pending"`

### Step 2: Review Research
```bash
python execution/review_research.py projects/blackberry_test/research/research_20260120_214340.json
```

**Options**:
1. ✅ **Approve** → Continue to script generation
2. ✏️  **Edit** → Manually edit JSON file, then review again
3. 🔄 **Regenerate** → Request new research generation
4. ❌ **Reject** → Stop workflow

### Step 3: Update Research (if edited)
```bash
# Option A: Edit JSON file directly, then:
python execution/review_research.py projects/blackberry_test/research/research_20260120_214340.json

# Option B: Review file will be created for editing
# Edit: projects/blackberry_test/research/research_20260120_214340_review.json
```

### Step 4: Approve Research
After review and approval, the research status changes to `review_status: "approved"` and is ready for script generation.

## Research File Structure

```json
{
  "project_name": "blackberry_test",
  "topic": "The rise and fall of Blackberry",
  "generated_at": "2024-01-20T21:43:40",
  "status": "generated",
  "review_status": "pending",
  "facts": [
    "**BlackBerry pioneered mobile email with early devices...",
    "**At its peak around 2010, BlackBerry held over 40-50%...",
    "**The 2007 iPhone launch disrupted BlackBerry's dominance...",
    "**By 2016, BlackBerry exited hardware, pivoting to cybersecurity...**"
  ],
  "sources": [],
  "raw_response": "**BlackBerry rose to dominance in the smartphone market...",
  "error": null
}
```

**After Review**:
```json
{
  ...
  "status": "approved",
  "review_status": "approved",
  "approved_at": "2024-01-20T21:45:00"
}
```

## Project Folder Organization

Each project now has organized subfolders by step:

```
projects/
└── {project_name}/
    ├── research/               # Research step
    │   ├── research_{timestamp}.json
    │   └── research_{timestamp}_review.json (if edited)
    └── script/                 # Script step (if generated)
        └── script_{timestamp}.json
```

**Benefits**:
- ✅ Organized by workflow step
- ✅ Easy to find specific outputs
- ✅ Clear project structure
- ✅ Easy to track progress

## Integration with Script Generation

After research is approved, you can use it for script generation:

```bash
# Research approved, now generate script
python execution/generate_script.py projects/blackberry_test/research/research_20260120_214340.json "The rise and fall of Blackberry" "History & Biographies" true "blackberry_test"
```

The script generator will automatically:
- ✅ Load the approved research
- ✅ Extract facts and sources
- ✅ Generate script based on research
- ✅ Save script to `projects/{project_name}/script/` (following same pattern)

## Benefits

1. **Organization**: Research organized by project and step
2. **Review Process**: Built-in quality gate before script generation
3. **Flexibility**: Edit and update research easily
4. **Traceability**: Full history of research generation and reviews
5. **Workflow Integration**: Seamlessly integrates with script generation step

## Test Results

**Status**: ✅ **Working**

**Test Command**:
```bash
python execution/research_topic.py "The rise and fall of Blackberry" 4 "blackberry_test"
```

**Result**:
- ✅ Research saved to: `projects/blackberry_test/research/research_20260120_214340.json`
- ✅ Found 4 facts about the topic
- ✅ Project folder structure created correctly
- ✅ Ready for review

## Next Steps

After research is approved:
- ✅ Proceed to script generation (Phase 3)
- ✅ Research data will be loaded automatically
- ✅ Script will reference approved research

See `RESEARCH_REVIEW_WORKFLOW.md` for detailed documentation.
