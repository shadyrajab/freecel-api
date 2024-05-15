import pandas as pd

from structures.abstract.ranking import Rankings
from structures.abstract.stats import Stats
from utils.variables import AVANCADA, FIXA, VVN


class Fixa(Stats, Rankings):
    def __init__(self, dataframe: pd.DataFrame) -> None:
        self.dataframe = dataframe
        super().__init__(dataframe)

    @property
    def media_consultor_fixa(self) -> float:
        return self.get_media("consultor", "receita", esteira=FIXA)

    @property
    def media_consultor_vvn(self) -> float:
        return self.get_media("consultor", "receita", esteira=VVN)

    @property
    def media_consultor_avancada(self) -> float:
        return self.get_media("consultor", "receita", esteira=AVANCADA)

    @property
    def ranking_fixa(self):
        return self.get_ranking("consultor", esteira=FIXA)

    @property
    def ranking_vvn(self):
        return self.get_ranking("consultor", esteira=VVN)

    @property
    def ranking_avancada(self):
        return self.get_ranking("consultor", esteira=AVANCADA)
