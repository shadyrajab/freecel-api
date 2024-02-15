from pydantic import BaseModel

class ConsultorModel(BaseModel):
    nome: str

class TokenModel(BaseModel):
    uuid: str

class VendaModel(BaseModel):
    cnpj: str
    cod_cnae: str
    colaboradores: str
    consultor: str
    data: str
    faturamento: str
    gestor: str
    nome_cnae: str
    plano: str
    quantidade_de_produtos: str
    revenda: str
    tipo: str
    uf: str
    valor_acumulado: str
    valor_do_plano: str

class ProdutoModel(BaseModel):
    nome: str
    preco: float