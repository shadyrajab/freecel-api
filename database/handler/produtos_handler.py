from typing import Optional

from asyncpg.pool import Pool
from pandas import DataFrame

from models.identify import ID
from models.produtos import Produto
from utils.queries import ADD_PRODUTO_QUERY, GET_PRODUTOS_QUERY, REMOVE_PRODUTO_QUERY


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

    async def update_produto(self, id: ID, **params):
        if not params:
            return
        set_clause = ", ".join(f"{key} = ${i + 2}" for i, key in enumerate(params))
        query = f"UPDATE produtos SET {set_clause} WHERE id = $1"
        values = [id.id] + list(params.values())
        async with self.pool.acquire() as connection:
            await connection.execute(query, values)
