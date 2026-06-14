from flask import Flask, request, jsonify
from flask_cors import CORS
from pyngrok import ngrok
from openai import OpenAI

# -----------------------------------
# CONFIG
# -----------------------------------

VLLM_URL = "http://localhost:8000/v1"
API_KEY = "abc-123"

PORT = 6050

# -----------------------------------
# OPENAI CLIENT
# -----------------------------------

client = OpenAI(
    api_key=API_KEY,
    base_url=VLLM_URL
)

# -----------------------------------
# FLASK
# -----------------------------------

app = Flask(__name__)
CORS(app)

# -----------------------------------
# NGROK
# -----------------------------------

ngrok.set_auth_token("2euoOMWZvAwibuTD9DTfC6V1LLm_6udm6jqeKjcJkhx72zHNu")

public_url = ngrok.connect(PORT)

print("\n")
print("=" * 50)
print("PUBLIC URL:")
print(public_url)
print("=" * 50)
print("\n")

# -----------------------------------
# HEALTH
# -----------------------------------

@app.route("/")
def home():
    return {
        "status": "running",
        "model": "Qwen3-30B-A3B"
    }

# -----------------------------------
# CHAT ENDPOINT
# -----------------------------------

@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    prompt = data.get("message", "")

    response = client.chat.completions.create(
        model="Qwen3-30B-A3B",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    answer = response.choices[0].message.content

    return jsonify({
        "response": answer
    })

# -----------------------------------
# START
# -----------------------------------

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=PORT
    )