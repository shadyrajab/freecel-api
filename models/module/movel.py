from datetime import datetime

from pydantic import validator

from ..abstract.venda import VendaRequestModel


class VendaMovelRequestModel(VendaRequestModel):
    data_ativacao: str
    ov: int

    @validator("data_ativacao")
    def validate_data_ativacao(cls, data_ativacao) -> datetime:
        # Erro potencial
        data_ativacao = datetime.strptime(data_ativacao, "%d-%m-%Y")
        return data_ativacao
