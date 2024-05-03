from typing import Optional

import pandas as pd
from asyncpg.pool import Pool

from models.identify import ID
from models.movel import VendaMovelRequestModel
from utils.queries import REMOVE_VENDA_MOVEL
from utils.query_builder import get_clause, get_vendas_query

from .abstract.vendas_handler import VendasHandlerDataBase


class MovelHandlerDatabase(VendasHandlerDataBase):
    def __init__(self, pool: Optional[Pool] = None) -> None:
        self.pool = pool

        super().__init__(pool)

    async def add_venda_movel(self, user: str, venda: VendaMovelRequestModel):
        values = venda.to_tuple()
        print(values)
        async with self.pool.acquire() as connection:
            await connection.execute()

    async def get_vendas_movel(self, **filters):
        QUERY, values = get_vendas_query(database="vendas_movel", **filters)
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
        QUERY, values = get_clause(database="vendas_movel", **params)
        async with self.pool.acquire() as connection:
            await connection.execute(QUERY, *values)
