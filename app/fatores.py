#fatores

"""
app/fatores.py - Base de Dados e Cotações Base
"""

from app.services import *

EMISSOES_MATERIAIS = {
    "Concreto C25": {"fator": 173.81, "unidade": "m³"},
    "Concreto C30": {"fator": 252.00, "unidade": "m³"},
    "Aço": {"fator": 1.90, "unidade": "kg"},
    "Formas (Madeira)": {"fator": 50.60, "unidade": "m³"}
}

# Inicialização Cloud-Ready
p_redd, _ = buscar_preco_institucional_redd()
p_euro, _ = buscar_referencial_europa()
p_verra, _ = buscar_preco_verra()
p_gold, _ = buscar_preco_gold_standard()
p_moss, _ = buscar_preco_moss()
p_toucan, _ = buscar_preco_toucan()

PRECOS_MERCADO = {
    "REDD+ Genérico (Base USD)": p_redd,
    "EU ETS Europa (Base EUR)": p_euro,
    "Carbonext (Balcão B2B BR)": 49.00,
    "Verra VCS (Premium)": p_verra,
    "Gold Standard (Impacto ODS)": p_gold,
    "Token Moss MCO2 (Spot)": p_moss,
    "Token Toucan BCT (Spot)": p_toucan
}