from client.client import Freecel
from dotenv import load_dotenv
from os import getenv
from json import load
from requests import request

from typing import Optional
from io import StringIO

from datetime import datetime

load_dotenv()

HOST = getenv('host')
DATABASE = getenv('database')
USER = getenv('user')
PASSWORD = getenv('password')
TOKENEMPRESAS = getenv('tokenEmpresas')

def create_client():
    return Freecel(
        host = HOST,
        database = DATABASE,
        user = USER,
        password = PASSWORD
    )

def return_wrong_cnpj(venda: VendaModel):
    valor_acumulado = venda.quantidade_de_produtos * venda.valor_do_plano

    return VendaSchema(
        cnpj=venda.cnpj, telefone=venda.telefone, consultor=venda.consultor, data=venda.data,
        gestor=venda.gestor, plano=venda.plano, quantidade_de_produtos=venda.quantidade_de_produtos, 
        revenda=venda.revenda, tipo=venda.tipo, uf=venda.uf, valor_acumulado=valor_acumulado, 
        valor_do_plano=venda.valor_do_plano, email=venda.email, quadro_funcionarios=None,
        faturamento=None, cnae=None, cep=None, municipio=None, porte=None, capital_social=None, 
        natureza_juridica=None, matriz=None, bairro=None, situacao_cadastral=None, regime_tributario=None 
    )

def get_cnpj_all_stats(venda: VendaModel):
    empresas_aqui = f'https://www.empresaqui.com.br/api/{TOKENEMPRESAS}/{venda.cnpj}'
    response = request('GET', url = empresas_aqui)

    if response.status_code == 200 and response.text:
        try:
            stats = response.json()
        except:
            return return_wrong_cnpj(venda)
    else:
        return return_wrong_cnpj(venda)
        
    return get_data_stats(venda, stats)

def formatar_regime_tributario(regime):
    regime_formatado = str(regime).split(';')

    if len(regime_formatado) > 5:
        return '; '.join(regime_formatado[-5:])
    else:
        return regime

def get_data_stats(venda: VendaModel, stats) -> VendaSchema:
    valor_acumulado = venda.quantidade_de_produtos * venda.valor_do_plano
    venda.data = str(datetime.strptime(venda.data, '%d-%m-%Y'))
    stats['regime_tributario'] = formatar_regime_tributario(stats.get('regime_tributario'))

    return VendaSchema(
        cnpj=venda.cnpj, telefone=venda.telefone, consultor=venda.consultor, data=venda.data,
        gestor=venda.gestor, plano=venda.plano, quantidade_de_produtos=venda.quantidade_de_produtos, 
        revenda=venda.revenda, tipo=venda.tipo, uf=venda.uf, valor_acumulado=valor_acumulado, 
        valor_do_plano=venda.valor_do_plano, email=venda.email, quadro_funcionarios=stats.get('quadro_funcionarios'),
        faturamento=stats.get('faturamento'), cnae=stats.get('cnae_principal'), cep=stats.get('log_cep'), 
        municipio=stats.get('log_municipio'), porte=stats.get('porte'), capital_social=stats.get('capital_social'), 
        natureza_juridica=stats.get('natureza_juridica'), matriz=stats.get('matriz'), bairro=stats.get('log_bairro'),
        situacao_cadastral=stats.get('situacao_cadastral'), regime_tributario=stats.get('regime_tributario'), 
    )

def jsonfy(dataframe):
    df = dataframe.to_json(orient = 'records')
    return load(StringIO(df))

def get_consultores():
    client = create_client()
    return jsonfy(client.get_consultores(to_dataframe = True))

def add_consultor_to_db(consultor: ConsultorModel):
    client = create_client()
    client.add_consultor(consultor)

def add_venda_to_db(venda: VendaModel):
    client = create_client()
    venda = get_cnpj_all_stats(venda)
    client.add_venda(venda)

def remove_venda_from_db(id: IdentifyModel):
    client = create_client()
    client.remove_venda(id.id)

def add_produto_to_db(produto: ProdutoModel):
    client = create_client()
    client.add_produto(
        nome = produto.nome,
        preco = produto.preco
    )

def remove_produto_from_db(id: IdentifyModel):
    client = create_client()
    client.remove_produto(id.id)

def remove_consultor_from_db(id: IdentifyModel):
    client = create_client()
    client.remove_consultor(id.id)

def get_vendas(ano: int, mes: str):
    client = create_client()
    return jsonfy(client.filter_by(ano, mes))

def get_produtos():
    client = create_client()
    return jsonfy(client.get_produtos(to_dataframe = True))

def token_authenticate(token: TokenModel):
    client = create_client()
    return client.jwt_authenticate(token)

class Stats:
    def __init__(
            self, ano: Optional[int] = None, mes: Optional[str] = None):
        client = create_client()
        consultor_do_mes_nome = client.consultor_do_mes(ano, mes).name
        self.receita_total = client.receita_total(ano, mes)
        self.quantidade_vendida = client.qtd_de_produtos_vendidos(ano, mes)
        self.quantidade_clientes = client.quantidade_clientes(ano, mes)
        self.ticket_medio = client.ticket_medio(ano, mes)
        self.receita_media_diaria = client.receita_media_diaria(ano, mes)
        self.media_por_consultor_geral = client.media_por_consultor(ano, mes)
        self.media_por_consultor_altas = client.media_por_consultor(ano, mes, 'ALTAS')
        self.media_por_consultor_migracao = client.media_por_consultor(ano, mes, 'MIGRAÇÃO PRÉ-PÓS')
        self.media_por_consultor_fixa = client.media_por_consultor(ano, mes, 'FIXA')
        self.media_por_consultor_avancada = client.media_por_consultor(ano, mes, 'AVANÇADA')
        self.media_por_consultor_vvn = client.media_por_consultor(ano, mes, 'VVN')
        self.maior_venda_mes = client.maior_venda_mes()

        if ano:
            self.delta_receita_total = client.delta_receita_total(ano, mes)
            self.delta_quantidade_produtos = client.delta_quantidade_produtos(ano, mes)
            self.delta_quantidade_clientes = client.delta_quantidade_clientes(ano, mes)
            self.delta_ticket_medio = client.delta_ticket_medio(ano, mes)
            self.delta_media_diaria = client.delta_media_diaria(ano, mes)
            self.delta_media_por_consultor = client.delta_media_por_consultor(ano, mes)
            self.consultor_do_mes = Consultor(consultor_do_mes_nome, ano, mes)

        self.qtd_vendas_por_cnae = jsonfy(client.qtd_vendas_por_cnae(ano, mes))
        self.qtd_vendas_por_faturamento = jsonfy(client.qtd_vendas_por_faturamento(ano, mes))
        self.qtd_vendas_por_colaboradores = jsonfy(client.qtd_vendas_por_colaboradores(ano, mes))
        self.qtd_vendas_por_uf = jsonfy(client.qtd_vendas_por_uf(ano, mes))
        self.ufs = client.ufs(ano, mes)
        self.tipo_venda = client.tipo_venda
        self.dates = client.dates

class Rankings:
    def __init__(
        self, ano: Optional[int] = None, mes: Optional[str] = None
    ):
        client = create_client()
        rankings = client.Ranking()
        self.ranking_consultores = jsonfy(rankings.consultores(ano, mes))
        self.ranking_produtos = jsonfy(rankings.produtos(ano, mes))
        self.ranking_fixa = jsonfy(rankings.consultores(ano, mes, tipo = 'FIXA'))
        self.ranking_avancada = jsonfy(rankings.consultores(ano, mes, tipo = 'AVANÇADA'))
        self.ranking_vvn = jsonfy(rankings.consultores(ano, mes, tipo = 'VVN'))
        self.ranking_migracao = jsonfy(rankings.consultores(ano, mes, tipo  = 'MIGRAÇÃO PRÉ-PÓS'))
        self.ranking_altas = jsonfy(rankings.consultores(ano, mes, tipo = 'ALTAS'))
        self.ranking_planos = jsonfy(rankings.planos(ano, mes))
        
class Consultor:
    def __init__(
            self, name: str, ano: Optional[int] = None, mes: Optional[str] = None, display_vendas: Optional[bool] = None
        ):
        client = create_client()
        consultor = client.Consultor(name)

        self.name = consultor.name

        self.receita_total =  consultor.receita(ano, mes)
        self.quantidade_vendida =  consultor.quantidade(ano, mes)
        self.quantidade_clientes = consultor.quantidade_clientes(ano, mes)

        self.receita_media_diaria =  consultor.receita_media_diaria(ano, mes)
        self.quantidade_media_diaria =  consultor.quantidade_media_diaria(ano, mes)

        self.quantidade_media_mensal = consultor.quantidade_media_mensal
        self.receita_media_mensal =  consultor.receita_media_mensal

        self.ticket_medio = consultor.ticket_medio(ano, mes)

        if ano:
            self.delta_receita_total = consultor.delta_receita_mensal(ano, mes)
            self.delta_quantidade_produtos = consultor.delta_quantidade_mensal(ano, mes)
            self.delta_quantidade_clientes = consultor.delta_quantidade_clientes(ano, mes)
            self.delta_ticket_medio = consultor.delta_ticket_medio(ano, mes)
            self.delta_media_diaria = consultor.delta_media_diaria(ano, mes)

        if display_vendas:
            self.vendas = jsonfy(consultor.filter_by(ano, mes))

        self.dates = consultor.dates
        self.ranking_planos = jsonfy(consultor.ranking_planos(ano, mes))
        self.ranking_produtos = jsonfy(consultor.ranking_produtos(ano, mes))