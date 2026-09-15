"""Representação do resultado de uma simulação."""

from dataclasses import dataclass
from typing import Optional

from fincalc.models.status import StatusProcessamento


@dataclass
class ResultadoSimulacao:
    """Resultado de um cálculo executado pelo controlador.

    Attributes:
        nome: nome da simulação, usado na exibição.
        status: código de status conforme StatusProcessamento.
        valor: resultado do cálculo. None enquanto não concluir ou se falhar.
        mensagem: descrição do erro quando o status for de exceção.
    """

    nome: str
    status: StatusProcessamento = StatusProcessamento.EM_EXECUCAO
    valor: Optional[float] = None
    mensagem: str = ""
