from ollama import chat

SYSTEM_PROMPT = """
You are Jarvex, an intelligent personal AI assistant created by Suraj.

Rules:
- Always introduce yourself as Jarvex.
- Be friendly and professional.
- Keep answers clear and helpful.
- If you don't know something, say so honestly.
"""

conversation = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

def ask_jarvex(user_input):
    conversation.append(
        {"role": "user", "content": user_input}
    )

    response = chat(
        model="gemma3:4b",
        messages=conversation
    )

    reply = response.message.content

    conversation.append(
        {"role": "assistant", "content": reply}
    )

    return reply