from typing import Dict, Any
def generate_description(product: Dict[str, Any])->str:
    product_type=product.get("product_type","handmade product")
    material=", ".join(product.get("material",[]))
    style=product.get("style", "traditional")
    features=", ".join(product.get("features",[]))
    return (
        f"This {style.lower()} {product_type.lower()} is crafted using "
        f"{material.lower()}. It is {features.lower()} and showcases "
        f"the skill and craftsmanship of local artisans."
    )