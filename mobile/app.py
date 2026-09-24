from flask import Flask, render_template, jsonify
import subprocess
import pyttsx3
import threading


app = Flask(__name__)

engine = pyttsx3.init()
engine.setProperty(
    "rate",
    150
)


def speak(text):

    engine.say(text)
    engine.runAndWait()


@app.route("/")
def home():

    return render_template(
        "index.html"
    )


@app.route("/command/<action>")
def command(action):

    reply = ""

    if action == "youtube":

        subprocess.Popen(
            "explorer https://www.youtube.com",
            shell=True
        )

        reply = "Opening YouTube, sir."

    elif action == "google":

        subprocess.Popen(
            "explorer https://www.google.com",
            shell=True
        )

        reply = "Opening Google, sir."

    elif action == "calculator":

        subprocess.Popen(
            "calc.exe"
        )

        reply = "Opening Calculator, sir."

    else:

        reply = "Unknown command."

    threading.Thread(
        target=speak,
        args=(reply,)
    ).start()

    return jsonify({
        "status": "success",
        "reply": reply
    })


if __name__ == "__main__":

    print(
        "JARVIS MOBILE SERVER RUNNING"
    )

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )