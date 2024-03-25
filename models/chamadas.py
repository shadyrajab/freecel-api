from datetime import datetime

from pydantic import BaseModel, validator


class Chamada(BaseModel):
    consultor: str
    telefone: str
    quantidade: int
    data: str

    @validator("data")
    def validate_data(cls, value):
        value = datetime.strptime(value, "%d-%m-%Y")
        return value
