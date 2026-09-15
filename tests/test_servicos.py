import pytest

from fincalc.services.servico_financiamento import ServicoFinanciamento
from fincalc.services.servico_investimento import ServicoInvestimento
from fincalc.services.servico_patrimonio import ServicoPatrimonio
from fincalc.services.servico_tributacao import ServicoTributacao


def test_juros_simples():
    # Arrange
    servico = ServicoInvestimento()
    # Act
    montante = servico.calcular_juros_simples(1000.0, 5.0, 2)
    # Assert
    assert round(montante, 2) == 1100.00


def test_aposentadoria_sem_aporte_e_sem_taxa_mantem_patrimonio():
    # Arrange
    servico = ServicoInvestimento()
    # Act
    patrimonio = servico.calcular_aposentadoria(10000.0, 0.0, 5, 0.0)
    # Assert
    assert round(patrimonio, 2) == 10000.00


@pytest.mark.parametrize(
    "salario_bruto, irrf_esperado",
    [
        (2000.00, 0.00),
        (2500.00, 18.06),
        (3000.00, 68.56),
        (5000.00, 462.23),
    ],
)
def test_irrf_por_faixa(salario_bruto, irrf_esperado):
    # Arrange
    servico = ServicoTributacao()
    # Act
    irrf = servico.calcular_irrf(salario_bruto)
    # Assert
    assert round(irrf, 2) == irrf_esperado


def test_parcela_price():
    # Arrange
    servico = ServicoFinanciamento()
    # Act
    parcela = servico.calcular_parcela_price(10000.0, 2.0, 12)
    # Assert
    assert round(parcela, 2) == 945.60


def test_depreciacao_linear():
    # Arrange
    servico = ServicoPatrimonio()
    # Act
    depreciacao = servico.calcular_depreciacao_linear(5000.0, 500.0, 2)
    # Assert
    assert round(depreciacao, 2) == 2250.00
