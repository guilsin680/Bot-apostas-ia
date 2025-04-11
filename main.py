import os
from flask import Flask
from predictor import prever_resultado  # Importa a função de previsão
from alerts import send_telegram_message  # Importa a função de alerta

app = Flask(__name__)

# Rota principal que gera uma previsão e envia alerta
@app.route('/')
def index():
    # Exemplo: time da casa fez 2 gols, visitante 1
    previsao = prever_resultado(2, 1)
    message = f"Previsão gerada: {previsao}"
    
    # Envia alerta para o Telegram
    send_telegram_message(message)
    
    return f"""
    <h1>Bot de Apostas com IA</h1>
    <p>Previsão: {previsao}</p>
    <p>Um alerta foi enviado para o Telegram.</p>
    <a href="/dashboard">Ir para o Dashboard</a>
    """

# Rota simples para o Dashboard
@app.route('/dashboard')
def dashboard():
    return """
    <h1>Dashboard do Bot</h1>
    <p>Aqui você pode ver informações e estatísticas sobre as previsões do bot.</p>
    <p>(Essa funcionalidade será expandida futuramente.)</p>
    <a href="/">Voltar</a>
    """

if __name__ == '__main__':
    # Configura a porta usando a variável de ambiente PORT (utilizada pelo Render)
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 10000)))
