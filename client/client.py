from structures.consultor import Consultor
from structures.ranking import Rankings
from structures.freecel import Freecel
from database.dataframe import DataFrame
    
class Client(DataFrame):
    def __init__(self, host, database, user, password):
        super().__init__(
            host,
            database,
            user,
            password
        )

    def Consultor(self, nome: str) -> Consultor:
        return Consultor(self.dataframe[self.dataframe['consultor'] == nome])
    
    def Ranking(self) -> Rankings:
        return Rankings(self.dataframe)
    
    def Freecel(self) -> Freecel:
        return Freecel(self.dataframe)