from io import StringIO
from json import load

from pandas import DataFrame

from utils.variables import MONTHS, adabas_mapping


def group_by(dataframe: DataFrame, column: str, sort: str) -> DataFrame:
    """Agrupa o DataFrame e ordena de acordo com a chave passada"""
    grouped_dataframe = (
        dataframe.groupby(column, as_index=False)
        .sum(numeric_only=True)
        .sort_values(by=sort, ascending=False)
    )

    return grouped_dataframe


def jsonfy(dataframe: DataFrame):
    """Converte um pd.DataFrame em um JSON"""
    df = dataframe.to_json(orient="records")
    return load(StringIO(df))


def get_adabas(equipe, tipo) -> str:
    """Mapeia e retorna o ADABAS da venda de acordo com a Equipe e o Tipo de venda"""
    return adabas_mapping.get((equipe, tipo), None)


def filter_by(dataframe: DataFrame, **filters: str) -> DataFrame:
    """Função para filtrar o DataFrame de acordo com os filtros passados em **filters"""
    for column, value in filters.items():
        if value is not None:
            value = int(value) if column == "ano" else value.upper()
            dataframe = dataframe[dataframe[column] == value]

    return dataframe


def get_mes(mes) -> str:
    """Função retorna o mês de acordo com o Index, feita para formatar as datas do DataFrame"""
    return MONTHS[mes - 1]
