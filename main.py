from flask import Flask
from predictor import prever_resultado  # Importa a função do predictor.py
import os

app = Flask(__name__)

# Rota principal que retorna a previsão
@app.route('/')
def home():
    # Chama a função de previsão
    resultado = prever_resultado()

    # Retorna o resultado como resposta para o usuário
    return f"Resultado da previsão: {resultado}"

if __name__ == '__main__':
    # Ajusta a porta conforme a variável de ambiente PORT fornecida pelo Render
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
