from typing import Optional

from asyncpg.pool import Pool

from models.movel import VendaMovelRequestModel

from .abstract.vendas_handler import VendasHandlerDataBase


class FixaHandlerDatabase(VendasHandlerDataBase):
    def __init__(self, pool: Optional[Pool] = None) -> None:
        self.pool = pool

        super().__init__(pool)

    async def add_venda_movel(self, user: str, venda: VendaMovelRequestModel):
        values = venda.to_tuple()
        print(values)
        async with self.pool.acquire() as connection:
            await connection.execute()
