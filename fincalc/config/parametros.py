"""Parâmetros operacionais da simulação padrão.

Todos os valores podem mudar entre execuções sem alteração de código, por
isso são lidos de variáveis de ambiente com prefixo ``FINCALC_``. Cada um
tem um valor padrão, então a aplicação roda sem nenhuma variável definida.

Taxas são informadas em porcentagem (ex.: ``5.0`` para 5%).
"""

from os import getenv

# Juros simples
CAPITAL_INICIAL = float(getenv("FINCALC_CAPITAL_INICIAL", "1000.0"))
TAXA_ANUAL_JUROS_SIMPLES = float(getenv("FINCALC_TAXA_ANUAL_JUROS_SIMPLES", "5.0"))
ANOS_JUROS_SIMPLES = int(getenv("FINCALC_ANOS_JUROS_SIMPLES", "2"))

# Aposentadoria
PATRIMONIO_ATUAL = float(getenv("FINCALC_PATRIMONIO_ATUAL", "10000.0"))
APORTE_MENSAL_APOSENTADORIA = float(
    getenv("FINCALC_APORTE_MENSAL_APOSENTADORIA", "500.0")
)
ANOS_APOSENTADORIA = int(getenv("FINCALC_ANOS_APOSENTADORIA", "20"))
TAXA_ANUAL_APOSENTADORIA = float(getenv("FINCALC_TAXA_ANUAL_APOSENTADORIA", "6.0"))

# IRRF
SALARIO_BRUTO = float(getenv("FINCALC_SALARIO_BRUTO", "3000.0"))

# Tabela Price
VALOR_EMPRESTIMO = float(getenv("FINCALC_VALOR_EMPRESTIMO", "10000.0"))
TAXA_MENSAL_EMPRESTIMO = float(getenv("FINCALC_TAXA_MENSAL_EMPRESTIMO", "2.0"))
MESES_EMPRESTIMO = int(getenv("FINCALC_MESES_EMPRESTIMO", "12"))

# Valor futuro
APORTE_MENSAL_VALOR_FUTURO = float(
    getenv("FINCALC_APORTE_MENSAL_VALOR_FUTURO", "500.0")
)
TAXA_MENSAL_VALOR_FUTURO = float(getenv("FINCALC_TAXA_MENSAL_VALOR_FUTURO", "1.0"))
MESES_VALOR_FUTURO = int(getenv("FINCALC_MESES_VALOR_FUTURO", "3"))

# Depreciação
VALOR_INICIAL_ATIVO = float(getenv("FINCALC_VALOR_INICIAL_ATIVO", "5000.0"))
VALOR_RESIDUAL_ATIVO = float(getenv("FINCALC_VALOR_RESIDUAL_ATIVO", "500.0"))
VIDA_UTIL_ANOS_ATIVO = int(getenv("FINCALC_VIDA_UTIL_ANOS_ATIVO", "2"))
