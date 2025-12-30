import requests
import random
import string

BASE_URL = "http://127.0.0.1:8000"

def random_string(n=8):
    return ''.join(random.choices(string.ascii_letters, k=n))

company_ids = []

for i in range(50):
    payload = {
        "name": f"Company_{i}",
        "country": random.choice(["USA", "Germany", "France", "Japan", "Korea"])
    }
    r = requests.post(f"{BASE_URL}/companies/", json=payload)
    r.raise_for_status()
    company_ids.append(r.json()["id"])

print(f"Created {len(company_ids)} companies")


project_ids = []

for i in range(200):
    payload = {
        "name": f"Project_{i}",
        "budget": random.randint(10_000, 1_000_000),
        "company_id": random.choice(company_ids),
        "metadata_json": {
            "type": random.choice(["residential", "industrial", "commercial"]),
            "city": random.choice(["Seoul", "Berlin", "Paris", "New York"]),
            "priority": random.randint(1, 5)
        }
    }
    r = requests.post(f"{BASE_URL}/projects/", json=payload)
    r.raise_for_status()
    project_ids.append(r.json()["id"])

print(f"Created {len(project_ids)} projects")

worker_count = 0

for project_id in project_ids:
    for _ in range(random.randint(3, 8)):
        payload = {
            "name": f"Worker_{random_string()}",
            "role": random.choice(["engineer", "manager", "architect", "technician"]),
            "project_id": project_id
        }
        r = requests.post(f"{BASE_URL}/workers/", json=payload)
        r.raise_for_status()
        worker_count += 1

print(f"Created {worker_count} workers")
