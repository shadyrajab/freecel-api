from datetime import datetime

from pydantic import BaseModel, validator
from requests import request

from utils.env import TOKENEMPRESAS


class Empresa(BaseModel):
    cnpj: str
    empresa: dict = {}

    def __init__(self, cnpj: str, **kwargs):
        super().__init__(cnpj=cnpj, **kwargs)
        cnpj = cnpj.replace('-', '').replace('/', '').replace('.', '')
        self.empresa = self.__get_empresa(cnpj)

    @property
    def razao_social(self):
        return self.empresa.get("razao")

    @property
    def porte(self):
        porte = {
            "0": None,
            "1": "MICROEMPRESA",
            "3": "PEQUENO PORTE",
            "5": "MÉDIO/GRANDE PORTE",
        }.get(self.empresa.get("porte", "0"))
        return porte

    @property
    def bairro(self):
        log_bairro = self.empresa.get("log_bairro")
        if log_bairro is not None:
            log_bairro = log_bairro.replace("'", "")

        return log_bairro

    @property
    def regime_tributario(self):
        return self.empresa.get("regime_tributario")

    @property
    def capital_social(self):
        return self.empresa.get("capital_social")

    @property
    def natureza_juridica(self):
        return self.empresa.get("natureza_juridica")

    @property
    def matriz(self):
        matriz = {"0": None, "1": "MATRIZ", "2": "FILIAL"}.get(
            self.empresa.get("matriz", "0")
        )
        return matriz

    @property
    def municipio(self):
        log_municipio = self.empresa.get("log_municipio")
        if log_municipio is not None:
            log_municipio = log_municipio.replace("'", "")

        return log_municipio

    @property
    def faturamento(self):
        return self.empresa.get("faturamento")

    @property
    def cnae(self):
        return self.empresa.get("cnae_principal")

    @property
    def uf(self):
        return self.empresa.get("log_uf")

    @property
    def quadro_funcionarios(self):
        return self.empresa.get("quadro_funcionarios")

    @property
    def data_abertura(self):
        data_abertura = self.empresa.get("data_abertura")
        if data_abertura is not None:
            data_abertura = datetime.strptime(data_abertura, "%Y%m%d")

        return data_abertura

    def __get_empresa(self, cnpj: str):
        url = f"https://www.empresaqui.com.br/api/{TOKENEMPRESAS}/{cnpj}"
        response = request("GET", url=url)
        print(response.json())
        if response.status_code == 200 and response.text:
            return response.json()

        return {}
