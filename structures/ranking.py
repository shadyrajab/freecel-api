from typing import Optional

import pandas as pd

from utils.functions import jsonfy
from utils.variables import ALTAS, AVANCADA, FIXA, MIGRACAO, SUPERVISORES, VVN


class Rankings:
    def __init__(self, dataframe: pd.DataFrame) -> None:
        self.dataframe = dataframe

    @property
    def planos(self):
        return self.__get_ranking("plano")

    @property
    def produtos(self):
        return self.__get_ranking("tipo")

    @property
    def geral(self) -> pd.DataFrame:
        return self.__get_ranking("consultor")

    @property
    def fixa(self) -> pd.DataFrame:
        return self.__get_ranking("consultor", FIXA)

    @property
    def avancada(self) -> pd.DataFrame:
        return self.__get_ranking("consultor", AVANCADA)

    @property
    def vvn(self) -> pd.DataFrame:
        return self.__get_ranking("consultor", VVN)

    @property
    def migracao(self) -> pd.DataFrame:
        return self.__get_ranking("consultor", MIGRACAO)

    @property
    def altas(self) -> pd.DataFrame:
        return self.__get_ranking("consultor", ALTAS)

    @property
    def periodo_trabalhado(self) -> int:
        dataframe = self.dataframe.copy()
        dataframe["periodo"] = dataframe["data"].dt.strftime("%m/%Y")
        meses_trabalhados = dataframe["periodo"].nunique()
        if meses_trabalhados <= 1:
            return 22

        return meses_trabalhados

    def to_json(self):
        data = {}
        for cls in reversed(self.__class__.__mro__):
            for attr_name, attr_value in vars(cls).items():
                if isinstance(attr_value, property):
                    data[attr_name] = getattr(self, attr_name)

        return data

    def __get_ranking(
        self, column: str, tipo_venda: Optional[str] = None
    ) -> pd.DataFrame:
        dataframe = self.dataframe.copy()
        if tipo_venda:
            dataframe = dataframe[dataframe["tipo"].isin(tipo_venda)]

        quantidade_de_vendas = dataframe[column].value_counts().reset_index()
        quantidade_de_vendas.columns = [column, "clientes"]

        ranking = dataframe.groupby(column, as_index=False).sum(numeric_only=True)
        if column == "consultor":
            ranking = ranking[~ranking["consultor"].isin(SUPERVISORES)]

        ranking.drop(
            [
                "preco",
                "id",
                "m",
                "ja_cliente",
                "valor_atual",
                "valor_inovacao",
                "valor_renovacao",
                "volume_inovacao",
            ],
            axis=1,
            inplace=True,
        )

        final_dataframe = pd.merge(ranking, quantidade_de_vendas, on=column)
        return jsonfy(final_dataframe)
