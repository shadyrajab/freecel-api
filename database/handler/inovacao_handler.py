from typing import Optional

from asyncpg.pool import Pool

from models.inovacao import InovacaoRequestModel


class FixaHandlerDatabase:
    def __init__(self, pool: Optional[Pool] = None) -> None:
        self.pool = pool

    async def add_inovacao(self, venda: InovacaoRequestModel):
        values = venda.to_tuple()
        print(values)
        async with self.pool.acquire() as connection:
            await connection.execute()
