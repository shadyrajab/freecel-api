from typing import Optional

from .abstract.venda import VendaRequestModel


class MigracaoRequestModel(VendaRequestModel):
    m: Optional[int] = 1
    tipo_m: str
    valor_atual: float
    valor_renovacao: float
