from datetime import datetime

from pydantic import validator

from .abstract.venda import VendaRequestModel


class VendaMovelRequestModel(VendaRequestModel):
    data_ativacao: str
    ov: int
    qtd_aparelho: int
    valor_aparelho: float
    m: int
    tipo_m: str
    valor_atual: float
    valor_renovacao: float
    pacote_inovacao: str
    qtd_inovacao: int
    valor_inovacao: float

    @validator("data_ativacao")
    def validate_data_ativacao(cls, data_ativacao) -> datetime:
        # Erro potencial
        data_ativacao = datetime.strptime(data_ativacao, "%d-%m-%Y")
        return data_ativacao

    @validator("tipo_m")
    def validate_tipo_m(cls, tipo_m) -> str:
        tipo_m = tipo_m.upper()
        if tipo_m not in ["PADRÃO", "UP", "DOWN"]:
            raise ValueError(f"O tipo de M {tipo_m} não existe.")

        return tipo_m
