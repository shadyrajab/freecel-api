from utils.variables import TIPO_VENDA, EQUIPE
from pydantic import EmailStr, validator, BaseModel
from client.instance import client
from datetime import datetime
from pycpfcnpj import cpfcnpj
from math import ceil
import re

class Venda(BaseModel):
    cnpj: str
    telefone: str
    consultor: str
    data: datetime
    gestor: str
    plano: str
    volume: int
    equipe: str
    tipo: str
    preco: float
    email: EmailStr
    
    @validator('plano')
    def validate_plano(cls, value):
        planos = client.get_produtos()
        planos = [plano[0] for plano in planos]

        if value.upper() not in planos:
            raise ValueError(f"Não existe nenhum plano na base de dados chamado {value}.")

    @validator('consultor')
    def validate_consultor(cls, value):
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
            value = datetime.strptime('%d-%m-%Y')
        except:
            raise ValueError("Formato de data inválido, por favor informe a data no formato %d-%m-%Y")

        return value

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
    