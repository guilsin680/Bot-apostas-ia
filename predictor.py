import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
import os

# Carregar o arquivo CSV com os dados históricos
df = pd.read_csv("historico_jogos.csv")

# Verificar as colunas do DataFrame para depuração
print("Colunas no arquivo CSV:", df.columns)

# Ajuste os nomes das colunas conforme necessário (verifique as colunas reais no arquivo CSV)
X = df[['gol_time_casa', 'gol_time_fora']]  # Características (gols dos times)
y = df['resultado']  # Resultado do jogo (vitória/empate/derrota)

# Dividindo os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar o pipeline de processamento e treinamento
pipeline = make_pipeline(StandardScaler(), LogisticRegression())

# Treinando o modelo
pipeline.fit(X_train, y_train)

# Função para prever o resultado
def prever_resultado():
    # Exemplo de valores fixos para gols
    gol_time_casa = 2  # Gols do time da casa
    gol_time_fora = 1  # Gols do time visitante

    # Realizando a previsão
    previsao = pipeline.predict([[gol_time_casa, gol_time_fora]])

    # Retorna a previsão como string
    return f"Apostar no {previsao[0]}"
