import os
from predictor import prever_resultado
from telegram_alert import enviar_telegram
import time

def home():
    # Obtenha a previsão
    resultado = prever_resultado()
    
    # Envie a previsão para o Telegram
    mensagem = f"A previsão para o próximo jogo é: {resultado}"
    enviar_telegram(mensagem)

if __name__ == "__main__":
    while True:
        home()
        # Aguarda 10 minutos antes de enviar novamente
        time.sleep(600)  # 600 segundos = 10 minutos
