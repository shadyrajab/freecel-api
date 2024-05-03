from typing import Optional

from asyncpg.pool import Pool
from pandas import DataFrame

from models.consultor import Vendedor
from models.identify import ID
from utils.queries import (
    ADD_CONSULTOR_QUERY,
    GET_CONSULTORES_QUERY,
    GET_EQUIPE_FLAVIO,
    REMOVE_CONSULTOR_QUERY,
)
from utils.query_builder import update_anth_query_builder


class ConsultorHandlerDataBase:
    def __init__(self, pool: Optional[Pool] = None):
        self.pool = pool

    async def get_consultores(self):
        async with self.pool.acquire() as connection:
            statement = await connection.prepare(GET_CONSULTORES_QUERY)
            result = await statement.fetch()
            columns = [desc[0] for desc in statement.get_attributes()]
            consultores = DataFrame(result, columns=columns)
            return consultores

    async def get_equipe_flavio(self):
        async with self.pool.acquire() as connection:
            statement = await connection.prepare(GET_EQUIPE_FLAVIO)
            result = await statement.fetch()
            columns = [desc[0] for desc in statement.get_attributes()]
            equipe = DataFrame(result, columns=columns)
            return equipe

    async def add_consultor(self, consultor: Vendedor):
        values = (
            consultor.name.upper(),
            consultor.vinculo,
            consultor.cargo,
        )
        async with self.pool.acquire() as connection:
            id = await connection.fetchval(ADD_CONSULTOR_QUERY, *values)
            return id

    async def remove_consultor(self, id: ID):
        values = (id.id,)
        async with self.pool.acquire() as connection:
            await connection.execute(REMOVE_CONSULTOR_QUERY, *values)

    async def update_consultor(self, **params):
        QUERY, values = update_anth_query_builder(database="consultores", **params)
        async with self.pool.acquire() as connection:
            await connection.execute(QUERY, *values)
