from flask import Flask, request, jsonify
from flask_cors import CORS

from core.brain import JarvisBrain
from core.agent import JarvisAgent


app = Flask(__name__)

# Allow the local frontend during development.
# We will add the Vercel URL after the frontend is deployed.
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
# HEALTH / STATUS
# ==============================

@app.get("/api/status")
def status():

    return jsonify({
        "status": "online",
        "core": "online",
        "ai_engine": "active",
        "voice": "cloud_disabled"
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
    print("CLOUD COMMAND:", text)


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
# START SERVER
# ==============================

if __name__ == "__main__":

    import os

    port = int(os.environ.get("PORT", 5001))

    print("=" * 50)
    print("       J.A.R.V.I.S CLOUD API")
    print("=" * 50)
    print(f"API PORT: {port}")
    print("=" * 50)

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )
@app.get('/api/debug/routes')
def debug_routes():
    return jsonify({'routes': [str(rule) for rule in app.url_map.iter_rules()]})

