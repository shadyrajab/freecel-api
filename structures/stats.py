from typing import Optional, Self

import pandas as pd

from utils.functions import filter_by
from utils.variables import MONTHS


class Stats:
    def __init__(
        self,
        dataframe: pd.DataFrame,
        ano: Optional[int] = None,
        mes: Optional[str] = None,
        equipe: Optional[str] = None,
        prev_stats: Optional[bool] = None,
    ) -> None:
        self.full_dataframe = dataframe
        self.dataframe = filter_by(dataframe, ano=ano, mes=mes, equipe=equipe)
        self.ano = ano
        self.mes = mes.upper() if mes else mes
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

    @property
    def dates(self) -> list[dict]:
        return [{f"{year}": self.months(year)} for year in self.years()]

    def calculate_delta(self, now_metric, prev_metric) -> float:
        return now_metric - prev_metric

    def get_prev_data(self, years) -> tuple[int, str | None]:
        if not self.ano and not self.mes:
            return None, None
        if self.ano == min(years) and not self.mes:
            return None, None
        if self.ano == min(years) and self.mes.upper() == "JANEIRO":
            return None, None

        if self.ano and not self.mes:
            prev_year = self.ano - 1
            return prev_year, None

        prev_year = self.ano - 1 if self.mes == "JANEIRO" else self.ano
        prev_month = MONTHS[MONTHS.index(self.mes) - 1]
        return prev_year, prev_month

    def __get_prev_stats(self) -> Self:
        prev_year, prev_month = self.get_prev_data(self.years())
        prev_stats = Stats(self.full_dataframe, prev_year, prev_month)

        return prev_stats
