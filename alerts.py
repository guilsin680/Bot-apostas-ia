import requests
import os

def send_telegram_message(message):
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    if not token or not chat_id:
        print("⚠️ Variáveis TELEGRAM_TOKEN ou TELEGRAM_CHAT_ID não configuradas")
        return

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message
    }

    response = requests.post(url, data=data)

    if response.status_code == 200:
        print("✅ Mensagem enviada com sucesso para o Telegram!")
    else:
        print(f"❌ Erro ao enviar mensagem: {response.text}")
