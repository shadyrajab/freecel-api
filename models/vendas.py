from pydantic import EmailStr, validator
from pycpfcnpj import cpfcnpj
from utils.variables import TIPO_VENDA, EQUIPE, UF, HOST, DATABASE, USER, PASSWORD
from math import ceil
from datetime import datetime
from client.client import Freecel
from models.empresa import Empresa
import re

class Venda(Empresa):
    cnpj: str
    telefone: str
    consultor: str
    data: str
    gestor: str
    plano: str
    volume: int
    equipe: str
    tipo: str
    uf: str
    preco: float
    email: EmailStr
    
    @validator('plano')
    def validate_plano(cls, value):
        client = cls.__create_client()
        planos = client.get_produtos()
        planos = [plano[0] for plano in planos]

        if value.upper() not in planos:
            raise ValueError(f"Não existe nenhum plano na base de dados chamado {value}.")

    @validator('consultor')
    def validate_consultor(cls, value):
        client = cls.__create_client()
        consultores = client.get_consultores()
        consultores = [consultor[0] for consultor in consultores]

        if value.upper() not in consultores:
            raise ValueError(f"Não existe nenhum consultor na base de dados chamado {value}.")
        
        return value.upper()

    @validator('gestor')
    def validate_gestor(cls, value):
        if re.search(r'\d', value):
            raise ValueError("O nome do gestor não deve conter caracteres numéricos.")
        
        return value

    @validator('telefone')
    def validate_telefone(cls, value):
        telefone = re.sub(r'[^0-9]', '', value)
        if len(telefone) != 11:
            raise ValueError("""
                O número de telefone informado está inválido. Informe o número DDD e os 9 dígitos 
                do telefone
            """)
        
        return telefone

    @validator('preco')
    def validate_preco(cls, value):
        if value < 1:
            raise ValueError("O preço do produto não pode ser menor do que 1")
        
        return value

    @validator('data')
    def validate_data(cls, value):
        try:
            value = datetime.strptime(value, '%Y-%m-%d').strftime('%d-%m-%Y')
        except:
            raise ValueError("Formato de data inválido, por favor informe a data no formato %d-%m-%Y")

        return value

    @validator('uf')
    def validate_uf(cls, value):
        if value.upper() not in UF:
            raise ValueError("A UF informada não existe.")
        
        return value.upper()

    @validator('equipe')
    def validate_equipe(cls, value):
        if value.upper() not in EQUIPE:
            raise ValueError(f"""
                O nome da equipe informado está inválido. O nome da equipe deve ser {str(EQUIPE)}, não {value}
            """)
        
        return value.upper()

    @validator('volume')
    def validate_volume(cls, value):
        if value < 1: 
            raise ValueError(f"O Volume da venda não pode ser menor do que 1.")
        
        return ceil(value)

    @validator('tipo')
    def validate_tipo(cls, value):
        if value.upper() not in TIPO_VENDA:
            raise ValueError(f"""
                O tipo de venda informado está inválido. O tipo deve ser {str(EQUIPE)}, não {value}
            """)
        
        return value.upper()
    
    @validator('cnpj')
    def validate_cnpj(cls, value):
        cnpj = re.sub(r'[^0-9]', '', value)
        if not cpfcnpj.validate(cnpj):
            raise ValueError(f"O CNPJ ou CPF informado está inválido.")
        
        return cnpj
    
    def __create_client():
        client = Freecel(
            host = HOST,
            database = DATABASE,
            user = USER,
            password = PASSWORD
        )

        return client