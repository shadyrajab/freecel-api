import asyncpg
import pandas as pd

from database.handler.aparelho_handler import AparelhoHandlerDatabase
from database.handler.consultor_handler import ConsultorHandlerDataBase
from database.handler.fixa_handler import FixaHandlerDatabase
from database.handler.inovacao_handler import InovacaoHandlerDatabase
from database.handler.migracoes_handler import MigracaoHandlerDatabase
from database.handler.movel_handler import MovelHandlerDatabase
from database.handler.produtos_handler import ProdutosHandlerDataBase
from utils.env import DATABASE, HOST, PASSWORD, USER
from utils.queries import JWT_QUERY
from utils.query_builder import COLUMNS_TO_SELECT, get_vendas_query_builder


class DataBase(
    ConsultorHandlerDataBase,
    ProdutosHandlerDataBase,
    FixaHandlerDatabase,
    MigracaoHandlerDatabase,
    MovelHandlerDatabase,
    AparelhoHandlerDatabase,
    InovacaoHandlerDatabase,
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
        MOVEL_QUERY, values = get_vendas_query_builder(
            database="vendas_movel", **filters
        )
        FIXA_QUERY, _ = get_vendas_query_builder(database="vendas_fixa", **filters)
        MIGRACAO_QUERY, _ = get_vendas_query_builder(database="migracoes", **filters)
        INOVACAO_QUERY, _ = get_vendas_query_builder(database="inovacoes", **filters)
        APARELHO_QUERY, _ = get_vendas_query_builder(database="aparelhos", **filters)
        QUERY = " UNION ALL ".join(
            [MOVEL_QUERY, FIXA_QUERY, MIGRACAO_QUERY, INOVACAO_QUERY, APARELHO_QUERY]
        ).replace("*", COLUMNS_TO_SELECT)
        async with self.pool.acquire() as connection:
            result = await connection.fetch(QUERY, *values)
            if len(result) == 0:
                return {"message": "Não foram encontrados dados para sua solicitação."}

            columns = result[0].keys()
            vendas = pd.DataFrame(result, columns=columns)
            return vendas
