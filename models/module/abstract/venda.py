import re
from datetime import datetime
from typing import Dict, Optional

from pycpfcnpj import cpfcnpj
from pydantic import EmailStr, validator

from empresas.empresas_aqui import Empresa
from utils.utils import ESTEIRA, STATUS_FIXA, STATUS_MOVEL, TIPOS_FIXA, TIPOS_MOVEL
from utils.variables import DDDS


class VendaRequestModel(Empresa):
    telefone: str
    consultor: str
    data_input: Optional[str] = None
    data_recebimento: Optional[str] = datetime.now().strftime("%d-%m-%Y")
    gestor: str
    plano: str
    volume: int
    tipo: str
    esteira: Optional[str] = "MÓVEL"
    email: EmailStr
    ddd: str
    status: str
    n_pedido: Optional[str] = ''
    observacao: Optional[str] = None
    adabas: str
    m: Optional[list] = []

    @validator("esteira")
    def validate_esteira(cls, esteira: str):
        esteira = esteira.upper()
        if esteira not in ESTEIRA:
            raise ValueError(f"A esteira {esteira} não existe")

        return esteira

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

    # @validator("telefone")
    # def validate_telefone(cls, value):
    #     telefone = re.sub(r"[^0-9]", "", value)
    #     if len(telefone) != 11 or telefone[0:2] not in DDDS:
    #         raise ValueError(
    #             """
    #             O número de telefone informado está inválido. Informe o número DDD e os 9 dígitos 
    #             do telefone.
    #         """
    #         )

    #     return telefone

    @validator("data_input")
    def validate_data_input(cls, value):
        value = datetime.strptime(value, "%d-%m-%Y")
        return value

    @validator("data_recebimento")
    def validate_data_recebimento(cls, value):
        # Erro potencial
        if isinstance(value, str):
            value = datetime.strptime(value, "%d-%m-%Y")

        return value

    @validator("tipo")
    def validate_tipo(cls, value):
        if value.upper() not in TIPOS_MOVEL + TIPOS_FIXA:
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
