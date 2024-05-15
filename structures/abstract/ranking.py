from typing import List, Optional

import pandas as pd

from utils.functions import jsonfy


class Rankings:
    def __init__(self, dataframe: pd.DataFrame) -> None:
        self.dataframe = dataframe

    @property
    def ranking_planos(self) -> pd.DataFrame:
        return self.get_ranking("plano")

    @property
    def ranking_consultores(self) -> pd.DataFrame:
        return self.get_ranking("consultor")

    @property
    def ranking_vinculos(self) -> pd.DataFrame:
        return self.get_ranking("vinculo")
    
    @property
    def ranking_equipes(self) -> pd.DataFrame:
        return self.get_ranking("equipe")

    @property
    def ranking_tipos(self) -> pd.DataFrame:
        return self.get_ranking("tipo")
    
    @property
    def ranking_status(self) -> pd.DataFrame:
        return self.get_ranking("status")

    def get_ranking(self, column: str, tipo: Optional[List] = None) -> pd.DataFrame:
        dataframe = self.dataframe.copy()
        print(dataframe.info())
        if tipo:
            dataframe = dataframe[dataframe["tipo"].isin(tipo)]

        dataframe["receita"] = dataframe["receita"].astype(float)
        ranking = dataframe.groupby(column, as_index=False).sum(numeric_only=True)[
            [column, "receita", "volume"]
        ]
        return jsonfy(ranking)
