import asyncpg

from database.handler.consultor_handler import ConsultorHandlerDataBase
from database.handler.fixa_handler import FixaHandlerDatabase
from database.handler.migracoes_handler import MigracaoRequestModel
from database.handler.movel_handler import VendaMovelRequestModel
from database.handler.produtos_handler import ProdutosHandlerDataBase
from database.handler.troca_aparelho_handler import TrocaAparelhoRequestModel
from utils.env import DATABASE, HOST, PASSWORD, USER
from utils.queries import JWT_QUERY


class DataBase(
    ConsultorHandlerDataBase,
    ProdutosHandlerDataBase,
    FixaHandlerDatabase,
    MigracaoRequestModel,
    VendaMovelRequestModel,
    TrocaAparelhoRequestModel,
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
