# import sounddevice as sd
# import numpy as np
# from faster_whisper import WhisperModel


# class VoiceRecognizer:

#     MIC_DEVICE = 2
#     SAMPLE_RATE = 16000

#     def __init__(self):

#         print("Loading Whisper model...")

#         self.model = WhisperModel(
#             "tiny",
#             device="cpu",
#             compute_type="int8"
#         )

#         print("Whisper ready.")

#         device = sd.query_devices(self.MIC_DEVICE)

#         print(f"Microphone: {device['name']}")
#         print(f"Sample rate: {self.SAMPLE_RATE} Hz")

#     def listen(self, duration=5):

#         print("Listening...")

#         try:

#             audio = sd.rec(
#                 int(duration * self.SAMPLE_RATE),
#                 samplerate=self.SAMPLE_RATE,
#                 channels=1,
#                 dtype="float32",
#                 device=self.MIC_DEVICE
#             )

#             sd.wait()

#             audio = audio.flatten()

#             volume = np.max(np.abs(audio))

#             print(f"Audio level: {volume:.4f}")

#             if volume < 0.01:

#                 print("Audio too quiet.")

#                 return ""

#             segments, info = self.model.transcribe(
#                 audio,
#                 language="en",
#                 beam_size=5
#             )

#             text = " ".join(
#                 segment.text for segment in segments
#             ).strip()

#             if text:

#                 print("You:", text)

#             else:

#                 print("No speech detected.")

#             return text

#         except Exception as e:

#             print("Voice recognition error:")
#             print(e)

#             return ""



import sounddevice as sd
import numpy as np
from faster_whisper import WhisperModel
import time


class VoiceRecognizer:

    MIC_DEVICE = 2
    SAMPLE_RATE = 16000
    BLOCK_SIZE = 1024

    START_THRESHOLD = 0.025
    SILENCE_THRESHOLD = 0.018
    SILENCE_DURATION = 0.8

    MAX_DURATION = 10

    def __init__(self):

        print("Loading Whisper model...")

        self.model = WhisperModel(
            "tiny",
            device="cpu",
            compute_type="int8"
        )

        print("Whisper ready.")

        device = sd.query_devices(
            self.MIC_DEVICE
        )

        print(
            f"Microphone: {device['name']}"
        )

        print(
            f"Sample rate: {self.SAMPLE_RATE} Hz"
        )

    def listen(self):

        print("Listening...")

        chunks = []

        recording = False
        silence_start = None
        start_time = None

        def callback(indata, frames, time_info, status):

            if status:
                print(
                    "Audio status:",
                    status
                )

            audio = indata[:, 0].copy()

            chunks.append(audio)

        try:

            chunks.clear()

            with sd.InputStream(
                device=self.MIC_DEVICE,
                samplerate=self.SAMPLE_RATE,
                channels=1,
                dtype="float32",
                blocksize=self.BLOCK_SIZE,
                callback=callback
            ):

                while True:

                    if not chunks:

                        time.sleep(0.01)

                        continue

                    audio = chunks.pop(0)

                    level = np.max(
                        np.abs(audio)
                    )

                    # -------------------------
                    # WAIT FOR SPEECH
                    # -------------------------

                    if not recording:

                        if level >= self.START_THRESHOLD:

                            print(
                                "Speech detected."
                            )

                            recording = True

                            start_time = (
                                time.time()
                            )

                            silence_start = None

                            recorded_audio = [
                                audio
                            ]

                        continue

                    # -------------------------
                    # RECORDING
                    # -------------------------

                    recorded_audio.append(
                        audio
                    )

                    elapsed = (
                        time.time()
                        - start_time
                    )

                    # -------------------------
                    # SPEAKING
                    # -------------------------

                    if level >= self.SILENCE_THRESHOLD:

                        silence_start = None

                    # -------------------------
                    # SILENCE
                    # -------------------------

                    else:

                        if silence_start is None:

                            silence_start = (
                                time.time()
                            )

                        silence_time = (
                            time.time()
                            - silence_start
                        )

                        if (
                            silence_time
                            >= self.SILENCE_DURATION
                        ):

                            break

                    # -------------------------
                    # MAXIMUM COMMAND TIME
                    # -------------------------

                    if elapsed >= self.MAX_DURATION:

                        print(
                            "Maximum recording time reached."
                        )

                        break

            audio_data = np.concatenate(
                recorded_audio
            )

            print(
                "Transcribing..."
            )

            segments, info = self.model.transcribe(
                audio_data,
                language="en",
                beam_size=1,
                vad_filter=True
            )

            text = " ".join(
                segment.text
                for segment in segments
            ).strip()

            if text:

                print(
                    "You:",
                    text
                )

            else:

                print(
                    "No speech detected."
                )

            return text

        except Exception as e:

            print(
                "Voice recognition error:"
            )

            print(e)

            return ""

