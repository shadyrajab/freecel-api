import pandas as pd
from database.dataframe import DataFrame
from typing import Optional
from structures.stats import Stats
from structures.ranking import Rankings
from utils.functions import jsonfy

class Consultor(Stats):
    def __init__(self, dataframe: DataFrame, ano: Optional[int] = None, mes: Optional[str] = None, jsonfy: Optional[bool] = None, display_vendas: Optional[bool] = None):
        self.dataframe = self.filter_by(dataframe, ano, mes)
        self.jsonfy = jsonfy
        self.display_vendas = display_vendas
        super().__init__(self.dataframe)

    @property
    def nome(self) -> str:
        return str(self.dataframe['consultor'].unique()[0])
    
    @property
    def ranking_planos(self) -> pd.DataFrame:
        return Rankings(self.dataframe, jsonfy = True).planos
    
    @property
    def ranking_produtos(self) -> pd.DataFrame:
        return Rankings(self.dataframe, jsonfy = True).produtos
    
    @property
    def vendas(self):
        if not self.display_vendas:
            return {}
        
        elif self.jsonfy:
            return jsonfy(self.dataframe)
        
        return self.dataframe
    
    def to_json(self):
        data = {}
        for cls in reversed(self.__class__.__mro__):
            for attr_name, attr_value in vars(cls).items():
                if isinstance(attr_value, property):
                    data[attr_name] = getattr(self, attr_name)
                    
        return data
