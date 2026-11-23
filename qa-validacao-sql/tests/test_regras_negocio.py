import pytest
from utils.db_connection import scalar


@pytest.mark.db
def test_valor_total_nao_negativo(db_connection):
    count = scalar(db_connection, "SELECT COUNT(*) FROM dbo.pedidos WHERE valor_total < 0 OR valor_total IS NULL")
    assert count == 0, f"Encontrados {count} pedidos com valor inválido"


@pytest.mark.db
def test_status_permitidos(db_connection):
    count = scalar(db_connection, """SELECT COUNT(*) FROM dbo.pedidos
        WHERE status NOT IN ('PENDENTE', 'PAGO', 'CANCELADO') OR status IS NULL""")
    assert count == 0, f"Encontrados {count} pedidos com status inválido"
