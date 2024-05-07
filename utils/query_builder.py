from datetime import datetime

COLUMNS_TO_SELECT = "id, adabas, bairro, capital_social, cnae, cnpj, consultor, data_abertura, data_input, data_recebimento, ddd, email, equipe, esteira, faturamento, gestor, matriz, municipio, n_pedido, natureza_juridica, observacao, plano, porte, preco, quadro_funcionarios, razao_social, regime_Tributario, responsavel, status, telefone, tipo, uf, volume"


def delete_vendas_query_builder(database: str, id):
    QUERY = f"DELETE FROM {database} WHERE id = ($1)"
    values = (id.id, )
    return QUERY, values

def post_vendas_query_builder(database: str, **values):
    colunas = ", ".join(values.keys())
    values = values.values()
    placeholders = ', '.join([f'${i+1}' for i in range(len(values))])
    QUERY = f"INSERT INTO {database} ({colunas}) VALUES ({placeholders}) RETURNING id;"

    return QUERY, tuple(values)


def update_anth_query_builder(database: str, **params):
    id = params.get("id", None)
    if id is None:
        return
    del params["id"]
    for i, (key, value) in enumerate(params.copy().items()):
        if value is None:
            del params[key]
    set_clause = ", ".join(
        f"{key} = ${i + 1}"
        for i, (key, value) in enumerate(params.items())
        if value is not None
    )

    values = [value for value in params.values() if value is not None] + [id]

    QUERY = f"UPDATE {database} SET {set_clause} WHERE id = ${len(values)}"
    return QUERY, values


def get_vendas_query_builder(database: str, **filters):
    data_inicio = datetime.strptime(filters.get("data_inicio"), "%d-%m-%Y")
    data_fim = datetime.strptime(filters.get("data_fim"), "%d-%m-%Y")
    periodo = (data_inicio, data_fim)

    del filters["data_inicio"]
    del filters["data_fim"]

    conditions = []
    values = []
    values.extend(periodo)
    for key, value in filters.items():
        if value is not None:
            if isinstance(value, str):
                conditions.append(f"AND {key} = ${len(values) + 1}")
                values.append(value)
            elif isinstance(value, list):
                or_conditions = []
                for v in value:
                    or_conditions.append(f"{key} = ${len(values) + 1}")
                    values.append(v)

                conditions.append("AND " + "(" + " OR ".join(or_conditions) + ")")

    QUERY = (
        f"SELECT * FROM {database} WHERE data_recebimento BETWEEN $1 AND $2 {" ".join(conditions)}"
    )

    return QUERY, values
