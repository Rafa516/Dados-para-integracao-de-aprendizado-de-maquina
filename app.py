import streamlit as st
import pandas as pd
import joblib

# Título da aplicação
st.title("Previsão de Evasão Escolar")

# Carregar o modelo salvo
model = joblib.load('modelo_evasao_escolar.pkl')

# Entradas do usuário
st.sidebar.header("Informações do Estudante")

idade = st.sidebar.number_input("Idade", min_value=6, max_value=18, value=12)
frequencia = st.sidebar.number_input("Frequência (%)", min_value=0, max_value=100, value=80)
nota_media = st.sidebar.number_input("Nota Média", min_value=0.0, max_value=10.0, value=7.5)
distancia_escola = st.sidebar.number_input("Distância da Escola (km)", min_value=1, max_value=20, value=5)
situacao_socioeconomica = st.sidebar.selectbox("Situação Socioeconômica", ["baixa", "media", "alta"])

# Converter a situação socioeconômica em variáveis dummy
situacao_dummy = pd.get_dummies([situacao_socioeconomica], prefix='situacao_socioeconomica', drop_first=True)

# Criar um DataFrame com os dados de entrada
input_data = pd.DataFrame({
    'idade': [idade],
    'frequencia': [frequencia],
    'nota_media': [nota_media],
    'distancia_escola': [distancia_escola]
})

# Adicionar as colunas dummy ao DataFrame de entrada
input_data = pd.concat([input_data, situacao_dummy], axis=1)

# Garantir que todas as colunas necessárias estejam presentes
# (caso alguma categoria não tenha sido selecionada, preencher com 0)
required_columns = ['idade', 'frequencia', 'nota_media', 'distancia_escola', 
                    'situacao_socioeconomica_media', 'situacao_socioeconomica_alta']
for col in required_columns:
    if col not in input_data.columns:
        input_data[col] = 0

# Reordenar as colunas para corresponder ao modelo treinado
input_data = input_data[required_columns]

# Botão para fazer a previsão
if st.sidebar.button("Prever Evasão"):
    # Fazer a previsão
    prediction = model.predict(input_data)
    probabilidade = model.predict_proba(input_data)[0]

    # Exibir o resultado
    st.write("### Resultado da Previsão")
    if prediction[0] == 1:
        st.error("O estudante está em **risco de evasão**.")
    else:
        st.success("O estudante **não está em risco de evasão**.")

    st.write(f"Probabilidade de evasão: {probabilidade[1] * 100:.2f}%")