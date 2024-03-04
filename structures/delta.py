# from typing import Optional
# from utils.variables import MONTHS
# from pandas import DataFrame
# from structures.stats import Stats

# class Delta:
#     def __init__(self, dataframe: DataFrame, ano: Optional[int] = None, mes: Optional[str] = None):
#         self.dataframe = dataframe
#         self.ano = ano
#         self.mes = mes.capitalize()

#     def filter_by(self, dataframe: DataFrame, ano: Optional[int] = None, mes: Optional[str] = None, tipo: Optional[str] = None):
#         return DataFrame.__filter_by__(
#             dataframe = dataframe, 
#             ano = ano, 
#             mes = mes, 
#             tipo = tipo
#         )
        
#     @property
#     def clientes(self) -> int:
#         now_stats, prev_stats = self.__get_stats()
#         return self.__calculate_delta(now_stats.clientes, prev_stats.clientes)
    
#     @property
#     def receita(self) -> float:
#         now_stats, prev_stats = self.__get_stats()
#         return self.__calculate_delta(now_stats.receita, prev_stats.receita)

#     @property
#     def volume(self) -> int:
#         now_stats, prev_stats = self.__get_stats()
#         return self.__calculate_delta(now_stats.volume, prev_stats.volume)
    
#     @property
#     def ticket_medio(self) -> int:
#         now_stats, prev_stats = self.__get_stats()
#         return self.__calculate_delta(now_stats.ticket_medio, prev_stats.ticket_medio)

#     @property
#     def clientes_media(self) -> int:
#         now_stats, prev_stats = self.__get_stats()
#         return self.__calculate_delta(now_stats.clientes_media, prev_stats.clientes_media)
    
#     @property
#     def receita_media(self) -> int:
#         now_stats, prev_stats = self.__get_stats()
#         return self.__calculate_delta(now_stats.receita_media, prev_stats.receita_media)

#     @property
#     def volume_media(self) -> int:
#         now_stats, prev_stats = self.__get_stats()
#         return self.__calculate_delta(now_stats.volume_media, prev_stats.volume_media)
    
#     def __calculate_delta(self, now_metric, prev_metric) -> float:
#         return now_metric - prev_metric
        
#     def __get_prev_data(self, years) -> tuple[int, str]:
#         if not self.ano and not self.mes: return 0
#         if self.ano == min(years) and not self.mes: return 0
#         if self.ano == min(years) and self.mes.lower() == 'janeiro': return 0

#         prev_year = self.ano - 1 if self.mes == 'Janeiro' else self.ano
#         prev_month = MONTHS[MONTHS.index(self.mes) - 1]
#         return prev_year, prev_month
    
#     def __get_stats(self):
#         now_stats = Stats(self.dataframe, self.ano, self.mes)
#         prev_year, prev_month = self.__get_prev_data(now_stats.years)
#         prev_stats = Stats(self.dataframe, prev_year, prev_month)
#         return now_stats, prev_stats