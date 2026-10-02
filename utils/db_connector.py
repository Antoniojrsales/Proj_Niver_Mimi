import pandas as pd
import streamlit as st
from utils.data_processing import process_data

#-- 🗂️Acessa as credenciais do secrets.toml --#
try:
    SHEET_ID = st.secrets["SHEET"]["SHEET_ID"]
except KeyError:
    st.error("SHEET_ID não encontrado no arquivo secrets.toml. Por favor, verifique as credenciais.")
    st.stop()

@st.cache_data(ttl=600)  # Recarrega a cada 10 minutos
def load_data(sheet_id: str, gid: str = "0") -> pd.DataFrame:
    """Busca o CSV público/compartilhado do Google Sheets e processa."""
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"
    
    try:
        data = pd.read_csv(url)
        if data.empty:
            return pd.DataFrame()
            
        df_dados = process_data(data)
        return df_dados

    except Exception as e:
        # Erros reais (ex: sem internet ou permissão negada)
        st.error(f"Erro ao carregar a planilha: {e}")
        return pd.DataFrame()


#-- 🚀 Como consumir no app principal --#
df = load_data(SHEET_ID)

if not df.empty:
    st.session_state['logged_in'] = True
    st.session_state['df_niver_mimi'] = df
    
else:
    st.warning("Nenhum dado encontrado na planilha.")