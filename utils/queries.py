ADD_VENDA_LIST_PARAMS = [
    "cnpj",
    "telefone",
    "responsavel",
    "consultor",
    "data",
    "gestor",
    "plano",
    "volume",
    "equipe",
    "tipo",
    "ddd",
    "uf",
    "receita",
    "preco",
    "email",
    "quadro_funcionarios",
    "faturamento",
    "cnae",
    "cep",
    "municipio",
    "porte",
    "capital_social",
    "natureza_juridica",
    "matriz",
    "regime_tributario",
    "bairro",
    "adabas",
    "ja_cliente",
    "numero_pedido",
    "status",
    "data_abertura",
]

placeholders = ", ".join(["$" + str(i + 1) for i in range(len(ADD_VENDA_LIST_PARAMS))])
columns = ", ".join(ADD_VENDA_LIST_PARAMS)
ADD_VENDA_QUERY = (
    f"INSERT INTO vendas_concluidas ({columns}) VALUES ({placeholders}) RETURNING id"
)
REMOVE_VENDA_QUERY = "DELETE FROM vendas_concluidas WHERE id = ($1)"
GET_VENDAS_QUERY = "SELECT * FROM vendas_concluidas"
REMOVE_PRODUTO_QUERY = "DELETE FROM produtos WHERE id = ($1)"
ADD_PRODUTO_QUERY = "INSERT INTO produtos (nome, preco) VALUES ($1, $2) RETURNING id"
GET_PRODUTOS_QUERY = "SELECT * FROM produtos"
REMOVE_CONSULTOR_QUERY = "DELETE FROM consultores WHERE id = ($1)"
ADD_CONSULTOR_QUERY = (
    "INSERT INTO consultores (nome, vinculo, cargo) VALUES ($1, $2, $3) RETURNING id"
)
GET_CONSULTORES_QUERY = "SELECT * FROM consultores"
JWT_QUERY = "SELECT nome FROM uuids WHERE uuid = $1"
GET_PRECO_QUERY = "SELECT preco FROM produtos WHERE nome = $1"
GET_EQUIPE_FLAVIO = "SELECT * FROM equipe_flavio"
