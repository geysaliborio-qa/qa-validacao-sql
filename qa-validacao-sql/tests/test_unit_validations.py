import pytest
from utils.validations import identifier, qualified_table, count_nulls_query, count_duplicates_query


def test_identificador_valido():
    assert identifier("id_cliente") == "[id_cliente]"


@pytest.mark.parametrize("value", ["dbo.clientes", "id;DROP TABLE x", "", "campo nome", "x]", None])
def test_identificador_invalido(value):
    with pytest.raises(ValueError):
        identifier(value)


def test_tabela_qualificada():
    assert qualified_table("dbo", "clientes") == "[dbo].[clientes]"


def test_consulta_nulos():
    assert count_nulls_query("dbo", "clientes", "email") == (
        "SELECT COUNT(*) FROM [dbo].[clientes] WHERE [email] IS NULL")


def test_consulta_duplicados():
    assert "HAVING COUNT(*) > 1" in count_duplicates_query("dbo", "clientes", "email")
