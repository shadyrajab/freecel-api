ADD_VENDA_QUERY = """
    INSERT INTO vendas_concluidas (
        cnpj, telefone, consultor, data, gestor, plano, quantidade_de_produtos, 
        revenda, tipo, uf, valor_acumulado, valor_do_plano, email, quadro_funcionarios,
        faturamento, cnae, cep, municipio, porte, capital_social, natureza_juridica,
        matriz, regime_tributario, bairro, adabas, ja_cliente
    ) VALUES (
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
    )
"""

REMOVE_VENDA_QUERY = "DELETE FROM vendas_concluidas WHERE id = (%s)"
GET_VENDAS_QUERY = "SELECT * FROM vendas_concluidas"
REMOVE_PRODUTO_QUERY = "DELETE FROM produtos WHERE id = (%s)"
ADD_PRODUTO_QUERY = "INSERT INTO produtos (nome, preco) VALUES (%s, %s)"
GET_PRODUTOS_QUERY = "SELECT * FROM produtos"
REMOVE_CONSULTOR_QUERY = "DELETE FROM consultores WHERE id = (%s)"
ADD_CONSULTOR_QUERY = "INSERT INTO consultores (nome, vinculo, cargo) VALUES ($1, $2, $3)"
GET_CONSULTORES_QUERY = "SELECT * FROM consultores"
JWT_QUERY = "SELECT * FROM uuids WHERE uuid = $1"
GET_PRECO_QUERY = "SELECT preco FROM produtos WHERE nome = %s"
