J.A.R.V.I.S Installation Guide



This guide explains how to install and run the J.A.R.V.I.S AI Assistant on Windows.



\---



1\. Requirements

==================

Install these applications before starting:



\- Python

\- Node.js

\- Git

\- Ollama

\- VS Code

\- A working microphone



\---









2\. Clone the Repository

=======================

Open PowerShell and run:



```powershell

git clone https://github.com/Abhishek9182/JARVIS-AI-Assistant.git



Enter the project:



cd JARVIS-AI-Assistant









3\. Create Python Virtual Environment

====================================

Create the virtual environment:



python -m venv .venv



Activate it:



.venv\\Scripts\\Activate.ps1



The terminal should now look similar to:



(.venv) PS C:\\...\\JARVIS-AI-Assistant>

PowerShell Activation Error



If PowerShell prevents the activation script from running, use:



Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned



Then activate again:



.venv\\Scripts\\Activate.ps1









4\. Install Python Dependencies

==============================

With the virtual environment activated:



pip install -r requirements.txt



This installs the Python packages required by the project.



Important packages include:



Flask

Flask-CORS

NumPy

SoundDevice

pyttsx3

Ollama

OpenWakeWord

Faster-Whisper

ONNX Runtime

Wikipedia

DuckDuckGo Search









5\. Install Ollama

=================

Install Ollama for Windows.



After installation, verify that Ollama is available:



ollama --version



Download the J.A.R.V.I.S AI model:



ollama pull llama3.2:3b



Test the model:



ollama run llama3.2:3b



When finished testing, exit Ollama with:



/bye









6\. Configure the Microphone

===========================

J.A.R.V.I.S uses the computer microphone for:



Wake-word detection

Voice command recording

Speech recognition



The current project uses a configured microphone device in:



core/wake\_word.py

core/voice.py



If the wrong microphone is selected, update the MIC\_DEVICE value in those files.









7\. Test the Microphone

======================

From the project root:



python core/test\_mic.py



Make sure the microphone receives audio correctly before testing the complete voice assistant.









8\. Test Wake-Word Detection

===========================

Run:



python test\_wake.py



The assistant should wait for:



Hey Jarvis



When the wake word is detected, the terminal should report the detection.









9\. Test the Agent

=================

Run:



python test\_agent.py



This checks the J.A.R.V.I.S agent and its command-routing logic.









10\. Start the J.A.R.V.I.S API

=============================

Open PowerShell in the project root.



Make sure the virtual environment is activated:



.venv\\Scripts\\Activate.ps1



Start the API:



python api.py



The server should start at:



http://127.0.0.1:5001



The API provides endpoints for:



GET  /api/status

POST /api/command

POST /api/voice/start

POST /api/voice/stop

GET  /api/voice/status







11\. Start the Voice Service

============================

With the API running, open another PowerShell window.



Activate the virtual environment:



.venv\\Scripts\\Activate.ps1



Start the voice service:



Invoke-RestMethod `

&#x20; -Uri "http://127.0.0.1:5001/api/voice/start" `

&#x20; -Method Post



J.A.R.V.I.S will then wait for:



Hey Jarvis



After the wake word is detected:



Hey Jarvis

&#x20;     ↓

Wake-word detection

&#x20;     ↓

Voice recording

&#x20;     ↓

Speech-to-text

&#x20;     ↓

JARVIS Agent

&#x20;     ↓

PC Action / Wikipedia / Web Search / Ollama

&#x20;     ↓

Voice response







12\. Start the React Frontend

============================

Open another terminal.



Navigate to the frontend:



cd frontend



Install Node.js dependencies:



npm install



Start the development server:



npm run dev



Vite will display a local URL, normally:



http://localhost:5173



If that port is already being used, Vite may select another port, such as:



http://localhost:5174



Open the displayed URL in your browser.







13\. Run the Complete System

============================

For the complete J.A.R.V.I.S setup, run:



Terminal 1 — Ollama



Make sure Ollama is running.



Terminal 2 — J.A.R.V.I.S API



From the project root:



python api.py

Terminal 3 — React Frontend

cd frontend

npm run dev



Then open the frontend URL shown by Vite.



Voice Service



Start the voice service through:



Invoke-RestMethod `

&#x20; -Uri "http://127.0.0.1:5001/api/voice/start" `

&#x20; -Method Post





14\. Basic Troubleshooting

=========================

Ollama is not responding



Check:

ollama list



Make sure:

llama3.2:3b



is installed.



Microphone is not working



Check the configured MIC\_DEVICE value in:



core/wake\_word.py

core/voice.py



Then run:



python core/test\_mic.py

Frontend cannot connect to the backend



Make sure the Flask API is running:



http://127.0.0.1:5001



Then check:



http://127.0.0.1:5001/api/status

Frontend port changes



Vite may use:



5173



or another available port such as:



5174



The Flask API CORS configuration must allow the frontend origin.



Wake word is not detected



Check:



Microphone permissions

Correct microphone device

Microphone input level

OpenWakeWord installation

Wake-word model availability



The project uses the hey\_jarvis\_v0.1.onnx wake-word model.





15\. Project Components

=======================

Component	        Purpose

\--------------------------------------------

api.py	                Flask API server

main.py	                Main voice-assistant loop

core/wake\_word.py	Wake-word detection

core/voice.py	        Speech recognition

core/tts.py	        Text-to-speech

core/brain.py	        Ollama AI interface

core/agent.py	        Command routing

core/actions.py  	PC automation

core/voice\_service.py	Background voice service

frontend/	        React + Three.js HUD

mobile/	                Mobile control interface

ui/	                Additional HUD interface





16\. Security

============

J.A.R.V.I.S can execute computer actions.



Do not expose the API publicly without adding appropriate security controls.



Before deploying outside your local computer/network:



Add authentication.

Restrict CORS origins.

Validate commands.

Protect system-level actions.

Never commit passwords or API keys.

Keep .env files out of Git.

17\. Development



J.A.R.V.I.S is an active development project.





Future improvements may include:



More PC automation

Faster voice responses

Better wake-word detection

Streaming AI responses

Persistent memory

More advanced 3D HUD effects

More mobile controls

Authentication

Additional AI tools

