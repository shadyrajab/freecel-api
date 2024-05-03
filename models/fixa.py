from datetime import datetime

from pydantic import validator

from utils.utils import TIPOS_CLIENTE

from .abstract.venda import VendaRequestModel


class VendaFixaRequestModel(VendaRequestModel):
    base_movel: bool
    campanha: str
    cep: int
    data_conclusao: str
    data_instalacao: str
    instancia: str
    internet_mbps: int
    linhas: int
    endereco: str
    tipo_cliente: str

    @validator("tipo_cliente")
    def validate_tipo_cliente(cls, tipo_cliente) -> str:
        tipo_cliente = tipo_cliente.upper()
        if tipo_cliente not in TIPOS_CLIENTE:
            raise ValueError("O tipo de cliente informado não existe.")

        return tipo_cliente

    @validator("data_conclusao")
    def validate_data_conclusao(cls, data_conclusao) -> datetime:
        # Erro potencial
        data_conclusao = datetime.strptime(data_conclusao, "%d-%m-%Y")
        return data_conclusao

    @validator("data_instalacao")
    def validate_data_instalacao(cls, data_instalacao) -> datetime:
        # Erro potencial
        data_instalacao = datetime.strptime(data_instalacao, "%d-%m-%Y")
        return data_instalacao
