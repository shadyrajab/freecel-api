from client.client import Freecel
from dotenv import load_dotenv
from os import getenv
from json import dumps, load

from typing import Optional
from io import StringIO

from base_model import VendaModel, ConsultorModel, ProdutoModel, TokenModel

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

def get_consultores():
    return jsonfy(client.get_consultores(to_dataframe = True))

def add_consultor_to_db(consultor: ConsultorModel):
    client.add_consultor(consultor)

def add_venda_to_db(venda: VendaModel):
    client.add_venda(
        cnpj = venda.cnpj, cod_cnae = venda.cod_cnae, colaboradores = venda.colaboradores, consultor = venda.consultor,
        data = venda.data, faturamento = venda.faturamento, gestor = venda.gestor, nome_cnae = venda.nome_cnae, 
        plano = venda.plano, quantidade_de_produtos = venda.quantidade_de_produtos, revenda = venda.revenda, 
        tipo = venda.tipo, uf = venda.uf, valor_acumulado = venda.valor_acumulado, valor_do_plano = venda.valor_do_plano
    )

def add_produto_to_db(produto: ProdutoModel):
    client.add_produto(
        nome = produto.nome,
        preco = produto.preco
    )

def get_vendas(ano: int, mes: str):
    return jsonfy(client.filter_by(ano, mes))

def get_produtos():
    return jsonfy(client.get_produtos(to_dataframe = True))

def authenticate(token: TokenModel):
    return client.jwt_aunthenticate(token)

class Freecel:
    def __init__(
            self, display_vendas: Optional[bool] = None, ano: Optional[int] = None, mes: Optional[str] = None):
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
            self.delta_quantidade_clientes = client.delta_quantidade_clientes(ano, mes)
            self.quantidade_clientes = client.quantidade_clientes(ano, mes)
            self.delta_ticket_medio = client.delta_ticket_medio(ano, mes)
            self.delta_media_diaria = client.delta_media_diaria(ano, mes)
            self.delta_media_por_consultor = client.delta_media_por_consultor(ano, mes)
            self.consultor_do_mes = Consultor(consultor_do_mes_nome, False, ano, mes)

        self.qtd_vendas_por_cnae = jsonfy(client.qtd_vendas_por_cnae(ano, mes))
        self.qtd_vendas_por_faturamento = jsonfy(client.qtd_vendas_por_faturamento(ano, mes))
        self.qtd_vendas_por_colaboradores = jsonfy(client.qtd_vendas_por_colaboradores(ano, mes))
        self.qtd_vendas_por_uf = jsonfy(client.qtd_vendas_por_uf(ano, mes))
        # self.consultores = client.consultores(ano, mes)
        self.ufs = client.ufs(ano, mes)
        self.tipo_venda = client.tipo_venda

        if display_vendas:
            self.vendas = jsonfy(client.filter_by(ano, mes))

class Rankings:
    def __init__(
        self, ano: Optional[int] = None, mes: Optional[str] = None
    ):
        
        rankings = client.Ranking()
        self.ranking_consultores = jsonfy(rankings.consultores(ano, mes))
        self.ranking_produtos = jsonfy(client.Ranking().produtos(ano, mes))
        self.ranking_fixa = jsonfy(client.Ranking().consultores(ano, mes, tipo = 'FIXA'))
        self.ranking_avancada = jsonfy(client.Ranking().consultores(ano, mes, tipo = 'AVANÇADA'))
        self.ranking_vvn = jsonfy(client.Ranking().consultores(ano, mes, tipo = 'VVN'))
        self.ranking_migracao = jsonfy(client.Ranking().consultores(ano, mes, tipo  = 'MIGRAÇÃO PRÉ-PÓS'))
        self.ranking_altas = jsonfy(client.Ranking().consultores(ano, mes, tipo = 'ALTAS'))
        
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
            self.delta_quantidade_clientes = consultor.delta_quantidade_clientes(ano, mes)

        if display_vendas:
            self.vendas = jsonfy(consultor.filter_by(ano, mes))

# Crm = jsonfy(client.crm)