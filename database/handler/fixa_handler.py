from typing import Optional

import pandas as pd
from asyncpg.pool import Pool

from models import ID, VendaFixaRequestModel
from utils.queries import REMOVE_VENDA_FIXA_QUERY
from utils.query_builder import (
    get_vendas_query_builder,
    post_vendas_query_builder,
    update_anth_query_builder,
)


class FixaHandlerDatabase:
    def __init__(self, pool: Optional[Pool] = None) -> None:
        self.pool = pool

    async def add_venda_fixa(self, user: str, venda: VendaFixaRequestModel):
        values = venda.to_dict()
        values["responsavel"] = user
        QUERY, values = post_vendas_query_builder(database="vendas_fixa", *values)
        async with self.pool.acquire() as connection:
            id = await connection.execute(QUERY, *values)
            return id

    async def remove_venda_fixa(self, id: ID):
        values = (id.id,)
        async with self.pool.acquire() as connection:
            await connection.execute(REMOVE_VENDA_FIXA_QUERY, *values)

    async def get_vendas_fixa(self, **filters):
        QUERY, values = get_vendas_query_builder(database="vendas_fixa", **filters)
        async with self.pool.acquire() as connection:
            result = await connection.fetch(QUERY, *values)
            if len(result) == 0:
                return {"message": "Não foram encontrados dados para sua solicitação."}

            columns = result[0].keys()
            vendas = pd.DataFrame(result, columns=columns)
            return vendas

    async def update_venda_fixa(self, **params):
        QUERY, values = update_anth_query_builder(database="vendas_fixa", **params)
        async with self.pool.acquire() as connection:
            await connection.execute(QUERY, *values)
