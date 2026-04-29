#calculos

"""
app/calculos.py - Motor Matemático
"""
from app.fatores import EMISSOES_MATERIAIS

def calcular_emissoes_totais(volumes: dict, perdas_percentual: float, fatores_usuario: dict, precos_dinamicos: dict) -> dict:
    detalhamento = {}
    total_bruto_t = 0.0

    for material, quantidade in volumes.items():
        if material in EMISSOES_MATERIAIS and quantidade > 0:
            fator = fatores_usuario.get(material, EMISSOES_MATERIAIS[material]["fator"])
            unidade = EMISSOES_MATERIAIS[material]["unidade"]
            emissao_t = (quantidade * fator) / 1000
            
            detalhamento[material] = {
                "emissao": round(emissao_t, 3),
                "quantidade": round(quantidade, 3),
                "unidade": unidade,
                "fator_utilizado": fator 
            }
            total_bruto_t += emissao_t

    emissao_perdas_t = total_bruto_t * perdas_percentual
    total_com_perdas_t = total_bruto_t + emissao_perdas_t

    custos_compensacao = {mercado: round(total_com_perdas_t * preco, 2) for mercado, preco in precos_dinamicos.items()}

    return {
        "detalhamento": detalhamento,
        "total_bruto": round(total_bruto_t, 3),
        "perdas": round(emissao_perdas_t, 3),
        "total_com_perdas": round(total_com_perdas_t, 3),
        "custos_estimados": custos_compensacao
    }