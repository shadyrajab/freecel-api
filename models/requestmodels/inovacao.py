from .abstract.vendas import VendaRequestModel


class InovacaoRequestModel(VendaRequestModel):
    pacote_inovacao: str
    qtd_inovacao: int
    valor_inovacao: float
