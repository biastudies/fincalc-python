from fincalc.controllers.controlador_simulacao import ControladorSimulacao
from fincalc.models.status import StatusProcessamento


def test_executar_retorna_todas_as_simulacoes_com_sucesso():
    # Arrange
    controlador = ControladorSimulacao()
    # Act
    resultados = controlador.executar()
    # Assert
    assert len(resultados) == 6
    assert all(r.status == StatusProcessamento.SUCESSO for r in resultados)
    assert all(r.valor is not None for r in resultados)


def test_erro_de_regra_de_negocio_gera_status_2():
    # Arrange
    controlador = ControladorSimulacao()

    def calculo_invalido():
        raise ValueError("valor invalido")

    # Act
    resultado = controlador._executar_simulacao("Teste", calculo_invalido)
    # Assert
    assert resultado.status == StatusProcessamento.EXCECAO_NEGOCIO
    assert resultado.mensagem == "valor invalido"
    assert resultado.valor is None


def test_erro_tecnico_gera_status_3():
    # Arrange
    controlador = ControladorSimulacao()

    def calculo_com_falha():
        raise ZeroDivisionError("division by zero")

    # Act
    resultado = controlador._executar_simulacao("Teste", calculo_com_falha)
    # Assert
    assert resultado.status == StatusProcessamento.EXCECAO_SISTEMA
    assert resultado.valor is None
