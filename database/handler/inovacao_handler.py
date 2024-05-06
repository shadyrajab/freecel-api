from typing import Optional

import pandas as pd
from asyncpg.pool import Pool

from models import ID, InovacaoRequestModel
from utils.queries import REMOVE_INOVACAO_QUERY
from utils.query_builder import (
    get_vendas_query_builder,
    post_vendas_query_builder,
    update_anth_query_builder,
)


class InovacaoHandlerDatabase:
    def __init__(self, pool: Optional[Pool] = None) -> None:
        self.pool = pool

    async def add_inovacao(self, user: str, venda: InovacaoRequestModel):
        values = venda.to_dict()
        values["responsavel"] = user
        QUERY, values = post_vendas_query_builder(database="inovacoes", *values)
        async with self.pool.acquire() as connection:
            id = await connection.execute(QUERY, *values)
            return id

    async def get_inovacoes(self, **filters):
        QUERY, values = get_vendas_query_builder(database="inovacoes", **filters)
        async with self.pool.acquire() as connection:
            result = await connection.fetch(QUERY, *values)
            if len(result) == 0:
                return {"message": "Não foram encontrados dados para sua solicitação."}

            columns = result[0].keys()
            vendas = pd.DataFrame(result, columns=columns)
            return vendas

    async def remove_inovacao(self, id: ID):
        values = (id.id,)
        async with self.pool.acquire() as connection:
            await connection.execute(REMOVE_INOVACAO_QUERY, *values)

    async def update_inovacao(self, **params):
        QUERY, values = update_anth_query_builder(database="inovacoes", **params)
        async with self.pool.acquire() as connection:
            await connection.execute(QUERY, *values)
