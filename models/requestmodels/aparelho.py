from .abstract.vendas import VendaRequestModel


class TrocaAparelhoRequestModel(VendaRequestModel):
    qtd_aparelho: int
    valor_aparelho: float
