from typing import Dict

import pandas as pd

from utils.functions import filter_by


class Stats:
    def __init__(self, dataframe: pd.DataFrame) -> None:
        dataframe["data_recebimento"] = pd.to_datetime(dataframe["data_recebimento"])
        dataframe["receita"] = dataframe["receita"].astype(float)
        self.dataframe = dataframe

    @property
    def periodo_trabalhado(self) -> int:
        dataframe = self.dataframe.copy()
        dataframe["periodo"] = dataframe["data_recebimento"].dt.strftime("%m/%Y")
        meses_trabalhados = dataframe["periodo"].nunique()
        if meses_trabalhados <= 1:
            return 22

        return meses_trabalhados

    @property
    def clientes(self) -> float:
        return float(self.dataframe.shape[0])

    @property
    def receita(self) -> float:
        return float(self.dataframe["receita"].sum())

    @property
    def volume(self) -> float:
        return float(self.dataframe["volume"].sum())

    @property
    def ticket_medio(self) -> float:
        return float(self.receita / self.clientes)

    @property
    def clientes_media(self) -> float:
        return float(self.clientes / self.periodo_trabalhado)

    @property
    def receita_media(self) -> float:
        return float(self.receita / self.periodo_trabalhado)

    @property
    def volume_media(self) -> float:
        return float(self.volume / self.periodo_trabalhado)

    def get_media(self, target: str, metric: str, **filters) -> float:
        dataframe = filter_by(self.dataframe.copy(), **filters)
        unique = dataframe[target].nunique()
        return (dataframe[metric].sum() / unique) if unique != 0 else unique

    def to_json(self) -> Dict:
        data = {}
        for cls in reversed(self.__class__.__mro__):
            for attr_name, attr_value in vars(cls).items():
                if isinstance(attr_value, property):
                    data[attr_name] = getattr(self, attr_name)

        return data
