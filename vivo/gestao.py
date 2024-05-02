import threading
from datetime import datetime, time

import pandas as pd
import requests

from utils.env import PAYLOAD


class VivoGestaoChamadas:
    def __init__(self, data_inicio: str, data_fim: str, consultores: pd.DataFrame):
        self.data_inicio = datetime.strptime(data_inicio, "%d-%m-%Y")
        self.data_fim = datetime.strptime(data_fim, "%d-%m-%Y")
        self.session_id, self.remote_ip = self.__login_vivo_gestao()
        self.consultores = consultores

        self.threads = []
        self.records = []

        self.__create_threads()
        self.__run_threads()

    def __login_vivo_gestao(self):
        URL = "https://vivogestao.vivoempresas.com.br/Portal/api/datapackcompanyinfo"
        response = requests.post(URL, json=PAYLOAD)
        data = response.json()
        return data["sessionId"], data["remoteIp"]

    def __create_threads(self):
        start_date = (
            int(datetime.combine(self.data_inicio, time.min).timestamp()) * 1000
        )
        end_date = int(datetime.combine(self.data_fim, time.max).timestamp()) * 1000 - 1
        for _index, row in self.consultores.iterrows():
            telefone = row["telefone"]
            consultor = row["nome"]
            URL = f"https://vivogestao.vivoempresas.com.br/Portal/api/voicereports?action=getCallHistory&msisdn={telefone}&startDate={start_date}&endDate={end_date}&startRow=1&fetchSize=50&sessionId={self.session_id}&remoteHost=gateway&remoteIp={self.remote_ip}&acessLogin=santosegomes"

            thread = threading.Thread(
                target=self.__get_total_record_count,
                args=(
                    URL,
                    consultor,
                    telefone,
                ),
            )

            thread.start()
            self.threads.append(thread)

    def __run_threads(self):
        for thread in self.threads:
            thread.join()

    def __get_total_record_count(self, url: str, consultor: str, telefone: str):
        response = requests.get(url)
        data = response.json()
        result = {
            "CONSULTOR": consultor,
            "TELEFONE": telefone,
            "CHAMADAS": data["totalRecordCount"],
        }

        self.records.append(result)
