import whisper

# Load model once
asr_model = whisper.load_model("base")

def transcribe_audio(audio_path):
    result = asr_model.transcribe(audio_path)

    transcript = result["text"]
    confidence = result.get("avg_logprob", 0.8)

    return transcript.strip(), confidence