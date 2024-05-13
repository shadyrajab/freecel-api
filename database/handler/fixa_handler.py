from typing import Optional

from asyncpg.pool import Pool

from models import ID, VendaFixaRequestModel

from .commom.vendas_handler import VendaHandlerDatabase


class FixaHandlerDatabase(VendaHandlerDatabase):
    def __init__(self, pool: Optional[Pool] = None) -> None:
        self.pool = pool
        super().__init__(pool)

    async def add_venda_fixa(self, user: str, venda: VendaFixaRequestModel):
        return await self.add_venda(database="vendas_fixa", user=user, venda=venda)

    async def remove_venda_fixa(self, id: ID):
        return await self.remove_venda(database="vendas_fixa", id=id)

    async def get_vendas_fixa(self, **filters):
        return await self.get_vendas(database="vendas_fixa", **filters)

    async def update_venda_fixa(self, **params):
        return await self.update_venda(database="vendas_fixa", **params)
