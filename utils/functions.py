from typing import Callable, Optional
from utils.variables import MONTHS
from pandas import DataFrame
from json import load
from io import StringIO
from client.client import Client
from utils.variables import HOST, DATABASE, USER, PASSWORD

def calculate_delta(years, metric_function: Callable, ano: int, mes: Optional[str] = None) -> float:
    if ano == min(years) and not mes:
        return 0
    
    if ano == min(years) and mes.lower() == 'janeiro':
        return 0
    
    if month:
        month = mes.capitalize()
        prev_year = ano - 1 if month == 'Janeiro' else ano
        prev_month_index = MONTHS.index(mes) - 1
        prev_month = MONTHS[prev_month_index]
        return metric_function(ano, mes) - metric_function(prev_year, prev_month)
    else:
        prev_year = ano - 1 if ano != min(years) else ano
        return metric_function(ano) - metric_function(prev_year)
    
def group_by(dataframe: DataFrame, column: str, sort: str) -> DataFrame:
    grouped_dataframe = dataframe.groupby(column, as_index = False).sum(
        numeric_only = True).sort_values(by = sort, ascending = False
    )

    return grouped_dataframe

def jsonfy(dataframe: DataFrame):
    df = dataframe.to_json(orient = 'records')
    return load(StringIO(df))

def create_client() -> Client:
    return Client(
        host = HOST,
        database = DATABASE,
        user = USER,
        password = PASSWORD
    )