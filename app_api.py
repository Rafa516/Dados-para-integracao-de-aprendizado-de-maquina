# app.py
import streamlit as st
import pandas as pd
import joblib
import os
import requests

# Título da aplicação
st.title("Previsão de Evasão Escolar")

# URL da API hospedada no Render
API_URL = "https://dados-para-integracao-de-aprendizado-de.onrender.com"  # Substitua pelo URL da sua API no Render

# Função para obter dados da API
def get_student_data():
    response = requests.get(f"{API_URL}/students/")  # Endpoint para obter todos os estudantes
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

    # Sidebar para escolher a fonte dos dados
    st.sidebar.header("Escolha a fonte dos dados")
    data_source = st.sidebar.radio("Selecione a fonte:", ("Inserir Manualmente", "Carregar da API"))

    # Variáveis para armazenar os dados
    idade = None
    frequencia = None
    nota_media = None
    distancia_escola = None
    situacao_socioeconomica = None

    if data_source == "Inserir Manualmente":
        # Entradas do usuário (inputs manuais)
        st.sidebar.header("Informações do Estudante")
        idade = st.sidebar.number_input("Idade", min_value=6, max_value=18, value=12)
        frequencia = st.sidebar.number_input("Frequência (%)", min_value=0, max_value=100, value=80)
        nota_media = st.sidebar.number_input("Nota Média", min_value=0.0, max_value=10.0, value=7.5)
        distancia_escola = st.sidebar.number_input("Distância da Escola (km)", min_value=1, max_value=20, value=5)
        situacao_socioeconomica = st.sidebar.selectbox("Situação Socioeconômica", ["baixa", "media", "alta"])

    elif data_source == "Carregar da API":
        # Carregar os dados da API automaticamente
        student_data_list = get_student_data()
        if student_data_list:
            # Pegar o primeiro estudante da lista (ou qualquer outro critério)
            student_data = student_data_list[0]

            # Preencher os inputs com os dados da API
            idade = student_data['idade']
            frequencia = student_data['frequencia']
            nota_media = student_data['nota_media']
            distancia_escola = student_data['distancia_escola']
            situacao_socioeconomica = student_data['situacao_socioeconomica']

            # Exibir os inputs preenchidos com os dados da API
            st.sidebar.header("Informações do Estudante (Carregadas da API)")
            idade = st.sidebar.number_input("Idade", min_value=6, max_value=18, value=idade)
            frequencia = st.sidebar.number_input("Frequência (%)", min_value=0, max_value=100, value=frequencia)
            nota_media = st.sidebar.number_input("Nota Média", min_value=0.0, max_value=10.0, value=nota_media)
            distancia_escola = st.sidebar.number_input("Distância da Escola (km)", min_value=1, max_value=20, value=distancia_escola)
            situacao_socioeconomica = st.sidebar.selectbox("Situação Socioeconômica", ["baixa", "media", "alta"], index=["baixa", "media", "alta"].index(situacao_socioeconomica))

    # Botão para fazer a previsão (disponível em ambos os modos)
    if st.sidebar.button("Prever Evasão"):
        if idade is not None and frequencia is not None and nota_media is not None and distancia_escola is not None and situacao_socioeconomica is not None:
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
        else:
            st.error("Por favor, insira os dados do estudante ou carregue os dados da API.")