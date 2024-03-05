import pandas as pd
from typing import Optional
from database.dataframe import DataFrame
from utils.variables import TIPO_VENDA
from utils.functions import jsonfy

class Rankings:
    def __init__(self, dataframe: pd.DataFrame, ano: Optional[int] = None, mes: Optional[str] = None, jsonfy: Optional[bool] = None):
        self.dataframe = self.filter_by(dataframe, ano, mes)
        self.jsonfy = jsonfy
        self.ano = ano
        self.mes = mes.capitalize() if mes else mes

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
    def geral(self) -> pd.DataFrame:
        return self.__get_ranking('consultor')

    @property
    def fixa(self) -> pd.DataFrame:
        return self.__get_ranking('consultor', 'FIXA')
    
    @property
    def avancada(self) -> pd.DataFrame:
        return self.__get_ranking('consultor', 'AVANÇADA')
    
    @property
    def vvn(self) -> pd.DataFrame:
        return self.__get_ranking('consultor', 'VVN')
    
    @property
    def migracao(self) -> pd.DataFrame:
        return self.__get_ranking('consultor', 'MIGRAÇÃO PRÉ-PÓS')
    
    @property
    def altas(self) -> pd.DataFrame:
        return self.__get_ranking('consultor', 'ALTAS')

    @property
    def altas(self) -> pd.DataFrame:
        return self.__get_ranking('consultor', 'PORTABILIDADE')
    
    def to_json(self):
        data = {}
        for cls in reversed(self.__class__.__mro__):
            for attr_name, attr_value in vars(cls).items():
                if isinstance(attr_value, property):
                    data[attr_name] = getattr(self, attr_name)

        return data
    
    def __get_ranking(self, column: str, tipo_venda: Optional[str] = None) -> DataFrame:
        if tipo_venda and tipo_venda not in TIPO_VENDA:
            raise ValueError(f"O tipo de venda deve ser {str(TIPO_VENDA)}")
        
        quantidade_de_vendas = self.dataframe[column].value_counts().reset_index()
        quantidade_de_vendas.columns = [column, 'quantidade_de_vendas']

        ranking = self.dataframe.groupby(column, as_index = False).sum(numeric_only = True)
        ranking.drop(['ano', 'valor_do_plano', 'id'], axis = 1, inplace = True)

        final_dataframe = pd.merge(ranking, quantidade_de_vendas, on = column)
        if self.jsonfy:
            return jsonfy(final_dataframe)
        
        return final_dataframe

