from typing import Optional

from asyncpg.pool import Pool

from models import ID, VendaMovelRequestModel

from .commom.vendas_handler import VendaHandlerDatabase


class MovelHandlerDatabase(VendaHandlerDatabase):
    def __init__(self, pool: Optional[Pool] = None) -> None:
        self.pool = pool
        super().__init__(pool)

    async def add_venda_movel(self, user: str, venda: VendaMovelRequestModel):
        return await self.add_venda(database="vendas_movel", user=user, venda=venda)

    async def get_vendas_movel(self, **filters):
        return await self.get_vendas(database="vendas_movel", **filters)

    async def remove_venda_movel(self, id: ID):
        return await self.remove_venda(database="vendas_movel", id=id)

    async def update_venda_movel(self, **params):
        return await self.update_venda(database="vendas_movel", **params)
