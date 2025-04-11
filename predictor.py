import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Carrega os dados do CSV
try:
    df = pd.read_csv("historico_jogos.csv")
except FileNotFoundError:
    print("Arquivo 'historico_jogos.csv' não encontrado. Coloque ele na mesma pasta do script.")
    exit()

# Cria uma feature simples: diferença de gols
df["goal_diff"] = df["home_goals"] - df["away_goals"]

# Adicionando mais features para melhorar a acurácia
df["home_win"] = (df["home_goals"] > df["away_goals"]).astype(int)
df["away_win"] = (df["away_goals"] > df["home_goals"]).astype(int)

# Define X (features) e y (alvo)
X = df[["goal_diff", "home_win", "away_win"]]
y = df["result"]

# Divide em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Cria e treina o modelo
model = RandomForestClassifier(n_estimators=100, random_state=42)  # Ajuste no número de árvores
model.fit(X_train, y_train)

# Avalia o modelo
pred = model.predict(X_test)
acc = accuracy_score(y_test, pred)
print("Acurácia do modelo:", round(acc * 100, 2), "%")

# Função de previsão
def prever_resultado(gol_time_casa, gol_time_fora):
    dif = gol_time_casa - gol_time_fora
    home_win = 1 if gol_time_casa > gol_time_fora else 0
    away_win = 1 if gol_time_fora > gol_time_casa else 0
    entrada = pd.DataFrame({"goal_diff": [dif], "home_win": [home_win], "away_win": [away_win]})
    return model.predict(entrada)[0]
