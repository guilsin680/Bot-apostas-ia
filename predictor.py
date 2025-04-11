import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import os

# Carregando os dados
df = pd.read_csv("data.csv")

print("Colunas no arquivo CSV:", df.columns)

# Ajusta os nomes das colunas para os que estão no CSV
X = df[['home_goals', 'away_goals']]
y = df['result']

# Pré-processamento
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Dividir dados para treino/teste
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2)

# Treinamento
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Validação cruzada (opcional, só para análise)
scores = cross_val_score(model, X_scaled, y, cv=2)
print("Usando validação cruzada com 2 folds")
print("CV Scores:", scores)
print("Média CV Score:", round(scores.mean() * 100, 2), "%")
print("Acurácia do modelo no conjunto de teste:", round(model.score(X_test, y_test) * 100, 2), "%")

# Função de previsão
def prever_resultado(gol_time_casa, gol_time_fora):
    entrada = pd.DataFrame([[gol_time_casa, gol_time_fora]], columns=['home_goals', 'away_goals'])
    entrada_scaled = scaler.transform(entrada)
    predicao = model.predict(entrada_scaled)[0]

    from alerts import send_telegram_message
    send_telegram_message(f"Resultado previsto: {predicao}")

    return predicao
