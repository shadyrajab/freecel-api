import pandas as pd

from utils.variables import AVANCADA, FIXA, VVN

from structures.abstract.ranking import Rankings
from structures.abstract.stats import Stats


class Fixa(Stats, Rankings):
    def __init__(self, dataframe: pd.DataFrame) -> None:
        self.dataframe = dataframe
        super().__init__(dataframe)

    @property
    def media_consultor_fixa(self) -> float:
        return self.__media_por_consultor(FIXA)

    @property
    def media_consultor_vvn(self) -> float:
        return self.__media_por_consultor(VVN)

    @property
    def media_consultor_avancada(self) -> float:
        return self.__media_por_consultor(AVANCADA)
