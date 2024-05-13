from typing import Optional

from pydantic import BaseModel, Field

from .abastract.venda_params import UpdateVendaParams


class UpdateProdutoParams(BaseModel):
    id: int = Field(description="ID do Produto")
    nome: Optional[str] = Field(None, description="Nome do Produto")
    preco: Optional[float] = Field(None, description="Preço do produto")


class UpdateVendaMovelParams(UpdateVendaParams):
    data_ativacao: Optional[str] = Field(None, description="Data da Ativação")
    data_entrega: Optional[str] = Field(None, description="Data de Entrega")
    historico: Optional[str] = Field(None, description="Histórico")
    qtd_aparelho: Optional[int] = Field(None, description="Quantidade de aparelhos")
    valor_aparelho: Optional[float] = Field(None, description="Valor do aparelho")
    pacote_inovacao: Optional[str] = Field(None, description="Pacote de Inovação")
    qtd_inovacao: Optional[int] = Field(None, description="Quantidade de Inovação")
    valor_inovacao: Optional[float] = Field(None, description="Valor da Inovação")
    valor_atual: Optional[float] = Field(None, description="Valor Atual")
    valor_renovacao: Optional[float] = Field(None, description="Valor da Renovação")
    pacote_inovacao: Optional[str] = Field(None, description="Pacote Inovação")
    qtd_renovacao: Optional[int] = Field(None, description="Volume Inovação")
    m: Optional[int] = Field(None, description="Valor de M")
    tipo_m: Optional[str] = Field(None, description="O tipo de M")
    volume_migracao: Optional[int] = Field(None, description="Quantidade de Migração")
    ov: Optional[int] = Field(None, description="Ov da Venda") 
    responsavel_input: Optional[str] = Field(None, description="Responsável pelo Input")


class UpdateVendaFixaParams(UpdateVendaParams):
    base_movel: Optional[bool] = Field(None, description="Se faz parte da base móvel")
    campanha: Optional[str] = Field(None, description="Campanha")
    cep: Optional[str] = Field(None, description="CEP")
    data_conclusao: Optional[str] = Field(None, description="Data de Conclusão")
    data_instalacao: Optional[str] = Field(None, description="Data de Instalação")
    instancia: Optional[str] = Field(None, description="Data de Instância")
    internet_mbps: Optional[int] = Field(None, description="Banda Larga")
    linhas: Optional[int] = Field(None, description="Quantidade de Linhas")


class UpdateConsultorParams(BaseModel):
    id: int = Field(description="ID do Consultor")
    nome: Optional[str] = Field(None, description="Nome do Consultor")
    vinculo: Optional[str] = Field(None, description="Tipo de Vínculo")
    cargo: Optional[str] = Field(None, description="Cargo do Consultor")
