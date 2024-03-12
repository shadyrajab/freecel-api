from structures.consultor import Consultor
from structures.ranking import Rankings
from structures.freecel import Freecel
from utils.functions import jsonfy, filter_by, get_mes
from typing import Optional
from database.connection import DataBase
import pandas as pd
    
class Client(DataBase):
    async def __aenter__(self):
        await super().__aenter__()
        return self
    
    async def __aexit__(self, exc_type, exc, tb):
        await super().__aexit__(exc_type, exc, tb)
         
    async def Consultor(self, nome: str, ano: Optional[int] = None, mes: Optional[str] = None, jsonfy: Optional[bool] = None, display_vendas: Optional[bool] = None) -> Consultor:
        dataframe = self.__format(await self.get_vendas(to_dataframe=True))
        return Consultor(dataframe[dataframe['consultor'] == nome], ano, mes, jsonfy, display_vendas)
    
    async def Ranking(self, ano: Optional[int] = None, mes: Optional[str] = None, jsonfy: Optional[bool] = None) -> Rankings:
        dataframe = self.__format(await self.get_vendas(to_dataframe=True))
        return Rankings(dataframe, ano, mes, jsonfy)
    
    async def Freecel(self, ano: Optional[int] = None, mes: Optional[str] = None, jsonfy: Optional[bool] = None) -> Freecel:
        dataframe = self.__format(await self.get_vendas(to_dataframe=True))
        return Freecel(dataframe, ano, mes, jsonfy, True)
    
    # Essas 3 funções abaixo estão muito mal escritas
    async def vendas(self, as_json: Optional[bool] = None, **filters: str):
        dataframe = self.__format(await self.get_vendas(to_dataframe=True))
        dataframe = filter_by(dataframe, **filters)
        if as_json:
            return jsonfy(dataframe)
        
        return dataframe
    
    async def produtos(self, as_json: Optional[bool] = None):
        produtos = await self.get_produtos(to_dataframe=True)
        if as_json:
            return jsonfy(produtos)
        
        return produtos
    
    async def consultores(self, as_json: Optional[bool] = None):
        consultores = await self.get_consultores(to_dataframe=True)
        if as_json:
            return jsonfy(consultores)
        
        return consultores

    def __format(self, dataframe: pd.DataFrame):
        dataframe['ano'] = dataframe['data'].dt.year
        dataframe['mes'] = dataframe['data'].dt.month.apply(lambda mes: get_mes(mes))
        dataframe[['valor_acumulado', 'valor_do_plano', 'quantidade_de_produtos']] = dataframe[
                ['valor_acumulado', 'valor_do_plano', 'quantidade_de_produtos']
            ].apply(pd.to_numeric, errors='coerce', downcast='integer')
        
        return dataframe
