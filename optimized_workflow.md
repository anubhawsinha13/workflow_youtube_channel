# Optimized YouTube Automation Workflow - Step-by-Step Guide

## Overview
This document provides an optimized, step-by-step workflow for building an automated YouTube video generation pipeline using Python, LangGraph (agent-based orchestration), and various AI APIs.

---

## Phase 1: Prerequisites & Environment Setup

### 1.1 Software Installation Checklist
- [ ] **Git** - Verify installation: `git --version`
- [ ] **Docker Desktop** - Install and verify: `docker --version`
- [ ] **Python 3.8+** - Verify installation: `python3 --version`
- [ ] **IDE** - VS Code, PyCharm, or preferred IDE installed

### 1.2 API Account Setup Checklist
- [ ] **OpenAI Account**
  - [ ] Create account at https://platform.openai.com
  - [ ] Generate API key from API Keys section
  - [ ] Set billing limits (recommended: $50-100/month initially)
  - [ ] Test API key with a simple curl request
  
- [ ] **Perplexity Account**
  - [ ] Sign up at https://www.perplexity.ai
  - [ ] Navigate to API section
  - [ ] Generate API key
  - [ ] Note: Free tier has rate limits
  
- [ ] **ElevenLabs Account**
  - [ ] Sign up at https://elevenlabs.io
  - [ ] Go to Profile Settings → API Keys
  - [ ] Generate API key
  - [ ] Test voice cloning (optional but recommended)
  
- [ ] **Creatomate Account**
  - [ ] Sign up at https://creatomate.com
  - [ ] Create a new project
  - [ ] Create or select a video template
  - [ ] Get Template ID from template settings
  - [ ] Document dynamic element names (e.g., "Text-1", "Image-1", "Voiceover-1")
  - [ ] Get API key from Project Settings
  
- [ ] **YouTube Data API v3**
  - [ ] Go to Google Cloud Console: https://console.cloud.google.com
  - [ ] Create a new project or select existing project
  - [ ] Enable YouTube Data API v3
  - [ ] Create OAuth 2.0 credentials (Desktop application)
  - [ ] Download credentials JSON file
  - [ ] Set up OAuth consent screen
  - [ ] Note: You'll need to authenticate once to get refresh token
  - [ ] Store credentials securely (add to .env or secure storage)

### 1.3 Project Structure Setup
- [ ] Create project directory: `mkdir youtube_automation && cd youtube_automation`
- [ ] Initialize Git repository: `git init`
- [ ] Create `.gitignore` file with:
  ```
  venv/
  .env
  __pycache__/
  *.pyc
  .DS_Store
  *.log
  ```
- [ ] Create Python virtual environment: `python3 -m venv venv`
- [ ] Activate virtual environment:
  - Mac/Linux: `source venv/bin/activate`
  - Windows: `.\venv\Scripts\activate`

### 1.4 Dependencies Installation
- [ ] Create `requirements.txt` with:
  ```
  requests>=2.31.0
  openai>=1.0.0
  perplexityai>=0.1.0
  elevenlabs>=0.2.0
  python-dotenv>=1.0.0
  google-auth>=2.23.0
  google-auth-oauthlib>=1.1.0
  google-auth-httplib2>=0.1.1
  google-api-python-client>=2.100.0
  langchain>=0.1.0
  langgraph>=0.0.40
  langchain-openai>=0.0.5
  langchain-community>=0.0.20
  pydantic>=2.0.0
  fastapi>=0.100.0  # For webhook endpoints (optional)
  uvicorn>=0.23.0   # For FastAPI server (optional)
  apscheduler>=3.10.0  # For scheduling (optional)
  ```
- [ ] Install dependencies: `pip install -r requirements.txt`
- [ ] Verify installations: `pip list`

### 1.5 Environment Configuration
- [ ] Create `.env` file in project root:
  ```env
  OPENAI_API_KEY=your_openai_key_here
  PERPLEXITY_API_KEY=your_perplexity_key_here
  ELEVENLABS_API_KEY=your_elevenlabs_key_here
  CREATOMATE_API_KEY=your_creatomate_key_here
  CREATOMATE_TEMPLATE_ID=your_template_id_here
  YOUTUBE_CLIENT_SECRETS_FILE=path/to/client_secrets.json
  YOUTUBE_CREDENTIALS_FILE=path/to/youtube_credentials.json
  ```
- [ ] Verify `.env` is in `.gitignore`
- [ ] Create `.env.example` template (without actual keys) for documentation
- [ ] Store YouTube OAuth credentials JSON file securely (not in Git)

---

## Phase 2: Core Python Script Development

### 2.1 Project Structure
- [ ] Create directory structure:
  ```
  youtube_automation/
  ├── src/
  │   ├── __init__.py
  │   ├── research.py
  │   ├── scriptwriter.py
  │   ├── fact_checker.py
  │   ├── review_gateway.py
  │   ├── compliance_checker.py
  │   ├── voiceover.py
  │   ├── video_generator.py
  │   ├── youtube_uploader.py
  │   ├── storage_manager.py
  │   ├── cost_tracker.py
  │   ├── style_optimizer.py
  │   ├── asset_manager.py
  │   ├── version_tracker.py
  │   ├── thumbnail_generator.py
  │   ├── performance_learner.py
  │   └── utils.py
  ├── tests/
  │   └── test_basic.py
  ├── config/
  │   └── config.py
  ├── credentials/
  │   ├── client_secrets.json
  │   └── youtube_credentials.json
  ├── .env
  ├── .env.example
  ├── .gitignore
  ├── requirements.txt
  ├── README.md
  └── generate_video.py
  ```

### 2.2 Configuration Module
- [ ] Create `config/config.py`:
  - [ ] Load environment variables
  - [ ] Validate all required keys are present
  - [ ] Create configuration class/constants
  - [ ] Add error handling for missing keys

### 2.3 Research Module (Perplexity)
- [ ] Create `src/research.py`:
  - [ ] Implement `research_topic(topic: str) -> dict` function
  - [ ] Add error handling for API failures
  - [ ] Add retry logic with exponential backoff
  - [ ] Parse and structure research results
  - [ ] **Cost Optimization**: Use GPT-4o-mini for research parsing (80% cost reduction)
  - [ ] Add logging for debugging
  - [ ] Return structured data: `{"facts": [...], "sources": [...]}`
  - [ ] Track cost per research operation

### 2.4 Script Writing Module (OpenAI)
- [ ] Create `src/scriptwriter.py`:
  - [ ] Implement `generate_script(research_data: dict) -> dict` function
  - [ ] **Cost Optimization**: Use GPT-4o-mini for initial research parsing
  - [ ] **Cost Optimization**: Use GPT-4o only for final script polish
  - [ ] Create prompt template for script generation
  - [ ] Ensure JSON output format
  - [ ] Parse JSON response with error handling
  - [ ] Validate script structure (scenes, text, visual prompts)
  - [ ] Return structured script: `{"scenes": [{"text": "...", "visual_prompt": "..."}]}`
  - [ ] Track cost per operation (mini vs full model)

### 2.5 Voiceover Module (ElevenLabs)
- [ ] Create `src/voiceover.py`:
  - [ ] Implement `generate_voiceover(script: dict, voice_id: str) -> list` function
  - [ ] **Idempotency**: Check if voiceover with same script hash exists before generating
  - [ ] **Cost Optimization**: Use ElevenLabs "Turbo" models for narration-heavy videos
  - [ ] Add configuration option to switch between standard and turbo models
  - [ ] Add text chunking for long scripts
  - [ ] Generate audio for each scene
  - [ ] Save audio files locally with TTL metadata
  - [ ] Return list of audio file paths
  - [ ] Add error handling for API failures
  - [ ] Track cost per operation (standard vs turbo)
  - [ ] **Version Tracking**: Store voice model version and settings used

### 2.6 Video Generation Module (Creatomate)
- [ ] Create `src/video_generator.py`:
  - [ ] Implement `generate_video(script: dict, audio_files: list) -> dict` function
  - [ ] Map script scenes to Creatomate template elements
  - [ ] Build Creatomate API payload
  - [ ] Handle render status polling
  - [ ] Download final video when ready
  - [ ] Return video metadata and file path

### 2.7 YouTube Upload Module
- [ ] Create `src/youtube_uploader.py`:
  - [ ] Implement OAuth 2.0 authentication flow
  - [ ] Implement `upload_video(video_path: str, metadata: dict) -> dict` function
  - [ ] **Cost Optimization**: Use GPT-4o-mini for metadata generation (title, description, tags, thumbnail)
  - [ ] Handle video upload with resumable upload for large files
  - [ ] Set video privacy (private/unlisted/public)
  - [ ] Add "Altered Content" disclosure (required for AI content)
  - [ ] Set category and tags
  - [ ] Handle upload errors and retries
  - [ ] Return YouTube video ID and URL
  - [ ] Add logging for upload progress
  - [ ] **Trigger TTL timer**: Mark raw assets for deletion 48 hours after successful upload
  - [ ] **Multi-Modal Buffering**: Upload 2-3 thumbnail variants for A/B testing
  - [ ] **Track thumbnail performance**: Monitor CTR for each variant
  - [ ] **Version Tracking**: Store metadata prompt version and model version used

### 2.8 Main Orchestration Script
- [ ] Create `generate_video.py`:
  - [ ] Import all modules
  - [ ] Implement main workflow function
  - [ ] Add progress logging
  - [ ] Add error handling at each step
  - [ ] Add cleanup for temporary files
  - [ ] Add command-line argument support for topic
  - [ ] Add option to upload to YouTube (--upload flag)
  - [ ] Integrate YouTube upload after video generation
  - [ ] Test with sample topic

### 2.9 Testing & Validation
- [ ] Create `tests/test_basic.py`:
  - [ ] Test API connectivity for each service
  - [ ] Test individual modules with mock data
  - [ ] Test end-to-end flow with a simple topic
  - [ ] Verify output files are created correctly
  - [ ] Test YouTube upload with test video (set to private)
  - [ ] Verify YouTube metadata generation

### 2.10 Documentation
- [ ] Create `README.md` with:
  - [ ] Project overview
  - [ ] Setup instructions
  - [ ] Usage examples
  - [ ] API key setup guide
  - [ ] Troubleshooting section

---

## Phase 3: Risk Management & Content Governance

**⚠️ Critical Phase**: This phase prevents "Reused Content" and "Low Effort" flags from YouTube by implementing quality gates before expensive API calls.

### 3.1 Human-in-the-Loop (HITL) Gateway
- [ ] Create `src/review_gateway.py`:
  - [ ] Implement `submit_for_review(script: dict, research_data: dict) -> dict` function
  - [ ] Create review queue system (database table or file-based)
  - [ ] Generate review dashboard/interface:
    - [ ] Display script text and visual prompts
    - [ ] Show original research data for context
    - [ ] Provide approve/reject/request_changes actions
    - [ ] Add reviewer comments field
  - [ ] Implement review status tracking (pending, approved, rejected, changes_requested)
  - [ ] Add notification system (email/Slack) when script is ready for review
  - [ ] Create review timeout mechanism (auto-approve after X hours if no action)
  - [ ] Store review history and decisions

- [ ] Create review interface options:
  - [ ] **Option A**: Simple web interface (Flask/FastAPI)
  - [ ] **Option B**: Email-based review (send script, reply to approve)
  - [ ] **Option C**: Database + CLI tool for reviewers
  - [ ] **Option D**: Integration with agent-based review coordinator

- [ ] Add review workflow:
  - [ ] Script generation → Submit to review queue
  - [ ] Wait for human approval
  - [ ] If approved → Continue to next phase
  - [ ] If rejected → Log reason, stop workflow
  - [ ] If changes requested → Regenerate script with feedback

### 3.2 Automated Fact-Checking Layer
- [ ] Create `src/fact_checker.py`:
  - [ ] Implement `fact_check_script(script: dict, research_data: dict) -> dict` function
  - [ ] Use second LLM instance (different model or same with different prompt):
    - [ ] Extract all factual claims from script
    - [ ] Compare each claim against original research data
    - [ ] Flag discrepancies, unsupported claims, or hallucinations
    - [ ] Generate confidence scores for each fact
  - [ ] Create fact-check report:
    - [ ] List all factual claims
    - [ ] Mark each as: verified, unverified, contradicted, or not_found_in_research
    - [ ] Provide evidence citations from research
    - [ ] Calculate overall script accuracy score
  - [ ] Implement threshold-based decision:
    - [ ] If accuracy < 80% → Flag for human review
    - [ ] If accuracy < 60% → Auto-reject and regenerate
    - [ ] If accuracy >= 80% → Auto-approve or flag for review
  - [ ] Add fact-check logging to database

- [ ] Integration with workflow:
  - [ ] Run fact-check after script generation
  - [ ] If flagged → Send to HITL gateway with fact-check report
  - [ ] If passed → Continue to next phase
  - [ ] Store fact-check results in database

### 3.3 Copyright & Compliance Check
- [ ] Create `src/compliance_checker.py`:
  - [ ] Implement `check_compliance(script: dict, metadata: dict) -> dict` function
  
  - [ ] **Fair Use Analysis**:
    - [ ] Check script for potential copyright issues
    - [ ] Scan for mentions of copyrighted characters, brands, or content
    - [ ] Analyze script for transformative use indicators
    - [ ] Flag potential fair use violations
    - [ ] Provide recommendations for compliance
  
  - [ ] **Altered Content Disclosure**:
    - [ ] Calculate AI-generated content percentage:
      - [ ] Analyze script (AI-generated text)
      - [ ] Analyze visual prompts (AI-generated images)
      - [ ] Analyze voiceover source (AI-generated voice)
      - [ ] Calculate total AI content percentage
    - [ ] Determine disclosure requirement:
      - [ ] If AI content > 50% → Require "Altered Content" disclosure
      - [ ] If AI content > 80% → Require disclosure + additional warnings
      - [ ] Store disclosure flag in metadata
    - [ ] Generate compliance report with recommendations
  
  - [ ] **Metadata Validation**:
    - [ ] Validate title length and content
    - [ ] Check description for required elements
    - [ ] Verify tags are appropriate and not spammy
    - [ ] Check for prohibited content in metadata
    - [ ] Validate thumbnail compliance
  
  - [ ] **YouTube Policy Check**:
    - [ ] Check against YouTube Community Guidelines
    - [ ] Verify content doesn't violate monetization policies
    - [ ] Flag potential "Reused Content" indicators
    - [ ] Flag potential "Low Effort" indicators
    - [ ] Provide improvement suggestions

- [ ] Create compliance report structure:
  ```json
  {
    "fair_use": {
      "status": "pass|warning|fail",
      "issues": [],
      "recommendations": []
    },
    "altered_content": {
      "ai_percentage": 85,
      "requires_disclosure": true,
      "disclosure_level": "standard|enhanced"
    },
    "metadata": {
      "status": "pass|warning|fail",
      "issues": []
    },
    "youtube_policies": {
      "reused_content_risk": "low|medium|high",
      "low_effort_risk": "low|medium|high",
      "recommendations": []
    }
  }
  ```

### 3.4 Integration with Main Workflow
- [ ] Update `generate_video.py`:
  - [ ] After script generation → Run fact-check
  - [ ] After fact-check → Submit to HITL gateway
  - [ ] Wait for human approval
  - [ ] After approval → Run compliance check
  - [ ] If compliance fails → Flag for review or auto-fix
  - [ ] Only proceed to expensive operations (voiceover, images) after all checks pass

- [ ] Add configuration options:
  - [ ] `REQUIRE_HUMAN_REVIEW` (default: true)
  - [ ] `FACT_CHECK_ENABLED` (default: true)
  - [ ] `FACT_CHECK_THRESHOLD` (default: 0.8)
  - [ ] `COMPLIANCE_CHECK_ENABLED` (default: true)
  - [ ] `AUTO_APPROVE_AFTER_HOURS` (default: 24)

### 3.5 Database Schema Updates
- [ ] Add tables for governance:
  - [ ] `reviews` table:
    - [ ] id, video_id, script_id, reviewer, status, comments, created_at, reviewed_at
  - [ ] `fact_checks` table:
    - [ ] id, video_id, script_id, accuracy_score, report_json, created_at
  - [ ] `compliance_checks` table:
    - [ ] id, video_id, script_id, report_json, status, created_at

### 3.6 Testing & Validation
- [ ] Test HITL gateway with sample scripts
- [ ] Test fact-checker with known good/bad scripts
- [ ] Test compliance checker with various scenarios
- [ ] Test workflow blocking when checks fail
- [ ] Test auto-approval timeout mechanism
- [ ] Verify all reports are generated correctly

---

## Phase 4: Enhanced Features & Error Handling

### 3.1 Image Generation Integration
- [ ] Research DALL-E API or Midjourney integration
- [ ] Create `src/image_generator.py`:
  - [ ] Implement image generation from visual prompts
  - [ ] **Idempotency**: Check if image with same prompt hash exists before generating
  - [ ] **Style Optimization**: Append optimal style attributes from performance data
  - [ ] Download and store generated images with TTL metadata
  - [ ] Resize/optimize images for Creatomate
  - [ ] Upload images to Creatomate or hosting service
  - [ ] Track storage costs per image
  - [ ] **Version Tracking**: Store prompt version and model version used

### 3.2 Improved Error Handling
- [ ] Add try-catch blocks in all API calls
- [ ] Implement retry logic with exponential backoff
- [ ] Add timeout handling
- [ ] Create error logging system
- [ ] Add graceful degradation (fallback options)

### 3.3 Data Persistence
- [ ] Create database schema (SQLite for simplicity):
  - [ ] Videos table (id, topic, status, created_at, video_url)
  - [ ] Scripts table (video_id, script_json)
  - [ ] Research table (video_id, research_data)
  - [ ] Reviews table (id, video_id, script_id, reviewer, status, comments, created_at, reviewed_at)
  - [ ] Fact_checks table (id, video_id, script_id, accuracy_score, report_json, created_at)
  - [ ] Compliance_checks table (id, video_id, script_id, report_json, status, created_at)
  - [ ] **Cost_tracking table** (id, video_id, operation, model_used, cost, tokens_used, created_at)
  - [ ] **Storage_assets table** (id, video_id, file_path, file_type, size_bytes, ttl_expires_at, youtube_uploaded_at, created_at)
  - [ ] **Assets table** (id, video_id, asset_type, asset_hash, file_path, cost, created_at, reused_from_video_id)
  - [ ] **Prompt_versions table** (id, video_id, operation, prompt_version, model_version, prompt_text_hash, created_at)
  - [ ] **Model_versions table** (id, model_name, version, release_date, deprecated_at)
  - [ ] **Version_performance table** (id, prompt_version_id, video_id, ctr, views, watch_time, revenue, created_at)
  - [ ] **Thumbnail_styles table** (id, video_id, style_attributes, ctr, views, created_at)
  - [ ] **Style_performance table** (id, style_attribute, avg_ctr, usage_count, last_updated)
  - [ ] **Thumbnail_variants table** (id, video_id, variant_number, file_path, style_attributes, prompt_used, created_at)
  - [ ] **Thumbnail_performance table** (id, video_id, variant_number, ctr, views, impressions, selected_for_primary, created_at)
- [ ] Implement database operations
- [ ] Add data backup functionality
- [ ] **Implement TTL (Time to Live) storage policy**:
  - [ ] Create `src/storage_manager.py` for asset lifecycle management
  - [ ] Implement `register_asset(video_id, file_path, file_type, size_bytes)` function
  - [ ] Implement `set_ttl(video_id, hours=48)` function
  - [ ] Auto-delete raw audio files 48 hours after successful YouTube upload
  - [ ] Auto-delete raw image files 48 hours after successful YouTube upload
  - [ ] Keep final video files (permanent)
  - [ ] Keep database records (permanent)
  - [ ] Implement cleanup job that runs daily (`cleanup_expired_assets()`)
  - [ ] Log all deletions for audit trail
  - [ ] Calculate storage savings from TTL policy

### 3.4 Logging & Monitoring
- [ ] Set up structured logging
- [ ] Create log files for each run
- [ ] Add performance metrics tracking
- [ ] Monitor API usage and costs

---

## Phase 5: Agent-Based Orchestration & Automation

### 5.1 Agent Framework Setup

**Why Agent-Based Approach?**
- Intelligent decision-making based on content quality
- Native Python integration (no Docker overhead)
- Better state management and error recovery
- Easier testing and debugging
- More flexible and extensible

See `AGENT_BASED_ARCHITECTURE.md` for detailed architecture explanation.

- [ ] Review agent architecture document
- [ ] Create `src/agents/` directory structure
- [ ] Create base agent class with common functionality
- [ ] Set up LangGraph workflow framework

### 5.2 Core Agent Implementation

- [ ] **Research Agent** (`src/agents/research_agent.py`):
  - [ ] Implement Perplexity API integration
  - [ ] Add fact extraction logic
  - [ ] Add citation management
  - [ ] Implement error handling and retries

- [ ] **Script Writer Agent** (`src/agents/script_agent.py`):
  - [ ] Implement OpenAI GPT-4 integration
  - [ ] Add structured output parsing
  - [ ] Generate visual prompts
  - [ ] Implement quality scoring

- [ ] **Quality Control Agent** (`src/agents/quality_agent.py`):
  - [ ] Implement fact-checking logic
  - [ ] Compare script claims vs research
  - [ ] Generate accuracy scores
  - [ ] Identify discrepancies

- [ ] **Review Coordinator Agent** (`src/agents/review_agent.py`):
  - [ ] Implement human-in-the-loop integration
  - [ ] Add email/Slack notifications
  - [ ] Implement approval tracking
  - [ ] Add timeout handling

- [ ] **Compliance Agent** (`src/agents/compliance_agent.py`):
  - [ ] Implement YouTube policy checking
  - [ ] Add Fair Use analysis
  - [ ] Verify AI disclosure requirements
  - [ ] Generate compliance reports

- [ ] **Voiceover Agent** (`src/agents/voiceover_agent.py`):
  - [ ] Implement ElevenLabs integration
  - [ ] Add audio file management
  - [ ] Implement quality validation
  - [ ] Handle audio optimization

- [ ] **Visual Agent** (`src/agents/visual_agent.py`):
  - [ ] Implement DALL-E integration
  - [ ] Add image optimization
  - [ ] Manage asset storage
  - [ ] Implement style consistency

- [ ] **Video Assembly Agent** (`src/agents/assembly_agent.py`):
  - [ ] Implement Creatomate integration
  - [ ] Build payload construction
  - [ ] Implement render monitoring
  - [ ] Handle video download

- [ ] **Publishing Agent** (`src/agents/publishing_agent.py`):
  - [ ] Implement OAuth 2.0 authentication
  - [ ] Generate video metadata (title, description, tags)
  - [ ] Handle resumable upload
  - [ ] Set "Altered Content" disclosure
  - [ ] Track upload status

### 5.3 LangGraph Workflow Orchestration

- [ ] **Define State Structure** (`src/workflow/state.py`):
  - [ ] Create `VideoGenerationState` TypedDict
  - [ ] Define all state fields
  - [ ] Add state validation

- [ ] **Create Workflow Graph** (`src/workflow/graph.py`):
  - [ ] Create LangGraph StateGraph
  - [ ] Add workflow nodes for each agent
  - [ ] Define state transitions
  - [ ] Add conditional routing:
    - [ ] Route based on fact-check results
    - [ ] Route based on quality scores
    - [ ] Route to human review when needed
    - [ ] Route to retry on failures

- [ ] **Implement Human-in-the-Loop** (`src/workflow/review_webhook.py`):
  - [ ] Create FastAPI webhook endpoints
  - [ ] Implement review submission endpoint
  - [ ] Add review status endpoint
  - [ ] Integrate with workflow state

- [ ] **Add Error Handling** (`src/workflow/error_handling.py`):
  - [ ] Implement retry mechanisms
  - [ ] Add fallback strategies
  - [ ] Implement error recovery
  - [ ] Add error notification

- [ ] **Configure State Persistence** (`src/workflow/persistence.py`):
  - [ ] Set up state checkpointer
  - [ ] Configure state storage (SQLite/file)
  - [ ] Implement state recovery
  - [ ] Add state history tracking

### 5.4 Scheduling & Automation

**Option 1: Python Scheduler (Local)**
- [ ] Install APScheduler
- [ ] Create scheduler script
- [ ] Configure cron-like schedules
- [ ] Test scheduled execution

**Option 2: Cloud Functions (Recommended)**
- [ ] Set up AWS Lambda / Google Cloud Functions
- [ ] Create function handler
- [ ] Configure CloudWatch / Cloud Scheduler
- [ ] Test cloud execution

**Option 3: Kubernetes CronJob**
- [ ] Create CronJob manifest
- [ ] Configure schedule
- [ ] Deploy to Kubernetes cluster
- [ ] Monitor execution

### 5.5 Testing Agent Workflow

- [ ] Test each agent individually:
  - [ ] Research Agent with sample topics
  - [ ] Script Writer Agent with research data
  - [ ] Quality Control Agent with sample scripts
  - [ ] Review Coordinator Agent with approval flow
  - [ ] Compliance Agent with various content
  - [ ] Voiceover Agent with sample scripts
  - [ ] Visual Agent with visual prompts
  - [ ] Assembly Agent with sample assets
  - [ ] Publishing Agent with test video

- [ ] Test complete workflow end-to-end:
  - [ ] Run full workflow with test topic
  - [ ] Verify state transitions
  - [ ] Test human review checkpoint
  - [ ] Verify final video output

- [ ] Test error scenarios:
  - [ ] API failures
  - [ ] Invalid inputs
  - [ ] Network timeouts
  - [ ] State recovery

- [ ] Test state persistence:
  - [ ] Resume failed workflow
  - [ ] Verify state recovery
  - [ ] Test workflow history

---

## Phase 6: Production Readiness

### 5.1 Security Hardening
- [ ] Review API key storage (use environment variables)
- [ ] Implement secrets management (if using cloud)
- [ ] Implement rate limiting
- [ ] Add input validation
- [ ] Secure webhook endpoints (if using FastAPI)
- [ ] Set up firewall rules if deploying to server

### 5.2 Performance Optimization
- [ ] Optimize API call sequences (parallel where possible)
- [ ] Implement caching for research results
- [ ] Optimize image/video processing
- [ ] Add queue system for batch processing

### 5.6 Cost Optimization & Financial Controls
- [ ] **Model Selection Strategy**:
  - [ ] Use GPT-4o-mini for research parsing (80% cost reduction)
  - [ ] Use GPT-4o-mini for metadata generation
  - [ ] Use GPT-4o only for final script polish
  - [ ] Use ElevenLabs Turbo models for voiceover (when appropriate)
  - [ ] Track model usage and costs per operation

- [ ] **Storage Cost Management**:
  - [ ] Implement TTL policy: Auto-delete raw assets 48 hours after YouTube upload
  - [ ] Monitor storage usage and costs
  - [ ] Set up alerts for storage threshold breaches
  - [ ] Archive old videos to cold storage if needed

- [ ] **Cost Tracking & Budget Controls**:
  - [ ] Create `src/cost_tracker.py`:
    - [ ] Track costs per video operation
    - [ ] Calculate total cost per video
    - [ ] Track daily/monthly spending
    - [ ] Implement budget alerts
    - [ ] Generate cost reports
  - [ ] Add cost limits per video (fail workflow if exceeded)
  - [ ] Add daily/monthly budget limits
  - [ ] Implement cost dashboard or reporting

- [ ] **Financial Controls**:
  - [ ] Set maximum cost per video threshold
  - [ ] Set daily budget limit
  - [ ] Set monthly budget limit
  - [ ] Auto-pause workflow when budget exceeded
  - [ ] Send alerts at 50%, 75%, 90% of budget
  - [ ] Generate weekly cost reports

- [ ] **Optimization Monitoring**:
  - [ ] Track cost savings from model optimization
  - [ ] Monitor storage savings from TTL policy
  - [ ] Compare optimized vs non-optimized costs
  - [ ] Generate optimization impact reports

### 5.3 Monitoring & Alerts
- [ ] Set up monitoring for agent workflows
- [ ] Configure alerts for failures
- [ ] Track API usage and costs
- [ ] Monitor video generation success rate
- [ ] Monitor agent execution times
- [ ] Track state transitions
- [ ] **Cost Monitoring**:
  - [ ] Real-time cost tracking dashboard
  - [ ] Daily cost summaries
  - [ ] Budget threshold alerts (50%, 75%, 90%, 100%)
  - [ ] Cost per video trending
  - [ ] Model usage analytics
  - [ ] Storage cost tracking

### 5.4 Backup & Recovery
- [ ] Set up workflow state backup
- [ ] Backup database regularly
- [ ] Document recovery procedures
- [ ] Test backup restoration
- [ ] Verify state recovery works

### 5.5 Documentation
- [ ] Document agent architecture
- [ ] Document LangGraph workflow structure
- [ ] Create runbook for operations
- [ ] Document API rate limits and costs
- [ ] Create troubleshooting guide
- [ ] Document deployment process

---

## Phase 7: Advanced Features (Optional)

### 6.1 Multi-Topic Batch Processing
- [ ] Create topic queue system
- [ ] Implement batch processing workflow
- [ ] Add progress tracking

### 6.2 Analytics & Reporting
- [ ] Track video performance
- [ ] Generate reports on generation success
- [ ] Analyze API costs per video
- [ ] Create dashboard for metrics

### 6.3 A/B Testing
- [ ] Implement multiple script variations
- [ ] Test different voice styles
- [ ] Compare thumbnail variations
- [ ] Track performance metrics

---

## Quick Start Checklist (Minimum Viable Product)

For a quick test, complete these essential steps:

1. **Setup (30 min)**
   - [ ] Install Docker, Python, Git
   - [ ] Get API keys (OpenAI, Perplexity, ElevenLabs, Creatomate)
   - [ ] Create project and virtual environment
   - [ ] Install dependencies

2. **Basic Script (1-2 hours)**
   - [ ] Create `generate_video.py` with basic structure
   - [ ] Implement research function (Perplexity)
   - [ ] Implement script writing (OpenAI)
   - [ ] Implement video generation (Creatomate)
   - [ ] Test with sample topic

5. **YouTube Upload (Optional - 1 hour)**
   - [ ] Set up YouTube Data API v3
   - [ ] Configure OAuth 2.0
   - [ ] Implement upload module
   - [ ] Test upload with private video

3. **Agent Framework (2-3 hours)**
   - [ ] Set up LangGraph workflow
   - [ ] Implement core agents (Research, Script, Voiceover, Visual, Assembly)
   - [ ] Create basic workflow graph
   - [ ] Test end-to-end

4. **Validation (30 min)**
   - [ ] Verify video output quality
   - [ ] Check error handling
   - [ ] Document findings

---

## Cost Estimation

### Base Cost (Without Optimization)

| Service | Estimated Cost per Video |
|---------|------------------------|
| OpenAI (GPT-4) | $0.10 - $0.30 |
| Perplexity | $0.05 - $0.15 |
| ElevenLabs | $0.20 - $0.50 |
| Creatomate | $0.10 - $0.30 |
| Storage (raw assets) | $0.01 - $0.05 |
| **Total** | **$0.46 - $1.30 per video** |

### Optimized Cost (With Cost Optimization Strategies)

| Service | Optimization | Estimated Cost per Video |
|---------|-------------|------------------------|
| OpenAI Research Parsing (GPT-4o-mini) | 80% reduction | $0.02 - $0.06 |
| OpenAI Script Polish (GPT-4o) | Final quality step | $0.05 - $0.15 |
| OpenAI Metadata (GPT-4o-mini) | 80% reduction | $0.01 - $0.03 |
| Perplexity | No change | $0.05 - $0.15 |
| ElevenLabs (Turbo) | 30-40% reduction | $0.12 - $0.30 |
| Creatomate | No change | $0.10 - $0.30 |
| Storage (with TTL) | 70% reduction | $0.003 - $0.015 |
| **Total Optimized** | **$0.35 - $0.90 per video** |

### Cost Savings Breakdown

- **LLM Optimization**: ~$0.08 - $0.18 saved per video (using GPT-4o-mini for parsing/metadata)
- **Voiceover Optimization**: ~$0.08 - $0.20 saved per video (using Turbo models)
- **Storage Optimization**: ~$0.007 - $0.035 saved per video (TTL policy)
- **Total Savings**: ~$0.17 - $0.40 per video (27-31% reduction)

### Scaling Impact

| Volume | Base Cost | Optimized Cost | Savings |
|--------|-----------|----------------|---------|
| 10 videos/day | $4.60 - $13.00 | $3.50 - $9.00 | $1.10 - $4.00/day |
| 100 videos/day | $46 - $130 | $35 - $90 | $11 - $40/day |
| 1,000 videos/month | $460 - $1,300 | $350 - $900 | $110 - $400/month |

*Note: Costs vary based on video length, API usage, and subscription tiers. Optimized costs assume proper model selection and TTL policy implementation.*

---

## Troubleshooting Guide

### Common Issues

1. **API Key Errors**
   - Verify keys in `.env` file
   - Check key permissions in service dashboards
   - Ensure no extra spaces in keys

2. **Agent Workflow Issues**
   - Verify all agents are imported correctly
   - Check LangGraph state structure matches
   - Review workflow graph for missing edges
   - Check state persistence is configured
   - Review agent logs for specific errors

3. **Video Generation Failures**
   - Verify Creatomate template ID is correct
   - Check template element names match payload
   - Review Creatomate API response for errors

4. **Script Generation Issues**
   - Ensure OpenAI model supports JSON output
   - Verify prompt formatting
   - Check token limits

5. **YouTube Upload Issues**
   - Verify OAuth credentials are valid
   - Check refresh token hasn't expired
   - Ensure video file size is within limits (256GB max)
   - Verify YouTube API quota hasn't been exceeded
   - Check that "Altered Content" disclosure is set
   - Review YouTube API error messages for specific issues

6. **Risk Management & Governance Issues**
   - **Review Gateway**: Check review queue for pending items
   - **Fact-Check Failures**: Review fact-check reports, may need to improve research or script prompts
   - **Compliance Failures**: Review compliance reports, adjust script or metadata
   - **Timeout Issues**: Check auto-approval settings if reviews are timing out
   - **Notification Issues**: Verify email/Slack notifications are configured correctly

---

## Best Practices & Advanced Optimizations

### 5.7 Style-Based Prompt Optimization

**Goal**: Automatically optimize thumbnail and image prompts based on performance data (CTR, engagement).

- [ ] Create `src/style_optimizer.py`:
  - [ ] Implement `analyze_thumbnail_performance(video_id: str) -> dict` function
  - [ ] Track thumbnail CTR (Click-Through Rate) from YouTube Analytics
  - [ ] Extract style attributes from high-performing thumbnails:
    - [ ] High-Contrast
    - [ ] Bold Text
    - [ ] Bright Colors
    - [ ] Face Close-up
    - [ ] Emotional Expression
    - [ ] Text Overlay Style
  - [ ] Store style-performance mapping in database
  - [ ] Implement `get_optimal_style_prompt(base_prompt: str) -> str` function
  - [ ] Automatically append winning style attributes to DALL-E prompts
  - [ ] Update style preferences based on rolling average (last 30 videos)

- [ ] Database schema for style tracking:
  - [ ] `thumbnail_styles` table:
    - [ ] id, video_id, style_attributes, ctr, views, created_at
  - [ ] `style_performance` table:
    - [ ] id, style_attribute, avg_ctr, usage_count, last_updated

- [ ] Integration with image generation:
  - [ ] Before generating thumbnail → Check style performance
  - [ ] Append top-performing style attributes to prompt
  - [ ] Track which style was used for each thumbnail
  - [ ] Update performance metrics after video publishes

- [ ] Configuration:
  - [ ] `STYLE_OPTIMIZATION_ENABLED` (default: true)
  - [ ] `STYLE_LOOKBACK_DAYS` (default: 30)
  - [ ] `MIN_VIDEOS_FOR_STYLE` (default: 10) - Minimum videos before applying style optimization

### 5.8 Idempotency & Asset Reuse

**Goal**: Prevent re-purchasing assets if they already exist, saving costs and time.

- [ ] Create `src/asset_manager.py`:
  - [ ] Implement `check_asset_exists(video_id: str, asset_type: str, hash: str) -> bool` function
  - [ ] Implement asset hashing:
    - [ ] Hash script content for voiceover reuse
    - [ ] Hash visual prompts for image reuse
    - [ ] Hash research data for script reuse
  - [ ] Implement `get_existing_asset(video_id: str, asset_type: str) -> str` function
  - [ ] Store asset metadata:
    - [ ] Asset hash
    - [ ] File path
    - [ ] Generation timestamp
    - [ ] Cost (if applicable)

- [ ] Database schema:
  - [ ] `assets` table:
    - [ ] id, video_id, asset_type, asset_hash, file_path, cost, created_at, reused_from_video_id

- [ ] Idempotency checks in each module:
  - [ ] **Voiceover Module**:
    - [ ] Before generating → Check if script hash exists
    - [ ] If exists → Reuse existing audio file
    - [ ] Log reuse in database
  - [ ] **Image Generation Module**:
    - [ ] Before generating → Check if visual prompt hash exists
    - [ ] If exists → Reuse existing image
    - [ ] Log reuse in database
  - [ ] **Script Generation Module**:
    - [ ] Before generating → Check if research hash + topic exists
    - [ ] If exists → Reuse existing script (optional, may want fresh scripts)
  - [ ] **Video Generation Module**:
    - [ ] Before rendering → Check if all assets match existing video
    - [ ] If exists → Reuse existing video (optional)

- [ ] Workflow integration:
  - [ ] Add idempotency check at start of each expensive operation
  - [ ] Skip generation if asset exists
  - [ ] Continue workflow with existing asset
  - [ ] Track cost savings from asset reuse

- [ ] Configuration:
  - [ ] `ENABLE_ASSET_REUSE` (default: true)
  - [ ] `REUSE_VOICEOVER` (default: true)
  - [ ] `REUSE_IMAGES` (default: true)
  - [ ] `REUSE_SCRIPTS` (default: false) - Usually want fresh scripts
  - [ ] `REUSE_VIDEOS` (default: false) - Usually want fresh videos

### 5.9 Prompt Versioning & Model Tracking

**Goal**: Track which prompt versions and model versions produced best-performing content.

- [ ] Create `src/version_tracker.py`:
  - [ ] Implement `track_prompt_version(video_id: str, operation: str, prompt_version: str, model_version: str) -> None` function
  - [ ] Store prompt templates with version numbers
  - [ ] Track model versions (e.g., "gpt-4o-2024-08-06", "gpt-5-2025-01-15")
  - [ ] Link versions to video performance metrics

- [ ] Database schema:
  - [ ] `prompt_versions` table:
    - [ ] id, video_id, operation, prompt_version, model_version, prompt_text_hash, created_at
  - [ ] `model_versions` table:
    - [ ] id, model_name, version, release_date, deprecated_at
  - [ ] `version_performance` table:
    - [ ] id, prompt_version_id, video_id, ctr, views, watch_time, revenue, created_at

- [ ] Version tracking implementation:
  - [ ] **Script Generation**:
    - [ ] Store prompt template version (e.g., "script_v2.1")
    - [ ] Store model version used
    - [ ] Hash prompt text for uniqueness
  - [ ] **Image Generation**:
    - [ ] Store DALL-E prompt template version
    - [ ] Store DALL-E model version
    - [ ] Track style attributes used
  - [ ] **Voiceover**:
    - [ ] Store voice model version
    - [ ] Store voice settings version
  - [ ] **Metadata Generation**:
    - [ ] Store metadata prompt version
    - [ ] Store model version

- [ ] Performance analysis:
  - [ ] Link prompt versions to video performance
  - [ ] Calculate average CTR per prompt version
  - [ ] Calculate average watch time per prompt version
  - [ ] Identify best-performing prompt versions
  - [ ] Generate version performance reports

- [ ] Migration strategy:
  - [ ] When model updates (GPT-4 → GPT-5):
    - [ ] Create new prompt version
    - [ ] Test with subset of videos
    - [ ] Compare performance
    - [ ] Gradually migrate if better
    - [ ] Keep old version available for rollback

- [ ] Configuration:
  - [ ] `PROMPT_VERSIONING_ENABLED` (default: true)
  - [ ] `AUTO_TRACK_VERSIONS` (default: true)
  - [ ] `VERSION_PERFORMANCE_LOOKBACK_DAYS` (default: 90)

### 5.10 Multi-Modal Buffering & A/B Testing

**Goal**: Generate multiple thumbnail options for YouTube A/B testing to maximize CTR.

- [ ] Create `src/thumbnail_generator.py`:
  - [ ] Implement `generate_thumbnail_variants(video_metadata: dict, count: int = 3) -> list` function
  - [ ] Generate 2-3 thumbnail variations:
    - [ ] Different style approaches (High-Contrast, Minimalist, Bold Text)
    - [ ] Different compositions (Close-up, Wide-shot, Text-focused)
    - [ ] Different color schemes
    - [ ] Different emotional tones
  - [ ] Store all variants in database
  - [ ] Upload all variants to YouTube for A/B testing

- [ ] Database schema:
  - [ ] `thumbnail_variants` table:
    - [ ] id, video_id, variant_number, file_path, style_attributes, prompt_used, created_at
  - [ ] `thumbnail_performance` table:
    - [ ] id, video_id, variant_number, ctr, views, impressions, selected_for_primary, created_at

- [ ] YouTube A/B testing integration:
  - [ ] Upload all thumbnail variants to YouTube
  - [ ] Set primary thumbnail (first variant)
  - [ ] Enable YouTube's thumbnail A/B testing feature
  - [ ] Track performance of each variant
  - [ ] Automatically switch to best-performing variant after 7 days

- [ ] Variant generation strategies:
  - [ ] **Strategy 1: Style Variations**
    - [ ] Variant 1: High-Contrast + Bold Text
    - [ ] Variant 2: Minimalist + Subtle Text
    - [ ] Variant 3: Bright Colors + Emotional
  - [ ] **Strategy 2: Composition Variations**
    - [ ] Variant 1: Face Close-up
    - [ ] Variant 2: Full Scene
    - [ ] Variant 3: Text-Heavy
  - [ ] **Strategy 3: Emotional Variations**
    - [ ] Variant 1: Excited/Happy
    - [ ] Variant 2: Serious/Professional
    - [ ] Variant 3: Curious/Intrigued

- [ ] Learning from A/B test results:
  - [ ] Track which variant performs best
  - [ ] Update style preferences based on winners
  - [ ] Use winning styles for future thumbnails
  - [ ] Generate reports on A/B test performance

- [ ] Configuration:
  - [ ] `THUMBNAIL_VARIANTS_COUNT` (default: 3)
  - [ ] `ENABLE_AB_TESTING` (default: true)
  - [ ] `AB_TEST_DURATION_DAYS` (default: 7)
  - [ ] `AUTO_SWITCH_BEST_VARIANT` (default: true)

### 5.11 Integration of Best Practices

- [ ] Update main workflow to include:
  - [ ] Style optimization before image generation
  - [ ] Idempotency checks before all asset generation
  - [ ] Version tracking for all prompts and models
  - [ ] Multi-variant thumbnail generation
  - [ ] Performance tracking and learning

- [ ] Create `src/performance_learner.py`:
  - [ ] Aggregate performance data from all sources
  - [ ] Learn optimal styles, prompts, and variants
  - [ ] Update generation strategies automatically
  - [ ] Generate performance reports

- [ ] Dashboard/reporting:
  - [ ] Style performance dashboard
  - [ ] Asset reuse statistics
  - [ ] Version performance comparison
  - [ ] A/B test results summary
  - [ ] Cost savings from optimizations

---

## Next Steps After Completion

1. **Scale Testing**: Generate 5-10 videos to test consistency
2. **Quality Review**: Manually review outputs for improvements
3. **Optimization**: Refine prompts and templates based on results
4. **Automation**: Set up scheduled runs (APScheduler or cloud functions)
5. **Monitoring**: Track success rates and costs
6. **Iteration**: Continuously improve based on feedback

---

## Notes

- Start with Phase 1-2 to get a working prototype
- Test thoroughly before moving to agent-based orchestration
- Keep API keys secure and never commit them to Git
- Monitor API usage to avoid unexpected costs
- Document any customizations or changes you make
