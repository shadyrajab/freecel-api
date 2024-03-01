from dotenv import load_dotenv
from os import getenv

load_dotenv()

TIPO_VENDA = {"FIXA", "AVANÇADA", "MIGRAÇÃO PRÉ-PÓS", "VVN", "ALTAS", "PORTABILIDADE"}
EQUIPE = {"FREECEL", "VALPARAISO", "PARCEIRO", "GOIÂNIA"}
UF = {
    "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT","MS", "MG", "TO"
    "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE"
}

MONTHS = [
    'Janeiro', 
    'Fevereiro', 
    'Março', 
    'Abril', 
    'Maio', 
    'Junho', 
    'Julho', 
    'Agosto', 
    'Setembro', 
    'Outubro', 
    'Novembro', 
    'Dezembro'
]

MONTHS_BY_NUMBERS = {
    'Janeiro': 1,
    'Fevereiro': 2,
    'Março': 3,
    'Abril': 4,
    'Maio': 5,
    'Junho': 6,
    'Julho': 7,
    'Agosto': 8,
    'Setembro': 9,
    'Outubro': 10,
    'Novembro': 11,
    'Dezembro': 12
}

HOST = getenv('host')
DATABASE = getenv('database')
USER = getenv('user')
PASSWORD = getenv('password')
TOKENEMPRESAS = getenv('tokenEmpresas')