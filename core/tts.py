import pyttsx3


class JarvisVoice:

    def __init__(self):
        self.engine = pyttsx3.init()

        self.engine.setProperty(
            "rate",
            150
        )

    def speak(self, text):
        print("JARVIS:", text)

        self.engine.say(text)
        self.engine.runAndWait()


if __name__ == "__main__":
    jarvis = JarvisVoice()

    jarvis.speak(
        "Hello sir. JARVIS voice system is online."
    )

