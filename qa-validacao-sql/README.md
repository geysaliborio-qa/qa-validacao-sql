# qa-validacao-sql

Projeto de **QA de dados em SQL Server** com **Python, pyodbc e pytest**, incluindo verificações de duplicidade, valores nulos, integridade referencial e regras de negócio.

## Pré-requisitos

- Python 3.10 ou superior
- Microsoft SQL Server acessível pela rede
- Microsoft **ODBC Driver 18 for SQL Server** instalado no sistema operacional
- Usuário SQL Server com permissão de **SELECT** nas tabelas testadas

> Segurança: os testes são somente leitura. Use uma conta com privilégios mínimos. O padrão é conexão criptografada com validação de certificado (`DB_ENCRYPT=yes`, `DB_TRUST_SERVER_CERTIFICATE=no`).

## Instalação

```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# Linux/macOS:
# source .venv/bin/activate
pip install -r requirements.txt
```

Copie `.env.example` para `.env` e configure servidor, banco e credenciais. **Nunca faça commit do `.env`.**

## Estrutura de dados esperada

Os testes de integração usam as tabelas `dbo.clientes(id_cliente, nome, email)` e `dbo.pedidos(id_pedido, id_cliente, valor_total, status)`. Os status permitidos são `PENDENTE`, `PAGO` e `CANCELADO`. Ajuste os testes para seu esquema real.

O script `sql/01_schema_exemplo.sql` serve **somente** para criar um esquema de demonstração em banco de desenvolvimento vazio. **Não execute em produção**. O script não popula dados; tabelas vazias passam nas validações por ausência de violações.

## Executar

```bash
# Testes unitários locais, sem conexão com SQL Server
python -m pytest -v

# Todos os testes, inclusive integração com SQL Server
python -m pytest -v --run-db

# Apenas testes de integração
python -m pytest -v -m db --run-db

# Relatório HTML (cria a pasta reports antes)
python -m pytest -v --run-db --html=reports/relatorio.html --self-contained-html
```

Crie a pasta de relatórios antes do último comando: `mkdir reports` (no PowerShell e no Linux/macOS).

Sem `--run-db`, testes de integração são marcados como ignorados. Se o banco não estiver acessível, os testes de integração falharão ao abrir a conexão; isso é esperado.

## Validações

| Teste | Regra |
|---|---|
| Duplicidade | Nenhum e-mail repetido em `dbo.clientes` |
| Nulos/vazios | Nome e e-mail preenchidos |
| Integridade | Todos os pedidos apontam para clientes existentes |
| Valor total | Valores não negativos e não nulos |
| Status | Apenas `PENDENTE`, `PAGO` ou `CANCELADO` |

## SQL de apoio

`sql/consultas_validacao.sql` contém consultas para diagnóstico manual no SSMS ou Azure Data Studio. O projeto não executa DDL automaticamente.

## Adaptação

Troque nomes de tabelas, colunas e regras de negócio conforme seu ambiente. Consultas de valores são parametrizáveis via `scalar(connection, sql, params)`. Para nomes de objetos SQL dinâmicos, use as funções de validação de identificadores em `utils/validations.py`, nunca interpolação de entradas externas sem validação.

## Próximos passos

Integração CI, fixtures de massa de teste, controle de ambientes e métricas de qualidade podem ser adicionados conforme o esquema real.
