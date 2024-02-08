from client.client import Freecel
from dotenv import load_dotenv
from os import getenv
from json import dumps, load

from typing import Optional
from io import StringIO

load_dotenv()

HOST = getenv('host')
DATABASE = getenv('database')
USER = getenv('user')
PASSWORD = getenv('password')

client = Freecel(
    host = HOST,
    database = DATABASE,
    user = USER,
    password = PASSWORD
)

def jsonfy(dataframe):
    df = dataframe.to_json(orient = 'records')
    return load(StringIO(df))

class Freecel:
    def __init__(self, ano: Optional[int] = None, mes: Optional[str] = None):
        consultor_do_mes_nome = client.consultor_do_mes(ano, mes).name
        self.receita_total = client.receita_total(ano, mes)
        self.quantidade_vendida = client.qtd_de_produtos_vendidos(ano, mes)
        self.quantidade_clientes = client.quantidade_clientes(ano, mes)
        self.ticket_medio = client.ticket_medio(ano, mes)
        self.receita_media_diaria = client.receita_media_diaria(ano, mes)
        self.media_por_consultor = client.media_por_consultor(ano, mes)
        self.maior_venda_mes = client.maior_venda_mes()

        if ano and mes:
            self.delta_receita_total = client.delta_receita_total(ano, mes)
            self.delta_quantidade_produtos = client.delta_quantidade_produtos(ano, mes)
            self.quantidade_clientes = client.quantidade_clientes(ano, mes)
            self.delta_ticket_medio = client.delta_ticket_medio(ano, mes)
            self.delta_media_diaria = client.delta_media_diaria(ano, mes)
            self.delta_media_por_consultor = client.delta_media_por_consultor(ano, mes)
            self.consultor_do_mes = Consultor(consultor_do_mes_nome, False, ano, mes)


        self.qtd_vendas_por_cnae = jsonfy(client.qtd_vendas_por_cnae(ano, mes))
        self.qtd_vendas_por_faturamento = jsonfy(client.qtd_vendas_por_faturamento(ano, mes))
        self.qtd_vendas_por_colaboradores = jsonfy(client.qtd_vendas_por_colaboradores(ano, mes))
        self.consultores = client.consultores(ano, mes)
        self.ufs = client.ufs(ano, mes)
        self.ranking_consultores = jsonfy(client.Ranking().ranking_consultores(ano, mes))
        self.ranking_produtos = jsonfy(client.Ranking().ranking_produtos(ano, mes))
        self.vendas = jsonfy(client.filter_by(ano, mes))

class Consultor:
    def __init__(
            self, name: str, display_vendas: Optional[bool] = None, 
            ano: Optional[int] = None, mes: Optional[str] = None
        ):
        consultor = client.Consultor(name)

        self.name = consultor.name

        self.receita_total =  consultor.receita(ano, mes)
        self.quantidade_vendida =  consultor.quantidade(ano, mes)
        self.quantidade_clientes = consultor.quantidade_clientes(ano, mes)

        self.receita_media_diaria =  consultor.receita_media_diaria(ano, mes)
        self.quantidade_media_diaria =  consultor.quantidade_media_diaria(ano, mes)

        self.quantidade_media_mensal = consultor.quantidade_media_mensal
        self.receita_media_mensal =  consultor.receita_media_mensal

        self.ticket_medio = consultor.ticket_medio

        if ano and mes:
            self.delta_receita_mensal = consultor.delta_receita_mensal(ano, mes)
            self.delta_quantidade_mensal = consultor.delta_quantidade_mensal(ano, mes)

        if display_vendas:
            self.vendas = jsonfy(consultor.filter_by(ano, mes))

Crm = jsonfy(client.crm)