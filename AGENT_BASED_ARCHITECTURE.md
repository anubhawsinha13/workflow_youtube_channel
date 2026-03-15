# Agent-Based Architecture - Replacing n8n with Intelligent Agents

## Overview

This document proposes replacing n8n workflow orchestration with an intelligent agent-based system using **LangGraph** and **LangChain**. This approach provides better decision-making, state management, and native Python integration while maintaining all automation capabilities.

## Why Replace n8n with Agents?

### Advantages of Agent-Based Approach

1. **Intelligent Decision-Making**
   - Agents can make contextual decisions based on content quality
   - Automatic retry with improved prompts based on failure analysis
   - Dynamic workflow adaptation based on intermediate results

2. **Better State Management**
   - LangGraph provides built-in state persistence
   - Easier to resume failed workflows
   - Better debugging with full state history

3. **Native Python Integration**
   - No Docker overhead (optional)
   - Easier to test and debug
   - Better IDE support
   - Version control friendly

4. **Advanced Capabilities**
   - Parallel agent execution for independent tasks
   - Self-correcting workflows
   - Quality-based routing
   - Learning from past workflows

5. **Simplified Deployment**
   - Single Python application
   - Easy to deploy to cloud (AWS Lambda, Google Cloud Run, etc.)
   - Better scaling options
   - No separate orchestration service

### Comparison

| Feature | n8n | Agent-Based System |
|---------|-----|-------------------|
| Setup Complexity | Medium (Docker required) | Low (Python only) |
| Decision Making | Rule-based | Intelligent, context-aware |
| State Management | Basic | Advanced with persistence |
| Error Recovery | Manual retry configuration | Automatic with learning |
| Testing | Requires n8n UI | Standard Python testing |
| Debugging | n8n logs | Python debugger support |
| Parallel Execution | Limited | Native support |
| Version Control | JSON workflow files | Python code (better diff) |
| Deployment | Docker container | Any Python runtime |

## Architecture Overview

### Agent Roles

1. **Research Agent** - Gathers information using Perplexity
2. **Script Writer Agent** - Creates engaging scripts from research
3. **Quality Control Agent** - Fact-checks and validates content
4. **Review Coordinator Agent** - Manages human-in-the-loop reviews
5. **Compliance Agent** - Ensures YouTube policy compliance
6. **Voiceover Agent** - Generates audio using ElevenLabs
7. **Visual Agent** - Creates images using DALL-E
8. **Video Assembly Agent** - Combines assets using Creatomate
9. **Publishing Agent** - Uploads to YouTube

### Workflow Orchestration

The system uses **LangGraph** to orchestrate agents with:
- State machine for workflow progression
- Conditional routing based on quality scores
- Automatic retry mechanisms
- Human-in-the-loop integration
- Error recovery and fallback strategies

## Implementation Stack

### Core Libraries

```python
# requirements.txt additions
langchain>=0.1.0
langgraph>=0.0.40
langchain-openai>=0.0.5
langchain-community>=0.0.20
pydantic>=2.0.0  # For state management
```

### Framework Choice: LangGraph

**LangGraph** is recommended because:
- Built on LangChain (compatible with existing tools)
- Excellent state management
- Visual workflow representation
- Built-in persistence
- Human-in-the-loop support
- Active development and community

**Alternative Options:**
- **CrewAI**: Role-based agents (simpler, less flexible)
- **AutoGen**: Microsoft's multi-agent framework (more complex)
- **Custom LangChain**: More control, more implementation work

## Agent System Architecture

```python
# Simplified architecture diagram

┌─────────────────────────────────────────────────────────┐
│                  Workflow Orchestrator                   │
│                  (LangGraph State Machine)               │
└─────────────────────────────────────────────────────────┘
                         │
         ┌───────────────┼───────────────┐
         │               │               │
    ┌────▼────┐    ┌────▼────┐    ┌────▼────┐
    │ Research│    │  Script │    │ Quality │
    │  Agent  │───▶│  Agent  │───▶│ Control │
    └─────────┘    └─────────┘    │  Agent  │
                                  └────┬────┘
                                       │
                            ┌──────────┴──────────┐
                            │                     │
                      ┌─────▼─────┐        ┌─────▼─────┐
                      │  Review   │        │Compliance │
                      │Coordinator│        │  Agent    │
                      └─────┬─────┘        └─────┬─────┘
                            │                     │
                            └──────────┬──────────┘
                                       │
                    ┌──────────────────┼──────────────────┐
                    │                  │                  │
            ┌───────▼──────┐   ┌──────▼──────┐   ┌──────▼──────┐
            │  Voiceover   │   │   Visual    │   │   Video     │
            │    Agent     │   │   Agent     │   │  Assembly   │
            └───────┬──────┘   └──────┬──────┘   │   Agent     │
                    │                  │          └──────┬──────┘
                    └──────────────────┼──────────────────┘
                                       │
                                  ┌────▼────┐
                                  │Publishing│
                                  │  Agent   │
                                  └─────────┘
```

## State Management

### Workflow State Structure

```python
from typing import TypedDict, List, Optional
from datetime import datetime

class VideoGenerationState(TypedDict):
    # Input
    topic: str
    niche: str
    video_title: Optional[str]
    
    # Research Phase
    research_data: Optional[dict]
    facts: Optional[List[str]]
    sources: Optional[List[str]]
    
    # Script Phase
    script: Optional[dict]
    script_quality_score: Optional[float]
    
    # Quality Control
    fact_check_report: Optional[dict]
    fact_check_passed: Optional[bool]
    requires_human_review: bool
    human_approval_status: Optional[str]  # "pending", "approved", "rejected"
    review_comments: Optional[str]
    
    # Compliance
    compliance_report: Optional[dict]
    compliance_passed: Optional[bool]
    
    # Assets
    voiceover_files: List[str]
    image_files: List[str]
    video_file: Optional[str]
    
    # Publishing
    youtube_video_id: Optional[str]
    youtube_url: Optional[str]
    
    # Metadata
    workflow_status: str  # "research", "scripting", "review", etc.
    errors: List[str]
    retry_count: int
    created_at: datetime
    updated_at: datetime
```

## Implementation Steps

### Phase 1: Core Agent Framework

1. **Install Dependencies**
   ```bash
   pip install langchain langgraph langchain-openai langchain-community pydantic
   ```

2. **Create Base Agent Class**
   - Define common agent interface
   - Implement error handling
   - Add retry logic

3. **Implement Research Agent**
   - Perplexity API integration
   - Fact extraction
   - Citation management

4. **Implement Script Writer Agent**
   - OpenAI GPT-4 integration
   - Structured output parsing
   - Visual prompt generation

### Phase 2: Quality Control Agents

1. **Fact-Check Agent**
   - Compare script claims vs research
   - Generate accuracy scores
   - Identify discrepancies

2. **Review Coordinator Agent**
   - Human-in-the-loop integration
   - Email/Slack notifications
   - Approval tracking

3. **Compliance Agent**
   - YouTube policy checking
   - Fair Use analysis
   - AI disclosure verification

### Phase 3: Content Generation Agents

1. **Voiceover Agent**
   - ElevenLabs integration
   - Audio file management
   - Quality validation

2. **Visual Agent**
   - DALL-E integration
   - Image optimization
   - Asset storage

3. **Video Assembly Agent**
   - Creatomate integration
   - Payload construction
   - Render monitoring

### Phase 4: Publishing Agent

1. **YouTube Publishing Agent**
   - OAuth 2.0 authentication
   - Metadata generation
   - Upload management
   - Status tracking

### Phase 5: LangGraph Orchestration

1. **Define State Machine**
   - Create LangGraph workflow
   - Define state transitions
   - Add conditional routing

2. **Implement Human-in-the-Loop**
   - Review checkpoint nodes
   - Webhook endpoints
   - Approval handling

3. **Add Error Handling**
   - Retry mechanisms
   - Fallback strategies
   - Error recovery

## Example Implementation

### Basic Agent Structure

```python
from langchain.agents import AgentExecutor
from langchain_openai import ChatOpenAI
from langchain.tools import Tool
from typing import Dict, Any

class ResearchAgent:
    def __init__(self, perplexity_api_key: str):
        self.perplexity_client = Perplexity(api_key=perplexity_api_key)
    
    def research_topic(self, topic: str) -> Dict[str, Any]:
        """Research topic and extract facts"""
        response = self.perplexity_client.chat.completions.create(
            model="sonar-medium-online",
            messages=[
                {"role": "system", "content": "You are a world-class researcher..."},
                {"role": "user", "content": f"Provide key facts about: {topic}"}
            ]
        )
        
        return {
            "facts": self._extract_facts(response),
            "sources": self._extract_sources(response),
            "raw_response": response.choices[0].message.content
        }
```

### LangGraph Workflow Example

```python
from langgraph.graph import StateGraph, END
from langgraph.checkpoint import MemorySaver

def create_workflow():
    workflow = StateGraph(VideoGenerationState)
    
    # Add nodes
    workflow.add_node("research", research_node)
    workflow.add_node("script", script_node)
    workflow.add_node("fact_check", fact_check_node)
    workflow.add_node("human_review", human_review_node)
    workflow.add_node("compliance", compliance_node)
    workflow.add_node("voiceover", voiceover_node)
    workflow.add_node("visual", visual_node)
    workflow.add_node("assemble", assemble_node)
    workflow.add_node("publish", publish_node)
    
    # Define edges
    workflow.set_entry_point("research")
    workflow.add_edge("research", "script")
    workflow.add_conditional_edges(
        "script",
        should_fact_check,
        {
            "fact_check": "fact_check",
            "skip": "compliance"
        }
    )
    workflow.add_conditional_edges(
        "fact_check",
        route_after_fact_check,
        {
            "human_review": "human_review",
            "approved": "compliance",
            "retry": "script"
        }
    )
    # ... more edges
    
    # Add persistence
    memory = MemorySaver()
    app = workflow.compile(checkpointer=memory)
    
    return app
```

## Human-in-the-Loop Integration

### Webhook-Based Review System

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class ReviewRequest(BaseModel):
    video_id: str
    script: dict
    fact_check_report: dict
    action: str  # "approve", "reject", "request_changes"

@app.post("/review/{video_id}")
async def submit_review(video_id: str, request: ReviewRequest):
    # Update state with review decision
    # Resume workflow
    pass

@app.get("/review/{video_id}")
async def get_review_status(video_id: str):
    # Return current review status
    pass
```

## Scheduling & Automation

### Option 1: Python Scheduler (APScheduler)

```python
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()
scheduler.add_job(
    run_workflow,
    'cron',
    day_of_week='mon-fri',
    hour=9,
    minute=0
)
scheduler.start()
```

### Option 2: Cloud Functions (Recommended)

- **AWS Lambda** with EventBridge
- **Google Cloud Functions** with Cloud Scheduler
- **Azure Functions** with Timer Trigger

### Option 3: Kubernetes CronJob

```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: video-generation
spec:
  schedule: "0 9 * * 1-5"  # Daily at 9 AM
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: workflow-runner
            image: youtube-automation:latest
          restartPolicy: OnFailure
```

## Migration Path from n8n

### Step 1: Parallel Implementation
- Keep n8n running
- Build agent system alongside
- Test with same inputs

### Step 2: Gradual Migration
- Migrate one workflow phase at a time
- Compare outputs
- Validate quality

### Step 3: Full Cutover
- Switch to agent system
- Monitor for issues
- Keep n8n as backup

## Monitoring & Observability

### Logging

```python
import logging
from langgraph.checkpoint import MemorySaver

# Structured logging
logger = logging.getLogger("video_workflow")
logger.info("Research completed", extra={
    "topic": state["topic"],
    "facts_count": len(state["facts"]),
    "duration": elapsed_time
})
```

### Metrics

- Workflow completion rate
- Average execution time
- Error rates by agent
- Quality scores
- Human review rates

### Dashboards

- Use **LangSmith** (LangChain's observability platform)
- Or integrate with Prometheus + Grafana
- Custom Python dashboard with Flask/Streamlit

## Benefits Summary

1. ✅ **No Docker overhead** - Pure Python
2. ✅ **Intelligent decisions** - Context-aware routing
3. ✅ **Better testing** - Standard Python test frameworks
4. ✅ **Easier debugging** - Python debugger support
5. ✅ **Version control** - Git-friendly Python code
6. ✅ **Scalability** - Deploy anywhere Python runs
7. ✅ **State persistence** - Resume failed workflows
8. ✅ **Advanced features** - Learning, adaptation, optimization

## Next Steps

1. Review this architecture document
2. Update `plan.md` with agent-based approach
3. Update `optimized_workflow.md` with implementation details
4. Update `CHECKLIST.md` to reflect agent setup
5. Begin implementation with Phase 1 (Core Agents)