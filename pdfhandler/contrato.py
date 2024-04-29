import io

import pandas as pd
import tabula
from PyPDF2 import PdfReader

from utils.functions import remove_rbar
from utils.variables import COMPOSICAO_COLUMNS, TERMO_COLUMNS


def read_termo_complementar(termo_complementar: str):
    termo_complementar = [
        item
        for item in termo_complementar.split("\n")[11:-7]
        if item not in TERMO_COLUMNS
    ]

    sublistas = []

    for i in range(0, len(termo_complementar), 4):
        sublista = termo_complementar[i : i + 4]
        sublistas.append(sublista)

    dataframe = pd.DataFrame(sublistas, columns=TERMO_COLUMNS)
    dataframe["Comp."] = dataframe["Comp."].str.replace("000000", "")
    return dataframe


def read_desc_composicao(contrato, page: int):
    composicao = tabula.read_pdf(contrato, pages=page, lattice=True)[2]
    composicao = composicao.iloc[2:, 0:26]

    if composicao["Unnamed: 14"].isnull().any():
        composicao["Unnamed: 14"] = "Não Informado"

    composicao.dropna(axis=1, inplace=True)
    composicao.columns = COMPOSICAO_COLUMNS

    for column in composicao.columns:
        composicao[column] = composicao[column].apply(lambda x: remove_rbar(x))

    return composicao


async def read_contract_pdf(contrato):
    contrato = io.BytesIO(await contrato.read())
    reader = PdfReader(contrato)

    for i, page in enumerate(reader.pages):
        if "7\n.\nAnexo II\nTermo Complementar \nRelação" in page.extract_text():
            termo_complementar = page.extract_text()

        if "\nID\nComposição\nDDD\nQtde.\nNegociação\nConta\n" in page.extract_text():
            desc_composicao = i + 1

    return (
        read_termo_complementar(termo_complementar),
        read_desc_composicao(contrato, desc_composicao),
    )
