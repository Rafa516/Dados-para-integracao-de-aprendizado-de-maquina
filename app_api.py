# app.py
import streamlit as st
import pandas as pd
import joblib
import os
import requests

# Título da aplicação
st.title("Previsão de Evasão Escolar")

# URL da API
API_URL = "http://127.0.0.1:8000"  # Altere para o endereço da sua API

# Função para obter dados da API
def get_student_data():
    response = requests.get(f"{API_URL}/student/")
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Erro ao obter dados da API")
        return None

# Verificar se o arquivo do modelo existe
if not os.path.exists('modelo_evasao_escolar.pkl'):
    st.error("Arquivo 'modelo_evasao_escolar.pkl' não encontrado. Certifique-se de que o modelo foi salvo corretamente.")
else:
    # Carregar o modelo salvo
    try:
        model = joblib.load('modelo_evasao_escolar.pkl')
    except Exception as e:
        st.error(f"Erro ao carregar o modelo: {e}")
        st.stop()

    # Botão para carregar dados da API
    if st.sidebar.button("Carregar Dados da API"):
        student_data = get_student_data()
        if student_data:
            # Preencher os campos com os dados da API
            idade = student_data['idade']
            frequencia = student_data['frequencia']
            nota_media = student_data['nota_media']
            distancia_escola = student_data['distancia_escola']
            situacao_socioeconomica = student_data['situacao_socioeconomica']

            # Criar um DataFrame com os dados de entrada
            input_data = pd.DataFrame({
                'idade': [idade],
                'frequencia': [frequencia],
                'nota_media': [nota_media],
                'distancia_escola': [distancia_escola],
                'situacao_socioeconomica_baixa': [1 if situacao_socioeconomica == "baixa" else 0],
                'situacao_socioeconomica_media': [1 if situacao_socioeconomica == "media" else 0],
            })

            # Reordenar as colunas para corresponder ao modelo treinado
            required_columns = ['idade', 'frequencia', 'nota_media', 'distancia_escola', 
                               'situacao_socioeconomica_baixa', 'situacao_socioeconomica_media']
            input_data = input_data[required_columns]

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