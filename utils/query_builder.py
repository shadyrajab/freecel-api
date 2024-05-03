from datetime import datetime


def post_vendas_query_builder(database: str, **values):
    colunas = ", ".join(values.keys())
    values = values.values()
    clause = ", ".join([f"'{v}'" for v in values])
    QUERY = f"INSERT INTO {database} ({colunas}) VALUES ({clause});"

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
    del filters["venda"]

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
        f"SELECT * FROM {database} WHERE data BETWEEN $2 AND $3 {" ".join(conditions)}"
    )
    return QUERY, values
