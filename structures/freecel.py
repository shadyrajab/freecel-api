from datetime import datetime
from typing import List, Optional, Self

import pandas as pd

from structures.stats import Stats
from utils.functions import filter_by
from utils.variables import SUPERVISORES


class Freecel(Stats):
    def __init__(
        self,
        dataframe: pd.DataFrame,
        data_inicio: Optional[int] = None,
        data_fim: Optional[str] = None,
        equipe: Optional[str] = None,
        jsonfy: Optional[bool] = None,
        prev_freecel: Optional[bool] = None,
    ) -> None:
        self.full_dataframe = dataframe
        self.jsonfy = jsonfy
        self.data_inicio = self.get_data_inicio(self.full_dataframe, data_inicio)
        self.data_fim = self.get_dafa_fim(data_fim)
        self.dataframe = filter_by(
            dataframe,
            data_inicio=self.data_inicio,
            data_fim=self.data_fim,
            equipe=equipe,
        )

        super().__init__(
            self.full_dataframe, self.data_inicio, self.data_fim, equipe, True
        )

        if prev_freecel is True:
            self.prev_freecel = self.__get_prev_freecel()

    @property
    def media_consultor_geral(self) -> float:
        return self.__media_por_consultor()

    @property
    def media_consultor_altas(self) -> float:
        return self.__media_por_consultor("ALTAS")

    @property
    def media_consultor_migracao(self) -> float:
        return self.__media_por_consultor("MIGRAÇÃO PRÉ-PÓS")

    @property
    def media_consultor_fixa(self) -> float:
        return self.__media_por_consultor("FIXA")

    @property
    def media_consultor_avancada(self) -> float:
        return self.__media_por_consultor("AVANÇADA")

    @property
    def media_consultor_portabilidade(self) -> float:
        return self.__media_por_consultor("PORTABILIDADE")

    @property
    def media_consultor_vvn(self) -> float:
        return self.__media_por_consultor("VVN")

    @property
    def delta_media_consultor_geral(self) -> float:
        return self.calculate_delta(
            self.media_consultor_geral, self.prev_freecel.media_consultor_geral
        )

    @property
    def ufs(self) -> List[str]:
        return list(self.dataframe["uf"].unique())

    def to_json(self):
        data = {}
        for cls in reversed(self.__class__.__mro__):
            for attr_name, attr_value in vars(cls).items():
                if isinstance(attr_value, property):
                    data[attr_name] = getattr(self, attr_name)

        return data

    def __media_por_consultor(self, tipo: Optional[str] = None) -> float:
        dataframe = filter_by(dataframe=self.dataframe, tipo=tipo)
        dataframe = dataframe[~dataframe["consultor"].isin(SUPERVISORES)]
        consultores = dataframe["consultor"].nunique()
        if consultores == 0:
            return 0

        media_por_consultor = dataframe["receita"].sum() / consultores
        return media_por_consultor

    def __get_prev_freecel(self) -> Self:
        prev_data_inicio, prev_data_fim = self.get_prev_data()
        prev_data_inicio = str(prev_data_inicio.strftime("%d-%m-%Y"))
        prev_data_fim = str(prev_data_fim.strftime("%d-%m-%Y"))
        prev_freecel = Freecel(
            self.full_dataframe, str(prev_data_inicio), str(prev_data_fim)
        )

        return prev_freecel
