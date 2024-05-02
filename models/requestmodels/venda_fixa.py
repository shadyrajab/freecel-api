# from pycpfcnpj import cpfcnpj
# from pydantic import BaseModel, EmailStr, validator


# class VendaFixaModel(BaseModel):
#     campanha: str
#     cep: int
#     tipo_cliente: str
#     cnpj: str
#     consultor: str
#     data: str
#     data_conclusao: str
#     data_instalacao: str
#     ddd: str
#     email: EmailStr
#     equipe: str
#     internet_mbps: int
#     linhas: int
#     plano: str
#     preco: float
#     status: str
#     telefone: str
#     tipo: str
#     uf: str
#     volume: int
#     numero_pedido: str

#     @validator
#     def validate_campanha(cls, campanha: str):
#         campanha = campanha.upper()
#         if campanha not in {"MASSIVO", "TOP"}:
#             raise ValueError(f"A campanha {campanha} não existe.")

#         return campanha

#     @validator
#     def validate_cep(cls, cep: int):
#         if len(str(cep) > 8):
#             raise ValueError(f"O CEP deve ter no máximo 8 dígitos.")

#         return cep

#     @validator
#     def tipo_cliente(cls, tipo_cliente: str):
