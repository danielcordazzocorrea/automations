import os
from dotenv import load_dotenv
from fastapi import FastAPI
from ai_assistent import AI_response
from services.send_message import send_message

app = FastAPI()

load_dotenv()

URL_CHATWOOT = os.getenv("URL_CHATWOOT")

@app.post("/webhook")
async def webhook(data: dict):
    print("WEBHOOK_RECEIVED")
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

        response_ai = AI_response(numero, mensagem)
        print(response_ai)
        send_message(URL_CHATWOOT, account_id, conversation_id, response_ai)

    else:
        print("MESSAGE_SENT_BY_ME")
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn

    port = int(os.environ.get("PORT", 8000))

    uvicorn.run(app, host="0.0.0.0", port=port)