from dotenv import load_dotenv
from os import getenv

load_dotenv()

TIPO_VENDA = {"FIXA", "AVANÇADA", "MIGRAÇÃO PRÉ-PÓS", "VVN", "ALTAS"}
EQUIPE = {"FREECEL", "VALPARAISO", "PARCEIRO", "ESCRITORIO"}
UF = {
    "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT","MS", "MG", "TO"
    "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE"
}

HOST = getenv('host')
DATABASE = getenv('database')
USER = getenv('user')
PASSWORD = getenv('password')
TOKENEMPRESAS = getenv('tokenEmpresas')