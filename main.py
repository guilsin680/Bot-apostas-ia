import os
import time
from flask import Flask
from predictor import prever_resultado
from telegram_alert import enviar_telegram

app = Flask(__name__)

# Defina a porta que o Render fornecer (para o Flask)
port = int(os.environ.get("PORT", 5000))

@app.route('/')
def home():
    resultado = prever_resultado()
    enviar_telegram(resultado)  # Envia a previsão para o Telegram
    return f"Previsão enviada: {resultado}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)
