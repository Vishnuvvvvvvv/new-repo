import requests

response = requests.post(
    "https://notebooks.amd.com/jupyter-hack-team-3322-260614163526-3d26ef61/proxy/6050/chat",
    json={
        "message": "What is the capital of France?"
    }
)

print(response.json())