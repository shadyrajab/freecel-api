import pandas as pd

from structures.abstract.ranking import Rankings
from structures.abstract.stats import Stats
from utils.variables import ALTAS, MIGRACAO_PREPOS, PEN, MIGRACAO


class Movel(Stats, Rankings):
    def __init__(self, dataframe: pd.DataFrame) -> None:
        self.dataframe = dataframe
        super().__init__(dataframe)

    @property
    def media_consultor_migracao_prepos(self) -> float:
        return self.media_por_consultor(MIGRACAO_PREPOS)

    @property
    def media_consultor_altas(self) -> float:
        return self.media_por_consultor(ALTAS)

    @property
    def media_consultor_pen(self) -> float:
        return self.media_por_consultor(PEN)

    @property
    def ranking_altas(self):
        return self.get_ranking("consultor", ALTAS)

    @property
    def ranking_pen(self):
        return self.get_ranking("consultor", PEN)

    @property
    def ranking_migracao_prepos(self):
        return self.get_ranking("consultor", MIGRACAO_PREPOS)

    @property
    def ranking_migracoes(self):
        return self.get_ranking("consultor", MIGRACAO)