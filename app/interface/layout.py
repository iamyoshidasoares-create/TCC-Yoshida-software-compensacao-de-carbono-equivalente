#Layout

"""
app/interface/layout.py - Orquestrador da Interface
"""
import streamlit as st
from app.interface.inputs import input_dados
from app.interface.results import render_graficos
from app.interface.style import aplicar_estilos
from app.calculos import calcular_emissoes_totais
from app.pdf_export import gerar_pdf_memorial
from app.fatores import EMISSOES_MATERIAIS, PRECOS_MERCADO
from app.services import *

def render_layout():
    aplicar_estilos()
    
    st.sidebar.title("Navegação")
    menu = st.sidebar.radio("Selecione a aba:", ["⚙️ Configurações Técnicas", "📊 Calculadora de Obra", "📈 Dashboard de Impacto", "📋 Memorial Técnico"])
    
    st.title("Sistema de Gestão de Carbono - TCC Beta")
    
    if 'fatores_personalizados' not in st.session_state:
        st.session_state.fatores_personalizados = {mat: info["fator"] for mat, info in EMISSOES_MATERIAIS.items()}
    if 'precos_dinamicos' not in st.session_state:
        st.session_state.precos_dinamicos = PRECOS_MERCADO.copy()
        
    for key in ['st_redd', 'st_euro', 'st_carb', 'st_verra', 'st_gold', 'st_moss', 'st_toucan']:
        if key not in st.session_state: st.session_state[key] = ("info", "Aguardando Sincronização...")

    if menu == "⚙️ Configurações Técnicas":
        st.header("Sincronização de Mercado (Real-Time Cloud)")
        
        st.subheader("🏢 Mercados Institucionais e Regulados")
        c1, c2, c3 = st.columns(3)
        with c1:
            if st.button("🔄 Sync REDD+ (USD)"):
                p, msg = buscar_preco_institucional_redd()
                st.session_state.precos_dinamicos["REDD+ Genérico (Base USD)"] = p
                st.session_state.st_redd = ("success", f"R$ {p} ({msg})")
            t, m = st.session_state.st_redd
            st.success(m) if t == "success" else st.info(m)
        with c2:
            if st.button("🔄 Sync Europa (EUR)"):
                p, msg = buscar_referencial_europa()
                st.session_state.precos_dinamicos["EU ETS Europa (Base EUR)"] = p
                st.session_state.st_euro = ("success", f"R$ {p} ({msg})")
            t, m = st.session_state.st_euro
            st.success(m) if t == "success" else st.info(m)
        with c3:
            if st.button("🔄 Sync Carbonext"):
                p, msg = buscar_preco_carbonext()
                st.session_state.precos_dinamicos["Carbonext (Balcão B2B BR)"] = p
                st.session_state.st_carb = ("warning", f"R$ {p} ({msg})")
            t, m = st.session_state.st_carb
            st.warning(m) if t == "warning" else st.info(m)

        st.divider()

        st.subheader("🥇 Padrões Globais de Certificação")
        c_v, c_g = st.columns(2)
        with c_v:
            if st.button("🔄 Sync Verra (VCS)"):
                p, msg = buscar_preco_verra()
                st.session_state.precos_dinamicos["Verra VCS (Premium)"] = p
                st.session_state.st_verra = ("success", f"R$ {p} ({msg})")
            t, m = st.session_state.st_verra
            st.success(m) if t == "success" else st.info(m)
        with c_g:
            if st.button("🔄 Sync Gold Standard"):
                p, msg = buscar_preco_gold_standard()
                st.session_state.precos_dinamicos["Gold Standard (Impacto ODS)"] = p
                st.session_state.st_gold = ("success", f"R$ {p} ({msg})")
            t, m = st.session_state.st_gold
            st.success(m) if t == "success" else st.info(m)

        st.divider()

        st.subheader("🪙 Mercado Secundário Web3 (Tokens)")
        st.info("**Nota Técnica:** Ativos digitais em blockchain (Spot Market). Devido à volatilidade, são úteis para análises financeiras comparativas e não para certificação final oficial.")
        
        c4, c5 = st.columns(2)
        with c4:
            if st.button("🔄 Sync Moss (MCO2)"):
                p, msg = buscar_preco_moss()
                st.session_state.precos_dinamicos["Token Moss MCO2 (Spot)"] = p
                st.session_state.st_moss = ("success" if "🟢" in msg else "warning", f"R$ {p} ({msg})")
            t, m = st.session_state.st_moss
            st.success(m) if t == "success" else st.warning(m) if t == "warning" else st.info(m)
        with c5:
            if st.button("🔄 Sync Toucan (BCT)"):
                p, msg = buscar_preco_toucan()
                st.session_state.precos_dinamicos["Token Toucan BCT (Spot)"] = p
                st.session_state.st_toucan = ("success" if "🟢" in msg else "warning", f"R$ {p} ({msg})")
            t, m = st.session_state.st_toucan
            st.success(m) if t == "success" else st.warning(m) if t == "warning" else st.info(m)

    elif menu == "📊 Calculadora de Obra":
        volumes, perda = input_dados()
        if st.button("Calcular Pegada de Carbono"):
            st.session_state.dados_calculados = calcular_emissoes_totais(volumes, perda, st.session_state.fatores_personalizados, st.session_state.precos_dinamicos)
            st.success("Cálculo pronto!")

    elif menu == "📈 Dashboard de Impacto":
        if 'dados_calculados' in st.session_state: render_graficos(st.session_state.dados_calculados)
        else: st.warning("Calcule primeiro.")

    elif menu == "📋 Memorial Técnico":
        st.header("Memorial de Engenharia")
        if 'dados_calculados' in st.session_state:
            pdf_buffer = gerar_pdf_memorial(st.session_state.dados_calculados)
            st.download_button("📥 Descarregar PDF", data=pdf_buffer, file_name="Memorial_Carbono.pdf", mime="application/pdf")