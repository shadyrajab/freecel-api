from pydantic import BaseModel
from typing import Optional

class ConsultorModel(BaseModel):
    nome: str

class TokenModel(BaseModel):
    uuid: str

class VendaModel(BaseModel):
    cnpj: str
    telefone: int
    consultor: str
    data: str
    gestor: str
    plano: str
    quantidade_de_produtos: str
    revenda: str
    tipo: str
    uf: str
    valor_acumulado: str
    valor_do_plano: str
    email: Optional[str] = None

class ProdutoModel(BaseModel):
    nome: str
    preco: float

class IdentifyModel(BaseModel):
    id: int