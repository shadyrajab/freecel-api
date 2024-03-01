from structures.stats import Stats
import pandas as pd
from typing import Optional
from utils.functions import calculate_delta

class Freecel(Stats):
    def __init__(self, dataframe: pd.DataFrame) -> None:
        self.dataframe = dataframe
        super().__init__(dataframe)

    @property
    def ufs(self) -> list[str]:
        return list(self.dataframe['uf'].unique())

    def media_por_consultor(self, ano: Optional[int] = None, mes: Optional[str] = None, tipo: Optional[str] = None) -> float:
        dataframe: pd.DataFrame = self.filter_by(ano, mes, tipo)
        consultores: int = dataframe['consultor'].nunique()
        media_por_consultor: int = dataframe['valor_acumulado'].sum() / consultores

        return media_por_consultor
    
    def delta_media_por_consultor(self, ano: Optional[int] = None, mes: Optional[str] = None) -> float:
        return calculate_delta(self.years, self.media_por_consultor, ano, mes)