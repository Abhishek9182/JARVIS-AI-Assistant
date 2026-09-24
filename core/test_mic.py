import sounddevice as sd
import numpy as np

MIC_DEVICE = 2
SAMPLE_RATE = 16000

print("=" * 40)
print("       JARVIS MIC TEST")
print("=" * 40)

device = sd.query_devices(MIC_DEVICE)

print(f"Microphone: {device['name']}")
print(f"Sample rate: {SAMPLE_RATE} Hz")
print()
print("Speak into your microphone...")
print("Press Ctrl+C to stop.")
print()

def callback(indata, frames, time, status):
    if status:
        print("Status:", status)

    level = np.max(np.abs(indata))

    if level > 0.01:
        print(f"Audio Level: {level:.4f}")


try:
    with sd.InputStream(
        device=MIC_DEVICE,
        channels=1,
        samplerate=SAMPLE_RATE,
        dtype="float32",
        callback=callback
    ):
        while True:
            sd.sleep(1000)

except KeyboardInterrupt:
    print("\n")
    print("JARVIS MIC TEST STOPPED")
    print("Microphone is working correctly.")

except Exception as e:
    print("\nMicrophone error:")
    print(e)

