import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score

def prever_resultado():
    # Carregar o dataset
    df = pd.read_csv('data.csv')  # Seu CSV deve ter as colunas 'home_goals' e 'away_goals'
    
    # Pré-processamento
    df['gol_time_casa'] = df['home_goals']
    df['gol_time_fora'] = df['away_goals']
    
    # Features e alvo
    X = df[['gol_time_casa', 'gol_time_fora']]  # Gols dos times
    y = df['result']  # Resultado da partida (vitória, derrota, empate)
    
    # Dividir em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Normalização
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    # Treinamento do modelo
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    # Acurácia do modelo no conjunto de teste
    accuracy = model.score(X_test, y_test)
    
    # Validando com validação cruzada
    cv_scores = cross_val_score(model, X, y, cv=2)
    print(f"CV Scores: {cv_scores}")
    print(f"Média CV Score: {cv_scores.mean() * 100:.2f}%")
    
    # Predição
    prediction = model.predict([[1, 2]])  # Exemplo de previsão (1 gol em casa e 2 fora)
    
    return prediction[0]
