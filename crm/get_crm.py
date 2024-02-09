from dotenv import load_dotenv
from os import getenv
import pandas as pd
from requests import request
from io import StringIO
import json

load_dotenv()

ESTRUTURA = getenv('tokenEstrutura')
USUARIO = getenv('tokenUsuario')
URL = 'https://app.neosales.com.br/producao-painel-integration-v2'

def to_data_frame(response) -> pd.DataFrame:
    try:
        dataframe = pd.read_csv(
            StringIO(response.text), sep=';', header=0, encoding='utf-8'
        )

        dataframe.to_excel('doidao.xlsx')

        # Remover colunas desnecessárias
        columns_to_drop = [
            'Pedido Vinculado',
            'Usuário ADM',
            'Revisão',
            'Item',
            'Data Instalação',
            'Período',
            'Cidade Instalação',
            'Estado Instalação',
            'Rpon',
            'Instância',
            'Consultor na Operadora',
            'Etapa Item'
        ]
        dataframe = dataframe.drop(columns=columns_to_drop, axis=1)

        # Converter todas as colunas para string
        dataframe = dataframe.astype(str)

        return dataframe

    except Exception as e:
        print(f"Erro ao processar resposta: {e}")
        return None

def get_crm(dataHoraInicioCarga: str, dataHoraFimCarga: str) -> pd.DataFrame:
    payload = json.dumps({
        "tokenEstrutura": ESTRUTURA,
        "tokenUsuario": USUARIO,
        "dataHoraInicioCarga": dataHoraInicioCarga,
        "dataHoraFimCarga": dataHoraFimCarga,
        "painelId": "15316",
        "outputFormat": "csv"
    })

    headers = {
        'Content-Type': 'text/plain',
        'Cookie': '__cflb=02DiuHcRebXBbQZs3gX28EM2MeLsdaT3jC2MMTm36LJzp'
    }

    response = request('GET', url = URL, data = payload, headers = headers)

    return to_data_frame(response)