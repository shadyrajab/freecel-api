from typing import Optional

from asyncpg.pool import Pool
from pandas import DataFrame

from models.consultor import Vendedor
from models.identify import ID
from utils.functions import get_clause
from utils.queries import (
    ADD_CONSULTOR_QUERY,
    GET_CONSULTORES_QUERY,
    REMOVE_CONSULTOR_QUERY,
)


class ConsultorHandlerDataBase:
    def __aenter__(self, pool: Optional[Pool] = None):
        self.pool = pool

    async def get_consultores(self, to_dataframe: Optional[bool] = None):
        async with self.pool.acquire() as connection:
            statement = await connection.prepare(GET_CONSULTORES_QUERY)
            result = await statement.fetch()
            if to_dataframe:
                columns = [desc[0] for desc in statement.get_attributes()]
                vendas = DataFrame(result, columns=columns)
                return vendas
            else:
                return result

    async def add_consultor(self, consultor: Vendedor):
        values = (
            consultor.name.upper(),
            consultor.vinculo,
            consultor.cargo,
        )
        async with self.pool.acquire() as connection:
            await connection.execute(ADD_CONSULTOR_QUERY, *values)

    async def remove_consultor(self, id: ID):
        values = (id.id,)
        async with self.pool.acquire() as connection:
            await connection.execute(REMOVE_CONSULTOR_QUERY, *values)

    async def update_consultor(self, **params):
        id, set_clause, values = get_clause(**params)
        query = f"UPDATE consultores SET {set_clause} WHERE id = ${len(values)}"
        async with self.pool.acquire() as connection:
            await connection.execute(query, *values)
