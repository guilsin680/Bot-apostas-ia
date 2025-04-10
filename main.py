from flask import Flask
import threading
import time

app = Flask(_name_)

def rodar_bot():
    while True:
        print("Bot de Apostas com IA Iniciado...")
        # Aqui vai sua lógica de IA e apostas
        print("Rodando modelo de IA para prever resultado...")
        print("Bot sugere: apostar no time A")
        time.sleep(30)  # espera 30 segundos antes de repetir

@app.route("/")
def status():
    return "Bot de Apostas com IA está rodando!"

if _name_ == "_main_":
    # Roda o bot em uma thread separada
    t = threading.Thread(target=rodar_bot)
    t.daemon = True
    t.start()

    # Inicia o servidor Flask
    app.run(host="0.0.0.0", port=10000)