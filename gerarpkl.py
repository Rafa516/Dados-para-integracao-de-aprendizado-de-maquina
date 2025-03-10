import joblib
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

# Exemplo de dados
data = pd.DataFrame({
    'idade': [12, 15, 10, 14, 16],
    'frequencia': [85, 70, 95, 80, 60],
    'nota_media': [7.5, 6.0, 8.5, 7.0, 5.5],
    'situacao_socioeconomica': ['baixa', 'media', 'alta', 'baixa', 'media'],
    'distancia_escola': [10, 5, 2, 8, 15],
    'evasao': [0, 1, 0, 0, 1]
})

# Codificar variáveis categóricas
X = pd.get_dummies(data.drop('evasao', axis=1), columns=['situacao_socioeconomica'], drop_first=True)
y = data['evasao']

# Treinar o modelo
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# Salvar o modelo
joblib.dump(model, 'modelo_evasao_escolar.pkl')
print("Modelo salvo como 'modelo_evasao_escolar.pkl'")