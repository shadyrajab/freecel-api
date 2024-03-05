from structures.stats import Stats
import pandas as pd
from typing import Optional, List
# from structures.delta import Delta

class Freecel(Stats):
    def __init__(self, dataframe: pd.DataFrame, ano: Optional[int] = None, mes: Optional[str] = None, jsonfy: Optional[bool] = None) -> None:
        self.full_dataframe = dataframe
        self.jsonfy = jsonfy
        self.dataframe = self.filter_by(dataframe, ano, mes)

        super().__init__(self.dataframe)

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
    def media_consultor_vvn(self) -> float:
        return self.__media_por_consultor('VVN')
    
    # @property
    # def delta_media_consultor_geral(self) -> float:
    #     delta, now_stats, prev_stats = self.__get_delta()
    #     return delta.__calculate_delta(now_stats.media_consultor_geral, prev_stats.media_consultor_geral)

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
        dataframe = self.filter_by(dataframe=self.dataframe, tipo=tipo)
        consultores = dataframe['consultor'].nunique()
        if consultores == 0:
            return 0
        
        media_por_consultor = dataframe['valor_acumulado'].sum() / consultores
        return media_por_consultor

    # def __get_delta(self):
    #     delta = Delta(self.full_dataframe, self.ano, self.mes)
    #     prev_year, prev_month = delta.__get_prev_data()
    #     now_stats = Freecel(self.full_dataframe, self.ano, self.mes)
    #     prev_stats = Freecel(self.full_dataframe, prev_year, prev_month)
    #     return delta, now_stats, prev_stats