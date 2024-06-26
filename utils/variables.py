CARGOS = {"SUPERVISOR", "ESTAGIÁRIO", "EFETIVO"}
ALTAS = [
    "INTERNET_TOTALIZACAO",
    "JÁ CLIENTE",
    "NOVO",
    "NOVO - VIVO TOTAL",
    "PORTABILIDADE",
    "PORTABILIDADE - VIVO TOTAL",
    "PORTABILIDADE CNPJ – CNPJ",
    "PORTABILIDADE PF + TT PF/PJ",
    "SERVIÇO",
    "TROCA",
    "NOVO_TOTALIZACAO",
    "TT PF/PJ + MIGRAÇÃO",
    "TT PJ/PJ",
    "JÁ CLIENTE - VIVO TOTAL",
    "FWT",
    "BASE_TOTALIZACAO",
    "PORTABILIDADE_TOTALIZACAO",
    "TT PF/PJ",
    "PORTABILIDADE PF + TT PF/PJ - VIVO TOTAL",
    "PORTABILIDADE FWT",
    "RENEGOCIAÇÃO",
    "RENEGOCIÇÃO + PORTABILIDADE",
    "RERNEGOCIAÇÃO + MIGRAÇÃO",
    "TRANSF. TITULARIDADE PÓS PF-PJ + MIGRAÇÃO - FWT",
    "TRANSF. TITULARIDADE PÓS PF-PJ + MIGRAÇÃO",
    "TOTALIZAÇÃO",
]


FIXA = ["FIXA"]
AVANCADA = ["AVANÇADA"]
VVN = ["VVN"]

MIGRACAO_PREPOS = [
    "MIGRAÇÃO PRÉ/PÓS",
    "MIGRAÇÃO PRÉ/PÓS - VIVO TOTAL",
    "MIGRAÇÃO PRÉ/PÓS + TROCA",
    "MIGRAÇÃO PRÉ/PÓS_TOTALIZACAO",
]

MIGRACAO = [
    "MIGRAÇÃO",
    "MIGRAÇÃO+TROCA",
    "MIGRAÇÃO DE TECNOLOGIA",
    "MIGRAÇÃO DE METALICO P/ METALICO",
    "MIGRAÇÃO DE GPON PARA GPON",
    "MIGRAÇÃO VVN",
]

TROCA = ["TROCA"]

PEN = ["INTERNET"]
INOVACAO = ["ATIVAÇÃO DE SERVIÇO"]
TIPO_VENDA = ALTAS + FIXA + AVANCADA + VVN + MIGRACAO_PREPOS

TERMO_COLUMNS = ["Nº", "Comp.", "DDD", "Nº da Linha"]
COMPOSICAO_COLUMNS = [
    "Comp.",
    "DDD",
    "Qtde.",
    "Negociação",
    "Conta",
    "Plano e Vlr. Unit.",
    "Serviço Vlr. Unit.",
    "Benefício da Oferta X Valor de Prateleira Unitário*",
    "Trade In",
    "Vlr. Unit. Composição/Comprometimento",
    "Aparelho",
    "Desconto de Aparelho",
    "Prazo de Vigência",
]

INDEX_COLUMNS = [
    "Nº",
    "Comp.",
    "Negociação",
    "DDD_x",
    "Telefone",
    "Plano e Vlr. Unit.",
    "M",
    "Recomendação",
    "Recomendação UP",
]

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
    "TO" "PA",
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
    ("GOIÂNIA", "MIGRAÇÃO PRÉ/PÓS"): GO_MOVEL,
    ("GOIÂNIA", "VVN"): GO_FIXA,
    ("GOIÂNIA", "FIXA"): GO_FIXA,
    ("GOIÂNIA", "AVANÇADA"): GO_FIXA,
    ("FREECEL", "ALTAS"): DF_MOVEL,
    ("FREECEL", "MIGRAÇÃO PRÉ/PÓS"): DF_MOVEL,
    ("FREECEL", "VVN"): DF_FIXA,
    ("FREECEL", "FIXA"): DF_FIXA,
    ("FREECEL", "AVANÇADA"): DF_FIXA,
    ("VALPARAISO", "ALTAS"): DF_MOVEL,
    ("VALPARAISO", "MIGRAÇÃO PRÉ/PÓS"): DF_MOVEL,
    ("VALPARAISO", "VVN"): DF_FIXA,
    ("VALPARAISO", "FIXA"): DF_FIXA,
    ("VALPARAISO", "AVANÇADA"): DF_FIXA,
    ("PARCEIRO", "ALTAS"): DF_MOVEL,
    ("PARCEIRO", "MIGRAÇÃO PRÉ/PÓS"): DF_MOVEL,
    ("PARCEIRO", "VVN"): DF_FIXA,
    ("PARCEIRO", "FIXA"): DF_FIXA,
    ("PARCEIRO", "AVANÇADA"): DF_FIXA,
    ("SAMAMBAIA", "ALTAS"): DF_MOVEL,
    ("SAMAMBAIA", "MIGRAÇÃO PRÉ/PÓS"): DF_MOVEL,
    ("SAMAMBAIA", "VVN"): DF_FIXA,
    ("SAMAMBAIA", "FIXA"): DF_FIXA,
    ("SAMAMBAIA", "AVANÇADA"): DF_FIXA,
}

CATEGORIAS = {
    "INTERNET_TOTALIZACAO": "ALTAS",
    "INTERNET": "ALTAS",
    "JÁ CLIENTE": "ALTAS",
    "MIGRAÇÃO": "ALTAS",
    "MIGRAÇÃO+TROCA": "ALTAS",
    "NOVO": "ALTAS",
    "NOVO - VIVO TOTAL": "ALTAS",
    "PORTABILIDADE": "ALTAS",
    "PORTABILIDADE - VIVO TOTAL": "ALTAS",
    "PORTABILIDADE CNPJ – CNPJ": "ALTAS",
    "PORTABILIDADE PF + TT PF/PJ": "ALTAS",
    "SERVIÇO": "ALTAS",
    "TROCA": "ALTAS",
    "NOVO_TOTALIZACAO": "ALTAS",
    "TT PF/PJ + MIGRAÇÃO": "ALTAS",
    "TT PJ/PJ": "ALTAS",
    "JÁ CLIENTE - VIVO TOTAL": "ALTAS",
    "FWT": "ALTAS",
    "BASE_TOTALIZACAO": "ALTAS",
    "PORTABILIDADE_TOTALIZACAO": "ALTAS",
    "TT PF/PJ": "ALTAS",
    "PORTABILIDADE PF + TT PF/PJ - VIVO TOTAL": "ALTAS",
    "PORTABILIDADE FWT": "ALTAS",
    "RENEGOCIAÇÃO": "ALTAS",
    "RENEGOCIÇÃO + PORTABILIDADE": "ALTAS",
    "RERNEGOCIAÇÃO + MIGRAÇÃO": "ALTAS",
    "TRANSF. TITULARIDADE PÓS PF-PJ + MIGRAÇÃO - FWT": "ALTAS",
    "TRANSF. TITULARIDADE PÓS PF-PJ + MIGRAÇÃO": "ALTAS",
    "TOTALIZAÇÃO": "ALTAS",
    "PEN": "ALTAS",
    "FIXA": "FIXA",
    "AVANÇADA": "AVANÇADA",
    "VVN": "VVN",
    "MIGRAÇÃO PRÉ/PÓS": "MIGRAÇÃO PRÉ/PÓS",
    "MIGRAÇÃO PRÉ/PÓS - VIVO TOTAL": "MIGRAÇÃO PRÉ/PÓS",
    "MIGRAÇÃO PRÉ/PÓS + TROCA": "MIGRAÇÃO PRÉ/PÓS",
    "MIGRAÇÃO PRÉ/PÓS_TOTALIZACAO": "MIGRAÇÃO PRÉ/PÓS",
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
