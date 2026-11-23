"""Conexão e execução segura de consultas parametrizadas."""
from config.database import DatabaseConfig


def connect(config=None):
    cfg = config or DatabaseConfig.from_env()
    # Montagem com chaves ODBC; valores de credenciais com escape de chaves.
    def safe(value):
        return "{" + str(value).replace("}", "}}") + "}"
    connection_string = (
        f"DRIVER={safe(cfg.driver)};SERVER={safe(cfg.server)};"
        f"DATABASE={safe(cfg.database)};UID={safe(cfg.username)};"
        f"PWD={safe(cfg.password)};Encrypt={cfg.encrypt};"
        f"TrustServerCertificate={cfg.trust_server_certificate};"
    )
    import pyodbc
    return pyodbc.connect(connection_string, timeout=10, autocommit=False)


def scalar(connection, query, params=()):
    cursor = connection.cursor()
    try:
        row = cursor.execute(query, *params).fetchone()
        return row[0] if row else None
    finally:
        cursor.close()
