import os
from dotenv import load_dotenv
from fastapi import FastAPI
from ai_assistent import AI_response
app = FastAPI()

load_dotenv()

URL_CHATWOOT = os.getenv("URL_CHATWOOT")

@app.post("/webhook")
async def webhook(data: dict):

    received = data["message_type"]

    if received != "outgoing":

        numero = data["sender"]["phone_number"]
        mensagem = data["content"]
        account_id = data["account"]["id"]
        conversation_id = data["conversation"]["id"]
        id = data["id"]

        print(f"""
            CLIENT_INFORMATION:
            ID: {id}
            ACCOUNT_ID: {account_id}
            CONVERSATION_ID: {conversation_id}
            TELEFONE: {numero}
            MENSAGEM: {mensagem}

        """)

        response_ai = AI_response(mensagem)
        print(response_ai)


    else:
        print("MESSAGE_SENT_BY_ME")
    return {"status": "ok"}