# Script Generation Directive

## Goal
Transform research facts into an engaging YouTube script with visual prompts.

## Inputs
- `research_data` (dict): Output from research directive
- `topic` (str): Original video topic
- `niche` (str, optional): Content niche (default: "History & Biographies")
- `target_length` (int, optional): Target word count (default: 1500)

## Execution
1. **Generate Script**: Run `execution/generate_script.py` with research data and topic.
2. **Manual Review**: Script is saved to `projects/{project_name}/script_{timestamp}.json`
3. **Review Step**: Run `execution/review_script.py` to review and optionally update the script.
4. **Update Script**: Edit the script file directly or use review interface, then approve.

## Outputs
- `script_file` (str): Path to saved script file in project folder
  - Location: `projects/{project_name}/script_{timestamp}.json`
- `script` (dict): Structured script with scenes
  - `scenes` (list): List of scene objects
    - `scene_number` (int): Scene sequence
    - `dialogue` (str): Voiceover/subtitle text (for ElevenLabs)
    - `visual_description` (str): Image/video generation prompt (for DALL-E/Gemini)
    - `duration_estimate` (int): Estimated seconds
  - `title` (str): Video title
  - `description` (str): Video description
  - `tags` (list): YouTube tags
- `review_status` (str): "pending", "approved", "edited", or "rejected"

## Tools
- **OpenAI API** (`openai` package)
  - Model: `gpt-4o` for script, `gpt-4o-mini` for metadata (cost optimization)
- **Google Gemini API** (`google-generativeai` package) - Alternative option
  - Model: `gemini-1.5-pro` for script generation (latest and most capable)
  - Often faster and more cost-effective than OpenAI
  - Supports native JSON output mode

## Edge Cases
- JSON parsing errors: Retry with stricter JSON format request
- Script too short/long: Adjust prompt with length constraints
- No visual descriptions: Ensure every scene has visual_description field
- No dialogue: Ensure every scene has dialogue field
- Invalid niche: Use default niche if provided niche not recognized

## Quality Requirements
- Script must have hook in first 10 seconds
- Each scene should be 15-30 seconds
- Visual prompts must be descriptive and specific
- Script should follow niche style guidelines

## Error Handling
- Parse JSON with fallback if response format is wrong
- Log script generation errors
- Return partial script if generation partially fails
- Retry up to 2 times on API errors

## Manual Review Workflow
1. **Script Generation**: Script is automatically saved to project folder
2. **Review**: Run `python execution/review_script.py projects/{project_name}/script_{timestamp}.json`
3. **Review Options**:
   - **Approve**: Continue to next phase (fact-check/compliance)
   - **Edit**: Modify script manually (edit JSON file directly)
   - **Regenerate**: Request new script generation with same inputs
   - **Reject**: Stop workflow
4. **Update After Review**:
   - Edit the script JSON file directly
   - Run review script again to approve updated version
   - Script file path: `projects/{project_name}/script_{timestamp}.json`

## Project Folder Structure
```
projects/
└── {project_name}/           # Auto-created from topic
    ├── script_{timestamp}.json       # Generated script
    ├── script_{timestamp}_review.json  # Review checkpoint
    ├── research_data.json    # (Optional) Research data
    └── final_script.json     # (After approval)
```

## Notes
- Script quality directly impacts video engagement
- Visual prompts are critical for image generation
- Ensure script flows naturally between scenes
- Add [VISUAL CUE: description] markers for clarity
- Always review before proceeding to voiceover generation
- Project folders organize scripts by topic/use case