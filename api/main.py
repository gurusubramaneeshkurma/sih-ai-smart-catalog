from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import Response
import traceback

from ai.analyzer import analyze_product as analyze_product_image
from ai.description import generate_description
from ai.pricing import recommend_price
from ai.voice import transcribe_voice
from ai.image_enhancer import enhance_product_image
from matching.matcher import recommend_markets


app = FastAPI(
    title="SIH AI Smart Catalog API",
    description="AI-powered artisan product analysis and market matching",
    version="1.0.0"
)


# =========================================================
# HOME
# =========================================================

@app.get("/")
def home():
    return {
        "message": "SIH AI Smart Catalog API is running"
    }


# =========================================================
# AI PRODUCT ANALYSIS
# =========================================================

@app.post("/api/analyze-product")
async def analyze_product(
    image: UploadFile = File(...)
):
    try:
        print(f"\n--- ANALYZING IMAGE: {image.filename} ---")

        image_bytes = await image.read()

        print("Image received:", len(image_bytes), "bytes")
        print("Running AI image analysis...")

        product = analyze_product_image(
            image_bytes,
            image.content_type
        )

        print("AI image analysis successful.")
        print("Generating descriptions...")

        description = generate_description(product)

        print("Description generation successful.")

        product.update(description)

        print("Running market matching...")

        product["recommended_markets"] = recommend_markets(product)

        product["image_filename"] = image.filename
        product["image_content_type"] = image.content_type

        print("--- ANALYSIS COMPLETE ---")

        return product

    except Exception as error:
        print("\n========== ANALYZE ERROR ==========")
        print(type(error).__name__)
        print(str(error))
        traceback.print_exc()
        print("===================================\n")

        raise HTTPException(
            status_code=500,
            detail={
                "error": type(error).__name__,
                "message": str(error)
            }
        )


# =========================================================
# AI IMAGE ENHANCER
# =========================================================

@app.post("/api/enhance-image")
async def enhance_image(
    image: UploadFile = File(...)
):
    try:
        print(f"\n--- ENHANCING IMAGE: {image.filename} ---")

        image_bytes = await image.read()

        print("Image received:", len(image_bytes), "bytes")
        print("Running image enhancement...")

        enhanced_image = enhance_product_image(image_bytes)

        output_path = "/tmp/enhanced_product.png"

        with open(output_path, "wb") as file:
            file.write(enhanced_image)

        print("Image enhancement successful.")
        print("Output:", output_path)
        print("Output size:", len(enhanced_image), "bytes")
        print("--- ENHANCEMENT COMPLETE ---")

        return {
            "success": True,
            "message": "Product image enhanced successfully",
            "original_filename": image.filename,
            "original_size_bytes": len(image_bytes),
            "enhanced_size_bytes": len(enhanced_image),
            "output_file": output_path,
            "output_format": "PNG"
        }

    except Exception as error:
        print("\n========== IMAGE ENHANCER ERROR ==========")
        print(type(error).__name__)
        print(str(error))
        traceback.print_exc()
        print("===========================================\n")

        raise HTTPException(
            status_code=500,
            detail={
                "error": type(error).__name__,
                "message": str(error)
            }
        )

# =========================================================
# DYNAMIC PRICE RECOMMENDATION
# =========================================================

@app.post("/api/recommend-price")
async def recommend_product_price(
    product_type: str,
    material_cost: float,
    labor_hours: float,
    labor_rate: float,
    packaging_cost: float = 0,
    overhead_percent: float = 10,
    profit_margin_percent: float = 20
):

    product = {
        "product_type": product_type,
        "material": [],
        "style": "Traditional"
    }

    result = recommend_price(
        product=product,
        material_cost=material_cost,
        labor_hours=labor_hours,
        labor_rate=labor_rate,
        packaging_cost=packaging_cost,
        overhead_percent=overhead_percent,
        profit_margin_percent=profit_margin_percent
    )

    return result


# =========================================================
# VOICE TRANSCRIPTION
# =========================================================

@app.post("/api/transcribe-voice")
async def transcribe_voice_endpoint(
    audio: UploadFile = File(...)
):
    try:
        print(f"\n--- TRANSCRIBING AUDIO: {audio.filename} ---")

        audio_bytes = await audio.read()

        print("Audio received:", len(audio_bytes), "bytes")

        temp_path = "/tmp/artisan_voice.mp3"

        with open(temp_path, "wb") as file:
            file.write(audio_bytes)

        print("Running voice transcription...")

        result = transcribe_voice(temp_path)

        print("Voice transcription successful.")

        return {
            "filename": audio.filename,
            "content_type": audio.content_type,
            **result
        }

    except Exception as error:
        print("\n========== VOICE ERROR ==========")
        print(type(error).__name__)
        print(str(error))
        traceback.print_exc()
        print("=================================\n")

        raise HTTPException(
            status_code=500,
            detail={
                "error": type(error).__name__,
                "message": str(error)
            }
        )