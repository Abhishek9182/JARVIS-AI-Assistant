import threading
import time

from core.voice import VoiceRecognizer
from core.tts import JarvisVoice
from core.wake_word import WakeWord
from core.agent import JarvisAgent


class VoiceService:

    def __init__(self, agent):

        self.agent = agent

        self.wake = WakeWord()
        self.voice = VoiceRecognizer()
        self.speaker = JarvisVoice()

        self.running = False
        self.thread = None

        self.state = "IDLE"
        self.last_command = ""
        self.last_reply = ""
        self.error = ""

    def start(self):

        if self.running:
            return

        self.running = True

        self.thread = threading.Thread(
            target=self._run,
            daemon=True
        )

        self.thread.start()

        print("VOICE SERVICE STARTED")

    def stop(self):

        self.running = False
        self.state = "IDLE"

        print("VOICE SERVICE STOPPED")

    def _run(self):

        while self.running:

            try:

                self.state = "IDLE"

                print()
                print("================================")
                print("JARVIS VOICE SERVICE")
                print("Waiting for: Hey Jarvis")
                print("================================")

                # Wait for wake word
                self.wake.wait()

                if not self.running:
                    break

                self.state = "LISTENING"

                print("WAKE WORD DETECTED")

                self.speaker.speak("Yes sir?")

                # Give Windows/Realtek a moment to release the speaker/audio resources
                time.sleep(0.3)

                # Listen for command
                text = self.voice.listen()

                if not self.running:
                    break

                if not text:
                    self.state = "IDLE"
                    continue

                self.last_command = text

                print("VOICE COMMAND:", text)

                # Process command
                self.state = "THINKING"

                reply = self.agent.process(text)

                if not reply:
                    reply = "I could not process that command, sir."

                self.last_reply = reply

                print("JARVIS REPLY:", reply)

                # Speak response
                self.state = "RESPONDING"

                self.speaker.speak(reply)

                self.state = "IDLE"

            except Exception as e:

                self.error = str(e)

                print("VOICE SERVICE ERROR:")
                print(e)

                self.state = "ERROR"

                time.sleep(1)

                self.state = "IDLE"


    def get_status(self):

        return {
            "running": self.running,
            "state": self.state,
            "last_command": self.last_command,
            "last_reply": self.last_reply,
            "error": self.error
        }