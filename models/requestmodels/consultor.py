from pydantic import BaseModel, validator

from utils.variables import CARGOS
from utils.utils import EQUIPES


class Vendedor(BaseModel):
    name: str
    vinculo: str
    cargo: str

    @validator("vinculo")
    def validate_vinculo(cls, value):
        if value not in EQUIPES:
            raise ValueError(f"A equipe {value} não existe")

        return value.upper()

    @validator("cargo")
    def validate_cargo(cls, value):
        if value not in CARGOS:
            raise ValueError(f"O cargo {value} não existe")

        return value.upper()
