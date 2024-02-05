import pandas as pd
from database.objects import dataframe_geral, meses
from database.connection import DataBase

from typing import Optional

class DataFrame(
    DataBase
):
    def __init__(self, host, database, user, password):
        super().__init__(
            host = host, 
            database = database, 
            user = user, 
            password = password
        )
        
        self.dataframe = self.get_full_dataframe()

    def get_full_dataframe(self):
        # query = 'SELECT * FROM VENDAS_CONCLUIDAS'
        # dataframe = pd.read_sql(self.cursor, query)

        dataframe_geral['DATA'] = dataframe_geral['ANO'].astype(str) + '/' + dataframe_geral['MÊS']
        return dataframe_geral

    @staticmethod
    def filter_by(
        dataframe, ano: Optional[int] = None, mes: Optional[str] = None, consultor: Optional[str] = None,
        tipo: Optional[int] = None):

        """
        Filtra um DataFrame com base nos parâmetros fornecidos.

        Parâmetros
        ----------
        dataframe : pd.DataFrame
            O DataFrame a ser filtrado.

        ano : int | None
            O ano para o qual deseja filtrar os dados.

        mes : str | None
            O mês para o qual deseja filtrar os dados.

        consultor : str | None
            O nome do consultor para o qual deseja filtrar os dados.

        Retorna
        -------
        pd.DataFrame
            O DataFrame filtrado.
        """
        # Verifica o formato do mês

        if mes and mes.capitalize() not in meses:
            raise ValueError('Formato de mês inválido. Por favor, escreva o nome do mês completo com acentos.')
        
        # Aplica os filtros
        filters = {
            'ANO': ano,
            'MÊS': mes,
            'CONSULTOR': consultor,
            'TIPO': tipo
        }

        for column, value in filters.items():
            if value is not None:
                dataframe = dataframe[dataframe[column] == value]

        return dataframe

