import os
from db.memory import *
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def AI_response(session_id, message):
    history = get_history(session_id)
    print(f"HISTORY: {history}")
    history.append({
        "role": "user",
        "content": message
    })

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=history
    )

    reply = response.choices[0].message.content

    save_message(session_id, "user", message)
    save_message(session_id, "assistant", reply)

    return reply
