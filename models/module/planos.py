from typing import Dict

from pydantic import BaseModel, validator


class Plano(BaseModel):
    plano: str
    preco: float

    @validator("preco")
    def validate_preco(cls, value):
        if value < 1:
            raise ValueError("O valor do plano não pode ser menor do que 1.")

        return value

    def to_dict(self) -> Dict:
        params = dict(self.__dict__.items())
        return params
