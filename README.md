\# J.A.R.V.I.S AI Assistant



J.A.R.V.I.S. (Just A Rather Very Intelligent System) is a personal AI desktop assistant built with Python and React.



\## Features



\- Voice commands

\- "Hey Jarvis" wake-word detection

\- Speech-to-text using Faster-Whisper

\- Text-to-speech using pyttsx3

\- Local AI using Ollama

\- PC automation

\- Wikipedia search

\- Web search

\- Flask API

\- React + Three.js futuristic HUD

\- Mobile control



\## Technology Stack



\### Backend

\- Python

\- Flask

\- Ollama

\- OpenWakeWord

\- Faster-Whisper

\- pyttsx3

\- NumPy

\- SoundDevice



\### Frontend

\- React

\- Vite

\- Three.js

\- React Three Fiber

\- Drei

\- GSAP

\- Lucide React



\## Project Structure



```text

JARVIS/

├── api.py

├── main.py

├── core/

├── frontend/

├── mobile/

└── ui/





Running the Backend

===================

Activate the virtual environment:

\---------------------------------

>.venv\\Scripts\\Activate.ps1



Start the API:

\-------------

>python api.py



The API runs on:

\----------------

http://127.0.0.1:5001





Running the Frontend

====================

Open another terminal:

\----------------------

>cd frontend

>npm install

>npm run dev

Then open the URL shown by Vite in your browser.



AI Model

========

J.A.R.V.I.S. uses Ollama with:

\------------------------------

llama3.2:3b



Install the model with:

\-----------------------

>ollama pull llama3.2:3b





Voice Pipeline

==============

Microphone

&#x20;   ↓

Hey Jarvis

&#x20;   ↓

OpenWakeWord

&#x20;   ↓

Faster-Whisper

&#x20;   ↓

Jarvis Agent

&#x20;   ↓

PC Actions / Web Search / Wikipedia / Ollama

&#x20;   ↓

pyttsx3

&#x20;   ↓

Voice Response





Author

======

Reddy Abhisheku



GitHub:

https://github.com/Abhishek9182



Project

https://github.com/Abhishek9182/JARVIS-AI-Assistant











