"""Ponto de entrada do FinCalc.

Uso: ``python -m fincalc``
"""

from typing import List

from fincalc.controllers.controlador_simulacao import ControladorSimulacao
from fincalc.models.resultado import ResultadoSimulacao
from fincalc.models.status import StatusProcessamento


def exibir_resultados(resultados: List[ResultadoSimulacao]) -> None:
    """Imprime cada resultado, com o valor ou o motivo da falha.

    Args:
        resultados: lista retornada por ``ControladorSimulacao.executar``.
    """
    for resultado in resultados:
        if resultado.status == StatusProcessamento.SUCESSO:
            print(f"{resultado.nome}: R$ {resultado.valor:.2f}")
        else:
            print(
                f"{resultado.nome}: falhou com status "
                f"{resultado.status.value} - {resultado.status.name} "
                f"({resultado.mensagem})"
            )


if __name__ == "__main__":
    print("Iniciando o sistema FinCalc...")

    controlador = ControladorSimulacao()
    exibir_resultados(controlador.executar())
