import pandas as pd

from utils.variables import ALTAS, MIGRACAO_PREPOS

from ..structures.abstract.ranking import Rankings
from ..structures.abstract.stats import Stats


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
