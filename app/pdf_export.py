"""
app/pdf_export.py - Motor PDF usando BytesIO (Evita erros em Servidores Web)
"""
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
from io import BytesIO
from datetime import datetime

def gerar_pdf_memorial(dados_calculados):
    # Usar BytesIO é obrigatório para o sistema funcionar via link/nuvem
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    p.setFont("Helvetica-Bold", 16)
    p.drawString(50, height - 50, "oii zecao, te amu")
    
    p.setFont("Helvetica", 10)
    p.drawString(50, height - 70, f"Documento Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    p.line(50, height - 80, width - 50, height - 80)

    y_pos = height - 110
    p.setFont("Helvetica-Bold", 12)
    p.drawString(50, y_pos, "1. Resumo da Pegada de Carbono da Obra")
    y_pos -= 25
    p.setFont("Helvetica", 11)
    p.drawString(60, y_pos, f"Pegada de Carbono Bruta: {dados_calculados['total_bruto']} tCO2e")
    y_pos -= 15
    p.drawString(60, y_pos, f"Adicional de Perdas: {dados_calculados['perdas']} tCO2e")
    y_pos -= 20
    p.setFont("Helvetica-Bold", 11)
    p.drawString(60, y_pos, f"TOTAL A COMPENSAR: {dados_calculados['total_com_perdas']} tCO2e")

    y_pos -= 45
    p.setFont("Helvetica-Bold", 12)
    p.drawString(50, y_pos, "2. Memória de Cálculo por Insumo")
    
    data_materiais = [["Material", "Quantidade", "Fator (kg/un)", "Subtotal (tCO2e)"]]
    for mat, info in dados_calculados['detalhamento'].items():
        data_materiais.append([mat, f"{info['quantidade']} {info['unidade']}", f"{info['fator_utilizado']}", f"{info['emissao']}"])

    t_mat = Table(data_materiais, colWidths=[160, 100, 110, 100])
    t_mat.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey), ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke), ('ALIGN', (0, 0), (-1, -1), 'CENTER'), ('GRID', (0, 0), (-1, -1), 0.5, colors.black), ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')]))
    t_mat.wrapOn(p, width, height)
    y_pos -= (len(data_materiais)*18 + 10)
    t_mat.drawOn(p, 50, y_pos)

    y_pos -= 40
    p.setFont("Helvetica-Bold", 12)
    p.drawString(50, y_pos, "3. Análise Financeira (Cenários)")
    
    data_financeira = [["Fonte de Crédito / Benchmark", "Custo Total Estimado"]]
    for mercado, custo in dados_calculados['custos_estimados'].items():
        data_financeira.append([mercado, f"R$ {custo:,.2f}"])

    t_fin = Table(data_financeira, colWidths=[270, 200])
    t_fin.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.darkgreen), ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke), ('GRID', (0, 0), (-1, -1), 0.5, colors.black), ('ALIGN', (1, 0), (1, -1), 'RIGHT'), ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')]))
    t_fin.wrapOn(p, width, height)
    y_pos -= (len(data_financeira)*18 + 10)
    t_fin.drawOn(p, 50, y_pos)

    p.setFont("Helvetica-Oblique", 8)
    p.line(50, 60, width - 50, 60)
    p.drawString(50, 45, "* Cotações baseadas em tempo real e referências institucionais via ecossistema web.")
    p.showPage()
    p.save()
    
    buffer.seek(0)
    return buffer
