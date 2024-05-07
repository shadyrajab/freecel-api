from database.connection import DataBase
from structures.aparelho import Aparelho
from structures.consultor import Consultor
from structures.fixa import Fixa
from structures.geral import Geral
from structures.inovacao import Inovacao
from structures.migracao import Migracao
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

    async def Inovacao(self, **filters: str) -> Inovacao:
        dataframe = await self.get_inovacoes(**filters)
        if isinstance(dataframe, dict):
            return dataframe
        return Inovacao(dataframe).to_json()

    async def Aparelho(self, **filters: str) -> Aparelho:
        dataframe = await self.get_aparelhos(**filters)
        if isinstance(dataframe, dict):
            return dataframe
        return Aparelho(dataframe).to_json()

    async def Migracao(self, **filters: str) -> Migracao:
        dataframe = await self.get_migracoes(**filters)
        if isinstance(dataframe, dict):
            return dataframe
        return Migracao(dataframe).to_json()

    async def Geral(self, **filters: str) -> Geral:
        dataframe = await self.get_vendas_geral(**filters)
        if isinstance(dataframe, dict):
            return dataframe
        return Geral(dataframe).to_json()
