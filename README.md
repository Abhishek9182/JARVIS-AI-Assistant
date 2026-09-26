# 🤖 J.A.R.V.I.S. — AI Voice Assistant & Automation System

> An end-to-end AI voice assistant that combines voice recognition, wake-word detection, local LLM processing, computer automation, web search, and an interactive React-based HUD.

J.A.R.V.I.S. is a personal AI assistant built with **Python, React, Flask, Faster-Whisper, OpenWakeWord and Ollama**.

The system can listen for the wake phrase **"Hey Jarvis"**, convert speech into text, process the request through an intelligent agent, execute supported computer actions or information searches, and respond using voice.

---

## ✨ Features

- 🎙️ **Wake-word detection** using OpenWakeWord
- 🗣️ **Speech-to-text** using Faster-Whisper
- 🧠 **Local AI processing** using Ollama and `llama3.2:3b`
- 🤖 **Intelligent command routing** using JarvisAgent
- 💻 **Computer automation** through supported PC actions
- 🌐 **Web search** integration
- 📚 **Wikipedia information retrieval**
- 🔊 **Text-to-speech** using pyttsx3
- 🖥️ **Interactive React HUD**
- 🎨 **3D interface** using Three.js / React Three Fiber
- 📱 **Mobile browser control interface**
- 🔌 **Flask REST API**
- ☁️ **Cloud API support**
- 🧪 **Testing utilities**
- ⚡ **Real-time assistant state visualization**

---

# 🏗️ System Architecture

```text
                         ┌─────────────────────┐
                         │       USER          │
                         │ Voice / Text Input  │
                         └──────────┬──────────┘
                                    │
                     ┌──────────────┴──────────────┐
                     │                             │
                     ▼                             ▼
              ┌──────────────┐             ┌──────────────┐
              │ React + Vite │             │ Microphone   │
              │    HUD       │             │              │
              └──────┬───────┘             └──────┬───────┘
                     │                            │
                     │ HTTP API                   ▼
                     │                    ┌─────────────────┐
                     │                    │ OpenWakeWord    │
                     │                    │ "Hey Jarvis"    │
                     │                    └────────┬────────┘
                     │                             │
                     │                             ▼
                     │                    ┌─────────────────┐
                     │                    │ Faster-Whisper  │
                     │                    │ Speech → Text   │
                     │                    └────────┬────────┘
                     │                             │
                     └──────────────┬──────────────┘
                                    ▼
                           ┌─────────────────┐
                           │   Flask API     │
                           │     api.py      │
                           └────────┬────────┘
                                    │
                                    ▼
                           ┌─────────────────┐
                           │   JarvisAgent   │
                           └────────┬────────┘
                                    │
                  ┌─────────────────┼─────────────────┐
                  │                 │                 │
                  ▼                 ▼                 ▼
           ┌─────────────┐   ┌─────────────┐   ┌─────────────┐
           │ PC Actions  │   │  Wikipedia  │   │ Web Search  │
           └─────────────┘   └─────────────┘   └─────────────┘
                                    │
                                    ▼
                           ┌─────────────────┐
                           │     Ollama      │
                           │   llama3.2:3b   │
                           └────────┬────────┘
                                    │
                                    ▼
                           ┌─────────────────┐
                           │   AI Response   │
                           └────────┬────────┘
                                    │
                                    ▼
                           ┌─────────────────┐
                           │     pyttsx3     │
                           │ Text → Speech   │
                           └────────┬────────┘
                                    │
                                    ▼
                           ┌─────────────────┐
                           │ Voice Response  │
                           └─────────────────┘

🔄 How J.A.R.V.I.S. Works
1. Wake Word Detection
The assistant continuously monitors the microphone for:
"Hey Jarvis"
OpenWakeWord detects the configured wake phrase and activates the voice-command pipeline.

2. Speech Recognition
After activation, the microphone captures the user's command.
Faster-Whisper converts:
Voice → Text

3. Command Processing
The transcribed command is passed to JarvisAgent.
The agent determines whether the request requires:
PC action
Wikipedia
Web search
Local AI processing

4. AI Processing
Requests that are not handled by specialized tools are passed to:
Ollama
   ↓
llama3.2:3b
   ↓
AI Response

5. Voice Response
The generated response is converted into speech using:
pyttsx3
The user then receives the response through the computer speaker.

🧠 AI Pipeline
User Voice
     ↓
OpenWakeWord
     ↓
Faster-Whisper
     ↓
JarvisAgent
     ↓
Tool Routing
     ↓
┌───────────────┬───────────────┬───────────────┐
│               │               │
PC Actions   Web Search     Wikipedia
│               │               │
└───────────────┴───────────────┘
                 ↓
             Ollama LLM
                 ↓
          llama3.2:3b
                 ↓
            AI Response
                 ↓
             pyttsx3
                 ↓
           Voice Output


🖥️ Frontend
The J.A.R.V.I.S. frontend is built using:
React
Vite
Three.js
React Three Fiber
Drei
GSAP
Lucide React
Web Audio API

The HUD represents different assistant states such as:

IDLE
  ↓
LISTENING
  ↓
THINKING
  ↓
EXECUTING
  ↓
RESPONDING
  ↓
IDLE
🔌 Backend API

The Flask backend provides communication between the frontend and the Python assistant.

Main endpoints
GET  /api/status
POST /api/command
POST /api/voice/start
POST /api/voice/stop
GET  /api/voice/status

Basic command flow:

React HUD
   ↓
POST /api/command
   ↓
Flask
   ↓
JarvisAgent
   ↓
Response
   ↓
React HUD

📁 Project Structure
JARVIS-AI-Assistant/
│
├── core/
│   ├── actions.py
│   ├── agent.py
│   ├── brain.py
│   ├── tts.py
│   ├── voice.py
│   ├── voice_service.py
│   └── wake_word.py
│
├── docs/
│   ├── ARCHITECTURE.md
│   ├── DEVELOPMENT.md
│   ├── INSTALLATION.md
│   └── VOICE_COMMANDS.md
│
├── frontend/
│
├── mobile/
│
├── ui/
│
├── api.py
├── api_cloud.py
├── main.py
│
├── requirements.txt
├── requirements-cloud.txt
│
├── test_agent.py
├── test_wake.py
│
├── .gitignore
└── README.md

🛠️ Technology Stack

Backend:
Python
Flask
REST API
AI / Speech
Ollama
Llama 3.2
Faster-Whisper
OpenWakeWord
pyttsx3

Frontend:
React
Vite
Three.js
React Three Fiber
Drei
GSAP
Lucide React
Web Audio API

Development:
Git
GitHub
VS Code
Postman

⚙️ Installation
Clone the repository:
git clone https://github.com/Abhishek9182/JARVIS-AI-Assistant.git

Move into the project:
cd JARVIS-AI-Assistant

Create a virtual environment:
python -m venv .venv

Activate it on Windows:
.venv\Scripts\Activate.ps1

Install Python dependencies:
pip install -r requirements.txt

Install and configure Ollama separately, then make sure the required model is available:
ollama run llama3.2:3b

Start the assistant:
python main.py

For frontend development:
cd frontend
npm install
npm run dev

Refer to docs/INSTALLATION.md for the detailed setup instructions.

🎤 Example Voice Commands
Examples supported by the current command-routing system include requests for:

"Hey Jarvis"

"Search for Python tutorials"

"What is machine learning?"

"Who is Alan Turing?"

"What's the latest news?"

"Open [supported application]"

"Execute [supported computer action]"

See:
docs/VOICE_COMMANDS.md
for the complete command documentation.

📚 Documentation

Detailed documentation is available in the docs/ directory.

Document               	Description
ARCHITECTURE.md	        System architecture and component communication
DEVELOPMENT.md         	Development workflow and project structure
INSTALLATION.md       	Installation and configuration
VOICE_COMMANDS.md     	Supported voice commands

🧪 Testing
The repository includes testing utilities for core assistant functionality.
python test_agent.py
python test_wake.py

🚀 Future Improvements
Planned areas for further development include:
Improved wake-word responsiveness
More computer automation capabilities
Better intent classification
Expanded tool integrations
More robust error handling
Improved conversation memory
Additional AI models
Enhanced mobile control
More advanced frontend animations
Improved deployment architecture

👨‍💻 Developer
Reddy Abhisheku
Python Full-Stack Developer | AI & Automation Enthusiast
GitHub:
https://github.com/Abhishek9182

⭐ If you find this project interesting, feel free to explore the source code and documentation.
