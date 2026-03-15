# Fact-Check Directive

## Goal
Verify script claims against research data and generate accuracy report.

## Inputs
- `script` (dict): Generated script from script_generation directive
- `research_data` (dict): Original research data

## Execution
Run `execution/fact_check_script.py` with script and research data.

## Outputs
- `fact_check_report` (dict):
  - `accuracy_score` (float): Overall accuracy (0-100)
  - `verified_claims` (list): Claims that match research
  - `discrepancies` (list): Claims that don't match research
  - `missing_citations` (list): Claims without research backing
  - `recommendation` (str): "approve", "review", or "reject"

## Quality Thresholds
- `accuracy_score >= 80`: Auto-approve, continue to compliance
- `accuracy_score 60-79`: Route to human review
- `accuracy_score < 60`: Reject, retry script generation

## Tools
- OpenAI API for comparison logic
- Model: `gpt-4o-mini` (cost-efficient for fact-checking)

## Edge Cases
- Empty research data: Flag all claims as unverified
- Ambiguous claims: Request clarification in report
- Contradictory research: Flag for human review
- New claims not in research: Check if acceptable or needs more research

## Error Handling
- If fact-check fails: Default to "review" recommendation
- Log all discrepancies for learning
- Don't block workflow on fact-check errors

## Notes
- Fact-check is critical for channel credibility
- False claims can lead to demonetization
- Balance accuracy with creative storytelling
- Update script based on fact-check findings
