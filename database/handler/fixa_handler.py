from typing import Optional

from asyncpg.pool import Pool

from models.fixa import VendaFixaRequestModel

from .abstract.vendas_handler import VendasHandlerDataBase


class FixaHandlerDatabase(VendasHandlerDataBase):
    def __init__(self, pool: Optional[Pool] = None) -> None:
        self.pool = pool

        super().__init__(pool)

    async def add_venda_fixa(self, user: str, venda: VendaFixaRequestModel, tipo: str):
        return await self.add_venda(user, venda)
