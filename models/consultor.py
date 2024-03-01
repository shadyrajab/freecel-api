from pydantic import BaseModel
from typing import List, Optional
from models.vendas import Venda

class Consultor(BaseModel):
    name: str
    receita: float
    volume: int
    clientes: int
    receita_media_diaria: float
    receita_media_mensal: float
    volume_medio_diaria: int
    volume_medio_mensal: int
    ticket_medio: float
    delta_receita_mensal: Optional[float] = None
    delta_quantidade_mensal: Optional[float] = None
    delta_quantidade_clientes: Optional[float] = None
    vendas: List[Venda]