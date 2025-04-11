from flask import Flask
import threading
import schedule
import time
from predictor import prever_resultado
from telegram_alert import enviar_telegram

app = Flask(__name__)

def agendamento():
    # Envia a cada 10 minutos
    schedule.every(10).minutes.do(executar_envio)

    while True:
        schedule.run_pending()
        time.sleep(60)

def executar_envio():
    resultado = prever_resultado()
    hora = time.strftime('%H:%M')
    enviar_telegram(f"🔔 Previsão automática ({hora}):\n{resultado}")

@app.route("/")
def home():
    resultado = prever_resultado()
    return f"<h1>Previsão atual:</h1><p>{resultado}</p>"

# Roda o agendamento em segundo plano
threading.Thread(target=agendamento, daemon=True).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
