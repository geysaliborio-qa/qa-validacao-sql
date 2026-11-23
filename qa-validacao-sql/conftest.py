"""Fixtures compartilhadas; testes de integração exigem --run-db."""
import pytest
from utils.db_connection import connect


def pytest_addoption(parser):
    parser.addoption("--run-db", action="store_true", default=False,
                     help="Executa testes de integração contra SQL Server")


def pytest_collection_modifyitems(config, items):
    if config.getoption("--run-db"):
        return
    skip_db = pytest.mark.skip(reason="Use --run-db para executar contra SQL Server")
    for item in items:
        if "db" in item.keywords:
            item.add_marker(skip_db)


@pytest.fixture(scope="session")
def db_connection(request):
    if not request.config.getoption("--run-db"):
        pytest.skip("Integração desabilitada")
    connection = connect()
    try:
        yield connection
    finally:
        connection.close()
