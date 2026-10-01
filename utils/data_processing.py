import pandas as pd
import streamlit as st
import numpy as np
from datetime import datetime

def process_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Processa os dados do DataFrame, tratando valores ausentes e convertendo tipos de dados.

    Args:
        df (pd.DataFrame): DataFrame contendo os dados a serem processados.

    Returns:
        pd.DataFrame: DataFrame com os dados processados.
    """
    if df.empty:
        st.warning("O DataFrame está vazio. Nenhum processamento será realizado.")
        return df

    if 'Data' in df.columns:
        # Converte a coluna 'Data' para o tipo datetime
        df['Data'] = pd.to_datetime(df['Data'], errors='coerce')

    if 'Parcelas_Restantes' in df.columns:
        # Substitui valores ausentes na coluna 'Parcelas_Restantes' por 0
        df['Parcelas_Restantes'] = df['Parcelas_Restantes'].fillna(0)
        df['Parcelas_Restantes'] = df['Parcelas_Restantes'].astype(int)

    lista_float = ['Valor_Total', 'Adiantamento', 'Valor_Parcela']
    if all(col in df.columns for col in lista_float):
        # Substitui valores ausentes nas colunas de float por 0.0
        df[lista_float] = df[lista_float].fillna(0.0)
        df[lista_float] = df[lista_float].astype(float)

    return df