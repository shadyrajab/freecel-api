import re
from datetime import datetime
from typing import Dict, Optional

from pycpfcnpj import cpfcnpj
from pydantic import EmailStr, validator

from empresas.empresas_aqui import Empresa
from utils.utils import (
    EQUIPES,
    STATUS_FIXA,
    STATUS_MOVEL,
    TIPOS_FIXA,
    TIPOS_MIGRACAO,
    TIPOS_MOVEL,
)
from utils.variables import DDDS


class VendaRequestModel(Empresa):
    telefone: str
    consultor: str
    data: str
    gestor: str
    preco: Optional[float] = None
    plano: str
    volume: int
    equipe: str
    tipo: str
    email: EmailStr
    ddd: str
    status: str
    numero_pedido: str
    uf: str

    @validator("ddd")
    def validate_ddd(cls, value):
        if value not in DDDS:
            raise ValueError(f"O DDD {value} não existe")

        return value

    @validator("gestor")
    def validate_gestor(cls, value):
        if re.search(r"\d", value):
            raise ValueError("O nome do gestor não deve conter caracteres numéricos.")

        return value

    @validator("telefone")
    def validate_telefone(cls, value):
        telefone = re.sub(r"[^0-9]", "", value)
        if len(telefone) != 11 or telefone[0:2] not in DDDS:
            raise ValueError(
                """
                O número de telefone informado está inválido. Informe o número DDD e os 9 dígitos 
                do telefone.
            """
            )

        return telefone

    @validator("data")
    def validate_data(cls, value):
        # Erro potencial
        value = datetime.strptime(value, "%d-%m-%Y")
        return value

    @validator("equipe")
    def validate_equipe(cls, value):
        if value.upper() not in EQUIPES:
            raise ValueError(f"A equipe {value} não existe")

        return value.upper()

    @validator("tipo")
    def validate_tipo(cls, value):
        if value.upper() not in TIPOS_MOVEL + TIPOS_FIXA + TIPOS_MIGRACAO:
            raise ValueError(f"Não existe nenhum tipo chamado {value}")

        return value.upper()

    @validator("status")
    def validate_status(cls, value):
        if value.upper() not in STATUS_MOVEL + STATUS_FIXA:
            raise ValueError(f"Não existe nenhum status chamado {value}")

        return value.upper()

    @validator("cnpj")
    def validate_cnpj(cls, value):
        cnpj = re.sub(r"[^0-9]", "", value)
        if not cpfcnpj.validate(cnpj):
            raise ValueError(f"O CNPJ ou CPF informado está inválido.")

        return cnpj

    def to_dict(self) -> Dict:
        params = dict(self.__dict__.items())
        for cls in reversed(self.__class__.__mro__):
            for attr_name, attr_value in vars(cls).items():
                if isinstance(attr_value, property):
                    params[attr_name] = getattr(self, attr_name)

        for param in [
            "model_extra",
            "model_fields_set",
            "empresa",
            "__fields__",
            "__fields_set__",
        ]:
            del params[param]

        return params
