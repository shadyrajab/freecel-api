from client.client import Client
from json import load
from requests import request
from io import StringIO
from datetime import datetime
from utils.variables import HOST, DATABASE, USER, PASSWORD, TOKENEMPRESAS
from models.vendas import Venda 
from models.empresa import Empresa

def return_wrong_cnpj(venda: Venda):
    valor_acumulado = venda.quantidade_de_produtos * venda.valor_do_plano

    return Venda(
        cnpj=venda.cnpj, telefone=venda.telefone, consultor=venda.consultor, data=venda.data,
        gestor=venda.gestor, plano=venda.plano, quantidade_de_produtos=venda.quantidade_de_produtos, 
        revenda=venda.revenda, tipo=venda.tipo, uf=venda.uf, valor_acumulado=valor_acumulado, 
        valor_do_plano=venda.valor_do_plano, email=venda.email, quadro_funcionarios=None,
        faturamento=None, cnae=None, cep=None, municipio=None, porte=None, capital_social=None, 
        natureza_juridica=None, matriz=None, bairro=None, situacao_cadastral=None, regime_tributario=None 
    )

def get_cnpj_all_stats(venda: Empresa):
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