from io import StringIO
from json import load
from typing import Dict

import pandas as pd

from utils.variables import CATEGORIAS, adabas_mapping


def jsonfy(dataframe: pd.DataFrame) -> Dict:
    df = dataframe.to_json(orient="records")
    return load(StringIO(df))


def get_adabas(equipe: str, tipo: str) -> str:
    categoria = CATEGORIAS.get(tipo)
    return adabas_mapping.get((equipe, categoria), "Não Informado")


def remove_rbar(x) -> str:
    if type(x) is not str:
        return x
    return x.replace("\r", " ")
