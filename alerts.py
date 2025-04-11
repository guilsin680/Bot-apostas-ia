# alerts.py

import os
import requests

def send_telegram_message(message):
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    if not token or not chat_id:
        print("Erro: TELEGRAM_TOKEN ou TELEGRAM_CHAT_ID não definidos nas variáveis de ambiente.")
        return

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }

    try:
        response = requests.post(url, data=payload)
        if response.status_code != 200:
            print("Erro ao enviar mensagem:", response.text)
        else:
            print("Mensagem enviada com sucesso!")
    except Exception as e:
        print("Erro na requisição:", e)
