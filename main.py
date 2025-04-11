from flask import Flask
from predictor import prever_resultado  # <- Importa a IA
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Exemplo: time da casa fez 2 gols, visitante 1
    previsao = prever_resultado(2, 1)  # Aqui você pode trocar os gols dinamicamente
    return f"""
    <h1>Bot de Apostas com IA</h1>
    <p>Rodando modelo de IA para prever resultado...</p>
    <p><strong>Bot sugere:</strong> apostar no resultado: {previsao}</p>
    """

if __name__ == '__main__':
    # Garantir que a aplicação Flask ouça a porta configurada no Render
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 10000)))  # Usa a variável de ambiente PORT ou 10000 como padrão
