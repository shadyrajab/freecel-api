from database.connection import DataBaseConnection
from structures.consultor.consultor import Consultor

import streamlit
    
class Client(
    DataBaseConnection
):
    def __init__(self, host, database, user, password):
        super().__init__(
            host,
            database,
            user,
            password
        )

        self.Consultor = Consultor