from datetime import datetime

from pydantic import validator

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

    @validator("campanha")
    def validate_campanha(cls, campanha) -> str:
        campanha = campanha.upper()
        if campanha not in {"MASSIVO", "TOP"}:
            raise ValueError("A campanha informada não existe")
        
        return campanha

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
