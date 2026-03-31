import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def AI_response(message):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user", "content": f"{message}"
            }
        ]
    )
    return response.choices[0].message.content
