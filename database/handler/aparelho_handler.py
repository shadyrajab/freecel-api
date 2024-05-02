from typing import Optional

from asyncpg.pool import Pool

from models.aparelho import TrocaAparelhoRequestModel

from .abstract.vendas_handler import VendasHandlerDataBase


class FixaHandlerDatabase(VendasHandlerDataBase):
    def __init__(self, pool: Optional[Pool] = None) -> None:
        self.pool = pool

        super().__init__(pool)

    async def add_troca_aparelho(self, user: str, venda: TrocaAparelhoRequestModel):
        values = venda.to_tuple()
        print(values)
        async with self.pool.acquire() as connection:
            await connection.execute()
