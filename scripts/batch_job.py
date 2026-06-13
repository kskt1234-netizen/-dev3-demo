import requests

def backfill_orders():
    resp = requests.get("https://legacy.internal/orders", timeout=30)
    return resp.json()
