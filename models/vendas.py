import re
from datetime import datetime
from math import ceil
from typing import Optional

from pycpfcnpj import cpfcnpj
from pydantic import BaseModel, EmailStr, validator

from client.client import Client
from utils.variables import DDDS, EQUIPE, STATUS_VENDA, TIPO_VENDA


class Venda(BaseModel):
    cnpj: str
    telefone: str
    consultor: str
    data: str
    gestor: str
    preco: Optional[float] = None
    plano: str
    volume: int
    equipe: str
    tipo: str
    ja_cliente: bool
    email: EmailStr
    ddd: str
    status: str
    numero_pedido: str

    @validator("ddd")
    def validate_ddd(cls, value):
        if value not in DDDS:
            raise ValueError(f"O DDD {value} não existe")

        return value

    @validator("status")
    def validate_status(cls, value):
        if value.upper() not in STATUS_VENDA:
            raise ValueError(f"Não existe nenhum status chamado {value}")

        return value.upper()

    # @validator("consultor")
    # async def validate_consultor(cls, value):
    #     async with Client() as client:
    #         consultores = await client.get_consultores()
    #         consultores = [consultor[0] for consultor in consultores]

    #         if value.upper() not in consultores:
    #             raise ValueError(
    #                 f"Não existe nenhum consultor na base de dados chamado {value}."
    #             )

    #     return value.upper()

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
                do telefone
            """
            )

        return telefone

    @validator("data")
    def validate_data(cls, value):
        value = datetime.strptime(value, "%d-%m-%Y")
        return value

    @validator("equipe")
    def validate_equipe(cls, value):
        if value.upper() not in EQUIPE:
            raise ValueError(
                f"""
                O nome da equipe informado está inválido. O nome da equipe deve ser {str(EQUIPE)}, não {value}
            """
            )

        return value.upper()

    @validator("volume")
    def validate_volume(cls, value):
        if value < 1:
            raise ValueError(f"O Volume da venda não pode ser menor do que 1.")

        return ceil(value)

    @validator("tipo")
    def validate_tipo(cls, value):
        if value.upper() not in TIPO_VENDA:
            raise ValueError(
                f"""
                O tipo de venda informado está inválido. O tipo deve ser {str(EQUIPE)}, não {value}
            """
            )

        return value.upper()

    @validator("cnpj")
    def validate_cnpj(cls, value):
        cnpj = re.sub(r"[^0-9]", "", value)
        if not cpfcnpj.validate(cnpj):
            raise ValueError(f"O CNPJ ou CPF informado está inválido.")

        return cnpj

    # @validator("plano")
    # async def validate_plano(cls, value, values):
    #     if int(values.get("preco")) != 0:
    #         return value

    #     async with Client() as client:
    #         planos = await client.get_produtos()
    #         planos = [plano[0] for plano in planos]

    #         if value.upper() not in planos:
    #             raise ValueError(
    #                 f"Não existe nenhum plano na base de dados chamado {value}."
    #             )

    #     return value.upper()
