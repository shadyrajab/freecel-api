import psycopg2

class DataBaseConnection:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

        self.cursor = self.__create_connection__()
    
    def __create_connection__(self):
        """
            Realizando a conexão com o banco de dados da Freecel.
        """
        
        connection = psycopg2.connect(
            host = 'localhost', 
            database = 'freecel', 
            user = 'postgres', 
            password = '@sH^2004_'
        )

        cursor = connection.cursor()

        return cursor