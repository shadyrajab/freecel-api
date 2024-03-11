import asyncpg
import pandas as pd
from typing import Optional 
from models.identify import ID
from models.produtos import Produto
from models.consultor import Vendedor
from empresas.empresas_aqui import Empresa
from utils.functions import get_adabas
from utils.variables import DDDS_valor_inteiro, HOST, DATABASE, USER, PASSWORD
from database.queries import *

class DataBase:
    async def __aenter__(self):
        self.pool = await asyncpg.create_pool(
            host = HOST,
            database = DATABASE,
            user = USER,
            password = PASSWORD
        )
        
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.pool.close()

    async def get_consultores(self, to_dataframe: Optional[bool] = None):
        async with self.pool.acquire() as connection:
            statement = await connection.prepare('SELECT * FROM consultores')
            result = await statement.fetch()
            if to_dataframe:
                columns = [desc[0] for desc in statement.get_attributes()]
                vendas = pd.DataFrame(result, columns=columns)
                return vendas
            else:
                return result
        
    async def jwt_authenticate(self, uuid: str):
        async with self.pool.acquire() as connection:
            statement = await connection.prepare('SELECT * FROM uuids WHERE uuid = $1')
            result = await statement.fetchval(uuid)
            return result if result else None

    async def add_consultor(self, consultor: Vendedor):
        values = (consultor.name.upper(), )
        async with self.pool.acquire() as connection:
            await connection.execute(ADD_CONSULTOR_QUERY, values)
    
    async def remove_consultor(self, id: ID):
        values = (id.id, )
        async with self.pool.acquire() as connection:
            await connection.execute(REMOVE_CONSULTOR_QUERY, values)
    
    async def get_produtos(self, to_dataframe: Optional[bool] = False):
        async with self.pool.acquire() as connection:
            statement = await connection.prepare(GET_PRODUTOS_QUERY)
            result = await statement.fetch()
            if to_dataframe:
                columns = [desc[0] for desc in statement.get_attributes()]
                produtos = pd.DataFrame(result, columns=columns)
                return produtos
            else:
                return result
    
    async def add_produto(self, produto: Produto):
        values = (produto.nome.upper(), produto.preco, )  
        async with self.pool.acquire() as connection:
            await connection.execute(ADD_PRODUTO_QUERY, values)

    async def remove_produto(self, id: ID):
        values = (id.id, )
        async with self.pool.acquire() as connection:
            await connection.execute(REMOVE_PRODUTO_QUERY, values)
    
    async def get_vendas(self, to_dataframe: Optional[bool] = False):
        async with self.pool.acquire() as connection:
            statement = await connection.prepare(GET_VENDAS_QUERY)
            result = await statement.fetch()
            
            if to_dataframe:
                columns = [desc[0] for desc in statement.get_attributes()]
                vendas = pd.DataFrame(result, columns=columns)
                return vendas
            else:
                return result

    
    async def get_preco(self, produto: str):
        async with self.pool.acquire() as connection:
            statement = await connection.prepare(GET_PRECO_QUERY, (produto, ))
            preco = await statement.fetchall()

        return preco[0][0]
    
    async def add_venda(self, venda):
        empresa = Empresa(venda.cnpj)
        adabas = get_adabas(venda.equipe, venda.tipo)
        DDD = venda.telefone[0:2]
        preco = self.get_preco(venda.plano) if venda.preco == 0 else venda.preco
            
        receita = preco * venda.volume
        if DDD not in DDDS_valor_inteiro:
            receita *= 0.3
            
        values = (
            venda.cnpj, venda.telefone, venda.consultor, venda.data, venda.gestor, venda.plano, 
            venda.volume, venda.equipe, venda.tipo, empresa.uf, receita, preco, venda.email, 
            empresa.quadro_funcionarios, empresa.faturamento, empresa.cnae, empresa.cep, empresa.municipio, 
            empresa.porte, empresa.capital_social, empresa.natureza_juridica, empresa.matriz, 
            empresa.regime_tributario, empresa.bairro, adabas, venda.ja_cliente
        )

        async with self.pool.acquire() as connection:
            await connection.execute(ADD_VENDA_QUERY, values)

    async def remove_venda(self, id: ID):
        values = (id.id, )
        async with self.pool.acquire() as connection:
            await connection.execute(REMOVE_VENDA_QUERY, values)
            