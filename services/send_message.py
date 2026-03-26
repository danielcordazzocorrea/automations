import os
import requests
from dotenv import load_dotenv
from utils.logger import get_logger
from logging.handlers import RotatingFileHandler 


load_dotenv()

TOKEN = os.getenv("WHATSAPP_TOKEN")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")

os.makedirs("logs", exist_ok=True)

logger = get_logger("whatsapp")


def send_message(numbers):
    url = f"https://graph.facebook.com/v22.0/{PHONE_NUMBER_ID}/messages"

    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }
    for number in numbers:
        data = {
        "messaging_product": "whatsapp",
        "to": f"{number}",
        "type": "interactive",
        "interactive": {
            "type": "button",
            "body": {
            "text": "Recebeu minha mensagem?"
            },
            "action": {
            "buttons": [
                {
                "type": "reply",
                "reply": {
                    "id": "opcao_1",
                    "title": "Sim✅"
                }
                },
                {
                "type": "reply",
                "reply": {
                    "id": "opcao_2",
                    "title": "Não❌"
                }
                }
            ]
            }
        }
        }



        try:
            logger.info(f"Enviando mensagem para {number}")

            response = requests.post(url, headers=headers, json=data, timeout=10)

            logger.info(f"Status: {response.status_code} | Numero: {number}")
            logger.info(f"Resposta: {response.text}")

        except requests.exceptions.RequestException as e:
            logger.error(f"Erro ao enviar para {number} | Erro: {e}")
