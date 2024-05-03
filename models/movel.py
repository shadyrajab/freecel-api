from datetime import datetime

from pydantic import validator

from .abstract.venda import VendaRequestModel


class VendaMovelRequestModel(VendaRequestModel):
    data_ativacao: str
    data_entrega: str
    historico: str

    @validator("data_ativacao")
    def validate_data_ativacao(cls, data_ativacao) -> datetime:
        # Erro potencial
        data_ativacao = datetime.strptime(data_ativacao, "%d-%m-%Y")
        return data_ativacao

    @validator("data_entrega")
    def validate_data_entrega(cls, data_entrega) -> datetime:
        # Erro potencial
        data_entrega = datetime.strptime(data_entrega, "%d-%m-%Y")
        return data_entrega
