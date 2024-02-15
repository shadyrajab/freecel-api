import psycopg2
import pandas as pd
from typing import Optional

class DataBase:
    def __init__(self, host, database, user, password):
        self.connection = self.__create_connection__(host, database, user, password)

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
        query = "INSET INTO consultores (nome) VALUES (%s)"
        values = (nome)

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
    
    def add_produto(self, nome: str, preco: int):
        query = "INSERT INTO produtos (nome, preco) VALUES (%s, %s)"
        values = (nome, preco)  

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
    
    def add_venda(connection, cnpj: str, cod_cnae: str, colaboradores: str, consultor: str,
            data: str, faturamento: str, gestor: str, nome_cnae: str, plano: str,
            quantidade_de_produtos: str, revenda: str, tipo: str, uf: str, valor_acumulado: str,
            valor_do_plano: str
        ):

        query = """
            INSERT INTO vendas_concluidas (
                cnpj, cod_cnae, colaboradores, consultor, data, faturamento, gestor,
                nome_cnae, plano, quantidade_de_produtos, revenda, tipo, uf, valor_acumulado,
                valor_do_plano
            ) VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
            )
        """
        values = (
            cnpj, cod_cnae, colaboradores, consultor, data, faturamento, gestor, nome_cnae,
            plano, quantidade_de_produtos, revenda, tipo, uf, valor_acumulado, valor_do_plano
        )

        with connection.cursor() as cursor:
            cursor.execute(query, values)
            connection.commit()

    
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