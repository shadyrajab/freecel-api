from typing import Optional, Union

import pandas as pd
from asyncpg.pool import Pool

from models import ID, VendaFixaRequestModel, VendaMovelRequestModel
from utils.queries import GET_PRECO_QUERY
from utils.query_builder import (
    delete_vendas_query_builder,
    get_vendas_query_builder,
    post_vendas_query_builder,
    update_anth_query_builder,
)


class VendaHandlerDatabase:
    def __init__(self, pool: Optional[Pool] = None) -> None:
        self.pool = pool

    async def add_venda(
        self,
        database: str,
        user: str,
        venda: Union[VendaMovelRequestModel, VendaFixaRequestModel],
    ):
        values = venda.to_dict()
        values["responsavel"] = user
        values["preco"] = await self.get_preco(venda.plano)
        QUERY, values = post_vendas_query_builder(database=database, **values)
        async with self.pool.acquire() as connection:
            id = await connection.fetchval(QUERY, *values)
            return id

    async def get_vendas(self, database: str, **filters):
        QUERY, values = get_vendas_query_builder(database=database, **filters)
        async with self.pool.acquire() as connection:
            result = await connection.fetch(QUERY, *values)
            if len(result) == 0:
                return {"message": "Não foram encontrados dados para sua solicitação."}

            columns = result[0].keys()
            vendas = pd.DataFrame(result, columns=columns)
            vendas["receita"] = vendas["preco"] * vendas["volume"]

            for index, row in vendas.iterrows():
                ddd = str(row["ddd"])
                if not (ddd.startswith("6") or ddd.startswith("9")):
                    vendas.at[index, "receita"] = (
                        float(vendas.at[index, "receita"]) * 0.3
                    )

            return vendas

    async def remove_venda(self, database: str, id: ID):
        QUERY, values = delete_vendas_query_builder(database=database, id=id)
        async with self.pool.acquire() as connection:
            await connection.execute(QUERY, *values)

    async def update_venda(self, database: str, **params):
        QUERY, values = update_anth_query_builder(database=database, **params)
        async with self.pool.acquire() as connection:
            await connection.execute(QUERY, *values)

    async def get_preco(self, plano: str):
        async with self.pool.acquire() as connection:
            preco = await connection.fetch(GET_PRECO_QUERY, plano)

        return preco[0]["preco"]
