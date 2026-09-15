"""Padronização de status de processamento."""

from enum import IntEnum


class StatusProcessamento(IntEnum):
    """Códigos de status usados em todo processamento da aplicação.

    EM_EXECUCAO: iniciado e ainda não finalizado.
    EXCECAO_NEGOCIO: falha por regra de negócio ou condição esperada.
    EXCECAO_SISTEMA: falha técnica inesperada.
    SUCESSO: concluído corretamente.
    CANCELADO: operação interrompida ou cancelada.
    """

    EM_EXECUCAO = 1
    EXCECAO_NEGOCIO = 2
    EXCECAO_SISTEMA = 3
    SUCESSO = 4
    CANCELADO = 5
