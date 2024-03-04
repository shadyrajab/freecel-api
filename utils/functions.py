from pandas import DataFrame
from json import load
from io import StringIO
from client.client import Client
from utils.variables import HOST, DATABASE, USER, PASSWORD
    
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