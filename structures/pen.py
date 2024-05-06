import pandas as pd

from utils.variables import PEN

from ..structures.abstract.ranking import Rankings
from ..structures.abstract.stats import Stats


class Pen(Stats, Rankings):
    def __init__(self, dataframe: pd.DataFrame) -> None:
        self.dataframe = dataframe
        super().__init__(dataframe)

    @property
    def media_consultor_pen(self) -> float:
        return self.media_por_consultor(PEN)
