from pydantic import BaseModel
from typing import Optional
from .base_model import VendaModel

class ProdutoSchema(BaseModel):
    nome: str
    preco: float

class CNPJStats(BaseModel):
    quadro_funcionarios: str
    faturamento: str
    cnae: str
    cep: str
    municipio: str
    porte: str
    capital_social: str
    natureza_juridica: str
    matriz: str
    situacao_cadastral: str
    regime_tributario: str
    bairro: str

class VendaSchema(VendaModel):
    quadro_funcionarios: Optional[str] = None
    faturamento: Optional[str] = None
    cnae: Optional[str] = None
    cep: Optional[str] = None
    municipio: Optional[str] = None
    porte: Optional[str] = None
    capital_social: Optional[str] = None
    natureza_juridica: Optional[str] = None
    matriz: Optional[str] = None
    situacao_cadastral: Optional[str] = None
    regime_tributario: Optional[str] = None
    bairro: Optional[str] = None