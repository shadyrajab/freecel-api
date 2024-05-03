# from datetime import datetime
from typing import Optional

import pandas as pd
from asyncpg.pool import Pool

from models.identify import ID
from models.migracao import MigracaoRequestModel
from utils.queries import REMOVE_MIGRACOES_QUERY
from utils.query_builder import get_clause, get_vendas_query


class MigracaoHandlerDatabase:
    def __init__(self, pool: Optional[Pool] = None) -> None:
        self.pool = pool

    async def remove_migracao(self, id: ID):
        values = (id.id,)
        async with self.pool.acquire() as connection:
            await connection.execute(REMOVE_MIGRACOES_QUERY, *values)

    async def add_migracao(self, user: str, venda: MigracaoRequestModel):
        values = venda.to_tuple()
        print(values)
        async with self.pool.acquire() as connection:
            await connection.execute()

    async def get_migracoes(self, **filters):
        QUERY, values = get_vendas_query(database="migracoes", **filters)
        async with self.pool.acquire() as connection:
            result = await connection.fetch(QUERY, *values)
            if len(result) == 0:
                return {"message": "Não foram encontrados dados para sua solicitação."}

            columns = result[0].keys()
            vendas = pd.DataFrame(result, columns=columns)
            return vendas

    async def update_migracao(self, **params):
        QUERY, values = get_clause(database="migracoes", **params)
        async with self.pool.acquire() as connection:
            await connection.execute(QUERY, *values)
