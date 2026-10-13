# Research Directive

## Goal
Gather verified facts and information about a video topic using Perplexity API.

## Inputs
- `topic` (str): The topic to research (e.g., "The rise and fall of Blackberry")
- `num_facts` (int, optional): Number of key facts to extract (default: 4)

## Execution
1. **Research**: Run `python scripts/research_brief.py "<topic>"`. This calls the shared `aegis-research` package with the `youtube` profile and writes `projects/{project_name}/research/research_{timestamp}.json`. `execution/research_topic.py` uses the same package when it is installed.
2. **Manual Review**: Review the research output (script saved to `projects/{project_name}/research/research_{timestamp}.json`)
3. **Review Step**: Run `execution/review_research.py` to approve, edit, or regenerate
4. **Update After Review**: Edit the research JSON file directly, then review again

## Outputs
- `facts` (list): List of extracted facts with citations
- `sources` (list): List of source URLs
- `raw_response` (str): Full research response from Perplexity
- `research_file` (str): Path to saved research file in project folder
- `review_status` (str): Status of review (pending, approved, rejected, edited)

## Manual Review Workflow
1. **Research Generation**: Research is automatically saved to project folder
2. **Review**: Run `python execution/review_research.py projects/{project_name}/research/research_{timestamp}.json`
3. **Review Options**:
   - **Approve**: Continue to script generation
   - **Edit**: Modify research manually (edit JSON file directly)
   - **Regenerate**: Request new research with same inputs
   - **Reject**: Stop workflow
4. **Update After Review**:
   - Edit the research JSON file directly
   - Run review script again to approve updated version
   - Research file path: `projects/{project_name}/research/research_{timestamp}.json`

## Project Folder Structure
```
projects/
└── {project_name}/           # Auto-created from topic
    └── research/             # Research step folder
        ├── research_{timestamp}.json       # Generated research
        └── research_{timestamp}_review.json  # Review checkpoint
```

## Tools
- Perplexity API (`perplexityai` package)
- Model: `sonar` (default Perplexity model)

## Edge Cases
- API rate limits: Implement retry with exponential backoff
- No results: Return empty facts list with error message
- Network timeout: Retry up to 3 times with increasing delays
- Invalid topic: Validate topic format before API call

## Error Handling
- Log all API errors with context
- Return structured error response: `{"error": "message", "facts": [], "sources": []}`
- Don't fail workflow on research errors, allow fact-check to catch issues

## Notes
- Research is foundation for script - quality here affects everything downstream
- Always request citations from Perplexity
- Prefer recent sources when available
- Verify facts are distinct and non-overlapping
