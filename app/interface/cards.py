# cards.py
# Componentes visuais (cards premium) do Fluxo 3.0

import streamlit as st

def card_kpi(titulo, valor, unidade=""):
    st.markdown(
        f"""
        <div style="
            padding:16px;
            border-radius:12px;
            background:#f8f9fa;
            border:1px solid #e1e1e1;
            text-align:center;">
            <h4 style="margin-bottom:4px;">{titulo}</h4>
            <h2 style="margin-top:0;"><b>{valor} {unidade}</b></h2>
        </div>
        """,
        unsafe_allow_html=True
    )

def card_destaque(titulo, valor):
    st.markdown(
        f"""
        <div style="
            padding:20px;
            border-radius:12px;
            background:#eef3ff;
            border:1px solid #c3d3ff;
            text-align:center;">
            <h3 style="margin-bottom:6px;">{titulo}</h3>
            <h2 style="margin-top:0; color:#1c3faa"><b>{valor}</b></h2>
        </div>
        """,
        unsafe_allow_html=True
    )
