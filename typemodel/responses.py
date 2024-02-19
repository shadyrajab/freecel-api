from pydantic import BaseModel
from typing import Optional

class ConsultorModel(BaseModel):
    nome: str

class TokenModel(BaseModel):
    uuid: str

class VendaModel(BaseModel):
    cnpj: str
    telefone: str
    consultor: str
    data: str
    gestor: str
    plano: str
    quantidade_de_produtos: int
    revenda: str
    tipo: str
    uf: str
    valor_do_plano: float
    email: str

class ProdutoModel(BaseModel):
    nome: str
    preco: float

class IdentifyModel(BaseModel):
    id: int