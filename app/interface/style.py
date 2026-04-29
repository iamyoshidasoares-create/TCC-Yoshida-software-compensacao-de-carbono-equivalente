"""
app/interface/style.py - Injeção de Estética Computacional
Garante o visual premium do sistema.
"""
import streamlit as st

def aplicar_estilos():
    st.markdown("""
        <style>
        /* Estilização do Botão Principal */
        .stButton>button {
            width: 100%;
            border-radius: 8px;
            height: 50px;
            background-color: #004d40;
            color: white;
            font-size: 16px;
            font-weight: bold;
            border: none;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #00251a;
            border: 1px solid #004d40;
        }
        /* Ajuste dos Cards de KPI */
        div[data-testid="metric-container"] {
            background-color: #f8f9fa;
            border: 1px solid #e0e0e0;
            padding: 5% 5% 5% 10%;
            border-radius: 8px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
        }
        </style>
    """, unsafe_allow_html=True)