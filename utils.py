from collections import defaultdict

def build_shopping_list(products, include_out_of_stock=True):
    """
    Aggregates matched products by name, calculates average price,
    and preserves stock status.
    """
    seen = defaultdict(lambda: {"price": 0.0, "count": 0, "in_stock": False, "name": ""})

    for item in products:
        name_key = item["name"].strip().lower()  # case-insensitive key
        seen[name_key]["price"] += item["price"]
        seen[name_key]["count"] += 1
        seen[name_key]["in_stock"] = seen[name_key]["in_stock"] or item["in_stock"]
        seen[name_key]["name"] = item["name"]  # preserve original casing

    result = []
    for val in seen.values():
        avg_price = round(val["price"] / val["count"], 2)
        item_data = {
            "name": val["name"],
            "price": avg_price,
            "in_stock": val["in_stock"]
        }
        if include_out_of_stock or val["in_stock"]:
            result.append(item_data)

    return sorted(result, key=lambda x: x["price"], reverse=True)  # sorted high to low


def calculate_total_cost(products, only_in_stock=True):
    """
    Returns total cost based on in-stock items by default.
    """
    if only_in_stock:
        return round(sum(item["price"] for item in products if item["in_stock"]), 2)
    else:
        return round(sum(item["price"] for item in products), 2)
