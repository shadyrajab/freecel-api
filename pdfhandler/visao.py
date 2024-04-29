import io

import pandas as pd
import tabula


async def read_visao_pdf(visao):
    visao = tabula.read_pdf(io.BytesIO(await visao.read()), pages="2")
    if len(visao) == 0:
        return pd.DataFrame(
            [
                {
                    "Produto": "Preencher manualmente.",
                    "Data Alta": "Preencher manualmente.",
                    "Telefone": "Preencher manualmente.",
                    "M": 1000,
                    "Blindado": "Preencher manualmente.",
                    "Linha Suspensa": "Preencher manualmente.",
                    "Plano": "Preencher manualmente.",
                    "Recomendação": "Preencher manualmente.",
                    "Recomendação UP": "Preencher manualmente.",
                }
            ]
        )
    
    return visao[0]
