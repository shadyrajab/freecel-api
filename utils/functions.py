from pandas import DataFrame
from json import load
from io import StringIO
from typing import Optional
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

def filter_by(dataframe, ano: Optional[int] = None, mes: Optional[str] = None, consultor: Optional[str] = None, tipo: Optional[str] = None):
    mes = mes.capitalize() if mes else mes
    ano = int(ano) if ano else ano
    tipo = tipo.upper() if tipo else tipo
    consultor = consultor.upper() if consultor else consultor

    if mes and mes not in MONTHS:
        raise ValueError('Formato de mês inválido. Por favor, escreva o nome do mês completo com acentos.')

    filters = {
        'ano': ano,
        'mês': mes,
        'consultor': consultor,
        'tipo': tipo
    }

    for column, value in filters.items():
        if value is not None:
            dataframe = dataframe[dataframe[column] == value]

    return dataframe

def get_mes(mes):
    return MONTHS[mes - 1]
