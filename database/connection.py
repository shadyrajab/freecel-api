from typing import Optional

import asyncpg
import pandas as pd

from database.handler.consultor_handler import ConsultorHandlerDataBase
from database.handler.produtos_handler import ProdutosHandlerDataBase
from database.handler.vendas_handler import VendasHandlerDataBase
from utils.queries import GET_CHAMADAS, JWT_QUERY
from utils.variables import DATABASE, HOST, PASSWORD, USER


class DataBase(
    ConsultorHandlerDataBase, ProdutosHandlerDataBase, VendasHandlerDataBase
):
    async def __aenter__(self):
        self.pool = await asyncpg.create_pool(
            host=HOST, database=DATABASE, user=USER, password=PASSWORD
        )

        super().__init__(self.pool)
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.pool.close()

    async def jwt_authenticate(self, uuid: str):
        async with self.pool.acquire() as connection:
            statement = await connection.prepare(JWT_QUERY)
            result = await statement.fetchval(uuid)
            return result if result else None

    async def get_chamadas(self, to_dataframe: Optional[bool] = False):
        async with self.pool.acquire() as connection:
            statement = await connection.prepare(GET_CHAMADAS)
            result = await statement.fetch()

            if to_dataframe:
                columns = [desc[0] for desc in statement.get_attributes()]
                chamadas = pd.DataFrame(result, columns=columns)
                return chamadas
            else:
                return result
