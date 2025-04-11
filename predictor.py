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

# Usar os nomes corretos das colunas
X = df[['home_goals', 'away_goals']]  # Características (gols dos times)
y = df['result']  # Resultado do jogo (vitória/empate/derrota)

# Dividindo os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar o pipeline de processamento e treinamento
pipeline = make_pipeline(StandardScaler(), LogisticRegression())

# Treinando o modelo
pipeline.fit(X_train, y_train)

# Função para prever o resultado
def prever_resultado(gol_time_casa, gol_time_fora):
    # Realizando a previsão
    previsao = pipeline.predict([[gol_time_casa, gol_time_fora]])

    # Retorna a previsão como string
    return f"Apostar no {previsao[0]}"
