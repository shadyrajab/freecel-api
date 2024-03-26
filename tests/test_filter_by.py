import pandas as pd

from utils.functions import filter_by

df = pd.read_excel("tests/df/vendas.xlsx")
df["data"] = pd.to_datetime(df["data"].copy(), unit="ms")


def test_filtragem_por_periodo():
    dataframe_filtrado = filter_by(df, data_inicio="01-01-2023 ", data_fim="31-01-2023")

    assert dataframe_filtrado.shape[0] == 191
    pass


def test_filtragem_por_equipe():
    dataframe_filtrado = filter_by(df, equipe="FREECEL")

    assert dataframe_filtrado.shape[0] == 2838
    pass


def test_filtragem_por_uf():
    dataframe_filtrado = filter_by(df, uf="DF")

    assert dataframe_filtrado.shape[0] == 3103
    pass


def test_filtragem_por_adabas():
    dataframe_filtrado = filter_by(df, adabas="DFP4059-001")

    assert dataframe_filtrado.shape[0] == 3286
    pass


def test_filtragem_geral():
    dataframe_filtrado = filter_by(
        df,
        adabas="DFP4059-001",
        uf="DF",
        equipe="FREECEL",
        data_inicio="01-01-2023",
        data_fim="31-01-2023",
    )

    assert dataframe_filtrado.shape[0] == 52
    pass
