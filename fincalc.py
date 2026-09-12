# FinCalc - Sistema de Cálculos Financeiros em Python


def calcular_juros_simples(
    capital: float, taxa_anual: float, anos: int
) -> float:
    """Calcula o montante final obtido por juros simples."""
    juros = capital * (taxa_anual / 100) * anos
    return capital + juros


def calcular_aposentadoria(
    patrimonio_atual: float,
    aporte_mensal: float,
    anos: int,
    taxa_anual: float,
) -> float:
    """Calcula o patrimônio acumulado para aposentadoria."""
    meses = anos * 12
    taxa_mensal = (taxa_anual / 100) / 12
    saldo = patrimonio_atual

    for _ in range(meses):
        saldo = (saldo + aporte_mensal) * (1 + taxa_mensal)

    return saldo


def calcular_irrf(salario_bruto: float) -> float:
    """Calcula a alíquota simplificada de Imposto de Renda Retido na Fonte."""
    if salario_bruto <= 2259.20:
        return 0.0
    elif salario_bruto <= 2826.65:
        return (salario_bruto * 0.075) - 169.44
    elif salario_bruto <= 3751.05:
        return (salario_bruto * 0.15) - 381.44
    else:
        return (salario_bruto * 0.225) - 662.77


def calcular_parcela_price(
    valor_emprestimo: float,
    taxa_mensal: float,
    meses: int
) -> float:

    """Calcula o valor da parcela fixa em um financiamento pela Tabela Price."""
    i = taxa_mensal / 100
    parcela = valor_emprestimo * (i * ((1 + i) ** meses)) / (((1 + i) ** meses) - 1)
    return parcela


if __name__ == "__main__":
    print("Iniciando o sistema FinCalc...")

    montante = calcular_juros_simples(1000.0, 5.0, 2)
    print(
        f"Juros Simples (R$ 1.000 a 5% por 2 anos): "
        f"R$ {montante:.2f}"
    )

    patrimonio = calcular_aposentadoria(
        10000.0, 500.0, 20, 6.0
    )
    print(
        f"Patrimônio Estimado para Aposentadoria: "
        f"R$ {patrimonio:.2f}"
    )

    salario = 3000.00
    imposto = calcular_irrf(salario)

    print(
        f"IRRF sobre R$ {salario:.2f}: "
        f"R$ {imposto:.2f}"
    )

    valor_emprestimo = 10000.00
    taxa_mensal = 2.0
    meses = 12

    parcela = calcular_parcela_price(
        valor_emprestimo,
        taxa_mensal,
        meses
    )

    print(
        f"Tabela Price (R$ {valor_emprestimo:.2f} "
        f"a {taxa_mensal:.1f}% por {meses} meses): "
        f"R$ {parcela:.2f}"
    )

def calcular_valor_futuro(
    aporte_mensal: float, taxa_mensal: float, meses: int
) -> float:
    """Calcula o valor futuro segundo a regra especificada no laboratorio."""
    if aporte_mensal < 0:
        raise ValueError("O aporte mensal nao pode ser negativo.")
    if meses < 0:
        raise ValueError("A quantidade de meses nao pode ser negativa.")
    if taxa_mensal < 0:
        raise ValueError("A taxa mensal nao pode ser negativa.")

    if meses == 0:
        return 0.0

    taxa = taxa_mensal / 100
    total_aportado = aporte_mensal * meses
    return total_aportado * (1 + taxa) ** (meses - 1)
