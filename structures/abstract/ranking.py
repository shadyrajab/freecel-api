import pandas as pd

from utils.functions import jsonfy
from utils.utils import SUPERVISORES


class Rankings:
    def __init__(self, dataframe: pd.DataFrame) -> None:
        self.dataframe = dataframe

    @property
    def planos(self) -> pd.DataFrame:
        return self.get_ranking("plano")

    @property
    def consultores(self) -> pd.DataFrame:
        return self.get_ranking("consultor")

    def get_ranking(self, column: str) -> pd.DataFrame:
        dataframe = self.dataframe.copy()

        quantidade_de_vendas = dataframe[column].value_counts().reset_index()
        quantidade_de_vendas.columns = [column, "clientes"]

        ranking = dataframe.groupby(column, as_index=False).sum(numeric_only=True)
        if column == "consultor":
            ranking = ranking[~ranking["consultor"].isin(SUPERVISORES)]

        final_dataframe = pd.merge(ranking, quantidade_de_vendas, on=column)
        return jsonfy(final_dataframe)