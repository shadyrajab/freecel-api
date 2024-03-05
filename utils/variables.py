from dotenv import load_dotenv
from os import getenv

load_dotenv()

HOST = getenv('host')
DATABASE = getenv('database')
USER = getenv('user')
PASSWORD = getenv('password')
TOKENEMPRESAS = getenv('tokenEmpresas')

TIPO_VENDA = {"FIXA", "AVANÇADA", "MIGRAÇÃO PRÉ-PÓS", "VVN", "ALTAS", "PORTABILIDADE"}
EQUIPE = {"FREECEL", "VALPARAISO", "PARCEIRO", "GOIÂNIA"}
UF = {
    "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT","MS", "MG", "TO"
    "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE"
}

DF_MOVEL = 'DFP4059-001'
GO_MOVEL = 'GOP4096-001'
DF_FIXA = 'DFPAE0005-1'
GO_FIXA = 'GOPAE0031-1'

adabas_mapping = {
    ('GOIÂNIA', 'ALTAS'): GO_MOVEL,
    ('GOIÂNIA', 'PORTABILIDADE'): GO_MOVEL,
    ('GOIÂNIA', 'MIGRAÇÃO PRÉ-PÓS'): GO_MOVEL,
    ('GOIÂNIA', 'VVN'): GO_FIXA,
    ('GOIÂNIA', 'FIXA'): GO_FIXA,
    ('GOIÂNIA', 'AVANÇADA'): GO_FIXA,
    ('FREECEL', 'ALTAS'): DF_MOVEL,
    ('FREECEL', 'PORTABILIDADE'): DF_MOVEL,
    ('FREECEL', 'MIGRAÇÃO PRÉ-PÓS'): DF_MOVEL,
    ('FREECEL', 'VVN'): DF_FIXA,
    ('FREECEL', 'FIXA'): DF_FIXA,
    ('FREECEL', 'AVANÇADA'): DF_FIXA,
    ('VALPARAISO', 'ALTAS'): DF_MOVEL,
    ('VALPARAISO', 'PORTABILIDADE'): DF_MOVEL,
    ('VALPARAISO', 'MIGRAÇÃO PRÉ-PÓS'): DF_MOVEL,
    ('VALPARAISO', 'VVN'): DF_FIXA,
    ('VALPARAISO', 'FIXA'): DF_FIXA,
    ('VALPARAISO', 'AVANÇADA'): DF_FIXA,
    ('PARCEIRO', 'ALTAS'): DF_MOVEL,
    ('PARCEIRO', 'PORTABILIDADE'): DF_MOVEL,
    ('PARCEIRO', 'MIGRAÇÃO PRÉ-PÓS'): DF_MOVEL,
    ('PARCEIRO', 'VVN'): DF_FIXA,
    ('PARCEIRO', 'FIXA'): DF_FIXA,
    ('PARCEIRO', 'AVANÇADA'): DF_FIXA,
    ('SAMAMBAIA', 'ALTAS'): DF_MOVEL,
    ('SAMAMBAIA', 'PORTABILIDADE'): DF_MOVEL,
    ('SAMAMBAIA', 'MIGRAÇÃO PRÉ-PÓS'): DF_MOVEL,
    ('SAMAMBAIA', 'VVN'): DF_FIXA,
    ('SAMAMBAIA', 'FIXA'): DF_FIXA,
    ('SAMAMBAIA', 'AVANÇADA'): DF_FIXA,
}


MONTHS = [
    'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 
    'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
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

DDDS = [
    '61', '62', '64', '65', '67', '82', '71', '73', '74', '75', '77', '85', '88', '98', '99', '83',
    '81', '87', '86', '89', '84', '79', '68', '96', '92', '97', '91', '93', '94', '69', '95', '63', 
    '27', '28', '31', '32', '33', '34', '35', '37', '38', '21', '22', '24', '11', '12', '13', '14', 
    '15', '16', '17', '18', '19', '41', '42', '43', '44', '45', '46', '51', '53', '54', '55', '47', 
    '48', '49'
]

DDDS_valor_inteiro = [
    '61', '62', '63', '64', '65', '66', '67', '68', '69', '91', '92', '93', '94', '95', '96,' '97', 
    '98', '99'
]