from pydantic import BaseModel, EmailStr, validator, ValidationError
from pycpfcnpj import cpfcnpj
from utils.variables import TIPO_VENDA, EQUIPE, UF
from math import ceil
from datetime import datetime
import re

class Venda(BaseModel):
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

    @validator('gestor')
    def validate_gestor(cls, value):
        if re.search(r'\d', value):
            raise ValidationError("O nome do gestor não deve conter caracteres numéricos.")
        
        return value

    @validator('telefone')
    def validate_telefone(cls, value):
        telefone = re.sub(r'[^0-9]', '', value)
        if len(telefone) != 11:
            raise ValidationError("""
                O número de telefone informado está inválido. Informe o número DDD e os 9 dígitos 
                do telefone
            """)
        
        return telefone

    @validator('preco')
    def validate_preco(cls, value):
        if value < 1:
            raise ValidationError("O preço do produto não pode ser menor do que 1")
        
        return value

    @validator('data')
    def validate_data(cls, value):
        try:
            value = datetime.strptime(value, '%Y-%m-%d')
            date = datetime.strftime(date, '%d-%m-%Y')
        except:
            raise ValidationError("Formato de data inválido, por favor informe a data no formato %d-%m-%Y")

        return date

    @validator('uf')
    def validate_uf(cls, value):
        if value.upper() not in UF:
            raise ValidationError("A UF informada não existe.")
        
        return value.upper()

    @validator('equipe')
    def validate_equipe(cls, value):
        if value.upper() not in EQUIPE:
            raise ValidationError(f"""
                O nome da equipe informado está inválido. O nome da equipe deve ser FREECEL,
                VALPARAISO, PARCEIRO ou ESCRITORIO, não {value}
            """)
        
        return value.upper()

    @validator('volume')
    def validate_volume(cls, value):
        if value < 1: 
            raise ValidationError(f"O Volume da venda não pode ser menor do que 1.")
        
        return ceil(value)

    @validator('tipo')
    def validate_tipo(cls, value):
        if value.upper() not in TIPO_VENDA:
            raise ValidationError(f"""
                O tipo de venda informado está inválido. O tipo deve ser FIXA, AVANÇADA, 
                MIGRAÇÃO-PRÉ-PÓS, VVN ou ALTAS, não {value}
            """)
        
        return value.upper()
    
    @validator('cnpj')
    def validate_cnpj(cls, value):
        cnpj = re.sub(r'[^0-9]', '', value)
        if not cpfcnpj.validate(cnpj):
            raise ValidationError(f"O CNPJ ou CPF informado está inválido.")
        
        return cnpj