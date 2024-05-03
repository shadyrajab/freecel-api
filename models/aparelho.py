from typing import Dict

from .abstract.venda import VendaRequestModel


class TrocaAparelhoRequestModel(VendaRequestModel):
    qtd_aparelho: int
    valor_aparelho: float
