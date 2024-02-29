from pydantic import BaseModel, validator

class ProdutoSchema(BaseModel):
    nome: str
    preco: float

    @validator('preco')
    def validate_preco(cls, value):
        if value < 1:
            raise ValueError("O valor do plano não pode ser menor do que 1.")

        return value
    