import requests

BASE_URL = "http://127.0.0.1:8000"

for i in range(10):
    r = requests.post(f"{BASE_URL}/companies/", json={"name": f"Company {i}", "country": "Country"})
    print(r.json())
