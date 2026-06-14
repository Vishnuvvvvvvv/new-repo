from openai import OpenAI

# Replace with AMD server IP
BASE_URL = "http://44.55.66.77:8000/v1"

client = OpenAI(
    api_key="abc-123",
    base_url=BASE_URL
)

response = client.chat.completions.create(
    model="Qwen3-30B-A3B",
    messages=[
        {
            "role": "user",
            "content": "What is the capital of France?"
        }
    ]
)

print("\nResponse:\n")
print(response.choices[0].message.content)