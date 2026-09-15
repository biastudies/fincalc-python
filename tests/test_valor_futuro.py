import pytest

from fincalc.services.servico_investimento import ServicoInvestimento


@pytest.fixture
def servico():
    return ServicoInvestimento()


def test_valor_futuro_aportes_padrao(servico):
    # Arrange & Act
    vf = servico.calcular_valor_futuro(500.0, 1.0, 3)
    # Assert
    assert round(vf, 2) == 1530.15


def test_valor_futuro_zero_meses(servico):
    # Arrange & Act
    vf = servico.calcular_valor_futuro(500.0, 1.0, 0)
    # Assert
    assert round(vf, 2) == 0.0


def test_valor_futuro_aporte_negativo(servico):
    # Arrange, Act & Assert
    with pytest.raises(ValueError):
        servico.calcular_valor_futuro(-200.0, 1.0, 12)
