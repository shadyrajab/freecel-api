from typing import Optional

import pandas as pd
from asyncpg.pool import Pool

from models.fixa import VendaFixaRequestModel
from models.identify import ID
from utils.queries import REMOVE_VENDA_FIXA_QUERY
from utils.query_builder import get_clause, get_vendas_query


class FixaHandlerDatabase:
    def __init__(self, pool: Optional[Pool] = None) -> None:
        self.pool = pool

    async def add_venda_fixa(self, venda: VendaFixaRequestModel):
        values = venda.to_dict()
        print(values)
        async with self.pool.acquire() as connection:
            await connection.execute()

    async def remove_venda_fixa(self, id: ID):
        values = (id.id,)
        async with self.pool.acquire() as connection:
            await connection.execute(REMOVE_VENDA_FIXA_QUERY, *values)

    async def get_vendas_fixa(self, **filters):
        QUERY, values = get_vendas_query(database="vendas_fixa", **filters)
        async with self.pool.acquire() as connection:
            result = await connection.fetch(QUERY, *values)
            if len(result) == 0:
                return {"message": "Não foram encontrados dados para sua solicitação."}

            columns = result[0].keys()
            vendas = pd.DataFrame(result, columns=columns)
            return vendas

    async def update_venda_fixa(self, **params):
        QUERY, values = get_clause(database="vendas_fixa", **params)
        async with self.pool.acquire() as connection:
            await connection.execute(QUERY, *values)
