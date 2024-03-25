from typing import Optional

import pandas as pd
from asyncpg.pool import Pool

from models.chamadas import Chamada
from models.identify import ID
from utils.queries import ADD_CHAMADA_QUERY, GET_CHAMADAS_QUERY, REMOVE_CHAMADA_QUERY


class ChamadasHandlerDatabase:
    def __init__(self, pool: Optional[Pool] = None):
        self.pool = pool

    async def get_chamadas(self, to_dataframe: Optional[bool] = False):
        async with self.pool.acquire() as connection:
            statement = await connection.prepare(GET_CHAMADAS_QUERY)
            result = await statement.fetch()

            if to_dataframe:
                columns = [desc[0] for desc in statement.get_attributes()]
                chamadas = pd.DataFrame(result, columns=columns)
                return chamadas
            else:
                return result

    async def add_chamada(self, chamada):
        values = (
            chamada.consultor.upper(),
            chamada.telefone,
            chamada.quantidade,
            chamada.data,
        )
        async with self.pool.acquire() as connection:
            id = await connection.fetchval(ADD_CHAMADA_QUERY, *values)
            return id

    async def remove_chamada(self, id: ID):
        values = (id.id,)
        async with self.pool.acquire() as connection:
            await connection.execute(REMOVE_CHAMADA_QUERY, *values)
