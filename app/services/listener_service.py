import sounddevice as sd
import soundfile as sf
from faster_whisper import WhisperModel
import tempfile
import os

# ==============================
# Load Whisper model (only once)
# ==============================

model = WhisperModel(
    "small",
    device="cpu",
    compute_type="int8"
)

# ==============================
# Your microphone device number
# ==============================

MIC_DEVICE = 1

# ==============================
# Listen Function
# ==============================

def listen():

    samplerate = 16000
    duration = 5

    print("🎤 Listening...")

    recording = sd.rec(
        int(duration * samplerate),
        samplerate=samplerate,
        channels=1,
        dtype="float32",
        device=MIC_DEVICE
    )

    sd.wait()

    # Save recording temporarily
    with tempfile.NamedTemporaryFile(
        suffix=".wav",
        delete=False
    ) as temp_audio:

        sf.write(temp_audio.name, recording, samplerate)
        temp_path = temp_audio.name

    try:

        segments, info = model.transcribe(
            temp_path,
            beam_size=5
        )

        text = ""

        for segment in segments:
            text += segment.text

        text = text.strip()

        # ==========================
        # Correct common mistakes
        # ==========================

        corrections = {
            "graduates": "Jarvex",
            "jarooks": "Jarvex",
            "jarvis": "Jarvex",
            "javax": "Jarvex",
            "jervis": "Jarvex",
            "jar vex": "Jarvex",
        }

        text_lower = text.lower()

        for wrong, correct in corrections.items():
            if wrong in text_lower:
                text = correct
                break

    finally:

        if os.path.exists(temp_path):
            os.remove(temp_path)

    return text