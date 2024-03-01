import pandas as pd
from typing import Optional
from database.dataframe import DataFrame

class Rankings:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def filter_by(self, ano: Optional[int] = None, mes: Optional[str] = None, tipo: Optional[str] = None):
        return DataFrame.__filter_by__(
            dataframe = self.dataframe, 
            ano = ano, 
            mes = mes, 
            tipo = tipo
        )
    
    def ranking_planos(self):
        return self.__get_ranking__('plano')
    
    def ranking_produtos(self):
        return self.__get_ranking__('tipo')

    def ranking_consultores(self, tipo_venda: Optional[str] = None) -> pd.DataFrame:
        return self.__get_ranking__('consultor', tipo_venda)
    
    def __get_ranking__(self, column: str, tipo_venda: Optional[str] = None) -> DataFrame:
        if tipo_venda and tipo_venda not in {'ALTAS', 'FIXA', 'AVANÇADA', 'VVN', 'MIGRAÇÃO PRÉ-PÓS'}:
            raise ValueError("O tipo de venda deve ser {'ALTAS', 'FIXA' | 'AVANÇADA' | 'VVN' | 'MIGRAÇÃO PRÉ-PÓS'}")
        
        quantidade_de_vendas = self.dataframe[column].value_counts().reset_index()
        quantidade_de_vendas.columns = [column, 'quantidade_de_vendas']

        ranking = self.dataframe.groupby(column, as_index = False).sum(numeric_only = True)
        ranking.drop(['ano', 'valor_do_plano', 'id'], axis = 1, inplace = True)

        return pd.merge(ranking, quantidade_de_vendas, on = column)

