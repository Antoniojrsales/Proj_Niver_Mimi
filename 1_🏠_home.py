import pandas as pd
import streamlit as st
from utils.data_processing import process_data
from utils.db_connector import load_data

st.set_page_config(page_title="Niver Mimi", 
                   page_icon="🎂",
                   layout="wide")

st.title("🎂 Niver Mimi - Acompanhamento da Aniversáriante")

st.subheader("Bem-vindo ao painel de acompanhamento da aniversariante Mimi! Aqui você pode visualizar e interagir com os dados relacionados aos aniversários.")

# Verifica se os dados já estão na sessão; se não estiverem, carrega
if 'df_niver_mimi' not in st.session_state or st.session_state['df_niver_mimi'].empty:
    try:
        sheet_id = st.secrets["SHEET"]["SHEET_ID"]
        with st.spinner("A carregar dados da planilha..."):
            st.session_state['df_niver_mimi'] = load_data(sheet_id)
            st.session_state['logged_in'] = True
    except KeyError:
        st.error("SHEET_ID não configurado nos secrets.")
        st.stop()

df_dados = st.session_state.get('df_niver_mimi', pd.DataFrame())

if df_dados.empty:
    st.warning("Dados não encontrados ou a planilha está vazia. Por favor, verifique a conexão com a planilha.")
    st.stop()

aba1, aba2 = st.tabs(["📊 Visualização de Dados", "📈 Inclusão de Dados"])

with aba1:
    st.subheader("Visualização de Dados")
    st.dataframe(df_dados)

    st.divider()
    st.markdown('Dimersao do DataFrame: ')
    st.markdown(f"Linhas: \t {df_dados.shape[0]}")
    st.markdown(f"Colunas: \t {df_dados.shape[1]}")
    st.divider()

st.markdown('Desenvolvido por [AntonioJrSales](https://antoniojrsales.github.io/meu_portfolio/)')
