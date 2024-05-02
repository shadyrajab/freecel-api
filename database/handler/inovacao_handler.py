from typing import Optional

import pandas as pd
from asyncpg.pool import Pool

from models.identify import ID
from models.inovacao import InovacaoRequestModel
from utils.queries import REMOVE_INOVACAO_QUERY
from utils.query_builder import get_vendas_query


class InovacaoHandlerDatabase:
    def __init__(self, pool: Optional[Pool] = None) -> None:
        self.pool = pool

    async def add_inovacao(self, venda: InovacaoRequestModel):
        values = venda.to_tuple()
        print(values)
        async with self.pool.acquire() as connection:
            await connection.execute()

    async def get_inovacoes(self, **filters):
        QUERY, values = get_vendas_query(database="inovacoes", **filters)
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
