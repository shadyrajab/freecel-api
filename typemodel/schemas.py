from pydantic import BaseModel
from typing import Optional, List, Dict
from .base_model import VendaModel

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

class Consultor(BaseModel):
    name: str
    receita_total: float
    quantidade_vendida: int
    quantidade_clientes: int
    receita_media_diaria: float
    quantidade_media_diaria: float
    quantidade_media_mensal: int
    receita_media_mensal: float
    ticket_medio: float
    delta_receita_mensal: Optional[float] = None
    delta_quantidade_mensal: Optional[float] = None
    delta_quantidade_clientes: Optional[float] = None
    vendas: List[VendaSchema]

class Stats(BaseModel):
    receita_total: float
    quantidade_vendida: int
    quantidade_clientes: int
    ticket_medio: float
    receita_media_diaria: float
    media_por_consultor: float
    maior_venda_mes: float
    delta_receita_total: Optional[float] = None
    delta_quantidade_produtos: Optional[int] = None
    delta_quantidade_clientes: Optional[int] = None
    quantidade_clientes: Optional[int] = None
    delta_ticket_medio: Optional[float] = None
    delta_media_diaria: Optional[float] = None
    delta_media_por_consultor: Optional[float] = None
    consultor_do_mes: Optional[Consultor] = None
    qtd_vendas_por_cnae: dict
    qtd_vendas_por_faturamento: dict
    qtd_vendas_por_colaboradores: dict
    qtd_vendas_por_uf: dict
    ufs: list
    tipo_venda: list

# class 