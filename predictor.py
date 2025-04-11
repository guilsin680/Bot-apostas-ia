import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from collections import Counter

# Utilize o CSV expandido
csv_file = "historico_jogos_expandido.csv"

try:
    df = pd.read_csv(csv_file)
except FileNotFoundError:
    print(f"Arquivo '{csv_file}' não encontrado. Coloque-o na mesma pasta do script.")
    exit()

# Cria uma feature simples: diferença de gols
df["goal_diff"] = df["home_goals"] - df["away_goals"]

# Neste exemplo, utilizamos as seguintes features:
features = ["goal_diff", "home_last5_avg", "away_last5_avg", "pos_home", "pos_away"]
X = df[features]
y = df["result"]

# Dividindo os dados para treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Calcula o número mínimo de amostras por classe no conjunto de treino
class_counts = Counter(y_train)
min_count = min(class_counts.values())
# Ajusta o número de folds: não pode ser maior que o mínimo de amostras em nenhuma classe
num_cv = max(2, min(5, min_count))
print("Usando validação cruzada com {} folds".format(num_cv))

# Cria um pipeline com escalonamento e RandomForest
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("rf", RandomForestClassifier(n_estimators=100, random_state=42))
])

# Uso de cross-validation para avaliar o desempenho
cv_scores = cross_val_score(pipeline, X_train, y_train, cv=num_cv)
print("CV Scores:", cv_scores)
print("Média CV Score:", round(cv_scores.mean() * 100, 2), "%")

# Treina o modelo final com o conjunto de treino completo
pipeline.fit(X_train, y_train)

# Avalia o modelo no conjunto de teste
predictions = pipeline.predict(X_test)
print("Acurácia do modelo no conjunto de teste:", round(accuracy_score(y_test, predictions) * 100, 2), "%")

# Função de previsão para ser utilizada pelo bot
def prever_resultado(gol_time_casa, gol_time_fora, home_last5_avg=1.5, away_last5_avg=1.3, pos_home=3, pos_away=5):
    """
    Recebe os parâmetros do jogo e retorna a previsão:
      - gol_time_casa: gols marcados pelo time da casa no jogo atual
      - gol_time_fora: gols sofridos pelo time visitante no jogo atual
      - home_last5_avg: média de gols marcados nos últimos 5 jogos (pode ser ajustada)
      - away_last5_avg: média de gols sofridos pelo visitante nos últimos 5 jogos
      - pos_home: posição atual do time da casa
      - pos_away: posição atual do time visitante
    """
    dif = gol_time_casa - gol_time_fora
    entrada = pd.DataFrame({
        "goal_diff": [dif],
        "home_last5_avg": [home_last5_avg],
        "away_last5_avg": [away_last5_avg],
        "pos_home": [pos_home],
        "pos_away": [pos_away]
    })
    return pipeline.predict(entrada)[0]

# Exemplo de uso:
if __name__ == "__main__":
    print("Exemplo: Time da casa fez 2 gols, visitante 1")
    resultado_previsto = prever_resultado(2, 1)
    print("Previsão:", resultado_previsto)
