from typing import Optional

from asyncpg.pool import Pool

from models import ID, MigracaoRequestModel

from .commom.vendas_handler import VendaHandlerDatabase


class MigracaoHandlerDatabase(VendaHandlerDatabase):
    def __init__(self, pool: Optional[Pool] = None) -> None:
        self.pool = pool
        super().__init__(pool)

    async def remove_migracao(self, id: ID):
        return await self.remove_venda(database="migracoes", id=id)

    async def add_migracao(self, user: str, venda: MigracaoRequestModel):
        return await self.add_venda(database="migracoes", user=user, venda=venda)

    async def get_migracoes(self, **filters):
        return await self.get_vendas(database="migracoes", **filters)

    async def update_migracao(self, **params):
        return await self.update_venda(database="migracoes", **params)
