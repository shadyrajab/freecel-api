from typing import Optional

from asyncpg.pool import Pool
from pandas import DataFrame

from models.identify import ID
from models.produtos import Produto
from utils.queries import ADD_PRODUTO_QUERY, GET_PRODUTOS_QUERY, REMOVE_PRODUTO_QUERY
from utils.functions import get_clause


class ProdutosHandlerDataBase:
    def __init__(self, pool: Optional[Pool] = None) -> None:
        self.pool = pool

    async def get_produtos(self, to_dataframe: Optional[bool] = False):
        async with self.pool.acquire() as connection:
            statement = await connection.prepare(GET_PRODUTOS_QUERY)
            result = await statement.fetch()
            if to_dataframe:
                columns = [desc[0] for desc in statement.get_attributes()]
                produtos = DataFrame(result, columns=columns)
                return produtos
            else:
                return result

    async def add_produto(self, produto: Produto):
        values = (
            produto.nome.upper(),
            produto.preco,
        )
        async with self.pool.acquire() as connection:
            await connection.execute(ADD_PRODUTO_QUERY, values)

    async def remove_produto(self, id: ID):
        values = (id.id,)
        async with self.pool.acquire() as connection:
            await connection.execute(REMOVE_PRODUTO_QUERY, values)

    async def update_produto(self, **params):
        id, set_clause, values = get_clause(**params)
        query = f"UPDATE produto SET {set_clause} WHERE id = ${len(values)}"
        async with self.pool.acquire() as connection:
            await connection.execute(query, *values)
