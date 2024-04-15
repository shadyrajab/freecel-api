import pandas as pd

from database.connection import DataBase
from structures.consultor import Consultor
from structures.freecel import Freecel
from structures.ranking import Rankings
from utils.functions import jsonfy


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

    async def vendas(self, **filters: str) -> dict:
        vendas = await self.get_vendas(**filters)
        if len(vendas) == 0:
            return vendas
        dataframe = self.__format(vendas)
        if filters.get("venda") == "~MIGRAÇÃO":
            dataframe.drop(
                axis=1,
                columns=[
                    "volume_migracao",
                    "m",
                    "tipo_m",
                    "valor_atual",
                    "valor_renovacao",
                    "valor_inovacao",
                    "pacote_inovacao",
                    "volume_inovacao",
                ],
                inplace=True,
            )

        return jsonfy(dataframe)

    async def produtos(self) -> dict:
        produtos = await self.get_produtos()
        return jsonfy(produtos)

    async def consultores(self) -> dict:
        consultores = await self.get_consultores()
        return jsonfy(consultores)

    def __format(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        dataframe[["receita", "preco", "volume"]] = dataframe[
            ["receita", "preco", "volume"]
        ].apply(pd.to_numeric, errors="coerce", downcast="integer")

        return dataframe
