from datetime import datetime
from typing import Optional, Tuple

import pandas as pd
from asyncpg.pool import Pool

from models.identify import ID
from utils.functions import get_clause
from utils.queries import GET_PRECO_QUERY, REMOVE_VENDA_QUERY


class VendasHandlerDataBase:
    def __init__(self, tipo_venda: str, pool: Optional[Pool] = None) -> None:
        self.pool = pool
        self.tipo_venda = tipo_venda

    async def get_preco(self, produto: str):
        async with self.pool.acquire() as connection:
            preco = await connection.fetch(GET_PRECO_QUERY, produto)

        return preco[0]["preco"] if preco else None

    async def get_vendas(self, **filters):
        QUERY, values = self.__GET_QUERY(**filters)
        async with self.pool.acquire() as connection:
            result = await connection.fetch(QUERY, *values)
            if len(result) == 0:
                return []
            
            columns = result[0].keys()
            vendas = pd.DataFrame(result, columns=columns)
            return vendas

    async def add_venda(self, values: Tuple[str], QUERY: str):
        # adabas = get_adabas(venda.equipe, venda.tipo)
        # preco = await self.get_preco(venda.plano) if not venda.preco else venda.preco
        # receita = preco * venda.volume
        # if venda.ddd not in DDDS_valor_inteiro:
        #     receita *= 0.3

        async with self.pool.acquire() as connection:
            id = await connection.fetchval(QUERY, *values)
            return id

    async def remove_venda(self, id: ID):
        values = (id.id,)
        async with self.pool.acquire() as connection:
            await connection.execute(REMOVE_VENDA_QUERY, *values)

    async def update_venda(self, **params):
        id, set_clause, values = get_clause(**params)
        query = f"UPDATE vendas_concluidas SET {set_clause} WHERE id = ${len(values)}"
        async with self.pool.acquire() as connection:
            await connection.execute(query, *values)

