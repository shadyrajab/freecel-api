from typing import Optional

import pandas as pd
from asyncpg.pool import Pool

from models import ID, Plano
from utils.queries import ADD_PLANO_QUERY, GET_PLANOS_QUERY, REMOVE_PLANO_QUERY
from utils.query_builder import update_anth_query_builder


class PlanosHandlerDataBase:
    def __init__(self, pool: Optional[Pool] = None) -> None:
        self.pool = pool

    async def get_planos(self):
        async with self.pool.acquire() as connection:
            statement = await connection.prepare(GET_PLANOS_QUERY)
            result = await statement.fetch()
            columns = [desc[0] for desc in statement.get_attributes()]
            plano = pd.DataFrame(result, columns=columns)
            return plano

    async def add_plano(self, plano: Plano):
        values = (
            plano.nome.upper(),
            plano.preco,
        )
        async with self.pool.acquire() as connection:
            id = await connection.fetchval(ADD_PLANO_QUERY, *values)
            return id

    async def remove_plano(self, id: ID):
        values = (id.id,)
        async with self.pool.acquire() as connection:
            await connection.execute(REMOVE_PLANO_QUERY, *values)

    async def update_plano(self, **params):
        QUERY, values = update_anth_query_builder(database="planos", **params)
        async with self.pool.acquire() as connection:
            await connection.execute(QUERY, *values)
