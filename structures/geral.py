import pandas as pd

from structures.fixa import Fixa
from structures.movel import Movel


class Geral(Fixa, Movel):
    def __init__(self, dataframe: pd.DataFrame) -> None:
        self.dataframe = dataframe
        super().__init__(dataframe)
