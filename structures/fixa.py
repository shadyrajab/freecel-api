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
        return self.media_por_consultor(FIXA)

    @property
    def media_consultor_vvn(self) -> float:
        return self.media_por_consultor(VVN)

    @property
    def media_consultor_avancada(self) -> float:
        return self.media_por_consultor(AVANCADA)

    @property
    def ranking_fixa(self):
        return self.get_ranking("consultor", FIXA)

    @property
    def ranking_vvn(self):
        return self.get_ranking("consultor", VVN)

    @property
    def ranking_avancada(self):
        return self.get_ranking("consultor", AVANCADA)
