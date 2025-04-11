import requests
import os

def send_telegram_message(message):
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        print("Token ou Chat ID do Telegram não estão definidos.")
        return
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": message}
    response = requests.post(url, data=data)
    if response.status_code != 200:
        print("Erro ao enviar mensagem para o Telegram:", response.text)
