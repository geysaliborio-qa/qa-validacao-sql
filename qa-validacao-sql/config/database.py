"""Configuração de conexão SQL Server via variáveis de ambiente."""
import os
from dataclasses import dataclass
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # Dependência necessária apenas para carregar .env automaticamente

@dataclass(frozen=True)
class DatabaseConfig:
    server: str
    database: str
    username: str
    password: str
    driver: str = "ODBC Driver 18 for SQL Server"
    encrypt: str = "yes"
    trust_server_certificate: str = "no"

    @classmethod
    def from_env(cls):
        required = ["DB_SERVER", "DB_NAME", "DB_USER", "DB_PASSWORD"]
        missing = [name for name in required if not os.getenv(name)]
        if missing:
            raise ValueError("Variáveis obrigatórias ausentes: " + ", ".join(missing))
        return cls(server=os.environ["DB_SERVER"], database=os.environ["DB_NAME"],
                   username=os.environ["DB_USER"], password=os.environ["DB_PASSWORD"],
                   driver=os.getenv("DB_DRIVER", "ODBC Driver 18 for SQL Server"),
                   encrypt=os.getenv("DB_ENCRYPT", "yes"),
                   trust_server_certificate=os.getenv("DB_TRUST_SERVER_CERTIFICATE", "no"))
