from typing import Optional

from asyncpg.pool import Pool
from pandas import DataFrame

from empresas.empresas_aqui import Empresa
from models.identify import ID
from utils.functions import get_adabas, get_clause
from utils.queries import (
    ADD_VENDA_QUERY,
    GET_PRECO_QUERY,
    GET_VENDAS_QUERY,
    REMOVE_VENDA_QUERY,
)
from utils.variables import DDDS_valor_inteiro


class VendasHandlerDataBase:
    def __init__(self, pool: Optional[Pool] = None) -> None:
        self.pool = pool

    async def get_vendas(self, to_dataframe: Optional[bool] = False):
        async with self.pool.acquire() as connection:
            statement = await connection.prepare(GET_VENDAS_QUERY)
            result = await statement.fetch()

            if to_dataframe:
                columns = [desc[0] for desc in statement.get_attributes()]
                vendas = DataFrame(result, columns=columns)
                return vendas
            else:
                return result

    async def get_preco(self, produto: str):
        async with self.pool.acquire() as connection:
            preco = await connection.fetch(GET_PRECO_QUERY, produto)

        return preco[0]["preco"] if preco else None

    async def add_venda(self, venda):
        empresa = Empresa(venda.cnpj)
        adabas = get_adabas(venda.equipe, venda.tipo)
        preco = await self.get_preco(venda.plano) if venda.preco == 0 else venda.preco
        receita = preco * venda.volume
        if venda.ddd not in DDDS_valor_inteiro:
            receita *= 0.3

        values = (
            venda.cnpj,
            venda.telefone,
            venda.consultor,
            venda.data,
            venda.gestor,
            venda.plano,
            venda.volume,
            venda.equipe,
            venda.tipo,
            venda.ddd,
            empresa.uf,
            receita,
            preco,
            venda.email,
            empresa.quadro_funcionarios,
            empresa.faturamento,
            empresa.cnae,
            empresa.cep,
            empresa.municipio,
            empresa.porte,
            empresa.capital_social,
            empresa.natureza_juridica,
            empresa.matriz,
            empresa.regime_tributario,
            empresa.bairro,
            adabas,
            venda.ja_cliente,
            venda.numero_pedido,
            venda.status,
        )

        async with self.pool.acquire() as connection:
            id = await connection.execute(ADD_VENDA_QUERY, *values)
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
