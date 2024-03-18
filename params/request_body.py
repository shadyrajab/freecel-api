from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class UpdateProdutoParams(BaseModel):
    id: int = Field(description="ID do Produto")
    nome: Optional[str] = Field(None, description="Nome do Produto")
    preco: Optional[float] = Field(None, description="Preço do produto")


class UpdateMigracaoParams(BaseModel):
    id: int = Field(description="ID do Produto")
    valor_atual: Optional[float] = Field(None, description="Valor Atual")
    valor_renovacao: Optional[float] = Field(None, description="Valor da Renovação")
    valor_inovacao: Optional[float] = Field(None, description="Valor da Inovação")
    pacote_inovacao: Optional[str] = Field(None, description="Pacote Inovação")
    volume_inovacao: Optional[int] = Field(None, description="Volume Inovação")


class UpdateVendaParams(BaseModel):
    id: int = Field(description="ID do Produto")
    cnpj: Optional[str] = Field(None, description="CNPJ do Cliente")
    consultor: Optional[str] = Field(None, description="Nome do Consultor")
    telefone: Optional[str] = Field(None, description="Telefone do Cliente")
    plano: Optional[str] = Field(None, description="Plano Comprado")
    gestor: Optional[str] = Field(None, description="Nome do Gestor")
    tipo: Optional[str] = Field(None, description="Tipo da Venda")
    status: Optional[str] = Field(None, description="Status da Venda")
    email: Optional[EmailStr] = Field(None, description="Email do Cliente")
    ja_cliente: Optional[bool] = Field(None, description="Já Cliente?")
    numero_pedido: Optional[str] = Field(None, description="Número do Pedido")
    equipe: Optional[str] = Field(None, description="O nome da equipe")


class UpdateConsultorParams(BaseModel):
    id: int = Field(description="ID do Consultor")
    nome: Optional[str] = Field(None, description="Nome do Consultor")
    vinculo: Optional[str] = Field(None, description="Tipo de Vínculo")
    cargo: Optional[str] = Field(None, description="Cargo do Consultor")
