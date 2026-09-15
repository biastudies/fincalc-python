"""Regras de negócio relacionadas a financiamentos."""


class ServicoFinanciamento:
    """Cálculos de empréstimos e financiamentos."""

    def calcular_parcela_price(
        self, valor_emprestimo: float, taxa_mensal: float, meses: int
    ) -> float:
        """Calcula o valor da parcela fixa em um financiamento pela Tabela Price.

        Args:
            valor_emprestimo: valor total financiado.
            taxa_mensal: taxa de juros ao mês, em porcentagem.
            meses: quantidade de parcelas.

        Returns:
            Valor de cada parcela mensal.
        """
        i = taxa_mensal / 100
        parcela = (
            valor_emprestimo * (i * ((1 + i) ** meses)) / (((1 + i) ** meses) - 1)
        )
        return parcela
