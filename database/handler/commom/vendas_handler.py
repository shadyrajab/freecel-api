from typing import Any, Optional

import pandas as pd
from asyncpg.pool import Pool

from models import ID
from utils.query_builder import (
    delete_vendas_query_builder,
    get_vendas_query_builder,
    post_vendas_query_builder,
    update_anth_query_builder,
)


class VendaHandlerDatabase:
    def __init__(self, pool: Optional[Pool] = None) -> None:
        self.pool = pool

    async def add_venda(self, database: str, user: str, venda: Any):
        values = venda.to_dict()
        values["responsavel"] = user
        QUERY, values = post_vendas_query_builder(database=database, **values)
        async with self.pool.acquire() as connection:
            id = await connection.fetchval(QUERY, *values)
            return id

    async def get_vendas(self, database: str, **filters):
        QUERY, values = get_vendas_query_builder(database=database, **filters)
        async with self.pool.acquire() as connection:
            result = await connection.fetch(QUERY, *values)
            if len(result) == 0:
                return {"message": "Não foram encontrados dados para sua solicitação."}

            columns = result[0].keys()
            vendas = pd.DataFrame(result, columns=columns)

            vendas["receita"] = vendas["preco"] * vendas["volume"]
            return vendas

    async def remove_venda(self, database: str, id: ID):
        QUERY, values = delete_vendas_query_builder(database=database, id=id)
        async with self.pool.acquire() as connection:
            await connection.execute(QUERY, *values)

    async def update_venda(self, database: str, **params):
        QUERY, values = update_anth_query_builder(database=database, **params)
        async with self.pool.acquire() as connection:
            await connection.execute(QUERY, *values)
