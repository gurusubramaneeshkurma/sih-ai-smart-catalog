from ai.voice import voice_assistant


audio_path = "api/WhatsApp Audio 2026-09-09 at 13.02.15.mp3"


result = voice_assistant(
    audio_path
)


print("\n")
print("============================================")
print("       VOICE ASSISTANT RESULT")
print("============================================")

print(
    "Language:",
    result["language"]
)

print(
    "Language code:",
    result["language_code"]
)

print(
    "Transcription:",
    result["transcription"]
)

print(
    "AI Response:",
    result["response"]
)

print(
    "Audio file:",
    result["audio_file"]
)

print("============================================")