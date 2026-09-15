"""Coordena a ordem de execução das simulações do FinCalc."""

from typing import Callable, List

from fincalc.config import parametros
from fincalc.models.resultado import ResultadoSimulacao
from fincalc.models.status import StatusProcessamento
from fincalc.services.servico_financiamento import ServicoFinanciamento
from fincalc.services.servico_investimento import ServicoInvestimento
from fincalc.services.servico_patrimonio import ServicoPatrimonio
from fincalc.services.servico_tributacao import ServicoTributacao


class ControladorSimulacao:
    """Orquestra a simulação padrão do sistema.

    Não contém regra de negócio. Instancia os serviços, entrega os
    parâmetros a cada um na ordem definida e registra o status do resultado.
    """

    def __init__(self) -> None:
        self.servico_investimento = ServicoInvestimento()
        self.servico_tributacao = ServicoTributacao()
        self.servico_financiamento = ServicoFinanciamento()
        self.servico_patrimonio = ServicoPatrimonio()

    def executar(self) -> List[ResultadoSimulacao]:
        """Executa todas as simulações na ordem definida e retorna os resultados.

        Os valores de entrada vêm de ``config.parametros``. Uma falha em
        uma simulação não interrompe as demais.

        Returns:
            Lista com um ResultadoSimulacao por cálculo, na ordem de execução.
        """
        return [
            self._executar_simulacao(
                "Juros Simples",
                lambda: self.servico_investimento.calcular_juros_simples(
                    parametros.CAPITAL_INICIAL,
                    parametros.TAXA_ANUAL_JUROS_SIMPLES,
                    parametros.ANOS_JUROS_SIMPLES,
                ),
            ),
            self._executar_simulacao(
                "Patrimônio Estimado para Aposentadoria",
                lambda: self.servico_investimento.calcular_aposentadoria(
                    parametros.PATRIMONIO_ATUAL,
                    parametros.APORTE_MENSAL_APOSENTADORIA,
                    parametros.ANOS_APOSENTADORIA,
                    parametros.TAXA_ANUAL_APOSENTADORIA,
                ),
            ),
            self._executar_simulacao(
                "IRRF",
                lambda: self.servico_tributacao.calcular_irrf(
                    parametros.SALARIO_BRUTO
                ),
            ),
            self._executar_simulacao(
                "Tabela Price",
                lambda: self.servico_financiamento.calcular_parcela_price(
                    parametros.VALOR_EMPRESTIMO,
                    parametros.TAXA_MENSAL_EMPRESTIMO,
                    parametros.MESES_EMPRESTIMO,
                ),
            ),
            self._executar_simulacao(
                "Valor Futuro",
                lambda: self.servico_investimento.calcular_valor_futuro(
                    parametros.APORTE_MENSAL_VALOR_FUTURO,
                    parametros.TAXA_MENSAL_VALOR_FUTURO,
                    parametros.MESES_VALOR_FUTURO,
                ),
            ),
            self._executar_simulacao(
                "Depreciação Anual",
                lambda: self.servico_patrimonio.calcular_depreciacao_linear(
                    parametros.VALOR_INICIAL_ATIVO,
                    parametros.VALOR_RESIDUAL_ATIVO,
                    parametros.VIDA_UTIL_ANOS_ATIVO,
                ),
            ),
        ]

    def _executar_simulacao(
        self, nome: str, calculo: Callable[[], float]
    ) -> ResultadoSimulacao:
        """Executa um cálculo e registra o status conforme a padronização.

        ValueError é tratado como exceção de negócio (status 2). Qualquer
        outra exceção é tratada como exceção de sistema (status 3).

        Args:
            nome: nome da simulação para o resultado.
            calculo: função sem argumentos que executa o cálculo.

        Returns:
            ResultadoSimulacao com valor e status preenchidos.
        """
        resultado = ResultadoSimulacao(nome=nome)

        try:
            resultado.valor = calculo()
            resultado.status = StatusProcessamento.SUCESSO
        except ValueError as erro:
            resultado.status = StatusProcessamento.EXCECAO_NEGOCIO
            resultado.mensagem = str(erro)
        except Exception as erro:
            resultado.status = StatusProcessamento.EXCECAO_SISTEMA
            resultado.mensagem = str(erro)

        return resultado
