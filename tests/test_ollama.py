from ollama import chat

response = chat(
    model="gemma3:4b",
    messages=[
        {
            "role": "user",
            "content": "Hello! Introduce yourself."
        }
    ]
)

print(response.message.content)