import psycopg2

class DataBase:
    def __init__(self, host, database, user, password):
        self.connection = self.__create_connection__(host, database, user, password)
        self.cursor = self.connection.cursor()
    
    def __create_connection__(self, host, database, user, password):
        """
            Realizando a conexão com o banco de dados da Freecel.
        """
        
        connection = psycopg2.connect(
            host = host, 
            database = database, 
            user = user, 
            password = password
        )

        return connection