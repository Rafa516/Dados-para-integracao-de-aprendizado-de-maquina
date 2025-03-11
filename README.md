# Dados para integração de aprendizado de máquina

# App Evasão Escolar
- **Modelo de testes de Aprendizagem:** [Link para o App](https://dados-para-integracao-de-aprendizado-de-maquina-hcqrmqmwsfkokf.streamlit.app/).

## 1. Objetivo do Aplicativo

O aplicativo tem como objetivo prever o risco de evasão escolar de estudantes da educação básica e treinar modelos de machine learning.

Ele usa um modelo de machine learning treinado para classificar se um estudante está em risco de evasão (classe 1) ou não (classe 0).

## 2. Funcionalidades

- **Entrada de Dados:** O usuário pode inserir informações sobre o estudante, como idade, frequência escolar, nota média, distância da escola e situação socioeconômica.
- **Previsão:** Com base nos dados inseridos, o aplicativo faz uma previsão sobre o risco de evasão.
- **Resultado:** O resultado é exibido como _"Em risco de evasão"_ ou _"Não está em risco de evasão"_, juntamente com a probabilidade de evasão.
- **Consumo de API:** O aplicativo pode consumir dados de uma API externa para preencher automaticamente os campos de entrada, permitindo que o usuário visualize e edite os dados antes de fazer a previsão.

## 3. Tecnologias Utilizadas

- **Streamlit:** Framework para criar interfaces web simples e interativas.
- **Pandas:** Biblioteca para manipulação e análise de dados.
- **Scikit-learn:** Biblioteca para machine learning (treinamento e previsão do modelo).
- **Joblib:** Biblioteca para salvar e carregar modelos de machine learning.
- **Imbalanced-learn:** Biblioteca para balanceamento de dados (uso do SMOTE).
- **FastAPI:** Framework para criar a API que fornece os dados dos estudantes.
- **Requests:** Biblioteca para fazer requisições HTTP e consumir a API.

## 4. Fluxo de Funcionamento

### Carregamento do Modelo

O aplicativo carrega o modelo de machine learning salvo (`modelo_evasao_escolar.pkl`).

### Entrada de Dados

O usuário pode escolher entre duas opções para fornecer os dados:
1. **Inserir Manualmente:** O usuário insere as informações do estudante na barra lateral.
2. **Carregar da API:** O aplicativo consome dados de uma API externa e preenche automaticamente os campos de entrada.

### Pré-processamento

Os dados inseridos são convertidos em um formato adequado para o modelo (codificação one-hot para variáveis categóricas).

### Previsão

O modelo faz a previsão com base nos dados inseridos.

### Exibição do Resultado

O resultado da previsão é exibido na tela, junto com a probabilidade de evasão.

## 5. Modelo de Machine Learning

- **Algoritmo:** Random Forest (Floresta Aleatória).

### Treinamento

O modelo foi treinado com um conjunto de dados sintéticos contendo informações como idade, frequência escolar, nota média, distância da escola e situação socioeconômica.

Para lidar com o desbalanceamento das classes, foi utilizado o SMOTE (_Synthetic Minority Over-sampling Technique_).

### Avaliação

O modelo foi avaliado usando métricas como **F1-score, precisão, recall e AUC-ROC**.

## 6. Balanceamento de Dados

O conjunto de dados original estava desbalanceado, com poucos exemplos de evasão (classe 1).

Para corrigir isso, foi aplicado o **SMOTE**, que gera exemplos sintéticos da classe minoritária, equilibrando as classes.

## 7. Interface do Usuário

- **Barra Lateral:** Contém campos para inserir as informações do estudante e uma opção para carregar dados da API.
- **Área Principal:** Exibe o resultado da previsão e a probabilidade de evasão.
- **Botão de Previsão:** Quando clicado, o aplicativo faz a previsão com base nos dados inseridos.

## 8. Pré-requisitos e Instalação

### Bibliotecas Necessárias

- Streamlit
- Pandas
- Scikit-learn
- Joblib
- Imbalanced-learn
- FastAPI
- Requests

### Instalação

As bibliotecas podem ser instaladas usando o comando:

```bash
pip install streamlit pandas scikit-learn joblib imbalanced-learn fastapi requests
```
## 9. API de Dados

### Funcionalidades da API

A API foi desenvolvida usando o **FastAPI** e hospedada no **Render**. Ela fornece dados de estudantes em formato JSON, que podem ser consumidos pelo aplicativo Streamlit.

- **Endpoint `/students/`:** Retorna uma lista de estudantes com informações como idade, frequência escolar, nota média, distância da escola e situação socioeconômica.
- **Endpoint `/student/`:** Retorna os dados de um único estudante.

### Consumo da API no Aplicativo

O aplicativo Streamlit consome a API para preencher automaticamente os campos de entrada. Quando o usuário seleciona a opção "Carregar da API", os dados são obtidos da API e exibidos na interface, permitindo que o usuário edite os valores antes de fazer a previsão.

## 10. Melhorias Futuras

- **Adicionar Mais Features:** Incluir variáveis como histórico de reprovações, participação em atividades extracurriculares, etc.
- **Interface Mais Amigável:** Adicionar gráficos e explicações sobre os fatores que influenciam a previsão.
- **Consumo de API de dados:** Consumir os dados através de fontes externas em tempo real, o qual seria benéfico para a integração com outros sistemas e a escalabilidade.
- **Expansão da API:** Adicionar mais endpoints para permitir a inserção e atualização de dados de estudantes.


