from core.voice import VoiceRecognizer
from core.tts import JarvisVoice
from core.brain import JarvisBrain
from core.wake_word import WakeWord
from core.agent import JarvisAgent


def main():

    print("=" * 50)
    print("          J.A.R.V.I.S")
    print("        AI AGENT ONLINE")
    print("=" * 50)

    wake = WakeWord()
    voice = VoiceRecognizer()
    speaker = JarvisVoice()
    brain = JarvisBrain()

    agent = JarvisAgent(brain)

    speaker.speak(
        "JARVIS AI Agent is online."
    )

    while True:

        wake.wait()

        speaker.speak(
            "Yes sir?"
        )

        text = voice.listen()

        if not text:
            continue

        if text.lower() in [
            "shutdown jarvis",
            "exit",
            "quit"
        ]:
            speaker.speak(
                "Goodbye sir."
            )
            break

        try:

            reply = agent.process(text)

            speaker.speak(reply)

        except Exception as e:

            print("ERROR:", e)

            speaker.speak(
                "An error occurred, sir."
            )


if __name__ == "__main__":
    main()