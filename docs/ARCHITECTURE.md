\# J.A.R.V.I.S Architecture



This document explains how the main components of J.A.R.V.I.S communicate with each other.



\---



\## 1. High-Level Architecture



```text

&#x20;                        J.A.R.V.I.S

&#x20;                             |

&#x20;             +---------------+---------------+

&#x20;             |                               |

&#x20;             v                               v

&#x20;      React + Vite HUD                 Voice Interface

&#x20;             |                               |

&#x20;             | HTTP API                      |

&#x20;             v                               v

&#x20;       Flask API                       Microphone

&#x20;         api.py                             |

&#x20;             |                              v

&#x20;             |                       OpenWakeWord

&#x20;             |                              |

&#x20;             |                         "Hey Jarvis"

&#x20;             |                              |

&#x20;             |                              v

&#x20;             |                       Faster-Whisper

&#x20;             |                              |

&#x20;             +---------------+--------------+

&#x20;                             |

&#x20;                             v

&#x20;                       JarvisAgent

&#x20;                        agent.py

&#x20;                             |

&#x20;               +-------------+-------------+

&#x20;               |             |             |

&#x20;               v             v             v

&#x20;          PC Actions     Wikipedia     Web Search

&#x20;               |             |             |

&#x20;               +-------------+-------------+

&#x20;                             |

&#x20;                             v

&#x20;                          Ollama

&#x20;                        llama3.2:3b

&#x20;                             |

&#x20;                             v

&#x20;                        AI Response

&#x20;                             |

&#x20;                             v

&#x20;                          pyttsx3

&#x20;                             |

&#x20;                             v

&#x20;                       Voice Response











2\. Main Components

==================

2.1 React Frontend



Location:



frontend/



The frontend provides the graphical J.A.R.V.I.S interface.



Main technologies:



React

Vite

Three.js

React Three Fiber

Drei

GSAP

Lucide React

Web Audio API



The HUD displays the current state of the assistant and provides a command interface.



The frontend communicates with the Python backend through the Flask API.











3\. Flask API

============

File:



api.py



The Flask API acts as the communication layer between the React frontend and the Python J.A.R.V.I.S backend.



Main endpoints:



GET  /api/status

POST /api/command

POST /api/voice/start

POST /api/voice/stop

GET  /api/voice/status

Command flow

React Frontend

&#x20;     |

&#x20;     | POST /api/command

&#x20;     v

&#x20;   Flask

&#x20;     |

&#x20;     v

&#x20;JarvisAgent

&#x20;     |

&#x20;     v

&#x20;  Response

&#x20;     |

&#x20;     v

&#x20;React HUD











4\. JarvisAgent

==============

File:



core/agent.py



JarvisAgent is responsible for routing user requests to the appropriate tool.



The current routing sequence is:



User Command

&#x20;    |

&#x20;    v

PC Action?

&#x20;    |

&#x20;  Yes ─────────> Execute PC Action

&#x20;    |

&#x20;   No

&#x20;    |

&#x20;    v

Wikipedia Query?

&#x20;    |

&#x20;  Yes ─────────> Wikipedia

&#x20;    |

&#x20;   No

&#x20;    |

&#x20;    v

Web Search Query?

&#x20;    |

&#x20;  Yes ─────────> DuckDuckGo

&#x20;    |

&#x20;   No

&#x20;    |

&#x20;    v

Ollama



This allows specific requests to be handled by specialized tools before falling back to the local language model.











5\. Local AI Brain

=================

File:



core/brain.py



The J.A.R.V.I.S brain uses Ollama as the local AI interface.



Current model:



llama3.2:3b



The brain sends the user's request and recent conversation context to Ollama.



User Input

&#x20;   |

&#x20;   v

JarvisBrain

&#x20;   |

&#x20;   v

Ollama

&#x20;   |

&#x20;   v

llama3.2:3b

&#x20;   |

&#x20;   v

AI Response



The current implementation limits normal responses to keep the assistant responsive.











6\. Voice Pipeline

=================

The voice system consists of several stages.



Microphone

&#x20;   |

&#x20;   v

OpenWakeWord

&#x20;   |

&#x20;   | "Hey Jarvis"

&#x20;   v

VoiceRecognizer

&#x20;   |

&#x20;   v

Faster-Whisper

&#x20;   |

&#x20;   | Speech → Text

&#x20;   v

JarvisAgent

&#x20;   |

&#x20;   v

Response

&#x20;   |

&#x20;   v

pyttsx3

&#x20;   |

&#x20;   v

Speaker











7\. Wake-Word Detection

======================

File:



core/wake\_word.py



The wake-word system uses OpenWakeWord.



The configured wake phrase is:



Hey Jarvis



The microphone audio is continuously analyzed while the voice service is waiting.



When the wake-word score reaches the configured threshold, J.A.R.V.I.S. activates the voice-command stage.



The project uses the OpenWakeWord model:



hey\_jarvis\_v0.1.onnx











8\. Speech Recognition

======================

File:



core/voice.py



The voice recognizer uses Faster-Whisper.



Current configuration:



Model: tiny

Device: CPU

Compute type: int8

Sample rate: 16000 Hz



The recognizer waits for speech, records the command, detects silence and sends the recorded audio to Faster-Whisper.



Microphone

&#x20;   |

&#x20;   v

Audio Stream

&#x20;   |

&#x20;   v

Speech Detection

&#x20;   |

&#x20;   v

Recording

&#x20;   |

&#x20;   v

Faster-Whisper

&#x20;   |

&#x20;   v

Text Command











9\. Text-to-Speech

=================

File:



core/tts.py



J.A.R.V.I.S. uses pyttsx3 to convert the generated response into speech.



AI Response

&#x20;    |

&#x20;    v

&#x20; pyttsx3

&#x20;    |

&#x20;    v

Computer Speaker



The current voice rate is configured in the TTS component.











10\. Voice Service

=================

File:



core/voice\_service.py



VoiceService connects the wake-word detector, speech recognizer, agent and TTS system into a background process.



Its main states are:



IDLE

LISTENING

THINKING

RESPONDING

ERROR



The general flow is:



IDLE

&#x20;|

&#x20;| Hey Jarvis

&#x20;v

LISTENING

&#x20;|

&#x20;| Voice command

&#x20;v

THINKING

&#x20;|

&#x20;| Agent processing

&#x20;v

RESPONDING

&#x20;|

&#x20;| Speech completed

&#x20;v

IDLE











11\. PC Actions

==============

File:



core/actions.py



The PC action layer handles commands that can be executed directly on the computer.



The agent checks for an available PC action before moving to information-search or AI processing.



This makes it possible for natural-language commands to trigger supported computer operations.











12\. Web Search

==============

File:



core/agent.py



DuckDuckGo search is used for requests that match the configured search keywords.



Examples include requests containing terms such as:



search

latest

news

weather



The agent returns a small set of search-result titles to the user.











13\. Wikipedia

=============

File:



core/agent.py



Wikipedia is used for requests beginning with supported patterns such as:



What is ...

Who is ...

Define ...



The agent requests a short Wikipedia summary and returns the result.









14\. Mobile Control

==================

Directory:



mobile/



The mobile component uses Flask to provide a browser-based control interface.



Structure:



mobile/

├── app.py

└── templates/

&#x20;   └── index.html



The mobile server can listen on:



0.0.0.0:5000



This allows devices on the same network to communicate with the Flask mobile interface when network and firewall settings permit it.









15\. Frontend System States

==========================

The React HUD uses system states to control the visual behavior of the interface.



Current states include:



IDLE

LISTENING

THINKING

RESPONDING

EXECUTING

ERROR



The 3D core, particle system and interface indicators can react to these states.



For example:



IDLE

&#x20;   ↓

LISTENING

&#x20;   ↓

THINKING

&#x20;   ↓

EXECUTING

&#x20;   ↓

RESPONDING

&#x20;   ↓

IDLE









16\. Complete Command Flow

=========================

A command entered through the frontend follows this general process:



User

&#x20;|

&#x20;v

React HUD

&#x20;|

&#x20;| POST /api/command

&#x20;v

Flask API

&#x20;|

&#x20;v

JarvisAgent

&#x20;|

&#x20;+----> PC Action

&#x20;|

&#x20;+----> Wikipedia

&#x20;|

&#x20;+----> Web Search

&#x20;|

&#x20;+----> Ollama

&#x20;         |

&#x20;         v

&#x20;      AI Reply

&#x20;         |

&#x20;         v

&#x20;     Flask API

&#x20;         |

&#x20;         v

&#x20;     React HUD











17\. Complete Voice Flow

=======================

A voice command follows this process:



User

&#x20;|

&#x20;| "Hey Jarvis"

&#x20;v

Microphone

&#x20;|

&#x20;v

OpenWakeWord

&#x20;|

&#x20;| Wake detected

&#x20;v

VoiceRecognizer

&#x20;|

&#x20;v

Faster-Whisper

&#x20;|

&#x20;| Text

&#x20;v

JarvisAgent

&#x20;|

&#x20;+----> PC Action

&#x20;|

&#x20;+----> Wikipedia

&#x20;|

&#x20;+----> Web Search

&#x20;|

&#x20;+----> Ollama

&#x20;         |

&#x20;         v

&#x20;      Response

&#x20;         |

&#x20;         v

&#x20;      pyttsx3

&#x20;         |

&#x20;         v

&#x20;      Speaker











18\. Project Architecture Summary

================================

J.A.R.V.I.S. is divided into several logical layers:



Presentation Layer

&#x20;       |

&#x20;       v

React + Three.js HUD

&#x20;       |

&#x20;       v

API Layer

&#x20;       |

&#x20;       v

Flask

&#x20;       |

&#x20;       v

Agent Layer

&#x20;       |

&#x20;       v

JarvisAgent

&#x20;       |

&#x20;       +-------------------+

&#x20;       |                   |

&#x20;       v                   v

Tool Layer             AI Layer

&#x20;       |                   |

&#x20;       v                   v

Actions/Search        Ollama

&#x20;       |                   |

&#x20;       +---------+---------+

&#x20;                 |

&#x20;                 v

&#x20;            Response

&#x20;                 |

&#x20;                 v

&#x20;         Voice / Frontend



This separation allows the frontend, voice interface, agent logic and AI engine to be developed independently.









19\. Future Architecture

=======================

Future versions can extend the architecture with:



Persistent memory

More desktop automation

Streaming AI responses

Vision capabilities

Additional AI models

More advanced task execution

Authentication

Secure remote access

More advanced 3D HUD components

Custom J.A.R.V.I.S. voice

Long-running background automation



The architecture is intentionally modular so these components can be added without replacing the entire system.





