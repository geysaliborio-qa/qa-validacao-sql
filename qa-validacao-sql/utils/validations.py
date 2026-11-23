"""Funções puras para construir consultas de validação."""
import re

_IDENTIFIER = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")


def identifier(name):
    """Permite apenas identificadores SQL simples; não aceita SQL arbitrário."""
    if not isinstance(name, str) or not _IDENTIFIER.fullmatch(name):
        raise ValueError(f"Identificador SQL inválido: {name!r}")
    return f"[{name}]"


def qualified_table(schema, table):
    return f"{identifier(schema)}.{identifier(table)}"


def count_nulls_query(schema, table, column):
    return f"SELECT COUNT(*) FROM {qualified_table(schema, table)} WHERE {identifier(column)} IS NULL"


def count_duplicates_query(schema, table, column):
    return (f"SELECT COUNT(*) FROM (SELECT {identifier(column)} "
            f"FROM {qualified_table(schema, table)} GROUP BY {identifier(column)} "
            f"HAVING COUNT(*) > 1) AS duplicates")
