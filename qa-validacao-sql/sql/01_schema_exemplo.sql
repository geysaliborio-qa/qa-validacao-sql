-- OPCIONAL: execute apenas em banco de desenvolvimento isolado.
-- O projeto de testes pressupõe dbo.clientes e dbo.pedidos.
CREATE TABLE dbo.clientes (
    id_cliente INT NOT NULL PRIMARY KEY,
    nome NVARCHAR(150) NOT NULL,
    email NVARCHAR(255) NOT NULL
);
GO
CREATE TABLE dbo.pedidos (
    id_pedido INT NOT NULL PRIMARY KEY,
    id_cliente INT NOT NULL,
    valor_total DECIMAL(12,2) NOT NULL,
    status NVARCHAR(20) NOT NULL,
    CONSTRAINT FK_pedidos_clientes FOREIGN KEY (id_cliente) REFERENCES dbo.clientes(id_cliente)
);
GO
