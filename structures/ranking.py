import pandas as pd
from typing import Optional
from database.dataframe import DataFrame
from utils.variables import TIPO_VENDA

class Rankings:
    def __init__(self, dataframe: pd.DataFrame, ano: Optional[int] = None, mes: Optional[str] = None):
        self.dataframe = self.filter_by(dataframe, ano, mes)

    def filter_by(self, dataframe: pd.DataFrame, ano: Optional[int] = None, mes: Optional[str] = None, tipo: Optional[str] = None):
        return DataFrame.__filter_by__(
            dataframe = dataframe, 
            ano = ano, 
            mes = mes, 
            tipo = tipo
        )
    
    @property
    def planos(self):
        return self.__get_ranking('plano')
    
    @property
    def produtos(self):
        return self.__get_ranking('tipo')

    @property
    def consultores(self) -> pd.DataFrame:
        return self.__get_ranking('consultor')

    @property
    def fixa(self) -> pd.DataFrame:
        return self.__get_ranking('tipo', 'FIXA')
    
    @property
    def avancada(self) -> pd.DataFrame:
        return self.__get_ranking('tipo', 'AVANÇADA')
    
    @property
    def vvn(self) -> pd.DataFrame:
        return self.__get_ranking('tipo', 'VVN')
    
    @property
    def migracao(self) -> pd.DataFrame:
        return self.__get_ranking('tipo', 'MIGRAÇÃO PRÉ-PÓS')
    
    @property
    def altas(self) -> pd.DataFrame:
        return self.__get_ranking('tipo', 'ALTAS')
    
    def __get_ranking(self, column: str, tipo_venda: Optional[str] = None) -> DataFrame:
        if tipo_venda and tipo_venda not in TIPO_VENDA:
            raise ValueError(f"O tipo de venda deve ser {str(TIPO_VENDA)}")
        
        quantidade_de_vendas = self.dataframe[column].value_counts().reset_index()
        quantidade_de_vendas.columns = [column, 'quantidade_de_vendas']

        ranking = self.dataframe.groupby(column, as_index = False).sum(numeric_only = True)
        ranking.drop(['ano', 'valor_do_plano', 'id'], axis = 1, inplace = True)

        return pd.merge(ranking, quantidade_de_vendas, on = column)

