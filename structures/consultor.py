from typing import Dict

import pandas as pd

from structures.abstract.ranking import Rankings
from structures.abstract.stats import Stats
from utils.functions import jsonfy


class Consultor(Stats):
    def __init__(self, dataframe: pd.DataFrame) -> None:
        self.dataframe = dataframe
        super().__init__(self.dataframe)

    @property
    def nome(self) -> str:
        return str(self.dataframe["consultor"].unique()[0])

    @property
    def ranking_planos(self) -> pd.DataFrame:
        return Rankings(self.dataframe).planos

    @property
    def ranking_produtos(self) -> pd.DataFrame:
        return Rankings(self.dataframe).produtos

    @property
    def vendas(self) -> Dict:
        return jsonfy(self.dataframe)
