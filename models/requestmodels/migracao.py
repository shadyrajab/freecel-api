from .abstract.vendas import VendaRequestModel


class MigracaoRequestModel(VendaRequestModel):
    m: int
    tipo_m: str
    valor_atual: float
    valor_inovacao: float
    volume_migracao: int
