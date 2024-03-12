from structures.stats import Stats
import pandas as pd
from typing import Optional, List, Self
from utils.functions import filter_by

class Freecel(Stats):
    def __init__(self, dataframe: pd.DataFrame, ano: Optional[int] = None, mes: Optional[str] = None, jsonfy: Optional[bool] = None, prev_freecel: Optional[bool] = None) -> None:
        self.full_dataframe = dataframe
        self.jsonfy = jsonfy
        self.ano = ano
        self.mes = mes.capitalize() if mes else mes
        self.dataframe = filter_by(dataframe, ano=ano, mes=mes)

        super().__init__(self.full_dataframe, ano, mes, True)

        if prev_freecel == True:
            self.prev_freecel = self.__get_prev_freecel()

    @property
    def media_consultor_geral(self) -> float:
        return self.__media_por_consultor()
    
    @property
    def media_consultor_altas(self) -> float:
        return self.__media_por_consultor('ALTAS')
    
    @property
    def media_consultor_migracao(self) -> float:
        return self.__media_por_consultor('MIGRAÇÃO PRÉ-PÓS')
    
    @property
    def media_consultor_fixa(self) -> float:
        return self.__media_por_consultor('FIXA')
    
    @property
    def media_consultor_avancada(self) -> float:
        return self.__media_por_consultor('AVANÇADA')
    
    @property
    def media_consultor_portabilidade(self) -> float:
        return self.__media_por_consultor('PORTABILIDADE')
    
    @property
    def media_consultor_vvn(self) -> float:
        return self.__media_por_consultor('VVN')
    
    @property
    def delta_media_consultor_geral(self) -> float:
        return self.calculate_delta(self.media_consultor_geral, self.prev_freecel.media_consultor_geral)

    @property
    def ufs(self) -> List[str]:
        return list(self.dataframe['uf'].unique())

    def to_json(self):
        data = {}
        for cls in reversed(self.__class__.__mro__):
            for attr_name, attr_value in vars(cls).items():
                if isinstance(attr_value, property):
                    data[attr_name] = getattr(self, attr_name)

        return data
    
    def __media_por_consultor(self, tipo: Optional[str] = None) -> float:
        dataframe = filter_by(dataframe=self.dataframe, tipo=tipo)
        consultores = dataframe['consultor'].nunique()
        if consultores == 0:
            return 0
        
        media_por_consultor = dataframe['valor_acumulado'].sum() / consultores
        return media_por_consultor
    
    def __get_prev_freecel(self) -> Self:
        prev_year, prev_month = self.get_prev_data(self.years())
        prev_freecel = Freecel(self.full_dataframe, prev_year, prev_month)

        return prev_freecel
    