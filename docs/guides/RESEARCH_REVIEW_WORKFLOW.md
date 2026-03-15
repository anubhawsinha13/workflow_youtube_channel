# Research Review Workflow - Complete ✅

## Summary

Added manual review step for research output with project folder organization.

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
projects/blackberry_history/
└── research/
    └── research_20260120_211500.json
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
python execution/research_topic.py "The rise and fall of Blackberry" 4 "blackberry_history"
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
python execution/research_topic.py "The rise and fall of Blackberry" 4 "blackberry_history"
```

**Output**:
- Research saved to: `projects/blackberry_history/research/research_20260120_211500.json`
- Status: `review_status: "pending"`

### Step 2: Review Research
```bash
python execution/review_research.py projects/blackberry_history/research/research_20260120_211500.json
```

**Options**:
1. ✅ **Approve** → Continue to script generation
2. ✏️  **Edit** → Manually edit JSON file, then review again
3. 🔄 **Regenerate** → Request new research generation
4. ❌ **Reject** → Stop workflow

### Step 3: Update Research (if edited)
```bash
# Option A: Edit JSON file directly, then:
python execution/review_research.py projects/blackberry_history/research/research_20260120_211500.json

# Option B: Review file will be created for editing
# Edit: projects/blackberry_history/research/research_20260120_211500_review.json
```

### Step 4: Approve Research
After review and approval, the research status changes to `review_status: "approved"` and is ready for script generation.

## Research File Structure

```json
{
  "project_name": "blackberry_history",
  "topic": "The rise and fall of Blackberry",
  "generated_at": "2024-01-20T21:15:00",
  "status": "generated",
  "review_status": "pending",
  "facts": [
    "Peak Market Dominance: At its height, BlackBerry controlled nearly 50% of the U.S. smartphone market...",
    "Original Innovation and Market Position: BlackBerry was founded in 1984 as Research in Motion...",
    "..."
  ],
  "sources": [],
  "raw_response": "Here are four key, distinct facts about the rise and fall of BlackBerry:...",
  "error": null
}
```

**After Review**:
```json
{
  ...
  "status": "approved",
  "review_status": "approved",
  "approved_at": "2024-01-20T21:20:30"
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
python execution/generate_script.py projects/blackberry_history/research/research_20260120_211500.json "The rise and fall of Blackberry" "History & Biographies" true "blackberry_history"
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

## Next Steps

After research is approved:
- ✅ Proceed to script generation
- ✅ Research data will be loaded automatically
- ✅ Script will reference approved research

## Notes

1. **Project Name**: Auto-created from topic if not provided
2. **Timestamp**: Used for versioning (multiple research runs possible)
3. **Review Status**: Tracks approval workflow
4. **Error Handling**: Failed research not saved to project folder
5. **Source Extraction**: Can be improved to capture more URLs from citations

## Usage Examples

### Basic Research
```bash
python execution/research_topic.py "Topic name" 4
```

### Research with Project Name
```bash
python execution/research_topic.py "Topic name" 4 "project_name"
```

### Review Research
```bash
python execution/review_research.py projects/project_name/research/research_20260120_123456.json
```

### Complete Workflow
```bash
# 1. Research
python execution/research_topic.py "The rise and fall of Blackberry" 4 "blackberry_history"

# 2. Review
python execution/review_research.py projects/blackberry_history/research/research_*.json

# 3. Generate Script (after approval)
python execution/generate_script.py projects/blackberry_history/research/research_*.json "The rise and fall of Blackberry" "History & Biographies" true "blackberry_history"

# 4. Review Script
python execution/review_script.py projects/blackberry_history/script/script_*.json
```

See `directives/research.md` for detailed documentation.
