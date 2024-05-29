from datetime import datetime, time

import pandas as pd
import requests

from utils.env import PAYLOAD
from utils.functions import jsonfy

LOGIN_URL = "https://vivogestao.vivoempresas.com.br/Portal/api/datapackcompanyinfo"
RELATORIO_URL = (
    "https://vivogestao.vivoempresas.com.br/Portal/api/voicereports?"
    "action=getCallHistory&msisdn={telefone}&startDate={startDate}&endDate={endDate}"
    "&startRow=1&fetchSize=10000&sessionId={sessionId}&remoteHost=gateway"
    "&remoteIp={remoteIp}&acessLogin=santosegomes"
)


class VivoGestaoChamadas:
    def __init__(self, data_inicio: str, data_fim: str, telefone: str, consultor: str):
        data_inicio = datetime.strptime(data_inicio, "%d-%m-%Y")
        data_fim = datetime.strptime(data_fim, "%d-%m-%Y")

        self.start_date = int(
            datetime.combine(data_inicio, time.min).timestamp() * 1000
        )
        self.end_date = int(datetime.combine(data_fim, time.max).timestamp() * 1000 - 1)

        self.session_id, self.remote_ip = self.__login_vivo_gestao()
        self.telefone = telefone
        self.consultor = consultor

        self.records = self.__get_records()

    def __login_vivo_gestao(self):
        URL = "https://vivogestao.vivoempresas.com.br/Portal/api/datapackcompanyinfo"
        response = requests.post(URL, json=PAYLOAD)
        data = response.json()
        return data["sessionId"], data["remoteIp"]

    def __get_records(self):
        url = RELATORIO_URL.format(
            telefone=self.telefone,
            startDate=self.start_date,
            endDate=self.end_date,
            sessionId=self.session_id,
            remoteIp=self.remote_ip,
        )
        response = requests.get(url)
        result = pd.DataFrame(response.json()['result'])

        result["Consultor"] = self.consultor
        result["Telefone"] = self.telefone

        return jsonfy(result)
