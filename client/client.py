from structures.consultor import Consultor
from structures.ranking import Rankings
from structures.freecel import Freecel
from database.dataframe import DataFrame
from utils.functions import jsonfy
from typing import Optional
    
class Client(DataFrame):
    def __init__(self, host, database, user, password):
        super().__init__(
            host,
            database,
            user,
            password
        )
    
    def Consultor(self, nome: str, ano: Optional[int] = None, mes: Optional[str] = None, jsonfy: Optional[bool] = None, display_vendas: Optional[bool] = None) -> Consultor:
        return Consultor(self.dataframe[self.dataframe['consultor'] == nome], ano, mes, jsonfy, display_vendas)
    
    def Ranking(self, ano: Optional[int] = None, mes: Optional[str] = None, jsonfy: Optional[bool] = None) -> Rankings:
        return Rankings(self.dataframe, ano, mes, jsonfy)
    
    def Freecel(self, ano: Optional[int] = None, mes: Optional[str] = None, jsonfy: Optional[bool] = None) -> Freecel:
        return Freecel(self.dataframe, ano, mes, jsonfy, True)
    
    def vendas(self, ano: Optional[int] = None, mes: Optional[str] = None, as_json: Optional[bool] = None):
        dataframe = self.__filter_by__(self.dataframe, ano, mes)
        if as_json:
            return jsonfy(dataframe)
        
        return dataframe
    
    def produtos(self, as_json: Optional[bool] = None):
        produtos = self.get_produtos(to_dataframe=True)
        if as_json:
            return jsonfy(produtos)
        
        return produtos
    
    def consultores(self, as_json: Optional[bool] = None):
        consultores = self.get_consultores(to_dataframe=True)
        if as_json:
            return jsonfy(consultores)
        
        return consultores
