import pandas as pd

from database.connection import DataBase
from structures.consultor import Consultor
from structures.freecel import Freecel
from structures.ranking import Rankings


class Client(DataBase):
    async def __aenter__(self):
        await super().__aenter__()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await super().__aexit__(exc_type, exc, tb)

    async def Consultor(self, **filters: str) -> Consultor:
        dataframe = self.__format(await self.get_vendas(**filters))
        return Consultor(dataframe)

    async def Ranking(self, **filters: str) -> Rankings:
        dataframe = self.__format(await self.get_vendas(**filters))
        return Rankings(dataframe)

    async def Freecel(self, **filters: str) -> Freecel:
        dataframe = self.__format(await self.get_vendas(**filters))
        return Freecel(dataframe)
