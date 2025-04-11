import os
import requests

def enviar_telegram(mensagem):
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    if not token or not chat_id:
        print("Token ou Chat ID do Telegram não configurado.")
        return

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": mensagem
    }

    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print("Mensagem enviada com sucesso.")
        else:
            print(f"Erro ao enviar mensagem: {response.text}")
    except Exception as e:
        print(f"Erro na requisição Telegram: {e}")
