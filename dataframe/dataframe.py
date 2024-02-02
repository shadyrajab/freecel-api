import pandas as pd

from database.connection import DataBaseConnection

class DataFrame(
    DataBaseConnection
):
    def __init__(self, host, database, user, password):
        super().__init__(
            host = host, 
            database = database, 
            user = user, 
            password = password
        )
    
        self.cursor = self.__create_connection__()
        self.dataframe = self.get_full_dataframe()

    def get_full_dataframe(self):
        query = 'SELECT * FROM VENDAS_CONCLUIDAS'
        dataframe = pd.read_sql(self.cursor, query)

        return dataframe
    
    def filter_by(self, ano: int = None, mes: str = None):
        dataframe = self.dataframe.copy()

        if ano:
            dataframe = dataframe[dataframe['ANO'] == ano]
        if mes and ano:
            dataframe = dataframe[dataframe['ANO'] == ano]

        self.dataframe = dataframe

        return self
