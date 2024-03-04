from pandas import DataFrame
from json import load
from io import StringIO
    
def group_by(dataframe: DataFrame, column: str, sort: str) -> DataFrame:
    grouped_dataframe = dataframe.groupby(column, as_index = False).sum(
        numeric_only = True).sort_values(by = sort, ascending = False
    )

    return grouped_dataframe

def jsonfy(dataframe: DataFrame):
    df = dataframe.to_json(orient = 'records')
    return load(StringIO(df))