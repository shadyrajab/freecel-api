from datetime import datetime


def get_vendas_query(database: str, **filters):
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
