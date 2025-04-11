import os
import requests

# Função para enviar mensagem para o Telegram
def enviar_telegram(mensagem):
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': mensagem
    }
    
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print(f"Mensagem enviada com sucesso: {mensagem}")
    else:
        print(f"Erro ao enviar mensagem: {response.text}")
