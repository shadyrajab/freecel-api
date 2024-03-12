from pandas import DataFrame
from json import load
from io import StringIO
from utils.variables import adabas_mapping, MONTHS
    
def group_by(dataframe: DataFrame, column: str, sort: str) -> DataFrame:
    grouped_dataframe = dataframe.groupby(column, as_index = False).sum(
        numeric_only = True).sort_values(by = sort, ascending = False
    )

    return grouped_dataframe

def jsonfy(dataframe: DataFrame):
    df = dataframe.to_json(orient = 'records')
    return load(StringIO(df))

def get_adabas(equipe, tipo):
    return adabas_mapping.get((equipe, tipo), None)

def filter_by(dataframe: DataFrame, **filters: str):
    filters = {
        'ano': filters.get('ano', 'NONE'),
        'mês': filters.get('mes', 'NONE').capitalize(),
        'consultor': filters.get('consultor', 'NONE').upper(),
        'tipo': filters.get('tipo', 'NONE').upper(),
        'adabas': filters.get('adabas', 'NONE').upper(),
        'uf': filters.get('uf', 'NONE').upper()
    }

    for column, value in filters.items():
        if value != 'NONE':
            if column == 'ano':
                value = int(value)
            dataframe = dataframe[dataframe[column] == value]

    return dataframe

def get_mes(mes):
    return MONTHS[mes - 1]
