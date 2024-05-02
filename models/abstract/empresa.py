from pydantic import BaseModel


class EmpresaRequestModel(BaseModel):
    razao_social: str
    porte: str
    regime_tributario: str
    capital_social: float
    natureza_juridica: str
    matriz: str
    municipio: str
    faturamento: str
    cnae: str
    uf: str
    quadro_funcionarios: str
    data_abertura: str
