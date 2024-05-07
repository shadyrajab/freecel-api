import asyncpg
import pandas as pd

from database.handler.consultor_handler import ConsultorHandlerDataBase
from database.handler.fixa_handler import FixaHandlerDatabase
from database.handler.movel_handler import MovelHandlerDatabase
from database.handler.produtos_handler import ProdutosHandlerDataBase
from utils.env import DATABASE, HOST, PASSWORD, USER
from utils.queries import JWT_QUERY
from utils.query_builder import COLUMNS_TO_SELECT, get_vendas_query_builder


class DataBase(
    ConsultorHandlerDataBase,
    ProdutosHandlerDataBase,
    FixaHandlerDatabase,
    MovelHandlerDatabase,
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

    async def get_vendas_geral(self, **filters) -> pd.DataFrame:
        QUERY, values = self.get_union_query(**filters)
        async with self.pool.acquire() as connection:
            result = await connection.fetch(QUERY, *values)
            if len(result) == 0:
                return {"message": "Não foram encontrados dados para sua solicitação."}

            columns = result[0].keys()
            vendas = pd.DataFrame(result, columns=columns)
            return vendas

    def get_union_query(self, **filters):
        MOVEL, values = get_vendas_query_builder(database="vendas_movel", **filters)
        FIXA, _ = get_vendas_query_builder(database="vendas_fixa", **filters)
        QUERY = " UNION ALL ".join([MOVEL, FIXA]).replace("*", COLUMNS_TO_SELECT)

        return QUERY, values
