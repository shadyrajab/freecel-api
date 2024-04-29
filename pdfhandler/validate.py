import re

import pandas as pd

from utils.variables import INDEX_COLUMNS

REG = r"\b\d{1,4}GB\b"


def merge_termo_composicao(termo: pd.DataFrame, composicao: pd.DataFrame):
    termo_composicao = pd.merge(termo, composicao, how="right", on="Comp.")
    termo_composicao.loc[:, "Nº da Linha"] = termo_composicao[
        "Nº da Linha"
    ].str.replace("-", "")
    termo_composicao.loc[:, "Telefone"] = (
        termo_composicao["DDD_x"].astype(str) + termo_composicao["Nº da Linha"]
    )

    return termo_composicao


def get_flags(m: int, recomendacao: int, recomendacaoup: int, plano: int, delta: float):
    if m >= 17:
        if delta > 0:
            return "Positiva"

        elif delta < 0 and plano >= recomendacaoup:
            return "Positiva"

        elif plano >= recomendacao:
            return "Padrão"

    elif m > 7 and m <= 17:
        if plano >= recomendacaoup and delta > 0:
            return "Positiva"

    return "Não Remunerado"


def merge_and_validate(
    composicao: pd.DataFrame, termo: pd.DataFrame, visao: pd.DataFrame, delta: float
):
    termo_composicao = merge_termo_composicao(composicao, termo)

    visao["Telefone"] = visao["Telefone"].astype(str)
    final = pd.merge(visao, termo_composicao, on="Telefone", how="right")[INDEX_COLUMNS]

    for column in ["Plano e Vlr. Unit.", "Recomendação", "Recomendação UP"]:
        final[column] = final[column].apply(
            lambda x: re.search(REG, x).group(0).replace("GB", "")
        )

    final["Remuneração"] = final.apply(
        lambda row: get_flags(
            row["M"],
            row["Recomendação"],
            row["Recomendação UP"],
            row["Plano e Vlr. Unit."],
            delta,
        ),
        axis=1,
    )

    return final
