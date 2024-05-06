import pandas as pd

from structures.abstract.ranking import Rankings
from structures.abstract.stats import Stats
from utils.variables import MIGRACAO


class Migracao(Stats, Rankings):
    def __init__(self, dataframe: pd.DataFrame) -> None:
        self.dataframe = dataframe
        super().__init__(dataframe)

    @property
    def media_consultor_migracao(self) -> float:
        return self.media_por_consultor(MIGRACAO)
