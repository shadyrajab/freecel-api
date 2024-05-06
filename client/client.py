from database.connection import DataBase
from structures.abstract.ranking import Rankings
from structures.aparelho import Aparelho
from structures.consultor import Consultor
from structures.fixa import Fixa
from structures.inovacao import Inovacao
from structures.migracao import Migracao
from structures.movel import Movel
from structures.pen import Pen


class Client(DataBase):
    async def __aenter__(self):
        await super().__aenter__()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await super().__aexit__(exc_type, exc, tb)

    async def Consultor(self, **filters: str) -> Consultor:
        dataframe = await self.get_vendas(**filters)
        return Consultor(dataframe)

    async def Movel(self, **filters: str) -> Movel:
        dataframe = await self.get_vendas_movel(**filters)
        return Movel(dataframe)

    async def Fixa(self, **filters: str) -> Fixa:
        dataframe = await self.get_vendas_fixa(**filters)
        return Fixa(dataframe)

    async def Inovacao(self, **filters: str) -> Inovacao:
        dataframe = await self.get_aparelhos(**filters)
        return Inovacao(dataframe)

    async def Aparelho(self, **filters: str) -> Aparelho:
        dataframe = await self.get_aparelhos(**filters)
        return Aparelho(dataframe)

    async def Migracao(self, **filters: str) -> Migracao:
        dataframe = await self.get_aparelhos(**filters)
        return Migracao(dataframe)

    async def Pen(self, **filters: str) -> Pen:
        filters.update({"tipo": "INTERNET"})
        dataframe = await self.get_vendas_movel(**filters)
        return Pen(dataframe)
