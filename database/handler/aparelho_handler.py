from typing import Optional

import pandas as pd
from asyncpg.pool import Pool

from models.aparelho import TrocaAparelhoRequestModel
from models.identify import ID
from utils.queries import REMOVE_APARELHO_QUERY
from utils.query_builder import get_vendas_query

from .abstract.vendas_handler import VendasHandlerDataBase


class AparelhoHandlerDatabase(VendasHandlerDataBase):
    def __init__(self, pool: Optional[Pool] = None) -> None:
        self.pool = pool

        super().__init__(pool)

    async def add_aparelho(self, user: str, venda: TrocaAparelhoRequestModel):
        values = venda.to_tuple()
        print(values)
        async with self.pool.acquire() as connection:
            await connection.execute()

    async def remove_aparelho(self, id: ID):
        values = (id.id,)
        async with self.pool.acquire() as connection:
            await connection.execute(REMOVE_APARELHO_QUERY, *values)

    async def get_inovacoes(self, **filters):
        QUERY, values = get_vendas_query(database="aparelhos", **filters)
        async with self.pool.acquire() as connection:
            result = await connection.fetch(QUERY, *values)
            if len(result) == 0:
                return {"message": "Não foram encontrados dados para sua solicitação."}

            columns = result[0].keys()
            vendas = pd.DataFrame(result, columns=columns)
            return vendas
