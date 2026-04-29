#inputs.py

import streamlit as st

def input_dados():
    st.subheader("Quantitativos da Obra")
    
    volumes_processados = {}
    col1, col2 = st.columns(2)
    
    with col1:
        volumes_processados["Concreto C25"] = st.number_input("Volume de Concreto C25 (m³)", min_value=0.0, step=1.0)
        volumes_processados["Concreto C30"] = st.number_input("Volume de Concreto C30 (m³)", min_value=0.0, step=1.0)
        
    with col2:
        volumes_processados["Aço"] = st.number_input("Peso de Aço (kg)", min_value=0.0, step=10.0)
        area_formas = st.number_input("Área de Formas (Madeira) (m²)", min_value=0.0, step=1.0)

    st.divider()
    st.subheader("Configurações Geométricas de Formas")
    st.info("O fator de emissão da madeira é volumétrico (m³). Informe a espessura para conversão.")
    
    espessura_mm = st.number_input("Espessura da chapa de madeira (mm)", min_value=1.0, value=18.0, step=1.0)
    
    # Cálculo de Conversão: m2 * (mm / 1000) = m3
    volumes_processados["Formas (Madeira)"] = area_formas * (espessura_mm / 1000)

    st.divider()
    st.subheader("Eficiência do Canteiro (Perdas)")
    perda_inteira = st.slider("Taxa de Perda de Material (%)", 5, 15, 10)
    
    return volumes_processados, (perda_inteira / 100.0)