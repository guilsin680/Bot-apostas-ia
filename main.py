from flask import Flask
from predictor import prever_resultado  # Importa a função do predictor.py

app = Flask(__name__)

@app.route("/")
def home():
    # Usando valores fixos para teste ou demonstração
    resultado = prever_resultado(2, 1)  # Exemplo: 2 gols time casa, 1 gol time fora
    return f"<h1>Previsão: {resultado}</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
