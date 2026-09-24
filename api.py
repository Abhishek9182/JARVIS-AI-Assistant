# from flask import Flask, request, jsonify
# from flask_cors import CORS

# from core.brain import JarvisBrain
# from core.agent import JarvisAgent


# app = Flask(__name__)

# CORS(
#     app,
#     resources={
#         r"/api/*": {
#             "origins": [
#                 "http://localhost:5173",
#                 "http://localhost:5174"
#             ]
#         }
#     }
# )


# # ========================================
# # JARVIS ENGINE
# # ========================================

# brain = JarvisBrain()
# agent = JarvisAgent(brain)


# # ========================================
# # STATUS
# # ========================================

# @app.get("/api/status")
# def status():

#     return jsonify({
#         "status": "online",
#         "core": "online",
#         "ai_engine": "active",
#         "voice": "ready"
#     })


# # ========================================
# # COMMAND
# # ========================================

# @app.post("/api/command")
# def command():

#     data = request.get_json(silent=True)

#     if not data:
#         return jsonify({
#             "success": False,
#             "error": "Invalid JSON request."
#         }), 400

#     text = data.get("command", "").strip()

#     if not text:
#         return jsonify({
#             "success": False,
#             "error": "No command provided."
#         }), 400

#     print("=" * 50)
#     print("FRONTEND COMMAND:", text)

#     try:

#         reply = agent.process(text)

#         print("JARVIS REPLY:", reply)

#         return jsonify({
#             "success": True,
#             "command": text,
#             "reply": reply
#         })

#     except Exception as e:

#         print("API ERROR:", e)

#         return jsonify({
#             "success": False,
#             "error": str(e)
#         }), 500


# # ========================================
# # START SERVER
# # ========================================

# if __name__ == "__main__":

#     print("=" * 50)
#     print("       J.A.R.V.I.S API SERVER")
#     print("=" * 50)
#     print("API: http://127.0.0.1:5001")
#     print("=" * 50)

#     app.run(
#         host="127.0.0.1",
#         port=5001,
#         debug=True
#     )

from flask import Flask, request, jsonify
from flask_cors import CORS

from core.brain import JarvisBrain
from core.agent import JarvisAgent
from core.voice_service import VoiceService


app = Flask(__name__)


CORS(
    app,
    resources={
        r"/api/*": {
            "origins": [
                "http://localhost:5173",
                "http://localhost:5174"
            ]
        }
    }
)


# ==============================
# JARVIS AI
# ==============================

brain = JarvisBrain()
agent = JarvisAgent(brain)


# ==============================
# VOICE SERVICE
# ==============================

voice_service = VoiceService(agent)


# ==============================
# SYSTEM STATUS
# ==============================

@app.get("/api/status")
def status():

    return jsonify({
        "status": "online",
        "core": "online",
        "ai_engine": "active",
        "voice": "ready"
    })


# ==============================
# TEXT COMMAND
# ==============================

@app.post("/api/command")
def command():

    data = request.get_json(silent=True)

    if not data:

        return jsonify({
            "success": False,
            "error": "Invalid JSON request."
        }), 400


    text = data.get("command", "").strip()


    if not text:

        return jsonify({
            "success": False,
            "error": "No command provided."
        }), 400


    print("=" * 50)
    print("FRONTEND COMMAND:", text)


    try:

        reply = agent.process(text)

        print("JARVIS REPLY:", reply)


        return jsonify({
            "success": True,
            "command": text,
            "reply": reply
        })


    except Exception as e:

        print("API ERROR:", e)


        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


# ==============================
# START VOICE
# ==============================

@app.post("/api/voice/start")
def start_voice():

    try:

        voice_service.start()

        return jsonify({
            "success": True,
            "message": "Voice service started."
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


# ==============================
# STOP VOICE
# ==============================

@app.post("/api/voice/stop")
def stop_voice():

    try:

        voice_service.stop()

        return jsonify({
            "success": True,
            "message": "Voice service stopped."
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


# ==============================
# VOICE STATUS
# ==============================

@app.get("/api/voice/status")
def voice_status():

    return jsonify(
        voice_service.get_status()
    )


# ==============================
# RUN SERVER
# ==============================

if __name__ == "__main__":

    print("=" * 50)
    print("       J.A.R.V.I.S API SERVER")
    print("=" * 50)
    print("API: http://127.0.0.1:5001")
    print("=" * 50)

    app.run(
        host="127.0.0.1",
        port=5001,
        debug=False
    )