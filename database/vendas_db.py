import asyncpg
from utils.variables import HOST, DATABASE, USER, PASSWORD, DDDS_valor_inteiro
from utils.functions import get_adabas
from database.queries import ADD_VENDA_QUERY, GET_VENDAS_QUERY
from typing import Optional
import pandas as pd
from empresas.empresas_aqui import Empresa

class VendasDB:
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