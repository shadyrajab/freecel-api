from datetime import datetime, timedelta
from typing import Optional, Self

import pandas as pd

from utils.functions import filter_by
from utils.variables import MONTHS


class Stats:
    def __init__(
        self,
        dataframe: pd.DataFrame,
        data_inicio: Optional[int] = None,
        data_fim: Optional[str] = None,
        equipe: Optional[str] = None,
        prev_stats: Optional[bool] = None,
    ) -> None:
        self.full_dataframe = dataframe
        self.data_inicio = self.get_data_inicio(self.full_dataframe, data_inicio)
        self.data_fim = self.get_dafa_fim(data_fim)
        self.dataframe = filter_by(
            dataframe,
            data_inicio=self.data_inicio,
            data_fim=self.data_fim,
            equipe=equipe,
        )
        if prev_stats is True:
            self.prev_stats = self.__get_prev_stats()

    def years(self) -> list[int]:
        return list(self.full_dataframe["ano"].unique())

    def months(self, ano) -> list[str]:
        return sorted(
            list(filter_by(self.full_dataframe, ano=ano)["mes"].unique()),
            key=MONTHS.index,
        )

    @property
    def periodo_trabalhado(self) -> int:
        dataframe = self.dataframe.copy()
        dataframe["periodo"] = dataframe["data"].dt.strftime("%m/%Y")
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

    @property
    def delta_clientes(self) -> int:
        return self.calculate_delta(self.clientes, self.prev_stats.clientes)

    @property
    def delta_receita(self) -> int:
        return self.calculate_delta(self.receita, self.prev_stats.receita)

    @property
    def delta_volume(self) -> int:
        return self.calculate_delta(self.volume, self.prev_stats.volume)

    @property
    def delta_ticket_medio(self) -> int:
        return self.calculate_delta(self.ticket_medio, self.prev_stats.ticket_medio)

    @property
    def delta_clientes_media(self) -> int:
        return self.calculate_delta(self.clientes_media, self.prev_stats.clientes_media)

    @property
    def delta_receita_media(self) -> int:
        return self.calculate_delta(self.receita_media, self.prev_stats.receita_media)

    @property
    def delta_volume_media(self) -> int:
        return self.calculate_delta(self.volume_media, self.prev_stats.volume_media)

    def calculate_delta(self, now_metric, prev_metric) -> float:
        return now_metric - prev_metric

    def get_prev_data(self) -> tuple[str]:
        data_inicio = datetime.strptime(self.data_inicio, "%d-%m-%Y")
        data_fim = datetime.strptime(self.data_fim, "%d-%m-%Y")
        diff = (data_fim - data_inicio).days
        prev_data_inicio = data_inicio - timedelta(days=diff)
        prev_data_fim = data_inicio
        return prev_data_inicio, prev_data_fim

    def __get_prev_stats(self) -> Self:
        prev_data_inicio, prev_data_fim = self.get_prev_data()
        prev_stats = Stats(self.full_dataframe, prev_data_inicio, prev_data_fim)
        return prev_stats

    @staticmethod
    def get_data_inicio(dataframe, data_inicio):
        if data_inicio is None:
            return dataframe["data"].min().strftime("%d-%m-%Y")

        return data_inicio

    @staticmethod
    def get_dafa_fim(data_fim):
        if data_fim is None:
            return datetime.now().strftime("%d-%m-%Y")

        return data_fim
