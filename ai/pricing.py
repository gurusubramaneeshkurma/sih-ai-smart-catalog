from typing import Dict, Any


def recommend_price(
    product: Dict[str, Any],
    material_cost: float,
    labor_hours: float,
    labor_rate: float,
    packaging_cost: float = 0,
    overhead_percent: float = 10,
    profit_margin_percent: float = 20
) -> Dict[str, Any]:

    # -----------------------------
    # 1. Calculate labor cost
    # -----------------------------
    labor_cost = labor_hours * labor_rate

    # -----------------------------
    # 2. Direct production cost
    # -----------------------------
    direct_cost = (
        material_cost
        + labor_cost
        + packaging_cost
    )

    # -----------------------------
    # 3. Calculate overhead
    # -----------------------------
    overhead_cost = (
        direct_cost * overhead_percent / 100
    )

    # -----------------------------
    # 4. Total production cost
    # -----------------------------
    total_cost = (
        direct_cost
        + overhead_cost
    )

    # -----------------------------
    # 5. Profit
    # -----------------------------
    profit = (
        total_cost * profit_margin_percent / 100
    )

    # -----------------------------
    # 6. Recommended price
    # -----------------------------
    recommended_price = total_cost + profit

    # -----------------------------
    # 7. Price range
    # -----------------------------
    minimum_price = total_cost * 1.10
    maximum_price = total_cost * 1.40

    # Round prices
    recommended_price = round(recommended_price)
    minimum_price = round(minimum_price)
    maximum_price = round(maximum_price)

    # -----------------------------
    # Product information
    # -----------------------------
    product_type = product.get(
        "product_type",
        "Handmade Product"
    )

    material = product.get(
        "material",
        []
    )

    style = product.get(
        "style",
        "Traditional"
    )

    # -----------------------------
    # Return result
    # -----------------------------
    return {
        "product_type": product_type,

        "material": material,

        "style": style,

        "cost_breakdown": {
            "material_cost": round(material_cost),
            "labor_cost": round(labor_cost),
            "packaging_cost": round(packaging_cost),
            "overhead_cost": round(overhead_cost),
            "total_production_cost": round(total_cost)
        },

        "profit": round(profit),

        "recommended_price": recommended_price,

        "price_range": {
            "minimum": minimum_price,
            "maximum": maximum_price
        },

        "currency": "INR",

        "pricing_method": "AI-assisted rule-based pricing",

        "artisan_final_decision": True,

        "message": (
            "This is a recommended selling price. "
            "The artisan has the final decision on the price."
        )
    }

