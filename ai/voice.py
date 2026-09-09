import os
from typing import Dict, Any

from dotenv import load_dotenv
from google import genai

load_dotenv(".env")

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def transcribe_voice(audio_path: str) -> Dict[str, Any]:
    print("Uploading voice recording to Gemini...")

    audio_file = client.files.upload(
        file=audio_path
    )

    print("Voice uploaded successfully.")
    print("Sending audio to Gemini 3.5 Transcribe...")

    interaction = client.interactions.create(
        model="gemini-3.5-transcribe",
        input=[
            {
                "type": "audio",
                "uri": audio_file.uri,
                "mime_type": audio_file.mime_type,
            }
        ],
        generation_config={
            "transcription_config": {
                "language_codes": []
            }
        }
    )

    transcription = interaction.output_text

    if not transcription:
        raise RuntimeError(
            "Gemini returned an empty transcription."
        )

    print("Voice transcription successful.")

    return {
        "transcription": transcription
    }