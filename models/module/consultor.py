from typing import Dict

from pydantic import BaseModel, validator

from utils.utils import EQUIPES
from utils.variables import CARGOS


class Vendedor(BaseModel):
    name: str
    vinculo: str
    cargo: str

    @validator("vinculo")
    def validate_vinculo(cls, value: str):
        if value not in EQUIPES:
            raise ValueError(f"A equipe {value} não existe")

        return value.upper()

    @validator("cargo")
    def validate_cargo(cls, value: str):
        if value not in CARGOS:
            raise ValueError(f"O cargo {value} não existe")

        return value.upper()

    def to_dict(self) -> Dict:
        params = dict(self.__dict__.items())
        return params
