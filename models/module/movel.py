from datetime import datetime
from typing import Optional

from pydantic import validator

from .abstract.venda import VendaRequestModel


class VendaMovelRequestModel(VendaRequestModel):
    data_ativacao: Optional[str] = None
    ov: Optional[int] = None
    qtd_aparelho: Optional[int] = None
    valor_aparelho: Optional[float] = None
    m: Optional[list] = None
    valor_atual: Optional[float] = None
    valor_renovacao: Optional[float] = None
    pacote_inovacao: Optional[str] = None
    qtd_inovacao: Optional[int] = None
    valor_inovacao: Optional[float] = None
    responsavel_input: Optional[str] = None

    @validator("data_ativacao")
    def validate_data_ativacao(cls, data_ativacao) -> datetime:
        # Erro potencial
        if data_ativacao is None:
            return data_ativacao
        data_ativacao = datetime.strptime(data_ativacao, "%d-%m-%Y")
        return data_ativacao
