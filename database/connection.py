import psycopg2

class DataBase:
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
        
        connection = psycopg2.connect(self.host, self.database, self.user, self.password)
        cursor = connection.cursor()

        return cursor