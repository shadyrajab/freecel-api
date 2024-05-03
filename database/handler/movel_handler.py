from typing import Optional

import pandas as pd
from asyncpg.pool import Pool

from models.identify import ID
from models.movel import VendaMovelRequestModel
from utils.queries import REMOVE_VENDA_MOVEL
from utils.query_builder import (
    get_vendas_query_builder,
    post_vendas_query_builder,
    update_anth_query_builder,
)


class MovelHandlerDatabase:
    def __init__(self, pool: Optional[Pool] = None) -> None:
        self.pool = pool

    async def add_venda_movel(self, user: str, venda: VendaMovelRequestModel):
        values = venda.to_dict()
        QUERY, values = post_vendas_query_builder(database="vendas_movel", **values)
        async with self.pool.acquire() as connection:
            await connection.execute(QUERY, *values)

    async def get_vendas_movel(self, **filters):
        QUERY, values = get_vendas_query_builder(database="vendas_movel", **filters)
        async with self.pool.acquire() as connection:
            result = await connection.fetch(QUERY, *values)
            if len(result) == 0:
                return {"message": "Não foram encontrados dados para sua solicitação."}

            columns = result[0].keys()
            vendas = pd.DataFrame(result, columns=columns)
            return vendas

    async def remove_venda_movel(self, id: ID):
        values = (id.id,)
        async with self.pool.acquire() as connection:
            await connection.execute(REMOVE_VENDA_MOVEL, *values)

    async def update_venda_movel(self, **params):
        QUERY, values = update_anth_query_builder(database="vendas_movel", **params)
        async with self.pool.acquire() as connection:
            await connection.execute(QUERY, *values)
