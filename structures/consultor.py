import pandas as pd
from database.dataframe import DataFrame
from typing import Optional
from structures.stats import Stats
from structures.ranking import Rankings

class Consultor(Stats):
    def __init__(self, dataframe: DataFrame, ano: Optional[int] = None, mes: Optional[str] = None):
        self.dataframe = self.filter_by(dataframe, ano, mes)
        super().__init__(self.dataframe)

    @property
    def nome(self):
        return str(self.dataframe['consultor'].unique().iloc[0])
    
    @property
    def ranking_planos(self) -> pd.DataFrame:
        return Rankings(self.dataframe).ranking_planos
    
    @property
    def ranking_produtos(self) -> pd.DataFrame:
        return Rankings(self.dataframe).ranking_produtos
    