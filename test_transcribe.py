import os
from dotenv import load_dotenv
from google import genai

load_dotenv(".env")

print("1. Creating Gemini client...")

api_key = os.getenv("GEMINI_API_KEY")
print("API key loaded:", bool(api_key))

client = genai.Client(
    api_key=api_key
)

audio_path = "api/WhatsApp Audio 2026-09-09 at 13.02.15.mp3"

print("2. Uploading audio...")

audio_file = client.files.upload(
    file=audio_path
)

print("3. Upload successful")
print("URI:", audio_file.uri)
print("MIME:", audio_file.mime_type)

print("4. Sending to Gemini Transcribe...")

interaction = client.interactions.create(
    model="gemini-3.5-transcribe",
    input=[
        {
            "type": "audio",
            "uri": audio_file.uri,
            "mime_type": audio_file.mime_type,
        }
    ],
)

print("5. Transcription successful!")
print("TRANSCRIPTION:")
print(interaction.output_text)

from ai.voice import voice_assistant

audio_path = "api/WhatsApp Audio 2026-09-09 at 13.02.15.mp3"

result = voice_assistant(audio_path)

print("\n========== VOICE ASSISTANT RESULT ==========")
print("Language:", result["language"])
print("Language code:", result["language_code"])
print("Transcription:", result["transcription"])
print("AI Response:", result["response"])
print("Audio file:", result["audio_file"])
print("============================================")