from flask import Flask
from predictor import prever_resultado
import os
import requests

app = Flask(__name__)

def enviar_telegram(mensagem):
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")

    if not token or not chat_id:
        print("Token ou Chat ID não configurado.")
        return

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": mensagem,
        "parse_mode": "HTML"
    }

    response = requests.post(url, data=payload)
    if response.status_code != 200:
        print(f"Erro ao enviar mensagem: {response.text}")

@app.route("/")
def home():
    resultado = prever_resultado()
    mensagem = f"📢 Previsão do modelo: <b>{resultado}</b>"
    enviar_telegram(mensagem)
    return f"<h1>{mensagem}</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
