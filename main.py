import os
from flask import Flask
from predictor import prever_resultado  # Importe a função de previsão que você configurou

app = Flask(__name__)

@app.route('/')
def home():
    resultado = prever_resultado()
    return f"A previsão é: {resultado}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
