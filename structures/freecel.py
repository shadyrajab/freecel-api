from typing import List, Optional

import pandas as pd

from structures.stats import Stats
from utils.functions import filter_by
from utils.variables import SUPERVISORES


class Freecel(Stats):
    def __init__(self, dataframe: pd.DataFrame) -> None:
        self.dataframe = dataframe

        super().__init__(dataframe)

    @property
    def media_consultor_geral(self) -> float:
        return self.__media_por_consultor()

    @property
    def media_consultor_altas(self) -> float:
        return self.__media_por_consultor("ALTAS")

    @property
    def media_consultor_migracao(self) -> float:
        return self.__media_por_consultor("MIGRAÇÃO PRÉ/PÓS")

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
