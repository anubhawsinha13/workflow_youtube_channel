Phase 1: Environment Setup & API Access
1. Install Essential Software
You will need Git and Python installed on your laptop.
Install Python: Ensure you have Python 3.8+ installed.
Install Git: For version control and managing code.
Note: Docker is optional and not required for the agent-based approach.
2. Get Your API Keys
You need accounts and API keys for the core services. Keep these secure.
OpenAI: Get your API key from the OpenAI API documentation.
Perplexity: Get your API key from the Perplexity API documentation.
ElevenLabs: Get your API key from your ElevenLabs profile settings.
Creatomate: Get your API key from the Project Settings in your Creatomate dashboard. You will also need to create a video template and get its Template ID and the names of dynamic elements (e.g., Text-1, Image-1, Voiceover-1).
3. Set up the Development Environment (IDE)
Open your IDE (VS Code, PyCharm, etc.).
Create a Project Folder: Open the terminal in your IDE and run:
bash
mkdir youtube_automation
cd youtube_automation
Use code with caution.

Create a Python Virtual Environment:
bash
python -m venv venv
# Activate the environment (Mac/Linux)
source venv/bin/activate
# Activate the environment (Windows)
.\venv\Scripts\activate
Use code with caution.

Install Required Python Libraries:
bash
pip install requests openai perplexityai elevenlabs python-dotenv langchain langgraph langchain-openai langchain-community pydantic
Use code with caution.

Create a .env file in your project root to store API keys securely. This file should be added to your .gitignore.
# .env file
OPENAI_API_KEY="your_openai_key"
PERPLEXITY_API_KEY="your_perplexity_key"
ELEVENLABS_API_KEY="your_elevenlabs_key"
CREATOMATE_API_KEY="your_creatomate_key"
CREATOMATE_TEMPLATE_ID="your_template_id"
Phase 2: Building the Python Script Pipeline
You will build a single Python script (generate_video.py) that executes the core logic of the agentic workflow manually for the sample video.
generate_video.py
Create a file named generate_video.py in your project folder and add the following structure:
python
import os
from dotenv import load_dotenv
import requests
from perplexity import Perplexity
from openai import OpenAI
import time

load_dotenv()

# --- Configuration ---
PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
CREATOMATE_API_KEY = os.getenv("CREATOMATE_API_KEY")
CREATOMATE_TEMPLATE_ID = os.getenv("CREATOMATE_TEMPLATE_ID")
VIDEO_TOPIC = "The core differences between a black hole and a wormhole" 

# Initialize clients
pplx_client = Perplexity(api_key=PERPLEXITY_API_KEY)
openai_client = OpenAI(api_key=OPENAI_API_KEY)

def step_1_research(topic):
    """Agentic Research Step using Perplexity API."""
    print(f"🕵️‍♀️ Researching: {topic}...")
    response = pplx_client.chat.completions.create(
        model="sonar-medium-online",
        messages=[
            {"role": "system", "content": "You are a world-class researcher. Your task is to gather verified facts with citations on the given topic."},
            {"role": "user", "content": f"Provide 4 key, distinct facts about: {topic}"}
        ]
    )
    facts = response.choices[0].message.content
    print("✅ Research complete.")
    return facts

def step_2_scriptwrite(facts):
    """Scriptwriting Step using OpenAI API."""
    print("✍️ Writing script and generating visual prompts...")
    prompt = f"""
    Act as a YouTube scriptwriter. Your task is to turn the following facts into four short, engaging scenes for an animated faceless video. 
    Format your output as a JSON list of objects, where each object has "text" (for voiceover/subtitles) and "visual_prompt" (a DALL-E image generation prompt for an animated scene).
    Facts: {facts}
    """
    response = openai_client.chat.completions.create(
        model="gpt-4o",
        response_format={"type": "json_object"}, # Ensure JSON output
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    # Note: response_format="json_object" is a hint, actual parsing might be needed.
    script_json_string = response.choices[0].message.content
    print("✅ Script complete.")
    return script_json_string 

def step_3_generate_video(payload):
    """Video Generation Step using Creatomate API."""
    print("🎬 Generating video with Creatomate...")
    
    headers = {
        "Authorization": f"Bearer {CREATOMATE_API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post("https://api.creatomate.com/v1/renders", headers=headers, json=payload)
    if response.status_code == 201:
        render_data = response.json()
        print(f"Video render initiated. Status: {render_data['status']}.")
        print(f"Video URL (will be ready in a minute or two): {render_data['url']}")
        return render_data
    else:
        print(f"Failed to initiate render: {response.text}")
        return None

# --- Main execution flow ---
if __name__ == "__main__":
    # Note: The visual generation part is omitted here as it's complex to automate fully
    # using simple Python scripts without a dedicated service like RunwayML API which requires more setup.
    # The Creatomate step uses pre-defined public image URLs for this sample script.

    # Run the steps sequentially for a sample video
    try:
        facts = step_1_research(VIDEO_TOPIC)
        # In a real agentic flow, the scriptwriter would parse 'facts' and format the 'payload'
        # script_json = step_2_scriptwrite(facts) 
        
        # For this simplified test, we use a static sample payload. 
        # In a full workflow, this payload would be dynamically generated
        # based on the script_json and potentially generated images.
        sample_payload_data = {
            "Voiceover-1.source": "A black hole is a region of spacetime where gravity is so strong that nothing can escape.",
            "Image-1.source": "https://cdn.creatomate.com",
            "Voiceover-2.source": "A wormhole is a hypothetical passage through space-time that could create shortcuts across the universe.",
            "Image-2.source": "https://cdn.creatomate.com",
        }
        
        # Prepare the full payload for the Creatomate API call
        full_creatomate_payload = {
            "template_id": CREATOMATE_TEMPLATE_ID,
            "modifications": sample_payload_data
        }
        
        step_3_generate_video(full_creatomate_payload)

    except Exception as e:
        print(f"An error occurred: {e}")
Use code with caution.

4. Run the Sample Video Script
In your IDE's terminal, with the virtual environment activated, run:
bash
python generate_video.py
Use code with caution.

The script will print the video URL. Wait a minute or two, then paste the URL into your browser to see the final generated video.
Phase 3: Building the Agent-Based Orchestrator
Once the Python logic works, you will build an intelligent agent-based orchestrator using LangGraph for full automation.
Why Agents Instead of n8n?
- Intelligent decision-making based on content quality
- Native Python integration (no Docker overhead)
- Better state management and error recovery
- Easier testing and debugging
- More flexible and extensible
See AGENT_BASED_ARCHITECTURE.md for detailed architecture explanation.
Implementation Steps:
1. Create Agent Classes:
   - Research Agent (Perplexity integration)
   - Script Writer Agent (OpenAI integration)
   - Quality Control Agent (fact-checking)
   - Review Coordinator Agent (human-in-the-loop)
   - Compliance Agent (YouTube policy checking)
   - Voiceover Agent (ElevenLabs integration)
   - Visual Agent (DALL-E integration)
   - Video Assembly Agent (Creatomate integration)
   - Publishing Agent (YouTube upload)

2. Build LangGraph Workflow:
   - Define state machine with workflow state
   - Create workflow nodes for each agent
   - Add conditional routing based on quality scores
   - Implement human-in-the-loop checkpoints
   - Add error handling and retry mechanisms

3. Add Scheduling (Optional):
   - Use APScheduler for local scheduling
   - Or deploy to cloud functions (AWS Lambda, Google Cloud Functions)
   - Or use Kubernetes CronJob for production

The agent-based approach provides intelligent orchestration with better decision-making, state persistence, and native Python integration while maintaining all automation capabilities. 
