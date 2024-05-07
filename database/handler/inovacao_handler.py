from typing import Optional

from asyncpg.pool import Pool

from models import ID, InovacaoRequestModel

from .commom.vendas_handler import VendaHandlerDatabase


class InovacaoHandlerDatabase(VendaHandlerDatabase):
    def __init__(self, pool: Optional[Pool] = None) -> None:
        self.pool = pool

    async def add_inovacao(self, user: str, venda: InovacaoRequestModel):
        return await self.add_venda(database="inovacoes", user=user, venda=venda)

    async def get_inovacoes(self, **filters):
        return await self.get_vendas(database="inovacoes", **filters)

    async def remove_inovacao(self, id: ID):
        return await self.remove_venda(database="inovacoes", id=id)

    async def update_inovacao(self, **params):
        return await self.update_venda(database="inovacoes", **params)
