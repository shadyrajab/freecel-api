from typing import Optional

from pydantic import BaseModel, EmailStr, Field


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
    n_pedido: Optional[str] = Field(None, description="Número do Pedido")
    equipe: Optional[str] = Field(None, description="O nome da equipe")
    adabas: Optional[str] = Field(None, description="ADABAS da venda")
    data_input: Optional[str] = Field(None, description="Data de Input")