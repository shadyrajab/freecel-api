from typing import List, Optional

import pandas as pd

from utils.functions import jsonfy
from utils.utils import SUPERVISORES


class Rankings:
    def __init__(self, dataframe: pd.DataFrame) -> None:
        self.dataframe = dataframe

    @property
    def ranking_planos(self) -> pd.DataFrame:
        return self.get_ranking("plano")

    @property
    def ranking_geral(self) -> pd.DataFrame:
        return self.get_ranking("consultor")

    def get_ranking(self, column: str, tipo: Optional[List] = None) -> pd.DataFrame:
        dataframe = self.dataframe.copy()
        if tipo:
            dataframe = dataframe[dataframe["tipo"].isin(tipo)]

        dataframe['receita'] = dataframe['receita'].astype(float)
        ranking = dataframe.groupby(column, as_index=False).sum(numeric_only=True)[[column,'receita', 'volume']]
        if column == "consultor":
            ranking = ranking[~ranking["consultor"].isin(SUPERVISORES)]

        return jsonfy(ranking)
