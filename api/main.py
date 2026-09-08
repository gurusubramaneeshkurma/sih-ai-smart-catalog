from fastapi import FastAPI, UploadFile, File
from ai.analyzer import analyze_product as analyze_product_image
from ai.description import generate_description
from matching.matcher import recommend_markets

app = FastAPI(
    title="SIH AI Smart Catalog API",
    description="AI-powered artisan product analysis and market matching",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "SIH AI Smart Catalog API is running"
    }


@app.post("/api/analyze-product")
async def analyze_product(
    image: UploadFile = File(...)
):
    image_bytes = await image.read()

    product = analyze_product_image(
        image_bytes,
        image.content_type
    )

    product["description"] = generate_description(product)

    product["recommended_markets"] = recommend_markets(product)

    product["image_filename"] = image.filename
    product["image_content_type"] = image.content_type

    return product