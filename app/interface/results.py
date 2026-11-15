#results

import streamlit as st
import plotly.express as px
import pandas as pd

def render_graficos(resultados):
    st.header("Análise de Resultados Reais")
    
    # "Achatamos" os dados para o gráfico
    dados_grafico = []
    for mat, info in resultados["detalhamento"].items():
        if info["emissao"] > 0:
            dados_grafico.append({"Material": mat, "tCO2e": info["emissao"]})
    
    df_carbono = pd.DataFrame(dados_grafico)
    
    kpi1, kpi2 = st.columns(2)
    kpi1.metric("Pegada Total (CO2e)", f"{resultados['total_com_perdas']} t", f"Bruto: {resultados['total_bruto']} t")
    kpi2.metric("Emissão por Perdas (CO2e)", f"{resultados['perdas']} t", "Desperdício Físico", delta_color="inverse")
    
    st.divider()
    
    if not df_carbono.empty:
        st.subheader("Emissões Detalhadas por Material (tCO2e)")
        col1, col2 = st.columns(2)
        
        with col1:
            fig_bar = px.bar(df_carbono, x='Material', y='tCO2e', text_auto='.2f',
                             color='Material', title="Impacto Absoluto")
            st.plotly_chart(fig_bar, use_container_width=True)

        with col2:
            fig_pie = px.pie(df_carbono, values='tCO2e', names='Material', hole=0.4,
                             title="Proporção do Impacto",
                             color_discrete_sequence=px.colors.qualitative.Pastel)
            st.plotly_chart(fig_pie, use_container_width=True)
    else:
        st.info("Nenhum material selecionado.")

    st.divider()
    st.subheader("Custo de Compensação (R$)")
    df_financeiro = pd.DataFrame(list(resultados["custos_estimados"].items()), columns=["Mercado", "Preço (R$)"])
    fig_fin = px.bar(df_financeiro, x='Mercado', y='Preço (R$)', color='Mercado', text_auto='.2f')
    st.plotly_chart(fig_fin, use_container_width=True)
