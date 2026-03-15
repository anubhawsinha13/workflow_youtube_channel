# YouTube Automation Workflow - Visual Diagrams

This document contains visual representations of the YouTube automation workflow using Mermaid diagrams.

---

## 1. High-Level Workflow Overview

```mermaid
graph TB
    Start([Start: Video Topic Input]) --> Setup[Phase 1: Environment Setup]
    Setup --> Research[Phase 2: Research Topic]
    Research --> Script[Phase 3: Generate Script]
    Script --> Voice[Phase 4: Generate Voiceover]
    Voice --> Images[Phase 5: Generate Images]
    Images --> Video[Phase 6: Generate Video]
    Video --> Upload[Phase 7: Upload to YouTube]
    Upload --> Output([Output: Published Video])
    
    Setup --> |API Keys| APIs[API Services]
    Research --> |Perplexity API| APIs
    Script --> |OpenAI API| APIs
    Voice --> |ElevenLabs API| APIs
    Images --> |DALL-E/Midjourney| APIs
    Video --> |Creatomate API| APIs
    Upload --> |YouTube Data API| APIs
    
    style Start fill:#90EE90
    style Output fill:#90EE90
    style Setup fill:#FFD700
    style Research fill:#87CEEB
    style Script fill:#87CEEB
    style Voice fill:#87CEEB
    style Images fill:#87CEEB
    style Video fill:#87CEEB
    style APIs fill:#FFA500
```

---

## 2. Detailed Process Flow

```mermaid
flowchart TD
    A[Input: Video Topic] --> B{Validate Input}
    B -->|Invalid| A
    B -->|Valid| C[Load Configuration]
    C --> D{Check API Keys}
    D -->|Missing| E[Error: Missing API Keys]
    D -->|Present| F[Step 1: Research with Perplexity]
    
    F --> G{Research Success?}
    G -->|No| H[Retry Research]
    H -->|Max Retries| E
    H -->|Retry| F
    G -->|Yes| I[Extract Facts & Sources]
    
    I --> J[Step 2: Generate Script with OpenAI]
    J --> K{Script Valid?}
    K -->|No| L[Retry Script Generation]
    L -->|Max Retries| E
    L -->|Retry| J
    K -->|Yes| M[Parse Script JSON]
    
    M --> FC[Step 2.5: Automated Fact-Check]
    FC --> FC_RESULT{Fact-Check Pass?}
    FC_RESULT -->|Accuracy < 60%| J
    FC_RESULT -->|Accuracy 60-80%| HITL[Step 2.6: Human Review Gateway]
    FC_RESULT -->|Accuracy >= 80%| COMP[Step 2.7: Compliance Check]
    
    HITL --> HITL_RESULT{Human Approved?}
    HITL_RESULT -->|Rejected| E
    HITL_RESULT -->|Changes Requested| J
    HITL_RESULT -->|Approved| COMP
    HITL_RESULT -->|Timeout| COMP
    
    COMP --> COMP_RESULT{Compliance Pass?}
    COMP_RESULT -->|Fail| HITL
    COMP_RESULT -->|Pass| N[Step 3: Generate Voiceover with ElevenLabs]
    N --> O{Audio Generated?}
    O -->|No| P[Retry Voiceover]
    P -->|Max Retries| E
    P -->|Retry| N
    O -->|Yes| Q[Save Audio Files]
    
    Q --> R[Step 4: Generate Images]
    R --> S{Images Generated?}
    S -->|No| T[Retry Image Generation]
    T -->|Max Retries| E
    T -->|Retry| R
    S -->|Yes| U[Upload Images to Storage]
    
    U --> V[Step 5: Build Creatomate Payload]
    V --> W[Step 6: Generate Video with Creatomate]
    W --> X{Video Rendered?}
    X -->|No| Y[Poll Render Status]
    Y -->|Timeout| E
    Y -->|In Progress| Y
    X -->|Yes| Z[Download Final Video]
    
    Z --> AA[Save to Database]
    AA --> AB{Upload to YouTube?}
    AB -->|Yes| AC[Step 7: Upload to YouTube]
    AB -->|No| AD[Cleanup Temporary Files]
    AC --> AE{Upload Success?}
    AE -->|No| AF[Retry Upload]
    AF -->|Max Retries| E
    AF -->|Retry| AC
    AE -->|Yes| AG[Set Video Metadata]
    AG --> AH[Add Altered Content Disclosure]
    AH --> AI[Save YouTube Video ID]
    AI --> AD
    AD --> AJ([Success: Video Published])
    
    E --> AD[Log Error]
    AD --> AE[Send Notification]
    AE --> AF([End: Error State])
    
    style A fill:#E6F3FF
    style AJ fill:#90EE90
    style AF fill:#FFB6C1
    style AC fill:#FFF4E6
    style E fill:#FFB6C1
    style F fill:#FFF4E6
    style J fill:#FFF4E6
    style FC fill:#FFE4B5
    style HITL fill:#FFB6C1
    style COMP fill:#FFE4B5
    style N fill:#FFF4E6
    style R fill:#FFF4E6
    style W fill:#FFF4E6
```

---

## 3. System Architecture

```mermaid
graph TB
    subgraph "Input Layer"
        UI[User Interface]
        CLI[Command Line]
        SCHED[Scheduler]
    end
    
    subgraph "Orchestration Layer"
        PY[Python Script]
        N8N[n8n Workflow]
    end
    
    subgraph "Processing Modules"
        RES[Research Module]
        SCR[Script Writer]
        FC[Fact Checker]
        RG[Review Gateway]
        CC[Compliance Checker]
        VOI[Voiceover Generator]
        IMG[Image Generator]
        VID[Video Generator]
        YTU[YouTube Uploader]
    end
    
    subgraph "External APIs"
        PERP[Perplexity API]
        OPEN[OpenAI API]
        ELEV[ElevenLabs API]
        DAL[DALL-E API]
        CREA[Creatomate API]
        YT[YouTube Data API]
    end
    
    subgraph "Data Layer"
        DB[(SQLite Database)]
        FS[File System]
        CACHE[Cache]
    end
    
    subgraph "Output"
        VIDEO[Final Video]
        LOGS[Logs]
        METRICS[Metrics]
    end
    
    UI --> PY
    CLI --> PY
    SCHED --> N8N
    
    PY --> RES
    PY --> SCR
    PY --> FC
    PY --> RG
    PY --> CC
    PY --> VOI
    PY --> IMG
    PY --> VID
    
    N8N --> RES
    N8N --> SCR
    N8N --> FC
    N8N --> RG
    N8N --> CC
    N8N --> VOI
    N8N --> IMG
    N8N --> VID
    N8N --> YTU
    
    RES --> PERP
    SCR --> OPEN
    VOI --> ELEV
    IMG --> DAL
    VID --> CREA
    YTU --> YT
    
    RES --> DB
    SCR --> DB
    VOI --> FS
    IMG --> FS
    VID --> FS
    
    RES --> CACHE
    SCR --> CACHE
    
    VID --> VIDEO
    PY --> LOGS
    N8N --> LOGS
    PY --> METRICS
    N8N --> METRICS
    
    style UI fill:#E6F3FF
    style CLI fill:#E6F3FF
    style SCHED fill:#E6F3FF
    style PY fill:#FFD700
    style N8N fill:#FFD700
    style VIDEO fill:#90EE90
```

---

## 4. n8n Workflow Structure

```mermaid
graph LR
    subgraph "n8n Workflow"
        TRIG[Trigger Node]
        TRIG -->|Manual/Schedule| VALID[Validate Input]
        
        VALID -->|Valid| PERP_NODE[Perplexity HTTP Request]
        VALID -->|Invalid| ERROR1[Error Handler]
        
        PERP_NODE -->|Success| PARSE1[Parse Research Data]
        PERP_NODE -->|Error| RETRY1[Retry Logic]
        RETRY1 -->|Max Retries| ERROR1
        RETRY1 -->|Retry| PERP_NODE
        
        PARSE1 --> OPENAI_NODE[OpenAI HTTP Request]
        OPENAI_NODE -->|Success| PARSE2[Parse Script JSON]
        OPENAI_NODE -->|Error| RETRY2[Retry Logic]
        RETRY2 -->|Max Retries| ERROR1
        RETRY2 -->|Retry| OPENAI_NODE
        
        PARSE2 --> FACT_CHECK[Fact-Check Node]
        FACT_CHECK -->|Pass| HITL_NODE[Human Review Node]
        FACT_CHECK -->|Fail| ERROR1
        
        HITL_NODE -->|Approved| COMP_CHECK[Compliance Check Node]
        HITL_NODE -->|Rejected| ERROR1
        HITL_NODE -->|Timeout| COMP_CHECK
        
        COMP_CHECK -->|Pass| TRANSFORM[Transform Data]
        COMP_CHECK -->|Fail| HITL_NODE
        
        TRANSFORM --> ELEV_NODE[ElevenLabs HTTP Request]
        ELEV_NODE -->|Success| DOWNLOAD[Download Audio]
        ELEV_NODE -->|Error| RETRY3[Retry Logic]
        RETRY3 -->|Max Retries| ERROR1
        RETRY3 -->|Retry| ELEV_NODE
        
        DOWNLOAD --> IMG_NODE[Image Generation]
        IMG_NODE -->|Success| UPLOAD[Upload Images]
        IMG_NODE -->|Error| RETRY4[Retry Logic]
        RETRY4 -->|Max Retries| ERROR1
        RETRY4 -->|Retry| IMG_NODE
        
        UPLOAD --> BUILD[Build Creatomate Payload]
        BUILD --> CREA_NODE[Creatomate HTTP Request]
        CREA_NODE -->|Success| POLL[Poll Render Status]
        CREA_NODE -->|Error| RETRY5[Retry Logic]
        RETRY5 -->|Max Retries| ERROR1
        RETRY5 -->|Retry| CREA_NODE
        
        POLL -->|In Progress| WAIT[Wait Node]
        WAIT --> POLL
        POLL -->|Complete| DOWNLOAD_VID[Download Video]
        POLL -->|Timeout| ERROR1
        
        DOWNLOAD_VID --> YT_NODE[YouTube Upload Node]
        YT_NODE -->|Success| YT_META[Set Video Metadata]
        YT_NODE -->|Error| RETRY6[Retry Logic]
        RETRY6 -->|Max Retries| ERROR1
        RETRY6 -->|Retry| YT_NODE
        
        YT_META --> YT_DISCLOSE[Add Altered Content Disclosure]
        YT_DISCLOSE --> SAVE[Save to Database]
        SAVE --> NOTIFY[Success Notification]
        NOTIFY --> END([End])
        
        ERROR1 --> ERROR_NOTIFY[Error Notification]
        ERROR_NOTIFY --> END
    end
    
    style TRIG fill:#90EE90
    style END fill:#90EE90
    style ERROR1 fill:#FFB6C1
    style ERROR_NOTIFY fill:#FFB6C1
    style PERP_NODE fill:#FFF4E6
    style OPENAI_NODE fill:#FFF4E6
    style FACT_CHECK fill:#FFE4B5
    style HITL_NODE fill:#FFB6C1
    style COMP_CHECK fill:#FFE4B5
    style ELEV_NODE fill:#FFF4E6
    style IMG_NODE fill:#FFF4E6
    style CREA_NODE fill:#FFF4E6
    style YT_NODE fill:#FFF4E6
```

---

## 5. Data Flow Diagram

```mermaid
flowchart LR
    subgraph "Input Data"
        TOPIC[Topic String]
    end
    
    subgraph "Research Phase"
        TOPIC --> PERP_API[Perplexity API]
        PERP_API --> RESEARCH_DATA[Research Data<br/>- Facts<br/>- Sources<br/>- Citations]
    end
    
    subgraph "Script Phase"
        RESEARCH_DATA --> OPENAI_API[OpenAI API]
        OPENAI_API --> SCRIPT_JSON[Script JSON<br/>- Scenes<br/>- Text<br/>- Visual Prompts]
    end
    
    subgraph "Risk Management Phase"
        SCRIPT_JSON --> FACT_CHECK[Fact-Check<br/>Compare vs Research]
        FACT_CHECK --> FACT_REPORT[Fact-Check Report<br/>- Accuracy Score<br/>- Verified Claims<br/>- Discrepancies]
        FACT_REPORT --> HITL_REVIEW[Human Review<br/>Approve/Reject]
        HITL_REVIEW --> COMP_CHECK[Compliance Check<br/>- Fair Use<br/>- AI Disclosure<br/>- Metadata]
        COMP_CHECK --> COMP_REPORT[Compliance Report<br/>- Status<br/>- Recommendations]
    end
    
    subgraph "Voiceover Phase"
        SCRIPT_JSON --> ELEV_API[ElevenLabs API]
        ELEV_API --> AUDIO_FILES[Audio Files<br/>- scene1.mp3<br/>- scene2.mp3<br/>- ...]
    end
    
    subgraph "Image Phase"
        SCRIPT_JSON --> DAL_API[DALL-E API]
        DAL_API --> IMAGE_FILES[Image Files<br/>- scene1.png<br/>- scene2.png<br/>- ...]
    end
    
    subgraph "Video Assembly"
        AUDIO_FILES --> PAYLOAD[Creatomate Payload]
        IMAGE_FILES --> PAYLOAD
        SCRIPT_JSON --> PAYLOAD
        PAYLOAD --> CREA_API[Creatomate API]
        CREA_API --> VIDEO_FILE[Final Video<br/>.mp4]
    end
    
    subgraph "YouTube Publishing"
        VIDEO_FILE --> YT_API[YouTube Data API]
        SCRIPT_JSON --> YT_META[Video Metadata<br/>- Title<br/>- Description<br/>- Tags]
        YT_META --> YT_API
        YT_API --> YT_VIDEO[Published Video<br/>YouTube URL]
    end
    
    subgraph "Storage"
        RESEARCH_DATA --> DB[(Database)]
        SCRIPT_JSON --> DB
        VIDEO_FILE --> DB
        VIDEO_FILE --> FS[File System]
        YT_VIDEO --> DB
    end
    
    style TOPIC fill:#E6F3FF
    style VIDEO_FILE fill:#90EE90
    style DB fill:#FFD700
    style FS fill:#FFD700
```

---

## 6. Error Handling Flow

```mermaid
stateDiagram-v2
    [*] --> NormalFlow
    
    state NormalFlow {
        [*] --> Research
        Research --> ScriptGen
        ScriptGen --> VoiceGen
        VoiceGen --> ImageGen
        ImageGen --> VideoGen
        VideoGen --> [*]
    }
    
    state ErrorHandling {
        [*] --> CheckErrorType
        CheckErrorType --> APIError: API Failure
        CheckErrorType --> ValidationError: Invalid Data
        CheckErrorType --> TimeoutError: Timeout
        CheckErrorType --> NetworkError: Network Issue
        
        APIError --> RetryLogic
        ValidationError --> LogError
        TimeoutError --> RetryLogic
        NetworkError --> RetryLogic
        
        RetryLogic --> CheckRetries
        CheckRetries --> Retry: Retries < Max
        CheckRetries --> Fallback: Retries >= Max
        
        Retry --> [*]
        Fallback --> LogError
        LogError --> Notify
        Notify --> [*]
    }
    
    Research --> ErrorHandling: Error
    ScriptGen --> ErrorHandling: Error
    VoiceGen --> ErrorHandling: Error
    ImageGen --> ErrorHandling: Error
    VideoGen --> ErrorHandling: Error
    
    ErrorHandling --> NormalFlow: Retry Success
    ErrorHandling --> [*]: Fatal Error
```

---

## 7. Phase-by-Phase Development Flow

```mermaid
gantt
    title YouTube Automation Workflow Development Timeline
    dateFormat  YYYY-MM-DD
    section Phase 1: Setup
    Software Installation           :2024-01-01, 1d
    API Key Setup                   :2024-01-02, 1d
    Project Structure               :2024-01-02, 1d
    Environment Configuration       :2024-01-03, 1d
    
    section Phase 2: Core Development
    Research Module                 :2024-01-04, 1d
    Script Writer Module            :2024-01-05, 1d
    Voiceover Module                :2024-01-06, 1d
    Video Generator Module          :2024-01-07, 1d
    Main Orchestration              :2024-01-08, 1d
    Testing                         :2024-01-09, 1d
    
    section Phase 3: Enhanced Features
    Image Generation                :2024-01-10, 1d
    Error Handling                  :2024-01-11, 1d
    Data Persistence                :2024-01-12, 1d
    Logging System                  :2024-01-13, 1d
    
    section Phase 4: n8n Integration
    n8n Setup                       :2024-01-14, 1d
    Workflow Creation               :2024-01-15, 2d
    Testing & Optimization          :2024-01-17, 1d
    
    section Phase 5: Production
    Security Hardening              :2024-01-18, 1d
    Performance Optimization        :2024-01-19, 1d
    Monitoring Setup                :2024-01-20, 1d
    Documentation                   :2024-01-21, 1d
```

---

## 8. Component Interaction Sequence

```mermaid
sequenceDiagram
    participant User
    participant MainScript
    participant Research
    participant ScriptWriter
    participant FactChecker
    participant ReviewGateway
    participant ComplianceChecker
    participant Voiceover
    participant ImageGen
    participant VideoGen
    participant Database
    
    User->>MainScript: Input Topic
    MainScript->>Research: research_topic(topic)
    Research->>Research: Call Perplexity API
    Research-->>MainScript: Return Research Data
    
    MainScript->>ScriptWriter: generate_script(research_data)
    ScriptWriter->>ScriptWriter: Call OpenAI API
    ScriptWriter-->>MainScript: Return Script JSON
    
    MainScript->>FactChecker: fact_check_script(script, research_data)
    FactChecker->>FactChecker: Compare claims vs research
    FactChecker-->>MainScript: Return Fact-Check Report
    
    MainScript->>ReviewGateway: submit_for_review(script, fact_report)
    ReviewGateway-->>MainScript: Wait for Human Approval
    Note over ReviewGateway: Human reviews script<br/>and visual prompts
    ReviewGateway-->>MainScript: Return Approval Status
    
    MainScript->>ComplianceChecker: check_compliance(script, metadata)
    ComplianceChecker->>ComplianceChecker: Check Fair Use, AI Disclosure
    ComplianceChecker-->>MainScript: Return Compliance Report
    
    MainScript->>Voiceover: generate_voiceover(script)
    Voiceover->>Voiceover: Call ElevenLabs API
    Voiceover-->>MainScript: Return Audio Files
    
    MainScript->>ImageGen: generate_images(script)
    ImageGen->>ImageGen: Call DALL-E API
    ImageGen-->>MainScript: Return Image Files
    
    MainScript->>VideoGen: generate_video(script, audio, images)
    VideoGen->>VideoGen: Build Creatomate Payload
    VideoGen->>VideoGen: Call Creatomate API
    VideoGen->>VideoGen: Poll Render Status
    VideoGen-->>MainScript: Return Video URL
    
    MainScript->>VideoGen: generate_video(script, audio, images)
    VideoGen->>VideoGen: Build Creatomate Payload
    VideoGen->>VideoGen: Call Creatomate API
    VideoGen->>VideoGen: Poll Render Status
    VideoGen-->>MainScript: Return Video URL
    
    MainScript->>VideoGen: download_video(video_url)
    VideoGen-->>MainScript: Return Video File Path
    
    MainScript->>YouTubeUploader: upload_to_youtube(video_path, metadata)
    YouTubeUploader->>YouTubeUploader: Authenticate with OAuth
    YouTubeUploader->>YouTubeUploader: Generate Metadata
    YouTubeUploader->>YouTubeUploader: Upload Video (Resumable)
    YouTubeUploader->>YouTubeUploader: Set Altered Content Flag
    YouTubeUploader-->>MainScript: Return YouTube Video ID & URL
    
    MainScript->>Database: Save Video Metadata
    MainScript->>Database: Save YouTube Video Info
    MainScript-->>User: Return Video File & YouTube URL
```

---

## 9. Decision Tree for Workflow Execution

```mermaid
graph TD
    START([Start Workflow]) --> CHECK_ENV{Environment<br/>Configured?}
    
    CHECK_ENV -->|No| SETUP_ENV[Run Setup Phase]
    SETUP_ENV --> CHECK_ENV
    CHECK_ENV -->|Yes| CHECK_APIS{All API Keys<br/>Valid?}
    
    CHECK_APIS -->|No| SETUP_APIS[Configure API Keys]
    SETUP_APIS --> CHECK_APIS
    CHECK_APIS -->|Yes| INPUT_TOPIC[Get Video Topic]
    
    INPUT_TOPIC --> VALIDATE_TOPIC{Topic Valid?}
    VALIDATE_TOPIC -->|No| INPUT_TOPIC
    VALIDATE_TOPIC -->|Yes| MODE{Execution Mode?}
    
    MODE -->|Python Script| PYTHON_FLOW[Run Python Pipeline]
    MODE -->|n8n Workflow| N8N_FLOW[Trigger n8n Workflow]
    
    PYTHON_FLOW --> EXECUTE_STEPS[Execute All Steps]
    N8N_FLOW --> EXECUTE_STEPS
    
    EXECUTE_STEPS --> CHECK_SUCCESS{All Steps<br/>Successful?}
    
    CHECK_SUCCESS -->|Yes| SAVE_RESULTS[Save Results]
    CHECK_SUCCESS -->|No| HANDLE_ERROR[Error Handling]
    
    HANDLE_ERROR --> RETRY{Retry<br/>Available?}
    RETRY -->|Yes| EXECUTE_STEPS
    RETRY -->|No| LOG_ERROR[Log Error]
    LOG_ERROR --> NOTIFY[Send Notification]
    
    SAVE_RESULTS --> CLEANUP[Cleanup Temp Files]
    NOTIFY --> CLEANUP
    CLEANUP --> END([End Workflow])
    
    style START fill:#90EE90
    style END fill:#90EE90
    style HANDLE_ERROR fill:#FFB6C1
    style LOG_ERROR fill:#FFB6C1
    style CHECK_ENV fill:#FFD700
    style CHECK_APIS fill:#FFD700
    style VALIDATE_TOPIC fill:#FFD700
```

---

## 10. Cost Flow Diagram (Optimized)

```mermaid
flowchart TD
    START([Workflow Start]) --> RESEARCH[Research Step]
    RESEARCH -->|Perplexity API| COST1[Cost: $0.05-0.15]
    
    COST1 --> PARSE[Research Parsing]
    PARSE -->|GPT-4o-mini<br/>80% savings| COST1A[Cost: $0.02-0.06]
    
    COST1A --> SCRIPT[Script Generation]
    SCRIPT -->|GPT-4o<br/>Final Polish| COST2[Cost: $0.05-0.15]
    
    COST2 --> METADATA[Metadata Generation]
    METADATA -->|GPT-4o-mini<br/>80% savings| COST2A[Cost: $0.01-0.03]
    
    COST2A --> VOICE[Voiceover Generation]
    VOICE -->|ElevenLabs Turbo<br/>30-40% savings| COST3[Cost: $0.12-0.30]
    
    COST3 --> IMAGES[Image Generation]
    IMAGES -->|DALL-E API| COST4[Cost: $0.10-0.20]
    
    COST4 --> VIDEO[Video Generation]
    VIDEO -->|Creatomate API| COST5[Cost: $0.10-0.30]
    
    COST5 --> STORAGE[Storage Assets]
    STORAGE -->|TTL Policy<br/>70% savings| COST6[Cost: $0.003-0.015]
    
    COST6 --> TOTAL[Total Optimized Cost<br/>$0.35-0.90 per video<br/>Savings: 27-31%]
    
    TOTAL --> TRACK[Track in Database]
    TRACK --> BUDGET_CHECK{Budget Check}
    
    BUDGET_CHECK -->|Daily Limit| CHECK_DAILY{Daily Budget<br/>Exceeded?}
    BUDGET_CHECK -->|Monthly Limit| CHECK_MONTHLY{Monthly Budget<br/>Exceeded?}
    BUDGET_CHECK -->|Per Video Limit| CHECK_VIDEO{Per Video Limit<br/>Exceeded?}
    
    CHECK_DAILY -->|Yes| ALERT_DAILY[Alert & Pause]
    CHECK_MONTHLY -->|Yes| ALERT_MONTHLY[Alert & Pause]
    CHECK_VIDEO -->|Yes| ALERT_VIDEO[Alert & Reject]
    
    CHECK_DAILY -->|No| CONTINUE[Continue]
    CHECK_MONTHLY -->|No| CONTINUE
    CHECK_VIDEO -->|No| CONTINUE
    
    ALERT_DAILY --> STOP[Stop Workflow]
    ALERT_MONTHLY --> STOP
    ALERT_VIDEO --> STOP
    
    CONTINUE --> CLEANUP[TTL Cleanup Job<br/>Delete assets after 48h]
    CLEANUP --> END([End])
    STOP --> END
    
    style START fill:#90EE90
    style END fill:#90EE90
    style TOTAL fill:#FFD700
    style STOP fill:#FFB6C1
    style ALERT_DAILY fill:#FFB6C1
    style ALERT_MONTHLY fill:#FFB6C1
    style ALERT_VIDEO fill:#FFB6C1
    style COST1 fill:#E6F3FF
    style COST1A fill:#90EE90
    style COST2 fill:#E6F3FF
    style COST2A fill:#90EE90
    style COST3 fill:#90EE90
    style COST4 fill:#E6F3FF
    style COST5 fill:#E6F3FF
    style COST6 fill:#90EE90
    style CLEANUP fill:#FFE4B5
```

---

## 11. Cost Optimization Strategy Diagram

```mermaid
graph TB
    subgraph "LLM Cost Optimization"
        A1[Research Parsing] -->|GPT-4o-mini| A2[80% Cost Reduction<br/>$0.02-0.06 vs $0.10-0.30]
        A3[Metadata Generation] -->|GPT-4o-mini| A4[80% Cost Reduction<br/>$0.01-0.03 vs $0.05-0.15]
        A5[Script Polish] -->|GPT-4o| A6[Final Quality Step<br/>$0.05-0.15]
    end
    
    subgraph "Voiceover Optimization"
        B1[Standard Model] -->|$0.20-0.50| B2[High Quality]
        B3[Turbo Model] -->|$0.12-0.30| B4[30-40% Savings<br/>Minimal Quality Loss]
    end
    
    subgraph "Storage Optimization"
        C1[Raw Assets Stored] -->|No TTL| C2[Growing Storage Costs<br/>$0.01-0.05/video]
        C3[TTL Policy<br/>48h after upload] -->|Auto-delete| C4[70% Storage Savings<br/>$0.003-0.015/video]
    end
    
    subgraph "Financial Controls"
        D1[Cost Tracking] --> D2[Per Video Limit]
        D1 --> D3[Daily Budget]
        D1 --> D4[Monthly Budget]
        D2 --> D5[Auto-Reject if Exceeded]
        D3 --> D6[Auto-Pause at Limit]
        D4 --> D7[Auto-Pause at Limit]
    end
    
    style A2 fill:#90EE90
    style A4 fill:#90EE90
    style B4 fill:#90EE90
    style C4 fill:#90EE90
    style D5 fill:#FFB6C1
    style D6 fill:#FFB6C1
    style D7 fill:#FFB6C1
```

---

## How to View These Diagrams

### In Markdown Viewers
- **GitHub**: Automatically renders Mermaid diagrams
- **VS Code**: Install "Markdown Preview Mermaid Support" extension
- **GitLab**: Native support for Mermaid
- **Notion**: Supports Mermaid diagrams

### Online Viewers
- **Mermaid Live Editor**: https://mermaid.live/
- Copy any diagram code and paste it into the editor

### Export Options
- Use Mermaid CLI to export as PNG/SVG
- Use online tools to convert to images
- Some IDEs can export diagrams directly

---

## Diagram Legend

### Colors Used
- 🟢 **Green**: Start/End points, Success states
- 🔵 **Blue**: Input/Output data, Information
- 🟡 **Yellow**: Processing steps, Important nodes
- 🟠 **Orange**: External services, APIs
- 🔴 **Red**: Error states, Failures

### Node Types
- **Rectangle**: Process/Step
- **Diamond**: Decision point
- **Rounded Rectangle**: Start/End
- **Cylinder**: Database
- **Parallelogram**: Input/Output

---

## Notes

- All diagrams are interactive in supported viewers
- Diagrams can be customized by editing the Mermaid code
- Use these as reference when building the actual workflow
- Update diagrams as the workflow evolves
