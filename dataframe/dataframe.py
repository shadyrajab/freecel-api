import pandas as pd

from database.connection import DataBaseConnection

class DataFrame(
    DataBaseConnection
):
    def __init__(self, dbname, user, host, port):
        super().__init__(
            dbname = dbname,
            user = user,
            host = host,
            port = port
        )
    
        self.database = self.__create_connection__(self)
        self.dataframe = self.__convert_database_to_dataframe__(self)

    def __convert_database_to_dataframe__(self):
        query = 'SELECT * FROM VENDAS_CONCLUIDAS'
        dataframe = pd.read_sql(self.database, query)

        return dataframe
    
