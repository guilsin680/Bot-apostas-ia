from flask import Flask
import threading
import time

app = Flask(__name__)

def rodar_bot():
    while True:
        print("Bot de Apostas com IA Iniciado...")
        # Simulação da lógica do bot de IA
        print("Rodando modelo de IA para prever resultado...")
        print("Bot sugere: apostar no time A")
        time.sleep(30)  # Espera 30 segundos antes de repetir

@app.route("/")
def status():
    return "Bot de Apostas com IA está rodando!"

if __name__ == "_main_":
    t = threading.Thread(target=rodar_bot)
    t.daemon = True
    t.start()

    app.run(host="0.0.0.0", port=10000)