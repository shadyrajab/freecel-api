# from datetime import datetime
from typing import Optional

from asyncpg.pool import Pool

from models.identify import ID
from models.migracao import MigracaoRequestModel
from utils.queries import REMOVE_MIGRACOES_QUERY


class MigracoesHandlerDatabase:
    def __init__(self, pool: Optional[Pool] = None) -> None:
        self.pool = pool

    async def remove_migracao(self, id: ID):
        values = (id.id,)
        async with self.pool.acquire() as connection:
            await connection.execute(REMOVE_MIGRACOES_QUERY, *values)

    async def add_migracao(self, venda: MigracaoRequestModel):
        values = venda.to_tuple()
        print(values)
        async with self.pool.acquire() as connection:
            await connection.execute()
