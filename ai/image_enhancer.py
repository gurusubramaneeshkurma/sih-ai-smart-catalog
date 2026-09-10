from PIL import Image, ImageEnhance
from rembg import remove
from io import BytesIO


def enhance_product_image(image_bytes: bytes) -> bytes:
    """
    Remove the background and apply basic lighting enhancement.
    Returns a PNG image with transparent background.
    """

    # Load image
    image = Image.open(BytesIO(image_bytes)).convert("RGBA")

    # Remove background
    output = remove(image)

    # Slight lighting improvement
    rgb_image = output.convert("RGB")

    brightness = ImageEnhance.Brightness(rgb_image)
    rgb_image = brightness.enhance(1.08)

    contrast = ImageEnhance.Contrast(rgb_image)
    rgb_image = contrast.enhance(1.08)

    # Convert back to RGBA
    final_image = rgb_image.convert("RGBA")

    # Save to memory
    output_buffer = BytesIO()
    final_image.save(
        output_buffer,
        format="PNG"
    )

    return output_buffer.getvalue()
