import os
import openwakeword
from openwakeword.model import Model
import sounddevice as sd
import numpy as np


class WakeWord:

    MIC_DEVICE = 2
    SAMPLE_RATE = 16000

    # 1280 samples = 80 ms at 16 kHz
    BLOCK_SIZE = 640

    THRESHOLD = 0.35

    def __init__(self):

        print("Loading wake-word model...")

        base_path = os.path.dirname(
            openwakeword.__file__
        )

        model_path = os.path.join(
            base_path,
            "resources",
            "models",
            "hey_jarvis_v0.1.onnx"
        )

        if not os.path.exists(model_path):
            raise FileNotFoundError(
                f"Wake-word model not found:\n{model_path}"
            )

        self.model = Model(
            wakeword_models=[model_path],
            inference_framework="onnx"
        )

        self.detected = False

        device = sd.query_devices(self.MIC_DEVICE)

        print(
            f"Wake-word microphone: {device['name']}"
        )

        print(
            f"Wake-word sample rate: "
            f"{self.SAMPLE_RATE} Hz"
        )

        print(
            f"Wake-word block size: "
            f"{self.BLOCK_SIZE} samples"
        )

    def callback(
        self,
        indata,
        frames,
        time,
        status
    ):

        if status:
            print("Audio status:", status)

        # SoundDevice gives float32 in range -1.0 to 1.0.
        # openWakeWord expects int16 PCM.
        audio = indata[:, 0]

        audio = np.clip(
            audio,
            -1.0,
            1.0
        )

        audio = (
            audio * 32767
        ).astype(np.int16)

        level = np.max(
            np.abs(audio)
        )

        # Convert back to a readable 0-1 level
        level_float = level / 32767.0

        if level_float > 0.02:

            print(
                f"Wake audio level: "
                f"{level_float:.4f}"
            )

            predictions = self.model.predict(
                audio
            )

            # print(
            #     "Wake scores:",
            #     predictions
            # )

            for name, score in predictions.items():

                score = float(score)

                if score >= self.THRESHOLD:

                    print()
                    print(
                        "================================"
                    )
                    print(
                        "   WAKE WORD DETECTED!"
                    )
                    print(
                        f"   {name}: {score:.3f}"
                    )
                    print(
                        "================================"
                    )
                    print()

                    self.detected = True

                    self.model.reset()

    def wait(self):

        self.detected = False

        print()
        print(
            "Listening for 'Hey Jarvis'..."
        )
        print(
            "Say: Hey Jarvis"
        )
        print()

        try:

            with sd.InputStream(
                device=self.MIC_DEVICE,
                samplerate=self.SAMPLE_RATE,
                channels=1,
                dtype="float32",
                blocksize=self.BLOCK_SIZE,
                callback=self.callback
            ):

                while not self.detected:

                    sd.sleep(100)

        except Exception as e:

            print(
                "Wake-word microphone error:"
            )

            print(e)

            return False

        return True
