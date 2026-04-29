"""
main.py - Ponto de Ignição do Sistema (Fluxo 4 Beta)
Orquestrador raiz da aplicação Streamlit.
"""
import streamlit as st
from app.interface.layout import render_layout

# Configuração global da página (Deve ser a primeira chamada do Streamlit)
st.set_page_config(
    page_title="Gestão de Carbono - TCC",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

if __name__ == "__main__":
    render_layout()