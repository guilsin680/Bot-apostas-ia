from flask import Flask
from predictor import prever_resultado
from alerts import send_telegram_message

app = Flask(__name__)

@app.route("/")
def home():
    print("Bot de Apostas com IA Iniciado...")

    resultado = prever_resultado()
    print("Bot sugere:", resultado)

    # Envia alerta no Telegram
    send_telegram_message(f"🤖 Bot de Apostas:\nSugestão: {resultado}")

    return f"<h2>🤖 Bot de Apostas com IA</h2><p>Sugestão: {resultado}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
