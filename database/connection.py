import psycopg2
import pandas as pd
from typing import Optional 
from models.identify import ID
from models.produtos import Produto
from models.consultor import Vendedor
from empresas.empresas_aqui import Empresa
from utils.functions import get_adabas
from utils.variables import DDDS_valor_inteiro, HOST, DATABASE, USER, PASSWORD
from database.queries import *

connection = psycopg2.connect(
    host = HOST, 
    database = DATABASE, 
    user = USER, 
    password = PASSWORD
)

class DataBase:
    def jwt_authenticate(self, uuid: str):
        JWT_QUERY = "SELECT * FROM uuids WHERE uuid = (%s)"
        with connection.cursor() as cursor:
            cursor.execute(JWT_QUERY, (uuid, ))
            user = cursor.fetchall()

        return user[0][2] if user else None

    def get_consultores(self, to_dataframe: Optional[bool] = False):
        with connection.cursor() as cursor:
            cursor.execute(GET_CONSULTORES_QUERY)
            consultores = cursor.fetchall()

        if to_dataframe:
            columns = [desc[0] for desc in cursor.description]
            consultores = pd.DataFrame(consultores, columns=columns)

        return consultores
    
    def add_consultor(self, consultor: Vendedor):
        values = (consultor.name.upper(), )
        with connection.cursor() as cursor:
            cursor.execute(ADD_CONSULTOR_QUERY, values)
            connection.commit()

    def remove_consultor(self, id: ID):
        values = (id.id, )
        with connection.cursor() as cursor:
            cursor.execute(REMOVE_CONSULTOR_QUERY, values)
            connection.commit()

    def get_produtos(self, to_dataframe: Optional[bool] = False):
        with connection.cursor() as cursor:
            cursor.execute(GET_PRODUTOS_QUERY)
            produtos = cursor.fetchall()
        
        if to_dataframe:
            columns = [desc[0] for desc in cursor.description]
            produtos = pd.DataFrame(produtos, columns=columns)

        return produtos
    
    def add_produto(self, produto: Produto):
        values = (produto.nome.upper(), produto.preco)  
        with connection.cursor() as cursor:
            cursor.execute(ADD_PRODUTO_QUERY, values)
            connection.commit()

    def remove_produto(self, id: ID):
        values = (id.id, )
        with connection.cursor() as cursor:
            cursor.execute(REMOVE_PRODUTO_QUERY, values)
            connection.commit()
    
    def get_vendas(self, to_dataframe: Optional[bool] = False):
        with connection.cursor() as cursor:
            cursor.execute(GET_VENDAS_QUERY)
            vendas = cursor.fetchall()
        if to_dataframe:
            columns = [desc[0] for desc in cursor.description]
            vendas = pd.DataFrame(vendas, columns=columns)
        
        return vendas
    
    def get_preco(self, produto: str):
        with connection.cursor() as cursor:
            cursor.execute(GET_PRECO_QUERY, (produto, ))
            preco = cursor.fetchall()

        return preco[0][0]
    
    def add_venda(self, venda):
        empresa = Empresa(venda.cnpj)
        adabas = get_adabas(venda.equipe, venda.tipo)
        DDD = venda.telefone[0:2]
        preco = self.get_preco(venda.plano)
        receita = preco * venda.volume
        if DDD not in DDDS_valor_inteiro:
            receita *= 0.3
            
        values = (
            venda.cnpj, venda.telefone, venda.consultor, venda.data, venda.gestor, venda.plano, 
            venda.volume, venda.equipe, venda.tipo, empresa.uf, receita, 
            preco, venda.email, empresa.quadro_funcionarios, empresa.faturamento, 
            empresa.cnae, empresa.cep, empresa.municipio, empresa.porte, empresa.capital_social, 
            empresa.natureza_juridica, empresa.matriz, empresa.regime_tributario, 
            empresa.bairro, adabas, 
        )

        with connection.cursor() as cursor:
            cursor.execute(ADD_VENDA_QUERY, values)
            connection.commit()


    def remove_venda(self, id: ID):
        values = (id.id, )
        with connection.cursor() as cursor:
            cursor.execute(REMOVE_VENDA_QUERY, values)
            connection.commit()
