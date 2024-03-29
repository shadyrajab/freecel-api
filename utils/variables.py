from os import getenv

from dotenv import load_dotenv

load_dotenv()

HOST = getenv("host")
DATABASE = getenv("database")
USER = getenv("user")
PASSWORD = getenv("password")
TOKENEMPRESAS = getenv("tokenEmpresas")

CARGOS = {"SUPERVISOR", "ESTAGIÁRIO", "EFETIVO"}
SUPERVISORES = {"FLAVIO HENRIQUE LEMOS DOS NASCIMENTO"}
TIPO_VENDA = {"FIXA", "AVANÇADA", "MIGRAÇÃO PRÉ-PÓS", "VVN", "ALTAS", "PORTABILIDADE"}
EQUIPE = {"FREECEL", "VALPARAISO", "PARCEIRO", "GOIÂNIA", "SAMAMBAIA"}
UF = {
    "AC",
    "AL",
    "AP",
    "AM",
    "BA",
    "CE",
    "DF",
    "ES",
    "GO",
    "MA",
    "MT",
    "MS",
    "MG",
    "TO" 
    "PA",
    "PB",
    "PR",
    "PE",
    "PI",
    "RJ",
    "RN",
    "RS",
    "RO",
    "RR",
    "SC",
    "SP",
    "SE",
}

DF_MOVEL = "DFP4059-001"
GO_MOVEL = "GOP4096-001"
DF_FIXA = "DFPAE0005-1"
GO_FIXA = "GOPAE0031-1"

adabas_mapping = {
    ("GOIÂNIA", "ALTAS"): GO_MOVEL,
    ("GOIÂNIA", "PORTABILIDADE"): GO_MOVEL,
    ("GOIÂNIA", "MIGRAÇÃO PRÉ-PÓS"): GO_MOVEL,
    ("GOIÂNIA", "VVN"): GO_FIXA,
    ("GOIÂNIA", "FIXA"): GO_FIXA,
    ("GOIÂNIA", "AVANÇADA"): GO_FIXA,
    ("FREECEL", "ALTAS"): DF_MOVEL,
    ("FREECEL", "PORTABILIDADE"): DF_MOVEL,
    ("FREECEL", "MIGRAÇÃO PRÉ-PÓS"): DF_MOVEL,
    ("FREECEL", "VVN"): DF_FIXA,
    ("FREECEL", "FIXA"): DF_FIXA,
    ("FREECEL", "AVANÇADA"): DF_FIXA,
    ("VALPARAISO", "ALTAS"): DF_MOVEL,
    ("VALPARAISO", "PORTABILIDADE"): DF_MOVEL,
    ("VALPARAISO", "MIGRAÇÃO PRÉ-PÓS"): DF_MOVEL,
    ("VALPARAISO", "VVN"): DF_FIXA,
    ("VALPARAISO", "FIXA"): DF_FIXA,
    ("VALPARAISO", "AVANÇADA"): DF_FIXA,
    ("PARCEIRO", "ALTAS"): DF_MOVEL,
    ("PARCEIRO", "PORTABILIDADE"): DF_MOVEL,
    ("PARCEIRO", "MIGRAÇÃO PRÉ-PÓS"): DF_MOVEL,
    ("PARCEIRO", "VVN"): DF_FIXA,
    ("PARCEIRO", "FIXA"): DF_FIXA,
    ("PARCEIRO", "AVANÇADA"): DF_FIXA,
    ("SAMAMBAIA", "ALTAS"): DF_MOVEL,
    ("SAMAMBAIA", "PORTABILIDADE"): DF_MOVEL,
    ("SAMAMBAIA", "MIGRAÇÃO PRÉ-PÓS"): DF_MOVEL,
    ("SAMAMBAIA", "VVN"): DF_FIXA,
    ("SAMAMBAIA", "FIXA"): DF_FIXA,
    ("SAMAMBAIA", "AVANÇADA"): DF_FIXA,
}


MONTHS = [
    "JANEIRO",
    "FEVEREIRO",
    "MARÇO",
    "ABRIL",
    "MAIO",
    "JUNHO",
    "JULHO",
    "AGOSTO",
    "SETEMBRO",
    "OUTUBRO",
    "NOVEMBRO",
    "DEZEMBRO",
]

MONTHS_BY_NUMBERS = {
    "JANEIRO": 1,
    "FEVEREIRO": 2,
    "MARÇO": 3,
    "ABRIL": 4,
    "MAIO": 5,
    "JUNHO": 6,
    "JULHO": 7,
    "AGOSTO": 8,
    "SETEMBRO": 9,
    "OUTUBRO": 10,
    "NOVEMBRO": 11,
    "DEZEMBRO": 12,
}

DDDS = [
    "61",
    "62",
    "64",
    "65",
    "67",
    "82",
    "71",
    "73",
    "74",
    "75",
    "77",
    "85",
    "88",
    "98",
    "99",
    "83",
    "81",
    "87",
    "86",
    "89",
    "84",
    "79",
    "68",
    "96",
    "92",
    "97",
    "91",
    "93",
    "94",
    "69",
    "95",
    "63",
    "27",
    "28",
    "31",
    "32",
    "33",
    "34",
    "35",
    "37",
    "38",
    "21",
    "22",
    "24",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "41",
    "42",
    "43",
    "44",
    "45",
    "46",
    "51",
    "53",
    "54",
    "55",
    "47",
    "48",
    "49",
]

DDDS_valor_inteiro = [
    "61",
    "62",
    "63",
    "64",
    "65",
    "66",
    "67",
    "68",
    "69",
    "91",
    "92",
    "93",
    "94",
    "95",
    "96," 
    "97",
    "98",
    "99",
]

STATUS_VENDA = [
    "AGUARDANDO CHAMADO",
    "CREDITO NEGADO",
    "AGUARDANDO CONSULTOR",
    "AGUARDANDO GERAÇÃO DO CONTRATO",
    "AGUARDANDO SS",
    "ANALISE BKO",
    "ANALISE DE CREDITO",
    "CANCELADO",
    "CHECK LIST PENDENTE",
    "CHECKLIST",
    "CONCLUÍDO",
    "CONCLUÍDO-EXECUTADO PARCIALMENTE",
    "CREDITO REPROVADO",
    "EXECUTADO PARCIALMENTE",
    "FATURANDO",
    "FATURANDO-PORTABILIDADE",
    "INPUT",
    "MESA DE FRAUDE",
    "REPROVADO POR FRAUDE",
    "SEM ESTOQUE",
    "BACKOFFICE REPROVADO",
    "AGUARDANDO CASO",
    "REFAZER",
    "PENDENTE",
    "EXPIRADO",
    "EM ANALISE",
    "AGUARDANDO SAV",
    "FATURANDO- INSTALADO",
    "AGUARDANDO 1º PEDIDO",
    "ABERTA",
    "CONCLUÍDO / PAGO",
    "Simulação Reprovada",
    "SIMPLIFIQUE",
    "VALIDAÇÃO DE DOCUMENTOS",
    "PORTABILIDADE NEGADA* CHAMADO",
    "PORTABILIDADE CANCELADA",
    "ATIVO",
    "ATIVO/PAGO",
    "CABEAMENTO",
    "CAIXA OBSTRUIDA",
    "TT PJ/PJ",
    "TT PF/PJ",
    "CANCELADO",
    "CONTRATO ENVIADO PARA ÁREA COMERCIAL",
    "ENVIADO",
    "INDISPONIVEL",
    "NECESSIDADE DE CABEAMENTO",
    "PORTA QUEIMADA",
    "RACO",
    "REPROVADO",
    "REPROVADO NO SAV",
    "SUPORTE",
    "RETIDO",
    "SAV",
    "MIGRAÇAO DE TECNOLOGIA",
    "AGUARDANDO CHAMADO",
    "ATIVO MIGRAÇÃO",
    "ANALISE DE CREDITO",
    "MESA DE FRAUDE",
    "MESA DE CRÉDITO",
    "AGUARDANDO INPUT",
    "FATURANDO",
    "ENVIADO MIGRAÇÃO",
    "ATIVO METALICO",
    "ENVIADO-PAGO",
    "FATURANDO INSTALADO",
    "ENVIADO METALICO",
    "PENDENCIA TECNICA",
    "REPROVADO SUPORTE",
    "CREDITO REPROVADO",
    "TOTALIZAÇÃO",
]
