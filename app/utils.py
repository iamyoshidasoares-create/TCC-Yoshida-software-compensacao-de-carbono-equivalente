# utils.py
# Funções auxiliares de validação e formatação do Fluxo 3.0

# --------------------------------------------------------
# Formatações numéricas
# --------------------------------------------------------

def format_kg(valor):
    return f"{valor:.2f} kg CO₂e"


def arred(val: float, casas: int = 2) -> float:
    """Arredonda valores para o número de casas decimais."""
    return round(float(val), casas)


def format_kg(valor: float) -> str:
    """Formata valores em kg CO₂e com padrão brasileiro."""
    try:
        return f"{valor:,.2f} kg CO₂e".replace(",", "X").replace(".", ",").replace("X", ".")
    except:
        return "0,00 kg CO₂e"


def format_reais(valor: float) -> str:
    """Formata valores monetários em reais."""
    try:
        return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    except:
        return "R$ 0,00"

# --------------------------------------------------------
# Validações de entrada
# --------------------------------------------------------

def validar_volume(val) -> float:
    """Garante que o volume seja numérico e não negativo."""
    try:
        v = float(val)
        return max(v, 0)
    except:
        return 0.0


def validar_classe_concreto(classe: str) -> str:
    """Normaliza a classe do concreto (C25/C30)."""
    try:
        c = classe.upper().replace(" ", "")
        return c if c in ["C25", "C30"] else "C25"
    except:
        return "C25"
