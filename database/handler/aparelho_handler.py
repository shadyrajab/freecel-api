from typing import Optional

import pandas as pd
from asyncpg.pool import Pool

from models import ID, TrocaAparelhoRequestModel
from utils.queries import REMOVE_APARELHO_QUERY
from utils.query_builder import (
    get_vendas_query_builder,
    post_vendas_query_builder,
    update_anth_query_builder,
)


class AparelhoHandlerDatabase:
    def __init__(self, pool: Optional[Pool] = None) -> None:
        self.pool = pool

    async def add_aparelho(self, user: str, venda: TrocaAparelhoRequestModel):
        values = venda.to_dict()
        QUERY, values = post_vendas_query_builder(database="aparelhos", **values)
        async with self.pool.acquire() as connection:
            id = await connection.execute(QUERY, *values)
            return id

    async def remove_aparelho(self, id: ID):
        values = (id.id,)
        async with self.pool.acquire() as connection:
            await connection.execute(REMOVE_APARELHO_QUERY, *values)

    async def get_aparelhos(self, **filters):
        QUERY, values = get_vendas_query_builder(database="aparelhos", **filters)
        async with self.pool.acquire() as connection:
            result = await connection.fetch(QUERY, *values)
            if len(result) == 0:
                return {"message": "Não foram encontrados dados para sua solicitação."}

            columns = result[0].keys()
            vendas = pd.DataFrame(result, columns=columns)
            return vendas

    async def update_aparelho(self, **params):
        QUERY, values = update_anth_query_builder(database="aparelhos", **params)
        async with self.pool.acquire() as connection:
            await connection.execute(QUERY, *values)
