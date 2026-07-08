import sounddevice as sd
import soundfile as sf

duration = 5  # seconds
sample_rate = 16000

print("🎤 Speak now...")

audio = sd.rec(
    int(duration * sample_rate),
    samplerate=sample_rate,
    channels=1,
    dtype="float32",
    device=1  # Realtek Microphone Array
)

sd.wait()

sf.write("recording.wav", audio, sample_rate)

print("✅ Recording saved as recording.wav")