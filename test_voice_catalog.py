from ai.voice import voice_catalog


# This is the Telugu transcription
# produced by your working voice assistant.

transcription = """
ఇది వెదురుతో చేతితో తయారు చేసిన బుట్ట.
ఇది పండ్లు మరియు ఇంటి వస్తువులు పెట్టుకోవడానికి ఉపయోగిస్తారు.
ఇది సంప్రదాయ పద్ధతిలో తయారు చేయబడింది.
"""

result = voice_catalog(
    transcription,
    "Telugu"
)


print("\n")
print("==========================================")
print("       MULTILINGUAL AI AUTO-CATALOG")
print("==========================================")

print("\nProduct Name:")
print(result["product_name"])

print("\nCategory:")
print(result["category"])

print("\nProduct Type:")
print(result["product_type"])

print("\nMaterial:")
print(result["material"])

print("\nStyle:")
print(result["style"])

print("\nColor:")
print(result["color"])

print("\nFeatures:")
print(result["features"])

print("\nEnglish Description:")
print(result["english_description"])

print("\nHindi Description:")
print(result["hindi_description"])

print("\nSEO Keywords:")
print(result["seo_keywords"])

print("\n==========================================")