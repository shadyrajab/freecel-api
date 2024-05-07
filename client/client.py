from database.connection import DataBase
from structures.consultor import Consultor
from structures.fixa import Fixa
from structures.geral import Geral
from structures.movel import Movel


class Client(DataBase):
    async def __aenter__(self):
        await super().__aenter__()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await super().__aexit__(exc_type, exc, tb)

    async def Consultor(self, **filters: str) -> Consultor:
        dataframe = await self.get_vendas(**filters)
        if isinstance(dataframe, dict):
            return dataframe
        return Consultor(dataframe).to_json()

    async def Movel(self, **filters: str) -> Movel:
        dataframe = await self.get_vendas_movel(**filters)
        if isinstance(dataframe, dict):
            return dataframe
        return Movel(dataframe).to_json()

    async def Fixa(self, **filters: str) -> Fixa:
        dataframe = await self.get_vendas_fixa(**filters)
        if isinstance(dataframe, dict):
            return dataframe
        return Fixa(dataframe).to_json()

    async def Geral(self, **filters: str) -> Geral:
        dataframe = await self.get_vendas_geral(**filters)
        if isinstance(dataframe, dict):
            return dataframe
        return Geral(dataframe).to_json()
