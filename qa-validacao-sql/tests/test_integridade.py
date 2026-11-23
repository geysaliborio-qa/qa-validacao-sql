import pytest
from utils.db_connection import scalar


@pytest.mark.db
def test_pedidos_referenciam_clientes_existentes(db_connection):
    count = scalar(db_connection, """SELECT COUNT(*) FROM dbo.pedidos p
        LEFT JOIN dbo.clientes c ON c.id_cliente = p.id_cliente
        WHERE c.id_cliente IS NULL""")
    assert count == 0, f"Encontrados {count} pedidos órfãos"
