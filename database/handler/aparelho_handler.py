from typing import Optional

from asyncpg.pool import Pool

from models import ID, TrocaAparelhoRequestModel

from .commom.vendas_handler import VendaHandlerDatabase


class AparelhoHandlerDatabase(VendaHandlerDatabase):
    def __init__(self, pool: Optional[Pool] = None) -> None:
        self.pool = pool
        super().__init__(pool)

    async def add_aparelho(self, user: str, venda: TrocaAparelhoRequestModel):
        return await self.add_venda(database="aparelhos", user=user, venda=venda)

    async def remove_aparelho(self, id: ID):
        return await self.remove_venda(database="aparelhos", id=id)

    async def get_aparelhos(self, **filters):
        return await self.get_vendas(database="aparelhos", **filters)

    async def update_aparelho(self, **params):
        return await self.update_venda(database="aparelhos", **params)
