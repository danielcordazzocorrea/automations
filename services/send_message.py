import requests
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("CHATWOOT_TOKEN")

def send_message(url_chatwoot, account_id, conversation_id, message):
    url = f"{url_chatwoot}/api/v1/accounts/{account_id}/conversations/{conversation_id}/messages"
    
    headers = {
        "Content-Type": "application/json",
        "api_access_token": f"{TOKEN}"
    }
    data = {
        "content": f"{message}"
    }

    try:
        response = requests.post(url, headers=headers, json=data, timeout=10)
        print(response)
    except requests.exceptions.RequestException as e:
        print("Erro:", e)

