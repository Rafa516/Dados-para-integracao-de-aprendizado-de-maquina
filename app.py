import streamlit as st
import pandas as pd
import joblib
import os

# Título da aplicação
st.title("Previsão de Evasão Escolar")

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

    # Entradas do usuário
    st.sidebar.header("Informações do Estudante")

    idade = st.sidebar.number_input("Idade", min_value=6, max_value=18, value=12)
    frequencia = st.sidebar.number_input("Frequência (%)", min_value=0, max_value=100, value=80)
    nota_media = st.sidebar.number_input("Nota Média", min_value=0.0, max_value=10.0, value=7.5)
    distancia_escola = st.sidebar.number_input("Distância da Escola (km)", min_value=1, max_value=20, value=5)
    situacao_socioeconomica = st.sidebar.selectbox("Situação Socioeconômica", ["baixa", "media", "alta"])

    # Criar um DataFrame com os dados de entrada
    input_data = pd.DataFrame({
        'idade': [idade],
        'frequencia': [frequencia],
        'nota_media': [nota_media],
        'distancia_escola': [distancia_escola],
        'situacao_socioeconomica_baixa': [0],  # Inicializar com 0
        'situacao_socioeconomica_media': [0],  # Inicializar com 0
    })

    # Atualizar as colunas dummy com base na seleção do usuário
    if situacao_socioeconomica == "baixa":
        input_data['situacao_socioeconomica_baixa'] = 1
    elif situacao_socioeconomica == "media":
        input_data['situacao_socioeconomica_media'] = 1

    # Reordenar as colunas para corresponder ao modelo treinado
    required_columns = ['idade', 'frequencia', 'nota_media', 'distancia_escola', 
                        'situacao_socioeconomica_baixa', 'situacao_socioeconomica_media']
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