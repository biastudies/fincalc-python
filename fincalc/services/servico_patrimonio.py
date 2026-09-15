"""Regras de negócio relacionadas a ativos e patrimônio."""


class ServicoPatrimonio:
    """Cálculos sobre ativos corporativos."""

    def calcular_depreciacao_linear(
        self, valor_inicial: float, valor_residual: float, vida_util_anos: int
    ) -> float:
        """Calcula o valor de depreciação anual de um ativo corporativo.

        Args:
            valor_inicial: valor de aquisição do ativo.
            valor_residual: valor estimado ao fim da vida útil.
            vida_util_anos: quantidade de anos de uso previstos.

        Returns:
            Valor depreciado a cada ano, igual em todos os anos.
        """
        return (valor_inicial - valor_residual) / vida_util_anos
