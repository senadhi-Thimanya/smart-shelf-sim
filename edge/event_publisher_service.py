import requests

def send_to_cloud(status):
    response = requests.post("http://localhost:5000/api/shelf", json={"status": status})
    print(f"[PUBLISH] Sent to cloud: {response.status_code}")
