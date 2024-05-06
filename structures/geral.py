import pandas as pd

from structures.abstract.ranking import Rankings
from structures.abstract.stats import Stats


class Geral(Stats, Rankings):
    def __init__(self, dataframe: pd.DataFrame) -> None:
        self.dataframe = dataframe
        super().__init__(dataframe)
