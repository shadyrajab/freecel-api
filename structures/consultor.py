import pandas as pd
from database.dataframe import DataFrame
from typing import Optional
from structures.stats import Stats
from structures.ranking import Rankings

class Consultor(Stats):
    def __init__(self, dataframe: DataFrame):
        self.dataframe = dataframe
        super().__init__(dataframe)
    
    def ranking_planos(self, ano: Optional[int] = None, mes: Optional[str] = None) -> pd.DataFrame:
        dataframe = self.filter_by(ano, mes)
        return Rankings(dataframe).ranking_planos(ano, mes)
    
    def ranking_produtos(self, ano: Optional[int] = None, mes: Optional[str] = None) -> pd.DataFrame:
        return self.__get_ranking__('tipo', ano, mes)
    