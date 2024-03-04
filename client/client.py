from structures.consultor import Consultor
from structures.ranking import Rankings
from structures.freecel import Freecel
from database.dataframe import DataFrame
from typing import Optional
    
class Client(DataFrame):
    def __init__(self, host, database, user, password):
        super().__init__(
            host,
            database,
            user,
            password
        )

    def Consultor(self, nome: str, ano: Optional[int] = None, mes: Optional[str] = None) -> Consultor:
        return Consultor(self.dataframe[self.dataframe['consultor'] == nome], ano, mes)
    
    def Ranking(self, ano: Optional[int] = None, mes: Optional[str] = None) -> Rankings:
        return Rankings(self.dataframe, ano, mes)
    
    def Freecel(self, ano: Optional[int] = None, mes: Optional[str] = None) -> Freecel:
        return Freecel(self.dataframe, ano, mes)