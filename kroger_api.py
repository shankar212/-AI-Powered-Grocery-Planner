# kroger_api.py
import requests
from kroger_auth import get_kroger_access_token

def get_product_matches(ingredients):
    token = get_kroger_access_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }

    matched_products = []
    for item in ingredients:
        params = {
            "filter.term": item,
            "filter.locationId": "01400943",  # Default Kroger store
            "filter.limit": 1
        }
        response = requests.get("https://api.kroger.com/v1/products", headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            if data.get("data"):
                product = data["data"][0]
                name = product["description"]
                price_info = product.get("items", [{}])[0].get("price", {})
                price = price_info.get("regular") or 0.0
                stock = product.get("items", [{}])[0].get("inventory", {}).get("stockLevel")
                in_stock = stock and stock.lower() != "out_of_stock"
                matched_products.append({
                    "name": name,
                    "price": price,
                    "in_stock": in_stock
                })
    return matched_products
