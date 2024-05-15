from typing import Dict

import pandas as pd

from structures.abstract.ranking import Rankings
from structures.abstract.stats import Stats
from utils.functions import jsonfy


class Consultor(Stats, Rankings):
    def __init__(self, dataframe: pd.DataFrame) -> None:
        self.dataframe = dataframe
        super().__init__(self.dataframe)

    @property
    def nome(self) -> str:
        return str(self.dataframe["consultor"].unique()[0])

    @property
    def vendas(self) -> Dict:
        return jsonfy(self.dataframe)
