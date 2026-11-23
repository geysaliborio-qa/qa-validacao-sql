-- Consultas de diagnóstico; devem retornar zero linhas quando os dados estão íntegros.
-- Duplicidade de e-mail
SELECT email, COUNT(*) AS quantidade
FROM dbo.clientes
GROUP BY email
HAVING COUNT(*) > 1;

-- Nulos em campos obrigatórios de negócio
SELECT id_cliente FROM dbo.clientes
WHERE nome IS NULL OR LTRIM(RTRIM(nome)) = '' OR email IS NULL OR LTRIM(RTRIM(email)) = '';

-- Pedidos sem cliente (inclui cenários sem FK)
SELECT p.id_pedido FROM dbo.pedidos p
LEFT JOIN dbo.clientes c ON c.id_cliente = p.id_cliente
WHERE c.id_cliente IS NULL;

-- Pedidos com valores negativos ou status inválidos
SELECT id_pedido FROM dbo.pedidos
WHERE valor_total < 0 OR status NOT IN ('PENDENTE', 'PAGO', 'CANCELADO') OR status IS NULL;
