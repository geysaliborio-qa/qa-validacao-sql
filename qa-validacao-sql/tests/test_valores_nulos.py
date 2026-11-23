import pytest
from utils.db_connection import scalar
from utils.validations import count_nulls_query


@pytest.mark.db
@pytest.mark.parametrize("coluna", ["nome", "email"])
def test_campos_obrigatorios_sem_nulos(db_connection, coluna):
    count = scalar(db_connection, count_nulls_query("dbo", "clientes", coluna))
    assert count == 0, f"Encontrados {count} nulos em clientes.{coluna}"


@pytest.mark.db
def test_campos_texto_sem_vazios(db_connection):
    count = scalar(db_connection, """SELECT COUNT(*) FROM dbo.clientes
        WHERE LTRIM(RTRIM(nome)) = '' OR LTRIM(RTRIM(email)) = ''""")
    assert count == 0, f"Encontrados {count} clientes com campos vazios"
