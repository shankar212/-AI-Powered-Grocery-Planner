import requests

def get_kroger_access_token():
    url = "https://api.kroger.com/v1/connect/oauth2/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials",
        "scope": "product.compact"
    }
    auth = ("groceryplannerai-bbc654cd", "mvmgWlTS3DHcnwbhcjzd8aPjTEWSaH3ngUFW8iJg")

    response = requests.post(url, headers=headers, data=data, auth=auth)
    response.raise_for_status()  # helpful for debugging
    return response.json()["access_token"]
