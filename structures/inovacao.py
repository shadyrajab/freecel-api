import pandas as pd

from utils.variables import INOVACAO

from ..structures.abstract.ranking import Rankings
from ..structures.abstract.stats import Stats


class Inovacao(Stats, Rankings):
    def __init__(self, dataframe: pd.DataFrame) -> None:
        self.dataframe = dataframe
        super().__init__(dataframe)

    @property
    def media_consultor_inovacao(self) -> float:
        return self.media_por_consultor(INOVACAO)
