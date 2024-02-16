from .client.client import Freecel
from dotenv import load_dotenv
from os import getenv
from json import dumps, load
from requests import request

from typing import Optional
from io import StringIO

from .types.base_model import (
    VendaModel, 
    ConsultorModel, 
    ProdutoModel, 
    TokenModel, 
    IdentifyModel
)

from .types.schemas import CNPJStats

load_dotenv()

HOST = getenv('host')
DATABASE = getenv('database')
USER = getenv('user')
PASSWORD = getenv('password')
TOKENEMPRESAS = getenv('tokenEmpresas')

client = Freecel(
    host = HOST,
    database = DATABASE,
    user = USER,
    password = PASSWORD
)

def get_cnpj_all_stats(cnpj):
    empresas_aqui = f'https://www.empresaqui.com.br/api/{TOKENEMPRESAS}/{cnpj}'
    response = request('GET', url = empresas_aqui)

    if response.status_code == 200:
        try:
            data = response.json()
        except:
            return
        
    return get_data_stats(data)

def get_data_stats(data) -> CNPJStats:
    quadro_funcionarios = data.get('quadro_funcionarios')
    faturamento = data.get('faturamento')
    cnae = data.get('cnae_principal')
    cep = data.get('log_cep')
    municipio = data.get('log_municipio')
    porte = data.get('porte')
    capital_social = data.get('capital_social')
    natureza_juridica = data.get('natureza_juridica')
    matriz = data.get('matriz')
    situacao_cadastral = data.get('situacao_cadastral')
    regime_tributario = data.get('regime_tributario')
    bairro = data.get('log_bairro')

    return CNPJStats(
        quadro_funcionarios = quadro_funcionarios,
        faturamento = faturamento,
        cnae = cnae,
        cep = cep,
        municipio = municipio,
        porte = porte,
        capital_social = capital_social,
        natureza_juridica = natureza_juridica,
        matriz = matriz,
        situacao_cadastral = situacao_cadastral,
        regime_tributario = regime_tributario,
        bairro = bairro
    )


def jsonfy(dataframe):
    df = dataframe.to_json(orient = 'records')
    return load(StringIO(df))

def get_consultores():
    return jsonfy(client.get_consultores(to_dataframe = True))

def add_consultor_to_db(consultor: ConsultorModel):
    client.add_consultor(consultor)

def add_venda_to_db(venda: VendaModel):
    stats = get_cnpj_all_stats(venda.cnpj)
    client.add_venda(
        venda.cnpj, venda.telefone, venda.consultor, venda.data, venda.gestor, venda.plano,
        venda.quantidade_de_produtos, venda.revenda, venda.tipo, venda.uf, venda.valor_acumulado, 
        venda.valor_do_plano, venda.email, stats.quadro_funcionarios, stats.faturamento, stats.cnae,
        stats.cep, stats.municipio, stats.porte, stats.capital_social, stats.natureza_juridica, 
        stats.matriz, stats.situacao_cadastral, stats.regime_tributario, stats.bairro
    )

def remove_venda_from_db(id: IdentifyModel):
    client.remove_venda(id.id)

def add_produto_to_db(produto: ProdutoModel):
    client.add_produto(
        nome = produto.nome,
        preco = produto.preco
    )

def remove_produto_from_db(id: IdentifyModel):
    client.remove_produto(id.id)

def remove_consultor_from_db(id: IdentifyModel):
    client.remove_consultor(id.id)

def get_vendas(ano: int, mes: str):
    return jsonfy(client.filter_by(ano, mes))

def get_produtos():
    return jsonfy(client.get_produtos(to_dataframe = True))

def token_authenticate(token: TokenModel):
    return client.jwt_authenticate(token)

class Freecel:
    def __init__(
            self, ano: Optional[int] = None, mes: Optional[str] = None):
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
        self.ufs = client.ufs(ano, mes)
        self.tipo_venda = client.tipo_venda

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
