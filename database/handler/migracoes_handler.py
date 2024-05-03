from typing import Optional

import pandas as pd
from asyncpg.pool import Pool

from models.identify import ID
from models.migracao import MigracaoRequestModel
from utils.queries import REMOVE_MIGRACOES_QUERY
from utils.query_builder import (
    get_vendas_query_builder,
    post_vendas_query_builder,
    update_anth_query_builder,
)


class MigracaoHandlerDatabase:
    def __init__(self, pool: Optional[Pool] = None) -> None:
        self.pool = pool

    async def remove_migracao(self, id: ID):
        values = (id.id,)
        async with self.pool.acquire() as connection:
            await connection.execute(REMOVE_MIGRACOES_QUERY, *values)

    async def add_migracao(self, user: str, venda: MigracaoRequestModel):
        values = venda.to_dict()
        QUERY, values = post_vendas_query_builder(database="migracoes", *values)
        async with self.pool.acquire() as connection:
            id = await connection.fetchval(QUERY, *values)
            return id

    async def get_migracoes(self, **filters):
        QUERY, values = get_vendas_query_builder(database="migracoes", **filters)
        async with self.pool.acquire() as connection:
            result = await connection.fetch(QUERY, *values)
            if len(result) == 0:
                return {"message": "Não foram encontrados dados para sua solicitação."}

            columns = result[0].keys()
            vendas = pd.DataFrame(result, columns=columns)
            return vendas

    async def update_migracao(self, **params):
        QUERY, values = update_anth_query_builder(database="migracoes", **params)
        async with self.pool.acquire() as connection:
            await connection.execute(QUERY, *values)
