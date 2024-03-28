import pandas as pd

from structures.ranking import Rankings
from structures.stats import Stats
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
    def vendas(self):
        return jsonfy(self.dataframe)

    def to_json(self):
        data = {}
        for cls in reversed(self.__class__.__mro__):
            for attr_name, attr_value in vars(cls).items():
                if isinstance(attr_value, property):
                    data[attr_name] = getattr(self, attr_name)

        return data
