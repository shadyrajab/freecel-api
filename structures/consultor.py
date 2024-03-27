from typing import Optional

import pandas as pd

from structures.ranking import Rankings
from structures.stats import Stats
from utils.functions import filter_by, jsonfy


class Consultor(Stats):
    def __init__(
        self,
        dataframe: pd.DataFrame,
        ano: Optional[int] = None,
        mes: Optional[str] = None,
        jsonfy: Optional[bool] = None,
        display_vendas: Optional[bool] = None,
    ) -> None:
        self.full_dataframe = dataframe
        self.dataframe = filter_by(dataframe, ano=ano, mes=mes)
        self.jsonfy = jsonfy
        self.display_vendas = display_vendas
        self.ano = ano
        self.mes = mes.capitalize() if mes else mes
        super().__init__(self.full_dataframe, ano=ano, mes=mes, prev_stats=True)

    @property
    def nome(self) -> str:
        return str(self.dataframe["consultor"].unique()[0])

    @property
    def ranking_planos(self) -> pd.DataFrame:
        return Rankings(self.dataframe, jsonfy=True).planos

    @property
    def ranking_produtos(self) -> pd.DataFrame:
        return Rankings(self.dataframe, jsonfy=True).produtos

    @property
    def vendas(self):
        if not self.display_vendas:
            return {}

        if self.jsonfy:
            return jsonfy(self.dataframe)

        return self.dataframe

    def to_json(self):
        data = {}
        for cls in reversed(self.__class__.__mro__):
            for attr_name, attr_value in vars(cls).items():
                if isinstance(attr_value, property):
                    data[attr_name] = getattr(self, attr_name)

        return data
