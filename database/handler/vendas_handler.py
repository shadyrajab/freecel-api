from datetime import datetime
from typing import Optional

import pandas as pd
from asyncpg.pool import Pool

from empresas.empresas_aqui import Empresa
from models.identify import ID
from utils.functions import get_adabas, get_clause
from utils.queries import ADD_VENDA_QUERY, GET_PRECO_QUERY, REMOVE_VENDA_QUERY
from utils.variables import DDDS_valor_inteiro


class VendasHandlerDataBase:
    def __init__(self, pool: Optional[Pool] = None) -> None:
        self.pool = pool

    async def get_vendas(self, **filters):
        QUERY, values = self.__GET_QUERY(**filters)
        async with self.pool.acquire() as connection:
            result = await connection.fetch(QUERY, *values)
            if len(result) == 0:
                return []
            
            columns = result[0].keys()
            vendas = pd.DataFrame(result, columns=columns)
            return vendas

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
            empresa.data_abertura,
        )

        async with self.pool.acquire() as connection:
            id = await connection.fetchval(ADD_VENDA_QUERY, *values)
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

    def __GET_QUERY(self, **filters):
        data_inicio = datetime.strptime(filters.get("data_inicio"), "%d-%m-%Y")
        data_fim = datetime.strptime(filters.get("data_fim"), "%d-%m-%Y")
        method = "=" if filters.get("tipo") == "MIGRAÇÃO" else "!="
        periodo = ('MIGRAÇÃO', data_inicio, data_fim)

        del filters["data_inicio"]
        del filters["data_fim"]
        del filters["tipo"]
        
        conditions = []
        values = []
        values.extend(periodo)
        for key, value in filters.items():
            if value is not None:
                conditions.append(f"AND {key} = ${len(values) + 1}")
                values.append(value)

        QUERY = f"SELECT * FROM vendas_concluidas WHERE tipo {method} $1 AND data BETWEEN $2 AND $3 {" ".join(conditions)}"
        return QUERY, values
