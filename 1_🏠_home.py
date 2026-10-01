import pandas as pd
import streamlit as st
from utils.data_processing import process_data
from utils.db_connector import load_data

st.set_page_config(page_title="Niver Mimi", 
                   page_icon="🎂",
                   layout="wide")

st.title("🎂 Niver Mimi - Acompanhamento da Aniversáriante")

st.subheader("Bem-vindo ao painel de acompanhamento da aniversariante Mimi! Aqui você pode visualizar e interagir com os dados relacionados aos aniversários.")

if 'df_niver_mimi' in st.session_state:
    df = st.session_state['df_niver_mimi']

aba1, aba2 = st.tabs(["📊 Visualização de Dados", "📈 Inclusão de Dados"])

with aba1:
    st.subheader("Visualização de Dados")
    if not df.empty:
        st.dataframe(df)
    else:
        st.warning("Nenhum dado disponível para exibir.")

    st.divider()
    st.markdown('Dimersao do DataFrame: ')
    st.markdown(f"Linhas: \t {df.shape[0]}")
    st.markdown(f"Colunas: \t {df.shape[1]}")
    st.divider()

st.markdown('Desenvolvido por [AntonioJrSales](https://antoniojrsales.github.io/meu_portfolio/)')
