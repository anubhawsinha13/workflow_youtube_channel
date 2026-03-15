# Manual Review Workflow - Phase 3

This guide explains the manual review process for generated scripts.

## Overview

After script generation, scripts are automatically saved to a project folder structure. You can then review, edit, and approve scripts before proceeding to the next phase.

## Project Folder Structure

Scripts are organized by project/use case in the `projects/` directory:

```
projects/
└── {project_name}/              # Auto-created from topic
    ├── script_{timestamp}.json  # Generated script
    ├── script_{timestamp}_review.json  # Review checkpoint
    ├── script_{timestamp}_backup_{timestamp}.json  # Auto-backup on update
    └── research_data.json       # (Optional) Research data
```

**Project Name**: Automatically generated from topic (e.g., "The rise and fall of Blackberry" → `blackberry`)

## Workflow Steps

### Step 1: Generate Script

```bash
python execution/generate_script.py .tmp/test_research.json "The rise and fall of Blackberry" "History & Biographies" true "blackberry_history"
```

**Output**: Script saved to `projects/blackberry_history/script_20240120_143022.json`

### Step 2: Review Script

```bash
python execution/review_script.py projects/blackberry_history/script_20240120_143022.json
```

**Review Options**:
1. **✅ Approve** - Continue to next phase (fact-check/compliance)
2. **✏️ Edit** - Manually edit the script JSON file
3. **🔄 Regenerate** - Request new script generation
4. **❌ Reject** - Stop workflow

### Step 3: Update Script (if needed)

**Option A: Edit JSON file directly**
1. Open the script JSON file in your editor
2. Make changes to title, description, tags, scenes, etc.
3. Save the file
4. Run review script again to approve

**Option B: Use update script**
```bash
python execution/update_script.py projects/blackberry_history/script_20240120_143022.json
```

This will:
- Show current script contents
- Allow you to edit the JSON file manually
- Create a backup before updating
- Reload and verify changes

### Step 4: Approve Script

After reviewing/editing, approve the script:

```bash
python execution/update_script.py projects/blackberry_history/script_20240120_143022.json --approve
```

Or use the review script and choose option 1 (Approve).

## Script File Structure

```json
{
  "project_name": "blackberry_history",
  "topic": "The rise and fall of Blackberry",
  "generated_at": "2024-01-20T14:30:22",
  "status": "generated",
  "review_status": "pending",
  "success": true,
  "script": {
    "scenes": [...],
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
  "approved_at": "2024-01-20T14:35:10",
  "updated_at": "2024-01-20T14:33:45"  // If edited
}
```

## Editing Scripts

### Common Edits

1. **Change Title**:
   ```json
   "title": "Your New Title Here"
   ```

2. **Update Description**:
   ```json
   "description": "Your updated description..."
   ```

3. **Modify Scene Text**:
   ```json
   "scenes": [
     {
       "scene_number": 1,
       "text": "Your edited text here",
       "visual_prompt": "...",
       "duration_estimate": 20
     }
   ]
   ```

4. **Update Visual Prompts**:
   ```json
   "visual_prompt": "Your updated DALL-E prompt here"
   ```

5. **Change Tags**:
   ```json
   "tags": ["tag1", "tag2", "tag3"]
   ```

## Best Practices

1. **Always Review**: Don't skip the review step - quality matters
2. **Create Backups**: Updates automatically create backups
3. **Version Control**: Consider committing approved scripts to git
4. **Project Organization**: Use descriptive project names
5. **Track Changes**: Check timestamps to see when scripts were updated

## Integration with Workflow

After approval, the script is ready for:
- ✅ Fact-checking
- ✅ Compliance checking
- ✅ Voiceover generation
- ✅ Visual generation
- ✅ Video assembly

## Troubleshooting

### Script file not found
- Check project folder exists
- Verify script file path is correct
- Use full path if needed

### Changes not saved
- Ensure file is saved before approving
- Check file permissions
- Verify JSON syntax is valid

### Backup files
- Backups are created automatically on update
- Format: `script_{timestamp}_backup_{backup_timestamp}.json`
- Can restore from backup if needed

## Example Workflow

```bash
# 1. Generate script
python execution/generate_script.py research.json "Blackberry" "History" true "blackberry"

# Output: ✅ Script saved to project folder: projects/blackberry/script_20240120_143022.json

# 2. Review script
python execution/review_script.py projects/blackberry/script_20240120_143022.json

# Choose option 2 (Edit)
# Edit the JSON file manually
# Save changes

# 3. Update and approve
python execution/update_script.py projects/blackberry/script_20240120_143022.json
python execution/update_script.py projects/blackberry/script_20240120_143022.json --approve

# ✅ Script approved and ready for next phase
```
