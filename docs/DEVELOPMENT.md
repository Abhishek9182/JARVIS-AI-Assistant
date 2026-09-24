\# J.A.R.V.I.S. Development Guide



1\. Development Environment

==========================

The project is developed on Windows using:



\- Python

\- Python virtual environment

\- VS Code

\- PowerShell

\- Node.js and npm

\- React

\- Vite

\- Flask

\- Ollama



Project location:



```text

C:\\Users\\Reddy Prizee\\Desktop\\JARVIS











2\. Project Structure

====================

The main project is organized into backend, frontend, core modules, and documentation.



JARVIS/

│

├── core/

│   ├── actions.py

│   ├── agent.py

│   ├── brain.py

│   ├── tts.py

│   ├── voice.py

│   ├── voice\_service.py

│   └── wake\_word.py

│

├── frontend/

│   ├── src/

│   ├── public/

│   ├── package.json

│   └── vite.config.js

│

├── docs/

│   ├── INSTALLATION.md

│   ├── ARCHITECTURE.md

│   ├── VOICE\_COMMANDS.md

│   └── DEVELOPMENT.md

│

├── api.py

├── main.py

├── requirements.txt

├── README.md

└── .gitignore









3\. Python Virtual Environment

=============================

The project uses a Python virtual environment.



Activate it from PowerShell:



.venv\\Scripts\\Activate.ps1



When the environment is active, PowerShell displays:



(.venv)



before the command prompt.









4\. Backend Development

======================

The Python backend contains the J.A.R.V.I.S. AI and voice systems.



The main API server is:



api.py



Start it with:



python api.py



The API runs on:



http://127.0.0.1:5001

5\. API Endpoints

System Status

GET /api/status



Returns the current J.A.R.V.I.S. API status.



Text Command

POST /api/command



Example request:



{

&#x20; "command": "Hello Jarvis"

}

Start Voice Service

POST /api/voice/start

Stop Voice Service

POST /api/voice/stop

Voice Status

GET /api/voice/status









6\. Frontend Development

=======================

The frontend is built using React and Vite.



Move into the frontend directory:



cd frontend



Start the development server:



npm run dev



The Vite development server currently uses:



http://localhost:5174/



The exact port can change if the configured port is already in use.











7\. Frontend Dependencies

========================

The frontend uses:



React

Vite

Three.js

React Three Fiber

Drei

GSAP

Lucide React

Web Audio API



Three.js and React Three Fiber are used for the J.A.R.V.I.S. 3D HUD.



GSAP is used for animation.



Lucide React provides interface icons.



The Web Audio API is used for browser microphone audio visualization.











8\. Backend Architecture

=======================

The backend follows this general flow:



API Request

&#x20;   ↓

JarvisAgent

&#x20;   ↓

PC Actions

&#x20;   ↓

Wikipedia

&#x20;   ↓

Web Search

&#x20;   ↓

Ollama



For voice operation:



Wake Word

&#x20;   ↓

Voice Recognition

&#x20;   ↓

JarvisAgent

&#x20;   ↓

Response

&#x20;   ↓

Text-to-Speech









9\. Ollama Development

=====================

J.A.R.V.I.S. currently uses the local Ollama model:



llama3.2:3b



The model is accessed through:



import ollama



The AI logic is implemented in:



core/brain.py



The system prompt instructs J.A.R.V.I.S. to provide concise responses.



The current configuration also limits the number of generated tokens for faster responses.











10\. Voice Development

=====================

Voice recognition is implemented in:



core/voice.py



The wake-word system is implemented in:



core/wake\_word.py



The voice service is implemented in:



core/voice\_service.py



Text-to-speech is implemented in:



core/tts.py



The voice pipeline uses:



OpenWakeWord

&#x20;   ↓

Faster-Whisper

&#x20;   ↓

JarvisAgent

&#x20;   ↓

Ollama / Tools

&#x20;   ↓

pyttsx3









11\. Agent Development

=====================

The main agent logic is implemented in:



core/agent.py



The agent determines how a command should be processed.



The current processing order is:



1\. PC Actions

2\. Wikipedia

3\. Web Search

4\. Ollama



This allows tool-based processing before falling back to the local language model.











12\. Making Changes

==================

Before modifying the project:



Activate the virtual environment.

Make the required code change.

Run the affected component.

Test the functionality.

Check the terminal for errors.

Test the frontend if the backend API was changed.

Test the backend if the frontend API integration was changed.









13\. Backend Testing

===================

Start the API server:



python api.py



Then test the API from another PowerShell terminal.



Example:



Invoke-RestMethod -Uri "http://127.0.0.1:5001/api/status"



For a command:



Invoke-RestMethod `

&#x20; -Uri "http://127.0.0.1:5001/api/command" `

&#x20; -Method POST `

&#x20; -ContentType "application/json" `

&#x20; -Body '{"command":"Hello Jarvis"}'









14\. Frontend and Backend Testing

================================

For full development:



Terminal 1 — Backend

cd C:\\Users\\Reddy Prizee\\Desktop\\JARVIS

.venv\\Scripts\\Activate.ps1

python api.py

Terminal 2 — Frontend

cd C:\\Users\\Reddy Prizee\\Desktop\\JARVIS\\frontend

npm run dev



Then open:



http://localhost:5174/



The frontend communicates with the Flask API running on:



http://127.0.0.1:5001









15\. Git Development Workflow

============================

Check the current repository status:



git status



Review changes before committing.



Stage changes:



git add .



Create a commit:



git commit -m "Describe the change"



Push changes to GitHub:



git push



The project repository is:



https://github.com/Abhishek9182/JARVIS-AI-Assistant









16\. Recommended Commit Style

============================

Use short and descriptive commit messages.



Examples:



Add voice command documentation

Improve Jarvis voice service

Update frontend HUD

Fix API CORS configuration

Optimize Ollama response









17\. Debugging

==============

When something does not work:



Step 1



Read the terminal error carefully.



Step 2



Identify which component produced the error:



Frontend

Backend

Voice

Wake Word

Whisper

Ollama

Agent

API

Step 3



Test that component separately.



Step 4



Fix the smallest affected component first.



Step 5



Run the complete system again.



Avoid changing multiple unrelated components at the same time.











18\. Development Principle

=========================

J.A.R.V.I.S. is being developed as a modular system.



Each major subsystem should have a separate responsibility:



Wake Word

&#x20;   → Detect activation



Voice Recognition

&#x20;   → Convert speech to text



Agent

&#x20;   → Select the appropriate tool



Actions

&#x20;   → Perform supported PC actions



Wikipedia

&#x20;   → Retrieve encyclopedia information



Web Search

&#x20;   → Retrieve web-search results



Ollama

&#x20;   → Generate AI responses



Text-to-Speech

&#x20;   → Speak responses



Flask API

&#x20;   → Connect frontend and backend



React HUD

&#x20;   → Provide the visual interface



Keeping these responsibilities separated makes the system easier to debug, extend, and maintain.

