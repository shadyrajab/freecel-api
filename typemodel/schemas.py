from pydantic import BaseModel
from typing import Optional
from .responses import VendaModel

class ProdutoSchema(BaseModel):
    nome: str
    preco: float

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
