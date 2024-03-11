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
        self.dataframe = await self.get_vendas(to_dataframe=True)
        self.__format()

        return self
    
    async def __aexit__(self, exc_type, exc, tb):
        await super().__aexit__(exc_type, exc, tb)
         
    def Consultor(self, nome: str, ano: Optional[int] = None, mes: Optional[str] = None, jsonfy: Optional[bool] = None, display_vendas: Optional[bool] = None) -> Consultor:
        return Consultor(self.dataframe[self.dataframe['consultor'] == nome], ano, mes, jsonfy, display_vendas)
    
    def Ranking(self, ano: Optional[int] = None, mes: Optional[str] = None, jsonfy: Optional[bool] = None) -> Rankings:
        return Rankings(self.dataframe, ano, mes, jsonfy)
    
    def Freecel(self, ano: Optional[int] = None, mes: Optional[str] = None, jsonfy: Optional[bool] = None) -> Freecel:
        return Freecel(self.dataframe, ano, mes, jsonfy, True)
    
    # Essas 3 funções abaixo estão muito mal escritas
    async def vendas(self, ano: Optional[int] = None, mes: Optional[str] = None, as_json: Optional[bool] = None):
        dataframe = filter_by(self.dataframe, ano, mes)
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

    def __format(self):
        self.dataframe['ano'] = self.dataframe['data'].dt.year
        self.dataframe['mês'] = self.dataframe['data'].dt.month.apply(lambda mes: get_mes(mes))
        self.dataframe[['valor_acumulado', 'valor_do_plano', 'quantidade_de_produtos']] = self.dataframe[
                ['valor_acumulado', 'valor_do_plano', 'quantidade_de_produtos']
            ].apply(pd.to_numeric, errors='coerce', downcast='integer')
