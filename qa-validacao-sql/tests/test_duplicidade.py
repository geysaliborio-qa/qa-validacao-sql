import pytest
from utils.db_connection import scalar
from utils.validations import count_duplicates_query


@pytest.mark.db
def test_emails_sem_duplicidade(db_connection):
    count = scalar(db_connection, count_duplicates_query("dbo", "clientes", "email"))
    assert count == 0, f"Encontrados {count} e-mails duplicados"
