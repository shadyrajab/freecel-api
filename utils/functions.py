from io import StringIO
from json import load

from pandas import DataFrame

from utils.variables import MONTHS, adabas_mapping


def get_clause(**params):
    """Cria os valores necessários para criar uma query SQL de acordo com os kwargs passados"""
    id = params.get("id", None)
    if id is None:
        return
    del params["id"]
    for i, (key, value) in enumerate(params.copy().items()):
        if value is None:
            del params[key]
    set_clause = ", ".join(
        f"{key} = ${i + 1}"
        for i, (key, value) in enumerate(params.items())
        if value is not None
    )

    values = [value for value in params.values() if value is not None] + [id]

    return id, set_clause, values


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
    for _i, (key, value) in enumerate(filters.copy().items()):
        if value is None:
            del filters[key]

    if "data_inicio" and "data_fim" in filters.keys():
        dataframe = dataframe.loc[
            (dataframe["data"] >= filters.get("data_inicio"))
            & (dataframe["data"] <= filters.get("data_fim"))
        ]

        del filters["data_inicio"]
        del filters["data_fim"]

    for column, value in filters.items():
        value = (
            value.upper()
            if type(value) == str
            else int(value) if column == "ano" else value
        )
        if column == "tipo" and value == "~MIGRAÇÃO":
            dataframe = dataframe[dataframe[column] != "MIGRAÇÃO"]
        else:
            dataframe = dataframe[dataframe[column] == value]

    return dataframe


def get_mes(mes) -> str:
    """Função retorna o mês de acordo com o Index, feita para formatar as datas do DataFrame"""
    return MONTHS[mes - 1]
