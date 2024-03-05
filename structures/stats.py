import pandas as pd
from database.dataframe import DataFrame
from typing import Optional
# from structures.delta import Delta

class Stats():
    def __init__(self, dataframe: pd.DataFrame, ano: Optional[int] = None, mes: Optional[str] = None):
        self.full_dataframe = dataframe
        self.dataframe = self.filter_by(dataframe, ano, mes)
        self.ano = ano
        self.mes = mes.capitalize() if mes else mes

    def filter_by(self, dataframe: pd.DataFrame, ano: Optional[int] = None, mes: Optional[str] = None, tipo: Optional[str] = None) -> pd.DataFrame:
        return DataFrame.__filter_by__(
            dataframe = dataframe, 
            ano = ano, 
            mes = mes, 
            tipo = tipo
        )
    
    # @property
    # def dates(self) -> list[dict]:
    #     return [{f"{year}": self.months(year)} for year in self.years]
    
    # @property
    # def years(self) -> list[int]:
    #     return list(self.dataframe['ano'].unique())
    
    # def months(self, ano) -> list[str]:
    #     return list(self.filter_by(ano)['mês'].unique())
    
    @property
    def periodo_trabalhado(self) -> int:
        meses_trabalhados = self.dataframe['mês'].nunique()
        if meses_trabalhados <=1:
            return 22
        
        return meses_trabalhados
    
    @property
    def clientes(self) -> float:
        return float(self.dataframe.shape[0])
    
    @property
    def receita(self) -> float:
        return float(self.dataframe['valor_acumulado'].sum())

    @property
    def volume(self) -> float:
        return float(self.dataframe['quantidade_de_produtos'].sum())
    
    @property
    def ticket_medio(self) -> float:
        return float(self.receita / self.clientes)
    
    @property
    def clientes_media(self) -> float:
        return float(self.clientes / self.periodo_trabalhado)
    
    @property
    def receita_media(self) -> float:
        return float(self.receita / self.periodo_trabalhado)
    
    @property
    def volume_media(self) -> float:
        return float(self.volume / self.periodo_trabalhado)
    
    # @property
    # def delta_clientes(self) -> int:
    #     delta = Delta(self.full_dataframe, self.ano, self.mes)
    #     return delta.clientes
    
    # @property
    # def delta_receita(self) -> int:
    #     delta = Delta(self.full_dataframe, self.ano, self.mes)
    #     return delta.receita

    # @property
    # def delta_volume(self) -> int:
    #     delta = Delta(self.full_dataframe, self.ano, self.mes)
    #     return delta.volume
    
    # @property
    # def delta_ticket_medio(self) -> int:
    #     delta = Delta(self.full_dataframe, self.ano, self.mes)
    #     return delta.ticket_medio
    
    # @property
    # def delta_clientes_media(self) -> int:
    #     delta = Delta(self.full_dataframe, self.ano, self.mes)
    #     return delta.clientes_media
    
    # @property
    # def delta_receita_media(self) -> int:
    #     delta = Delta(self.full_dataframe, self.ano, self.mes)
    #     return delta.receita_media

    # @property
    # def delta_volume_media(self) -> int:
    #     delta = Delta(self.full_dataframe, self.ano, self.mes)
    #     return delta.volume_media