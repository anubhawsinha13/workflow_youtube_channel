# YouTube Workflow Automation - Agent-Based System

This project implements an intelligent agent-based workflow for automated YouTube video generation using a 3-layer architecture.

## Architecture Overview

This system follows a **3-layer architecture** that separates concerns:

### Layer 1: Directive (What to do)
- SOPs written in Markdown, located in `directives/`
- Define goals, inputs, tools, outputs, and edge cases
- Natural language instructions for each workflow phase

### Layer 2: Orchestration (Decision making)
- AI agent (you) that reads directives and makes intelligent decisions
- Routes to appropriate execution scripts
- Handles errors, retries, and workflow state

### Layer 3: Execution (Doing the work)
- Deterministic Python scripts in `execution/`
- Handle API calls, data processing, file operations
- Reliable, testable, and fast

## Project Structure

```
workflow_youtube_channel/
├── directives/          # Layer 1: SOPs and instructions
│   ├── research.md
│   ├── script_generation.md
│   ├── fact_check.md
│   ├── voiceover_generation.md
│   ├── visual_generation.md
│   ├── video_assembly.md
│   └── youtube_publish.md
├── execution/           # Layer 3: Python scripts
│   ├── __init__.py
│   ├── research_topic.py
│   └── [other scripts]
├── .tmp/               # Temporary files (gitignored)
├── credentials/        # OAuth credentials (gitignored)
├── .env               # Environment variables (gitignored)
├── .env.example       # Environment variable template
├── requirements.txt   # Python dependencies
├── agents.md          # Architecture instructions
└── README.md          # This file
```

## Setup

1. **Install Python 3.8+** and create virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment**:
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

4. **Get API keys**:
   - OpenAI: https://platform.openai.com
   - Perplexity: https://www.perplexity.ai
   - ElevenLabs: https://elevenlabs.io
   - Creatomate: https://creatomate.com
   - YouTube Data API: https://console.cloud.google.com

## Usage

The system is designed to be orchestrated by an AI agent. However, you can run individual execution scripts directly:

```bash
# Research a topic
python execution/research_topic.py "The rise and fall of Blackberry" 4

# Other scripts follow similar pattern
```

## Workflow Phases

1. **Research** - Gather facts using Perplexity
2. **Script Generation** - Create engaging script with OpenAI
3. **Fact Check** - Verify script accuracy
4. **Human Review** - Optional review checkpoint
5. **Compliance Check** - Verify YouTube policy compliance
6. **Voiceover Generation** - Create audio with ElevenLabs
7. **Visual Generation** - Generate images with DALL-E
8. **Video Assembly** - Combine assets with Creatomate
9. **YouTube Publishing** - Upload to YouTube

## Key Principles

- **Check for tools first** - Look in `execution/` before creating new scripts
- **Self-anneal** - Fix errors, update tools, learn from mistakes
- **Update directives** - Keep directives current with learnings
- **Be pragmatic** - Focus on reliability and determinism

## Documentation

### Core Documentation
- `agents.md` - Full architecture explanation
- `plan.md` - Implementation plan
- `optimized_workflow.md` - Detailed workflow guide
- `AGENT_BASED_ARCHITECTURE.md` - Technical architecture details
- `directives/*.md` - Individual phase instructions

### Organized Documentation
- `docs/setup/` - Setup and configuration guides (7 files)
- `docs/guides/` - Feature guides and technical documentation (21 files)
- `docs/archive/` - Historical status files (9 files)
- See [docs/README.md](docs/README.md) for complete documentation index

## License

This project is for educational purposes. Ensure compliance with all API terms of service.
# workflow_youtube_channel
