import psycopg2
import pandas as pd
from typing import Optional
from typemodel.schemas import VendaSchema 

class DataBase:
    def __init__(self, host, database, user, password):
        self.connection = self.__create_connection__(host, database, user, password)

    def jwt_authenticate(self, uuid: str):
        query = f"SELECT * FROM uuids WHERE uuid = '{uuid}'"

        with self.connection.cursor() as cursor:
            cursor.execute(query)
            user = cursor.fetchall()

        return user[0][2] if user else None

    def get_consultores(self, to_dataframe: Optional[bool] = False):
        query = "SELECT * FROM consultores"

        with self.connection.cursor() as cursor:
            cursor.execute(query)
            consultores = cursor.fetchall()

        if to_dataframe:
            columns = [desc[0] for desc in cursor.description]
            consultores = pd.DataFrame(consultores, columns=columns)

        return consultores
    
    def add_consultor(self, nome: str):
        query = "INSERT INTO consultores (nome) VALUES (%s)"
        values = (nome.upper(), )

        with self.connection.cursor() as cursor:
            cursor.execute(query, values)
            self.connection.commit()

    def remove_consultor(self, id: int):
        query = "DELETE FROM consultores WHERE id = (%s)"
        values = (id, )

        with self.connection.cursor() as cursor:
            cursor.execute(query, values)
            self.connection.commit()

    def get_produtos(self, to_dataframe: Optional[bool] = False):
        query = "SELECT * FROM produtos"

        with self.connection.cursor() as cursor:
            cursor.execute(query)
            produtos = cursor.fetchall()
        
        if to_dataframe:
            columns = [desc[0] for desc in cursor.description]
            produtos = pd.DataFrame(produtos, columns=columns)

        return produtos
    
    def add_produto(self, nome: str, preco: float):
        query = "INSERT INTO produtos (nome, preco) VALUES (%s, %s)"
        values = (nome.upper(), preco)  

        with self.connection.cursor() as cursor:
            cursor.execute(query, values)
            self.connection.commit()

    def remove_produto(self, id: int):
        query = "DELETE FROM produtos WHERE id = (%s)"
        values = (id, )

        with self.connection.cursor() as cursor:
            cursor.execute(query, values)
            self.connection.commit()
    
    def get_vendas(self, to_dataframe: Optional[bool] = False):
        query = "SELECT * FROM vendas_concluidas"

        with self.connection.cursor() as cursor:
            cursor.execute(query)
            vendas = cursor.fetchall()
        
        if to_dataframe:
            columns = [desc[0] for desc in cursor.description]
            vendas = pd.DataFrame(vendas, columns=columns)
        
        return vendas
    
    def add_venda(self, venda: VendaSchema):
        query = """
            INSERT INTO vendas_concluidas (
                cnpj, telefone, consultor, data, gestor, plano, quantidade_de_produtos, 
                revenda, tipo, uf, valor_acumulado, valor_do_plano, email, quadro_funcionarios,
                faturamento, cnae, cep, municipio, porte, capital_social, natureza_juridica,
                matriz, situacao_cadastral, regime_tributario, bairro, adabas
            ) VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
            )
        """
        values = (
            venda.cnpj, venda.telefone, venda.consultor, venda.data, venda.gestor, venda.plano, 
            venda.quantidade_de_produtos, venda.revenda, venda.tipo, venda.uf, venda.valor_acumulado, 
            venda.valor_do_plano, venda.email, venda.quadro_funcionarios, venda.faturamento, 
            venda.cnae, venda.cep, venda.municipio, venda.porte, venda.capital_social, 
            venda.natureza_juridica, venda.matriz, venda.situacao_cadastral, venda.regime_tributario, 
            venda.bairro, venda.adabas
        )

        with self.connection.cursor() as cursor:
            cursor.execute(query, values)
            self.connection.commit()


    def remove_venda(self, id: int):
        query = "DELETE FROM vendas_concluidas WHERE id = (%s)"
        values = (id, )

        with self.connection.cursor() as cursor:
            cursor.execute(query, values)
            self.connection.commit()

    
    def __create_connection__(self, host, database, user, password):
        """
            Realizando a conexão com o banco de dados da Freecel.
        """
        
        connection = psycopg2.connect(
            host = host, 
            database = database, 
            user = user, 
            password = password
        )

        return connection