from requests import request

from utils.variables import TOKENEMPRESAS


class Empresa:
    def __init__(self, cnpj: str):
        self.empresa = self.__get_empresa(cnpj)

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
        return self.empresa.get("log_bairro", None)

    @property
    def regime_tributario(self):
        return self.empresa.get("regime_tributario", None)

    @property
    def capital_social(self):
        return self.empresa.get("capital_social", None)

    @property
    def natureza_juridica(self):
        return self.empresa.get("natureza_juridica", None)

    @property
    def matriz(self):
        matriz = {"0": None, "1": "MATRIZ", "2": "FILIAL"}.get(
            self.empresa.get("matriz", "0")
        )
        return matriz

    @property
    def municipio(self):
        return self.empresa.get("log_municipio", None)

    @property
    def faturamento(self):
        return self.empresa.get("faturamento", None)

    @property
    def cnae(self):
        return self.empresa.get("cnae_principal", None)

    @property
    def cep(self):
        return self.empresa.get("log_cep", None)

    @property
    def uf(self):
        return self.empresa.get("log_uf", None)

    @property
    def quadro_funcionarios(self):
        return self.empresa.get("quadro_funcionarios", None)

    @property
    def data_abertura(self):
        return self.empresa.get("data_empresa", None)

    def __get_empresa(self, cnpj: str):
        url = f"https://www.empresaqui.com.br/api/{TOKENEMPRESAS}/{cnpj}"
        response = request("GET", url=url)
        if response.status_code == 200 and response.text:
            return response.json()

        return {}
