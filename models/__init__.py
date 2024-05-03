from .module.aparelho import TrocaAparelhoRequestModel
from .module.consultor import Vendedor
from .module.fixa import VendaFixaRequestModel
from .module.identify import ID
from .module.inovacao import InovacaoRequestModel
from .module.migracao import MigracaoRequestModel
from .module.movel import VendaMovelRequestModel
from .module.produtos import Produto

__all__ = [
    TrocaAparelhoRequestModel,
    Vendedor,
    VendaFixaRequestModel,
    ID,
    InovacaoRequestModel,
    MigracaoRequestModel,
    VendaMovelRequestModel,
    Produto,
]
