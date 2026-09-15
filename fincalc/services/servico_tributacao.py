"""Regras de negócio relacionadas a tributação."""


class ServicoTributacao:
    """Cálculos de impostos sobre a renda.

    As faixas e deduções ficam no código por serem constantes do domínio,
    não variam por ambiente.
    """

    def calcular_irrf(self, salario_bruto: float) -> float:
        """Calcula a alíquota simplificada de Imposto de Renda Retido na Fonte.

        Aplica a tabela progressiva: isento até 2259.20, depois 7,5%, 15%
        e 22,5%, cada faixa com sua parcela a deduzir.

        Args:
            salario_bruto: salário mensal antes dos descontos.

        Returns:
            Valor do imposto a reter. Zero para a faixa isenta.
        """
        if salario_bruto <= 2259.20:
            return 0.0
        elif salario_bruto <= 2826.65:
            return (salario_bruto * 0.075) - 169.44
        elif salario_bruto <= 3751.05:
            return (salario_bruto * 0.15) - 381.44
        else:
            return (salario_bruto * 0.225) - 662.77
