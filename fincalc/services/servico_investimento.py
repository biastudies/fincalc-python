"""Regras de negócio relacionadas a investimentos."""


class ServicoInvestimento:
    """Cálculos de rendimento: juros simples, aposentadoria e valor futuro.

    Não possui estado. Todas as entradas chegam por parâmetro e as taxas
    são sempre informadas em porcentagem (ex.: 5.0 para 5%).
    """

    def calcular_juros_simples(
        self, capital: float, taxa_anual: float, anos: int
    ) -> float:
        """Calcula o montante final obtido por juros simples.

        Args:
            capital: valor inicial aplicado.
            taxa_anual: taxa de juros ao ano, em porcentagem.
            anos: prazo da aplicação em anos.

        Returns:
            Capital somado aos juros do período.
        """
        juros = capital * (taxa_anual / 100) * anos
        return capital + juros

    def calcular_aposentadoria(
        self,
        patrimonio_atual: float,
        aporte_mensal: float,
        anos: int,
        taxa_anual: float,
    ) -> float:
        """Calcula o patrimônio acumulado para aposentadoria.

        Aplica juros compostos mês a mês sobre o saldo mais o aporte.

        Args:
            patrimonio_atual: valor já acumulado hoje.
            aporte_mensal: valor depositado todo mês.
            anos: quantidade de anos até a aposentadoria.
            taxa_anual: taxa de rendimento ao ano, em porcentagem.

        Returns:
            Saldo final após todos os meses do período.
        """
        meses = anos * 12
        taxa_mensal = (taxa_anual / 100) / 12
        saldo = patrimonio_atual

        for _ in range(meses):
            saldo = (saldo + aporte_mensal) * (1 + taxa_mensal)

        return saldo

    def calcular_valor_futuro(
        self, aporte_mensal: float, taxa_mensal: float, meses: int
    ) -> float:
        """Calcula o valor futuro segundo a regra especificada no laboratorio.

        Args:
            aporte_mensal: valor depositado todo mês.
            taxa_mensal: taxa de rendimento ao mês, em porcentagem.
            meses: quantidade de meses de aporte.

        Returns:
            Total aportado corrigido pela taxa. Retorna 0.0 quando meses é 0.

        Raises:
            ValueError: se aporte, meses ou taxa forem negativos.
        """
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
